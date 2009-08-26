#format rst

Overview
========

An easy way to add attributes or user-defined methods to an array is to define a subclass of ``ndarray``. Typically, your new class needs to define at least a ``__new__`` method and a ``__array_finalize__``.

The __new__ method
~~~~~~~~~~~~~~~~~~

The ``__new__`` is the class constructor. A call to ``__new__(cls,...)`` creates a new instance of the class ``cls``, but doesn't initialize the instance. According to the python documentation,

::

   If new() returns an instance of cls, then the new instance's init() method will be invoked like "init(self[, ...])", where self is  the new instance and the remaining arguments are the same as were passed to  new().
   If new() does not return an instance of cls, then the new instance's init() method will not be invoked.
   new() is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance creation.

It turns out that even if ndarrays are not immutable *stricto sensu*, they have some characteristics of immutable types: they use a definite portion of memory which is allocated at their creation, and this portion of memory cannot be *drastically* altered.  For example, you can substitute one element or a group of elements to others that have the same type, but you cannot extend a standard ndarray as you could with lists or strings, nor can you mix types (unless particular cases, but that's another story). In other terms, from a python point of view, the ``__new__`` method of your subclass does not call ``__init__``. The docstring of the ``ndarray.__new__`` method is quite clear:

::

   No __init__ method is needed because the array is fully initialized after the __new__ method.

However, we need to keep in mind that any attribute that we define in the ``__new__`` method will be shared among all the instances. If we want instance-specific attributes, we still need some specific initialization. We cannot use the ``__init__`` method, as it won't be called. That's where  ``__array_finalize__`` comes to play.

Some words of caution
:::::::::::::::::::::

The definition of default values for subclass attributes (as opposed to instance attributes) in the ``__new__`` method is strongly discouraged for several reasons:

* It is not thread-safe.

* An array of a given subclass can be created from an array of another subclass without any call to the ``__new__`` method at all. This situation occurs with the use of the ``view`` method. In that case, we must still initialize the attributes of the new subclass with the ``__array_finalize__`` method.

The __array_finalize__ method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

According to the numpy documentation, the ``.__array_finalize__(self, obj)`` method

::

   is called whenever the system internally allocates a new array from obj, where obj is a subclass (subtype) of the (big)ndarray [. It can be used to change attributes of self after construction (so as to ensure a 2-d matrix for example), or to update meta-information from the “parent.” Subclasses inherit a default implementation of this method that does nothing."

In other terms, ``__array_finalize__`` is called:

* Once an array is created with a function or a method that invokes ``__new__``: the ``obj`` argument is then what was returned by ``__new__``.

* Each time a method returns a modified array, without invoking ``__new__``. In that case, the ``obj`` argument is the modified array.

* Each time an array is created as a view from another array. In that case, the ``obj`` argument is the array that calls the ``view`` method.

Note that if a method returns nothing, then ``__array_finalize__`` won't be called.

``__array_finalize__`` is thus where we need to transform the attributes from class-generic (as they were defined by ``__new__``) to instance-specific. More generally, it is where we must define the default attributes of the subclass.

Example
~~~~~~~

The short example below is an example of subclassed ndarray, where an extra ``info`` tag can be used to store some metainformation. To illustrate the calls to ``__new__`` and ``__array_finalize__``, some messages will be printed.

::

   import numpy as N
   class InfoArray(N.ndarray):
       def __new__(subtype, data, info=None, dtype=None, copy=False):
           print "__new__ received %s" % type(data)
           # Make sure we are working with an array, and copy the data if requested
           subarr = N.array(data, dtype=dtype, copy=copy)
           # Transform 'subarr' from an ndarray to our new subclass.
           subarr = subarr.view(subtype)
           # Use the specified 'info' parameter if given
           if info is not None:
               subarr.info = info
           # Otherwise, use data's info attribute if it exists
           elif hasattr(data, 'info'):
                   subarr.info = data.info
           # Finally, we must return the newly created object:
           return subarr
       def __array_finalize__(self,obj):
           # We use the getattr method to set a default if 'obj' doesn't have the 'info' attribute
           self.info = getattr(obj, 'info', {})
           # We could have checked first whether self.info was already defined:
           #if not hasattr(self, 'info'):
           #    self.info = getattr(obj, 'info', {})
       def __repr__(self):
           desc="""\
   array(data=
     %(data)s,
         tag=%(tag)s)"""
           return desc % {'data': str(self), 'tag':self.info }

Such a class can be used like this:

::

   >>> x = InfoArray(N.arange(10), info={'name':'x'})
   __new__ received <type 'numpy.ndarray'>
   >>> x
   array(data=
     [0 1 2 3 4 5 6 7 8 9],
         tag={'name': 'x'})
   >>> y = InfoArray(N.arange(10), info={'name':'y'})
   >>> assert (x.info['name']=='x')
   >>> assert (y.info['name']=='y')
   # Now, let's try the view method...
   >>> z = N.arange(10).view(InfoArray)
   >>> assert (isinstance(z, InfoArray))
   >>> assert (z.info == {})
   # Explanation:
   # We created an InfoArray from a standard ndarray with the 'view' method.
   # As a ndarray does not have a 'info' attribute, the default {} is used.
   >>> z = x.view(InfoArray)
   >>> assert(z.info == x.info)
   # Here, we created a new InfoArray from an existing one with the 'view' method.
   # Therefore, the 'info' attribute is propagated to the view.
   #
   # Now, let's apply a numpy function to an InfoArray: the 'view' method will be called internally...
   # ... and the result will inherit the 'info' attribute of the original InfoArray
   >>> z = N.sqrt(x)
   >>> z
   array(data=
     [ 0.          1.          1.41421356  1.73205081  2.          2.23606798
     2.44948974  2.64575131  2.82842712  3.        ],
         tag={'name': 'x'})

Note that this InfoArray class is fairly basic, and can lead to surprises. For example, we haven't defined how the metadata must be updated when combining two InfoArrays. The default behavior is to use the ``info`` tag of the first element:

::

   >>> assert((x+y).info['name']=='x')
   True
   >>> assert((y+x).info['name']=='y')
   True

If we want to change this behavior, we need to update the ``__add__`` method (or whatever method is required).

The __array_wrap__ method
~~~~~~~~~~~~~~~~~~~~~~~~~

When a numpy ufunc is called on a subclass of ndarray, the ``__array_wrap__`` method is called to transform the result into a new instance of the subclass. By default, ``__array_wrap__`` will call ``__array_finalize__``, and the attributes will be inherited.

By defining a specific ``__array_wrap__`` method for our subclass, we can tweak the output. The ``__array_wrap__`` method requires one argument, the object on which the ufunc is applied, and an optional parameter ``context``. This parameter is returned by some ufuncs as a 3-element tuple: (name of the ufunc, argument of the ufunc, domain of the ufunc).

For example, let's modify our ``InfoArray`` class, so that we can keep track of the modifications:

::

   def __array_wrap__(self,obj, context=None):
       result = obj.view(type(self))
       result.info.update(self.info)
       if context is not None:
               modif = result.info.get('modif','modified by')
               modif += ": %s" % context[0]
               result.info.update({'modif': modif})
       return result

Using the same example as earlier:

::

   >>> z = N.sqrt(x)
   >>> z
   array(data=
     [ 0.          1.          1.41421356  1.73205081  2.          2.23606798
     2.44948974  2.64575131  2.82842712  3.        ],
         tag={'modif': "modified by: <ufunc 'sqrt'>", 'name': 'x'})
   # Let's add 1 in place
   >>> z +=1
   >>> z
   array(data=
     [ 1.          2.          2.41421356  2.73205081  3.          3.23606798
     3.44948974  3.64575131  3.82842712  4.        ],
         tag={'modif': "modified by: <ufunc 'sqrt'>: <ufunc 'add'>", 'name': 'x'})

A more realistic example of a ``__array_wrap__`` methods is available in the ``maskedarray`` package. There, the mask of the output is modified to take the domain of the ufunc into account.

