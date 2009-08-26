#format rst

TableOfContents_

General questions about numpy
=============================

What is numpy?
--------------

numpy is a python extension module to support efficient operation on arrays of homogeneous data. It allows python to serve as a high-level language for manipulating numerical data, much like IDL, MATLAB, or Yorick.

Why use numpy rather than IDL, MATLAB, Octave, or Yorick?
---------------------------------------------------------

As always, you should choose the programming tools that suit your problem and your environment. Advantages many people cite are that it is open-source, it doesn't cost anything, it uses the general-purpose language python rather than a sui generis programming language, and it is relatively easy to connect existing C and FORTRAN code to the python interpreter.

What are numpy arrays?
----------------------

A numpy array is a multidimensional array of objects all of the same type. In memory, it is an object which points to a block of memory, keeps track of the type of data stored in that memory, keeps track of how many dimensions there are and how large each one is, and - importantly - the spacing between elements along each axis.

So, for example, you might have a numpy array that represents the numbers from zero to nine, stored as 32-bit integers, one right after another, in a single block of memory. (For comparison, each python integer needs to have some type information stored alongside it.) You might also have the array of even numbers from zero to eight, stored in the same block of memory, but with a gap of four bytes between elements. This is called "striding", and it means that you can often create a new array referring to a subset of the elements in an array without copying any data. Such subsets are called "views". This is an efficiency gain, obviously, but it also allows modification of selected elements of an array in various ways.

An important constraint on numpy arrays is that for a given axis, all the elements must be spaced by the same number of bytes in memory. numpy cannot use double-indirection to access array elements, so indexing modes that would require this must produce copies. This constraint makes it possible for all the inner loops to be written in efficient C code.

numpy arrays offer a number of other possibilities, including using a memory-mapped disk file as the storage space for an array, and "record arrays", which have fields of different data types.

Why not use lists?
------------------

Python's lists are efficient general-purpose containers. They support (fairly) efficient insertion, deletion, appending, and concatenation, and python's list comprehensions make them easy to construct and manipulate. However, they have certain limitations: they don't support "vectorized" operations like elementwise addition and multiplication, and the fact that they can contain objects of differing types mean that python must store type information for every element, and must execute type dispatching code when operating on each element. This also means that very few list operations can be carried out by efficient C loops.

What's the story with Numeric, numarray, and numpy?
---------------------------------------------------

The short version is that Numeric was the original package that provided efficient homogeneous numeric arrays for python, but some developers felt it lacked certain essential features, so they began developing an independent implementation called numarray. Having two incompatible implementations of array was clearly a disaster in the making, so numpy was designed to be an improvement on both.

Neither Numeric nor numarray is currently supported. numpy has been the standard array package for a number of years now. If you use Numeric or numarray, you should upgrade; numpy is explicitly designed to have all the capabilities of both. There are tools available to ease the upgrade process; only C code should require much modification.

General questions about SciPy
=============================

What is SciPy?
--------------

SciPy is a set of Open Source scientific and numeric tools for Python. It currently supports special functions, integration, ordinary differential equation (ODE) solvers, gradient optimization, genetic algorithms, parallel programming tools, an expression-to-C++ compiler for fast execution, and others.

How much does it cost?
----------------------

SciPy is freely available. It is distributed as Open Source software, meaning that you have complete access to the source code and can use it in anyway allowed by its liberal BSD license.

What are SciPy's licensing terms?
---------------------------------

SciPy's license is free for both commercial and non-commercial use, under the [:License_Compatibility:BSD terms].

Why Python?
-----------

1. Python is interactive.

     People familiar with Matlab and Mathematica understand how powerful their command line interfaces are for exploring mathematical relationships and scientific data sets. Python provides a similar interactive environment with the added benefit of a full featured programming language behind it.

#. Python is productive for beginners and experts alike.

     SciPy is targeted at engineers, scientists, financial analysts, and others who consider programming a necessary evil. Any time spent learning a language or tracking down bugs is time spent not solving their real problem. Python has a short learning curve and most people can do real and useful work with it within a day of learning it. Its clean syntax and interactive nature facilitates this. Python is also nice for CS language weenies. Its feature set includes the things one would expect from a modern programming language (object oriented, automatic garbage collection, etc.), and it scales well to large projects. While you're unlikely to see an operating system written in Python, it is suitable for almost any other task you're likely to do in a compiled langauge. And, for tasks better handled in C and Fortran, Python interfaces with these languages very well.

