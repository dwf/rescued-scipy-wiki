#format rst

Description
-----------

The ``numexpr`` package supplies routines for the fast evaluation of array expressions elementwise by using a vector-based virtual machine. It's comparable to ``scipy.weave.blitz`` (in ["Weave"]), but doesn't require a separate compile step of C or C++ code.

Building
--------

The project is hosted `here <http://code.google.com/p/numexpr/wiki/Overview>`_.

To use it as a standalone package, you can grab it from the Subversion repository at `http://numexpr.googlecode.com/svn/trunk/`_, and do the usual ``python setup.py install``. You will need NumPy_ installed.

Using
-----

The main routine to be concerned with is ``numexpr.evaluate``. It acts like this:

::

   >>> from numexpr import evaluate
   >>> a = arange(10)
   >>> b = arange(0,20,2)
   >>> evaluate("a+b")
   array([ 0,  3,  6,  9, 12, 15, 18, 21, 24, 27])

The full signature of ``evaluate`` is ``evaluate(ex, local_dict=None, global_dict=None, **kwargs)``. ``ex`` is a string forming an expression, like "``2*a+3*b``". The values for ``a`` and ``b`` will by default be taken from the calling function's frame (through the use of ``sys._getframe()``). Alternatively, they can be specified using the ``local_dict`` or global_dict` arguments, or passed as keyword arguments.

Expressions are cached, so reuse is fast. Arrays or scalars are allowed for the variables, which must be of type int, float64 (double), or complex128 (double,double). The arrays must all be the same size.

How it works
------------

The string passed to ``evaluate`` is compiled into an object representing the expression and types of the arrays used by the function ``numexpr``.

The expression is first compiled using Python's ``compile`` function (this means that the expressions have to be valid Python expressions). From this, the variable names can be taken. The expression is then evaluated using instances of a special object that keep track of what is being done to them, and which builds up the parse tree of the expression.

This parse tree is then compiled to a bytecode program, which describes how to perform the operation elementwise. The virtual machine uses "vector registers": each register is many elements wide (by default, the first pass uses 128 elements). The key to ``numexpr``'s speed is handling chunks of elements at a time.

There are two extremes to evaluating an expression elementwise. You can do each operation as arrays, returning temporary arrays. This is what you do when you use NumPy_: ``2*a+3*b`` uses three temporary arrays as large as ``a`` or ``b``. This strategy wastes memory (a problem if your arrays are large), and also is not a good use of cache memory: for large arrays, the results of ``2*a`` and ``3*b`` won't be in cache when you do the add.

The other extreme is to loop over each element, as in

::

   for i in xrange(len(a)):
       c[i] = 2*a[i] + 3*b[i]

This doesn't consume extra memory, and is good for the cache, but, if the expression is not compiled to machine code, you will have a big case statement (or a bunch of if's) inside the loop, which adds a large overhead for each element, and will hurt the branch-prediction used on the CPU.

``numexpr`` uses a in-between approach. Arrays are handled as chunks (the first pass uses 128 elements) at a time, using a register machine. As Python code, it looks something like this:

::

   for i in xrange(0, len(a), 128):
       r0 = a[i:i+128]
       r1 = b[i:i+128]
       multiply(r0, 2, r2)
       multiply(r1, 3, r3)
       add(r2, r3, r2)
       c[i:i+128] = r2

(remember that the 3-arg form stores the result in the third argument, instead of allocating a new array). This achieves a good balance between cache and branch-prediction. And the virtual machine is written entirely in C, which makes it faster than the Python above.

There is some more information and history at `http://isobaric.blogspot.com/2006/03/numerical-expression-evaluator-now-in.html`_.

Credits
-------

Numexpr was initially written by DavidCooke_, and extended to more types by TimHochberg_.

See also
--------

* ["Cookbook/Autovectorize"]

* [`http://thread.gmane.org/gmane.comp.python.numeric.general/17266/focus=17280`_ Re: vectorizing loops - Discussion on scipy list]

-------------------------



  CategorySciPyPackages_

