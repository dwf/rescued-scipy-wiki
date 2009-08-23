#format rst

Addressing Array Columns by Name
================================

There are two very closely related ways to access array columns by name: recarrays and structured arrays.  Structured arrays are just ndarrays with a complicated data type:

::

   In [1]: from numpy import *
   In [2]: ones(3, dtype=dtype([('foo', int), ('bar', float)]))
   Out[2]:
   array([(1, 1.0), (1, 1.0), (1, 1.0)],
         dtype=[('foo', '<i4'), ('bar', '<f8')])
   In [3]: r = _
   In [4]: r['foo']
   Out[4]: array([1, 1, 1])

recarray is a subclass of ndarray that just adds attribute access to structured arrays:

::

   In [10]: r2 = r.view(recarray)
   In [11]: r2
   Out[11]:
   recarray([(1, 1.0), (1, 1.0), (1, 1.0)],
         dtype=[('foo', '<i4'), ('bar', '<f8')])
   In [12]: r2.foo
   Out[12]: array([1, 1, 1])

One downside of recarrays is that the attribute access feature slows down all field accesses, even the r['foo'] form, because it sticks a bunch of pure Python code in the middle. Much code won't notice this, but if you end up having to iterate over an array of records, this will be a hotspot for you.

Structured arrays are sometimes confusingly called record arrays.

  - lightly adapted from a Robert Kern post of Thu, 26 Jun 2008 15:25:11 -0500