#. Python has a huge standard library.

     Python standard library contains more than 200 libraries covering Internet programming (web, telnet, FTP, email, etc.), systems programming, text processing, file compression, cryptography, and many others. There is also a large pool of open source tools for database connectivity, PDF generation, and other tasks. By and large, these are well designed and are written by experts in the field so that you and I don't have to. This allows us to concentrate on our field while simultaneously benefiting from advances made by others. Open source is a beautiful thing. A number of other points can be made about the merits of Python for scientific computing, but this covers the highlights. Python's low price tag ($0.00) is important to some people, but its technical merits are more important in our minds.

What scientific libraries are available in SciPy?
-------------------------------------------------

The core SciPy has all the functionality of the old Numeric module: support for arrays and matrices, fast Fourier transforms, and basic input/output functionality.

The full SciPy also has the following modules:

cluster
  information theory functions (currently, vq and kmeans)

fftpack
  fast Fourier transform module based on fftpack and fftw when available

integrate
  numeric integration for bounded and unbounded ranges. ODE solvers.

interpolate
  interpolation of values from a sample data set.

io
  reading and writing numeric arrays, MATLAB .mat, and Matrix Market .mtx files

lib
  access to the BLAS and LAPACK libraries

linalg
  linear algebra and BLAS routines based on the ATLAS implementation of LAPACK

maxentropy
  Support for fitting maximum entropy models, either discrete or continuous

misc
  other routines that don't clearly fit anywhere else.  The Python Image Library (PIL) interface is located here.

optimize
  constrained and unconstrained optimization methods and root-finding algorithms

signal
  signal processing (1-D and 2-D filtering, filter design, LTI systems, etc.)

sparse
  Some sparse matrix support. LU factorization and solving Sparse linear systems

special
  special function types (bessel, gamma, airy, etc.)

stats
  statistical functions (stdev, var, mean, etc.)

weave
  compilation of numeric expressions to C++ for fast execution

See `scikits <http://scipy.org/scipy/scikits>`_ for more packages: MlabWrap_, AudioLab_, `Learn <http://scipy.org/scipy/scikits/wiki/MachineLearning>`_, `GenericOpt <http://scipy.org/scipy/scikits/wiki/Optimization>`_, `OpenOpt <http://scipy.org/scipy/scikits/wiki/OpenOpt>`_ etc

The following modules are in testing in the "sandbox":

cow
  parallel programming via a Cluster Of Workstations

delaunay
  Delaunay Triangulation, used for interpolation

ga
  genetic algorithms

gplt
  plotting using Gnuplot

image
  some useful image processing routines

montecarlo
  fast routines for sampling from an arbitrary probability distribution

nd_image
  more image processing routines

odr
  wrappers for the ODRPACK Orthogonal Distance Regression library

plt
  plotting library

pysparse
  version of PySparse_ compatible with numpy

umfpack
  UMFPACK wrappers for sparse matrices

xplt
  yet another plotting library

To build packages in the sandbox, uncomment the following line from Lib/sandbox/setup.py:

::

      config.add_subpackage('packagename')

How can SciPy be fast if it is written in an interpreted language like Python?
------------------------------------------------------------------------------

Actually, the time-critical loops are usually implemented in C or Fortran. Much of SciPy is a thin layer of code on top of the scientific routines that are freely available at www.netlib.org. Netlib is a huge repository of incredibly valuable and robust scientific algorithms written in C and Fortran. It would be silly to rewrite these algorithms and would take years to debug them. SciPy uses a variety of methods to generate "wrappers" around these algorithms so that they can be used in Python. Some wrappers were generated by hand coding them in C. The rest were generated using either SWIG or f2py.

In what directions do you see SciPy expanding?
----------------------------------------------

SciPy will evolve to cover a wide variety of disciplines. We'd like to see a variety of Numeric codes either integrated into or associated with SciPy.

Here's a sample of general areas where interest has been indicated:

* Circuit Analysis (wrapper around Spice?)

* Micro-Electro Mechanical Systems simulators (MEMs)

* Medical image processing

* Neural networks

* 3-D Visualization via VTK

* Financial analysis

* Economic analysis

* Hidden Markov Models

And here are some other, though more specialized, candidates:

* Radar processing

* Electromagnetics simulators (MoM, FDTD, FEM)

* Fluid dynamics codes

* 2-D and 3-D Modeling/CAD module (Open Cascade?)

We're open to pretty much any suggestions, so let us know what fields are of interest.

I've found a bug.  What do I do?
--------------------------------

