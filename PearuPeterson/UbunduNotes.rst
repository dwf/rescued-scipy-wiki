#format rst

Notes on installing Numpy/Scipy and friends on a Ubundu
=======================================================

Computer: Mobile Pentium 4, 2.2GHz

OS: Ubuntu 5.10, Linux kernel 2.6.12-10-386

Python: 2.4.2

Local setup to simplify installing python modules as an ordinary user:

::

   # chown -R pearu:admin /usr/local/

Prerequisities
--------------

Minimal set of software packages for building numpy:

::

   python-dev gcc

Minimal set of software packages for building scipy:

::

   python-dev gcc g77 g++

Additional recommended software packages for getting higher performance in numpy/scipy components:

::

   atlas3-base-dev atlas3-sse2

Check using

::

   python numpy/distutils/cpuinfo.py

for 3dnow, sse, sse2 support in your CPU.

Building and testing NumPy
--------------------------

::

   $ cd svn/numpy
   $ python setup.py install --prefix=/usr/local
   $ cd      # get out of numpy source directory
   $ python
   >>> import numpy
   >>> numpy.test(10)
   ...
   Ran 354 tests in 2.302s
   ...
   OK

To rebuild numpy, run

::

   $ cd svn/numpy
   $ rm -rf build
   $ python setup.py install --prefix=/usr/local

Building and testing SciPy
--------------------------

Optional packages for building SciPy packages:

::

   libumfpack4-dev swig
   fftw3-dev

Note: libumfpack4 is linked against atlas2 libraries.

To install scipy, run

::

   $ cd svn/scipy
   $ python setup.py install --prefix=/usr/local
   $ cd # get out of scipy source directory
   $ python
   >>> import scipy
   >>> scipy.test(10)
   ...
   Ran 1520 tests in 65.730s
   ...
   OK

Installing matplotlib
---------------------

Building matplotlib requires the following packages to be installed:

::

   libglib2.0-dev libgtk2.0-dev python-gtk2-dev tk8.4-dev dvipng

Make sure that you can open display from a command prompt, e.g. use ``ssh -X`` login, before trying to build matplotlib.

Get matplotlib from svn:

::

   $ svn co https://svn.sourceforge.net/svnroot/matplotlib/trunk/matplotlib matplotlib

To install and test matplotlib, run

::

   $ cd svn/matplotlib
   $ python setup.py install --prefix=/usr/local
   $ cd
   $ export NUMERIX=numpy
   $ python
   >>> from pylab import *
   >>> plot([1,2])
   >>> show()

Installing ipython
------------------

Get ipython from svn:

::

   $ svn co http://ipython.scipy.org/svn/ipython/ipython/trunk ipython

::

   $ cd svn/ipython
   $ python setup.py install --prefix=/usr/local
   $ cd
   $ ipython -pylab
   >>> plot([1,2])

Installing Enthought (numpy port)
---------------------------------

To install enthought, you must have the following packages installed:

::

   python-vtk libxtst-dev

To use enthought, have the following packages installed:

::

   python-wxgtk2.6 python-celementtree msttcorefonts

To install and test enthought, run

::

   $ cd svn/enthought_lib_numpy
   $ python setup.py install --prefix=/usr/local
   $ cd
   $ python
   >>> import enthought
   >>> enthought.test()

