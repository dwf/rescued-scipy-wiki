#format rst

This page is intended to help people evaluate the benefits of some commercial packages against Python+NumPy+SciPy+Matplotlib+IPython (PyLab) for scientific computing.  This is done by listing the advantages of PyLab and its disadvantages compared to other packages.  Basic functionality is similar enough that the detailed stylistic differences are not necessary to document here. 

PyLab Advantages
----------------

* very nice modern language with great builtin-objects

* featureful extended library means sophisticated large-scale programs can be written quickly.

* very easy to extend in C/C++ or Fortran 

* many, many third-party libraries (because of the previous point) that allow Python to do almost anything a computer can do

* everything is passed by reference rather than by value

* NumPy arrays

  * Simple consistent syntax for efficient simple vector operations

    * slicing gives a view into an array rather than a copy

  * Highly elaborate vector operations possible

  * NumPy array is a sophisticated multi-dimensional array object

  * NumPy arrays can hold complicated data-types including mis-aligned, non native byte-order formats, and record arrays. 

  * memory-mapped arrays are easily dealt with 

* algorithms (mostly) based on fast, robust legacy code

* libraries available to input and output binary files in a variety of formats (raster images in practically any consumer format, CDF, astronomical FITS data, ...)

* a variety of different tools are available to accelerate key pieces of code (see PerformancePython_ for a comparison)

* free as in 'beer' and as in 'speech'

* no licensing issues --- you are not becoming dependent on a single vendor. 

PyLab Disadvantages (compared with MATLAB)
------------------------------------------

* nothing quite like Simulink

* not as much documentation

* not as much functionality in select areas (assuming you've purchased all the toolboxes)

* smaller user-base

* verbose-ness in code that does a lot of linear algebra caused by switching between arrays and matrices.  This is due to not having two in-fix operators to represent array multiplication and element-by-element multiplication.

* package functionality is sometimes duplicated

* moving target; many bugs in older versions

* often difficult to determine which of the many packages available on the Net is needed to solve your problem

* IDEs not as integrated or as easy to use (especially for profiling)

PyLab Disadvantages (compared with Maple)
-----------------------------------------

* no graphical representation of formulas

* no arbitrary-precision floating-point

* no equivalent of "notebooks"

* no built-in symbolic manipulation ([`http://code.google.com/p/sympy/`_ SymPy_] is coming along nicely though.)

PyLab Disadvantages (compared with Mathematica)
-----------------------------------------------

* no equivalent of "notebooks"

* no built-in symbolic manipulation ([`http://code.google.com/p/sympy/`_ SymPy_] is coming along nicely though.)

Some of these deficiencies are expected to be remedied by packages now in development. See PyLabAwaits_

[:NumPyTestimony_: User testimony] on comparing the MatLab/PyLab comparison.

See also NumPyProConDiscussion_ for a more free-form page.

.. ############################################################################

.. _PerformancePython: ../PerformancePython

.. _SymPy: ../SymPy

.. _PyLabAwaits: ../PyLabAwaits

.. _NumPyTestimony: ../NumPyTestimony

.. _NumPyProConDiscussion: ../NumPyProConDiscussion