The SciPy development team works hard to make SciPy as reliable as possible, but, as in any software product, bugs do occur. If you find bugs that affect your software, please tell us by entering a ticket in the `tracker <http://projects.scipy.org/scipy/scipy/report/1:ticket>`_.

How can I get involved in SciPy?
--------------------------------

Drop us a mail on the mailing lists.  We are keen for more people to help out writing code, unit tests, documentation (including translations into other languages), and helping out with the website.

Is there commercial support available?
--------------------------------------

Yes, commercial support is offered for SciPy by Enthought. Please contact `eric@enthought.com`_ for more information.

Basic SciPy/numpy usage
=======================

What is the preferred way to test if an array is empy?
------------------------------------------------------

If you are certain a variable is an array, then use the "size" attribute. If the variable may be a list or other sequence type, use len(). The size attribute is preferable to len because:

::

       a = numpy.zeros((1,0))
       a.size == 0

but

::

       len(a) == 1

I want to load an array from a text file. Can you help me make this code more efficient?
----------------------------------------------------------------------------------------

Use numpy.loadtxt. Even if your text file has header and footer lines or comments, loadtxt can almost certainly read it; it is convenient and efficient.

I want to save an array on disk for later use. What's the best way?
-------------------------------------------------------------------

There are a large number of alternatives, depending on your needs (and on which version of numpy/scipy you are using):

* Text files: slow, huge, portable, human-readable; built into numpy * Raw binary: no metadata, totally unportable, fast; built into numpy * pickle: somewhat slow, somewhat portable (may be incompatible with different numpy versions); built into numpy * MATLAB format: portable; built into scipy * HDF5: high-powered kitchen-sink format; available through pytables * .npy: numpy native binary data format, simple, efficient, portable; built into numpy as of 1.0.5.

What's the difference between matrices and arrays?
--------------------------------------------------

numpy's basic data type is the multidimensional array. These can be one-dimensional (that is, one index, like a list or a vector), two-dimensional (two indices, like an image), three-dimensional, or more. (zero-dimensional arrays are sort of a weird corner case.) They support various operations, inluding addition, subtraction, multiplication, exponentiation, and so on - but all of these are *elementwise* operations. If you want matrix multiplication between two two-dimensional arrays, the function numpy.dot() does this. It works fine for getting the matrix product of a two-dimensional array and a one-dimensional array, in either direction, or two one-dimensional arrays. If you want some kind of matrix multiplication-like operation on higher-dimensional arrays (tensor contraction), you need to think which indices you want to be contracting over. Some combination of tensordot() and rollaxis() should do what you want.

However, some users find that they are doing so many matrix multiplications that always having to write dot() is too cumbersome, or they really want to keep row and column vectors separate. For these users, there is a matrix class. This is simply a transparent wrapper around arrays that forces arrays to be at least two-dimensional, and that overloads the multiplication and exponentiation operations. Multiplication becomes matrix multiplication, and exponentiation becomes matrix exponentiation. If you want elementwise multiplication, use numpy.multiply().

The function asmatrix() converts an array into a matrix (without ever copying any data); asarray() converts matrices to arrays. asanyarray() makes sure that the result is either a matrix or an array (but not, say, a list). Unfortunately, a few of numpy's many functions use asarray() when they should use asanyarray(), so from time to time you may find your matrices accidentally get converted into arrays. Just use asmatrix(), and consider filing a bug.

I personally never use matrices. dot() really isn't much trouble, and it's more or less the only difference.

Why not just have a separate operator for matrix multiplication?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unfortunately python does not allow extension modules to define new operators, and there is no operator we can overload to mean matrix operations.

How do I find the indices of an array where some condition is true?
-------------------------------------------------------------------

The prefered idiom for doing this is to use the function np.nonzero(), or the nonzero() method of ndarray. Given an array a, the condition a > 3 returns a boolean array and since False is interpreted as 0 in Python and Numpy, np.nonzero(a > 3) yields the indices of a where the condition is true.

::

   >>> import numpy as np
   >>> a = np.array([[1,2,3],[4,5,6],[7,8,9]])
   >>> a > 3
   array([[False, False, False],
          [ True,  True,  True],
          [ True,  True,  True]], dtype=bool)
   >>> np.nonzero(a > 3)
   (array([1, 1, 1, 2, 2, 2]), array([0, 1, 2, 0, 1, 2]))

The nonzero method of the boolean array can also be called.

