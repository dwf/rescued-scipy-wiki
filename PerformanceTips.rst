#format rst

This page collects tips and tricks to increase the speed  of your code using numpy/scipy.

For general tips and tricks to improve the performance of your Python programs see http://wiki.python.org/moin/PythonSpeed/PerformanceTips.

Python built-ins vs. numpy functions
====================================

Note that the built-in python ``min`` function   can be much slower (up to 300-500 times)  than using the ``.min()`` method of an array. I.e.: use ``x.min()`` instead of ``min(x)``.

The same applies to ``max``.

This is also true for the new ``any`` and ``all`` functions for Python >=2.5.

Beyond pure Python
==================

Sometimes there are tasks for which pure python code can be too slow.

Possible solutions can be obtained via:

* hand-written [:Cookbook/C_Extensions: C extensions]

* psyco

* pyrex

* ctypes

* f2py

* weave

* swig

* boost

* SIP

* CXX

For a full discussion with examples on performance gains through interfacing with other languages see [:PerformancePython_: this article].

Examples
========

Tips and tricks for specific situations.

Finding the row and column of the min or max value of an array or matrix
------------------------------------------------------------------------

A slow, but straightforward, way to find the row and column indices of the minimum value of an array or matrix *x*:

::

   import numpy as np
   def min_ij(x):
       i, j = np.where(x == x.min())
       return i[0], j[0]

This can be made quite a bit faster:

::

   def min_ij(x):
       i, j = divmod(x.argmin(), x.shape[1])
       return i, j

The fast method is about 4 times faster on a 500 by 500 array.

Removing the i-th row and j-th column of a 2d array or matrix
-------------------------------------------------------------

The slow way to remove the i-th row and j-th column from a 2d array or matrix:

::

   import numpy as np
   def remove_ij(x, i, j):
       # Remove the ith row
       idx = range(x.shape[0])
       idx.remove(i)
       x = x[idx,:]
       # Remove the jth column
       idx = range(x.shape[1])
       idx.remove(j)
       x = x[:,idx]
       return x

The fast way, because it avoids making copies, to remove the i-th row and j-th column from a 2d array or matrix:

::

   def remove_ij(x, i, j):
       # Row i and column j divide the array into 4 quadrants
       y = x[:-1,:-1]
       y[:i,j:] = x[:i,j+1:]
       y[i:,:j] = x[i+1:,:j]
       y[i:,j:] = x[i+1:,j+1:]
       return y

For a 500 by 500 array the second method is over 25 times faster.

.. ############################################################################

.. _PerformancePython: ../PerformancePython

