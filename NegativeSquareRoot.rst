#format rst

Every now and then, the behaviour of ``sqrt`` for negative values is discussed on the mailing list.  Hopefully, by summarising `http://thread.gmane.org/gmane.comp.python.numeric.general/8704/focus=8704 the latest thread`_ here, we don't need to do so again in the future.

Why does numpy.sqrt(-1) return nan?  Why does it not yield 1j, which is surely the correct answer?
--------------------------------------------------------------------------------------------------

If you assume the domain of computation is the field of complex numbers, then yes, the above assumption is true -- that the square root of ``-1`` is ``1j``.  However, ``numpy`` supports many different data types, and in the context of these data types, the answer may vary.

By default, ``numpy`` assumes that you are working with real numbers (which is a reasonable assumption).  What you are then asking ``numpy`` is: "What is the square root of ``-1`` (but please limit your answer to real numbers)?".  Since the answer is ``1j``, numpy cannot provide a real value, so it rather yields ``nan``.

On the other hand, if you specifically ask ``numpy`` for the complex answer in one of several ways, it will be happy to oblige:

::

   In [49]: N.sqrt(-1+0j)
   Out[49]: 1j
   In [50]: N.sqrt(complex(-1))
   Out[50]: 1j
   In [50]: N.sqrt(N.asarray(-1,dtype=complex))
   Out[50]: 1j

Simply put, ``sqrt``'s output is of the same type as the input (``numpy`` does no checking).  The only exception is for integers, in which case ``sqrt`` returns floats.

Why can't numpy just provide complex numbers by default?
--------------------------------------------------------

Imagine having to calculate the square roots of a large array of numbers.  If numpy calculates complex answers, that would mean that the complex answer would take up twice as much memory as the real answer.  Clearly, this case is not a desirable default.  Of course, ``numpy`` could check whether negative numbers are present, and only *then* calculate complex answers, but again, this leads to inconsistent behaviour.  Furthermore, if a user wants to operate on positive real numbers only, why burden his calculations with the extra time-consuming complexity?

How can I change the default behaviour?
---------------------------------------

``Numpy`` provides functions to automatically return complex numbers for negative real arguments.  These reside in ``numpy.lib.scimath`` and can be imported using

::

   from numpy.lib.scimath import *

to replace ``sqrt`` in the current namespace.  

However, it is better style to use

::

   from numpy.lib import scimath as SM
   SM.sqrt(-1)

Note that this doesn't actually change the default behavior.  Still ``numpy.sqrt(-1)`` will return ``nan``.  It just makes the version of sqrt that checks for complex results more accessible via ``SM.sqrt`` instead of ``numpy.lib.scimath.sqrt``.

Another alternative is to take advantage of the fact that any python file is a module, and make a mini-module that makes complex behavior the default.  Then you just import that instead of numpy.

::

   # File: cnumpy.py
   from numpy import *
   from numpy.lib.scimath import *

Then from your files, or from the interpreter, you use your ``cnumpy`` module like so:

::

   >>> import cnumpy
   >>> cnumpy.sqrt(-1)
   1j
   >>> a = cnumpy.ones((2,2)) * -1
   >>> cnumpy.sqrt(a)
   array([[ 0. +1.00000000e+00j,  0. +1.00000000e+00j],
          [ 0. +1.00000000e+00j,  0. +1.00000000e+00j]])

In all respects it looks just like a new version of ``numpy`` that happens to return ``1j`` for ``sqrt(-1)``.

Changing error reporting behavior
:::::::::::::::::::::::::::::::::

The ``numpy`` error handler can also be asked to complain if negative values are passed to ``sqrt``:

::

   In [1]: N.sqrt(-1)
   Out[1]: nan
   In [2]: saved_error_handler = N.seterr(invalid='raise') # or 'warn'
   In [3]: N.sqrt(-1)
   ---------------------------------------------------------------------------
   exceptions.FloatingPointError                        Traceback (most recent call last)
   /home/stefan/work/prasa2006/<ipython console>
   FloatingPointError: invalid encountered in sqrt
   In [4]: N.seterr(**saved_error_handler)
   Out[4]: {'over': 'ignore', 'divide': 'ignore', 'invalid': 'warn', 'under': 'ignore'}
   In [5]: N.sqrt(-1)
   Out[5]: nan

With Python 2.5 it should soon be possible to do

::

   with errstate(invalid='raise'):
       sqrt(-1) # raise exception

Alternatively, you can simply use complex arrays throughout. 

Do numpy and scipy behave differently?
--------------------------------------

Yes, ``scipy`` exposes ``numpy.lib.scimath`` by default.

::

   >>> import scipy
   >>> scipy.sqrt(-1)
   1j