::

   >>> (a > 3).nonzero()
   (array([1, 1, 1, 2, 2, 2]), array([0, 1, 2, 0, 1, 2]))

Advanced NumPy/SciPy usage
==========================

Does NumPy support nan ("not a number")?
----------------------------------------

nan, short for "not a number", is a special floating point value defined by the IEEE-754 specification along with "inf" (infinity) and other values and behaviors. In theory, IEEE nans were specifically designed to address the problem of missing values, but the reality is that different platforms behave differently, making life more difficult. On some platforms, the presence of nans slows calculations 10-100 times.  For integer data, no nan value exists. Some platforms, notably older Crays and VAX machines, don't support nans whatsoever.

Despite all these issues NumPy (and SciPy) endeavor to support IEEE-754 behavior (based on NumPy's predecessor numarray). The most significant challenge is a lack of cross-platform support within Python itself. Because NumPy is written to take advantage of C99, which supports IEEE-754, it can side-step such issues internally, but users may still face problems when, for example, comparing values within Python interpreter. In fact, NumPy currently assumes IEEE-754 behavior of the underlying floats, a decision that may have to be revisited when the VAX community rises up in rebellion.

Those wishing to avoid potential headaches will be interested in an alternative solution which has a long history in NumPy's predecessors -- masked arrays. Masked arrays are standard arrays with a second "mask" array of the same shape to indicate whether the value is present or missing. Masked arrays are the domain of the numpy.ma module, and continue the cross-platform Numeric/numarray tradition. See ["Cookbook/Matplotlib/Plotting values with masked arrays"] for example, to avoid plotting missing data in matplotlib. Despite their additional memory requirement, masked arrays are faster than nans on many floating point units. See also the NumPy developer's wiki at NumPyTrac:wiki/MaskedArray.

I have a multiprocessor/multicore machine. How can I use this to speed up my code?
----------------------------------------------------------------------------------

There are a variety of techniques, but none of them are automatic. See ParallelProgramming_.

Why doesn't A[[0,1,1,2]]+=1 do what I think it should?
------------------------------------------------------

This comes up from time to time on the mailing list. See `here <http://projects.scipy.org/pipermail/numpy-discussion/2006-March/006877.html>`_ for one extensive discussion.

::

   >>> A = numpy.zeros(3)
   >>> A[[0,1,1,2]] += 1
   >>> A
   array([ 1.,  1.,  1.])

One might, quite reasonably, have expected A to contain [1,2,1]. Unfortunately this is not what is implemented in numpy. More, the `Python Reference Manual <http://docs.python.org/ref/augassign.html>`_ specifies that

::

   >>> x = x + y

and

::

   >>> x += y

should result in x having the same value (though not necessarily the same identity). More, even if the numpy developers wanted to modify this behaviour, python does not provide an overloadable :underline:`indexed_iadd` function; the code acts like

::

   >>> tmp = A.__getitem__([0,1,1,2])
   >>> tmp.__iadd__(1)
   >>> A.__setitem__([0,1,1,2],tmp)

This leads to other peculiarities sometimes; if the indexing operation is actually able to provide a view rather than a copy, the :underline:`iadd` writes to the array, then the view is copied into the array, so that the array is written to twice.

NumPy/SciPy installation
========================

See also the ["Installing SciPy_"] page.

Basics
------

First make sure that all `NumPy/SciPy`_ prerequisites are installed and working properly.  Then be sure to remove any old !NumPy/!SciPy_ installations (e.g. /usr/lib/python2.4/site-packages/{numpy,scipy} or $HOME/lib/python2.4/site-packages/{numpy,scipy}).

Prerequisities
~~~~~~~~~~~~~~

NumPy requires the following software installed:

1. `Python <http://www.python.org>`_ 2.4.x or 2.5.x

Debian packages: python python-dev

Make sure that the Python package distutils is installed before continuing. For example, in Debian GNU/Linux, distutils is included in the python-dev package.

Python must also be compiled with the zlib module enabled.

2. A C compiler.

3. Optionally an optimized LAPACK library. Similar, to scipy setup.py script, numpy setup.py script can detect optimized LAPACK libraries in the system. See SciPy_ notes below.

Scipy requires the following software installed:

1. `NumPy <http://www.numpy.org/>`_ 0.9.2 or newer and its prerequisities.

2. Complete `LAPACK <http://www.netlib.org/lapack/>`_ library.

Debian packages: atlas2-headers atlas2-base atlas2-base-dev

Various SciPy_ packages do linear algebra computations using the LAPACK routines. SciPy_'s setup.py scripts can use number of different LAPACK library setups, including optimized LAPACK libraries such as ATLAS :underline:`or the Accelerate/vecLib framework on OS X. The notes below give more information on how to prepare the build environment so that` SciPy_:underline:`'s setup.py scripts can use whatever LAPACK library setup one has.`

:underline:`3. C and Fortran compilers.`

Installation using tar-ball
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unpack numpy/scipy-<version>.tar.gz, change to the numpy/scipy-<version> directory, and run

::

   python setup.py install

This may take several minutes to an hour depending on the speed of your computer.  This may require root privileges.  To install to a user-specific location instead, run

::

   python setup.py install --prefix=$MYDIR

where $MYDIR is, for example, $HOME or $HOME/usr.

Testing
~~~~~~~

To test SciPy_ after installation (highly recommended), execute in Python

::

   >>> import numpy
   >>> numpy.test(level=1)
   >>> import scipy
   >>> scipy.test(level=1)

where the test level can be varied from 1 to 10. To get detailed messages about what tests are being executed, use

::

   >>> numpy.test(level=1, verbosity=2)

for instance.

Customizing
-----------

Compilers
~~~~~~~~~

Note that !NumPy/!SciPy_ is developed mainly using GNU compilers. Compilers from other vendors such as Intel, Absoft, Sun, NAG, Compaq, Vast, Porland, Lahey, HP, IBM are supported in the form of community feedback.

gcc 3.x compilers are recommended.  gcc 4.0.x also works on some platforms (e.g. Linux x86).  SciPy_ is not fully compatible with gcc 4.0.x on OS X.  If building on OS X, we recommend you use gcc 3.3, by typing:

::

   gcc_select 3.3

Building NumPy requires only a C compiler. To build SciPy, also a Fortran compiler is required.

If BLAS/LAPACK libraries used by NumPy_ linalg module is built with a Fortran compiler, then linking extension modules must be carried out with Fortran linker (then all necessary Fortran compiler specific libraries are correctly linked to extension modules). This is the only case where Fortran compiler is required for building NumPy.

You can specify which Fortran compiler to use by using the following install command

::

   python setup.py config_fc --fcompiler=<Vendor> install

To see a valid list of <Vendor> names, run

::

   python setup.py config_fc --help-fcompiler

IMPORTANT: It is highly recommended that all libraries that scipy uses (e.g. blas and atlas libraries) are built with the same Fortran compiler.

xplt for plotting
~~~~~~~~~~~~~~~~~

If after installing scipy, you want to follow a manual and encounter commands about xplt for plotting, the following could be interesting:  `http://www.scipy.net/pipermail/scipy-user/2006-April/007693.html`_

Basically, to enable xplt, you have to edit the file setup.py in /Lib/sanbox/. However, it seems that in the last tarball (0.4.9), xplt is not present anymore and enabling it causes an error at built time.

Known installation problems
---------------------------

BLAS sources shipped with LAPACK are incomplete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some distributions (e.g. Redhat Linux 7.1) provide BLAS libraries that are built from such incomplete sources and therefore cause import errors like

::

   ImportError: .../fblas.so: undefined symbol: srotmg_

Fix: Use ATLAS or the official release of BLAS libraries.

LAPACK library provided by ATLAS is incomplete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will notice it when getting import errors like

::

   ImportError: .../flapack.so : undefined symbol: sgesdd_

To be sure that !NumPy/!SciPy_ is built against a complete LAPACK, check the size of the file liblapack.a - it should be about 6MB. The location of liblapack.a is shown by executing

::

   python numpy/distutils/system_info.py lapack

To fix: follow the instructions in `Building a complete LAPACK library <http://math-atlas.sourceforge.net/errata.html#completelp>`_ to create a complete liblapack.a. Then copy liblapack.a to the same location where libatlas.a is installed and retry with scipy build.

Using ATLAS 3.2.1
~~~~~~~~~~~~~~~~~

If import clapack fails with the following error

::

   ImportError: .../clapack.so : undefined symbol: clapack_sgetri

then clapack is probably using ATLAS 3.2.1 but linalg module was built for a newer versions of ATLAS.

Using non-GNU Fortran Compiler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If import scipy shows a message

::

   ImportError: undefined symbol: s_wsfe

and you are using non-GNU Fortran compiler, then it means that any of the (may be system provided) Fortran libraries such as LAPACK or BLAS were compiled with g77.

Recommended fix: Recompile all Fortran libraries with the same Fortran compiler and rebuild/reinstall scipy.

Using non-GNU Fortran compiler with gcc/g77 compiled Atlas/Lapack libraries
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

When Atlas/Lapack libraries are compiled with GNU compilers but one wishes to build scipy with some non-GNU Fortran compiler then linking extension modules may require -lg2c. You can specify it in installation command line as follows

::

   python setup.py build build_ext -lg2c install

If using non-GNU C compiler or linker, the location of g2c library can be specified in a similar manner using -L</path/to/libg2c.a> after build_ext command.

Intel Fortran Compiler
::::::::::::::::::::::

Note that code compiled by the Intel Fortran Compiler (IFC) is not binary compatible with code compiled by g77. Therefore, when using IFC, all Fortran codes used in SciPy must be compiled with IFC. This also includes the LAPACK, BLAS, and ATLAS libraries. Using GCC for compiling C code is OK. IFC version 5.0 is not supported (because it has bugs that cause SciPy_'s tests to segfault).

Minimum IFC flags for building LAPACK and ATLAS are

::

     -FI -w90 -w95 -cm -O3 -unroll

Also consult 'ifc -help' for additional optimization flags suitable for your computers CPU.

When finishing LAPACK build, you must recompile ?lamch.f, xerbla.f with optimization disabled (otherwise infinite loops occur when using these routines)

::

     make lapacklib   # in /path/to/src/LAPACK/
     cd SRC
     ifc -FI -w90 -w95 -cm -O0 -c ?lamch.f xerbla.f
     cd ..
     make lapacklib

Advanced Issues
---------------

Why numpy headers are installed using add_data_dir and not add_headers?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable several versions of numpy to be installed at the same time, as well as to deal more easily with eggs.

More precisely: add_headers install headers system-wide (e.g. in /usr/include/ on unix if /usr is the prefix for installation), whereas add_data_dir install the headers in package-specific location (for example somewhere in /usr/lib/python2.5/site-packages/numpy/). Installing the headers system-wide prevents multiple version of numpy to be installed at the same time, and that's why add_headers use is discouraged for numpy/scipy.

Troubleshooting
---------------

If you experience problems when building/installing/testing SciPy_, you can ask help from `scipy-user@scipy.org`_ or `scipy-dev@scipy.org`_ mailing lists. Please include the following information in your message: os.name, ``uname -a``, sys.platform, sys.version, numpy.version:underline:`, ATLAS version, compiler versions, etc.  This information can be generated by executing:`

::

Feel free to add any other relevant information. For example, the full output (both stdout and stderr) of the SciPy installation command can be very helpful. Since this output can be rather large, ask before sending it into the mailing list (or better yet, to one of the developers, if asked).

In case of failing to import extension modules, the output of

::

   ldd /path/to/ext_module.so

can be very informative.

Miscellaneous Issues
====================

Why doesn't the bdist_rpm command work with config_fc?
------------------------------------------------------

The bdist_rpm in Python distutils hardcodes python setup.py build command for building rpms and so any additional options given in command line are not passed to the acctual build command. So, bdist_rpm has never worked together with config_fc. As a workaround, do the following:

1) Run

::

     python setup.py bdist_rpm
     python setup.py bdist_rpm --spec-only

to create rmpbuild tree and dist/package.spec.

2) Edit the setup.py build command in dist/package.spec. For example, insert config_fc --fcompiler=absoft just before the setup.py build command.

3) Insert the _topdir definition line to dist/package.spec, for example

::

   %define _topdir %(echo $PWD)/build/bdist.linux-i686/rpm

4) Run

::

     rpmbuild -ba  dist/f2py_ext.spec

This will create package rpm files somewhere under build/bdist.linux-i686/rpm/ directory.

RPM experts are welcome to simplify the above howto.

.. ############################################################################

.. _TableOfContents: ../TableOfContents

.. _MlabWrap: ../MlabWrap

.. _AudioLab: ../AudioLab

.. _GenericOpt: ../GenericOpt

.. _OpenOpt: ../OpenOpt

.. _PySparse: ../PySparse

.. _eric@enthought.com: mailto:eric@enthought.com

.. _ParallelProgramming: ../ParallelProgramming

.. _SciPy: ../SciPy

.. _NumPy/SciPy: ../NumPy/SciPy

.. _NumPy: ../NumPy

.. _scipy-user@scipy.org: mailto:scipy-user@scipy.org

.. _scipy-dev@scipy.org: mailto:scipy-dev@scipy.org

