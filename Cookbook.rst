#format rst

This page hosts "recipes", or worked examples of commonly-done tasks.    Some are introductory in nature, while others are quite advanced (these are at the bottom of the page).  We encourage new users to post recipes even for simple tasks that are not yet represented here.  Our goal is an easy learning experience for new users.  Some of these recipes may be incorporated into tutorials in the future.

NumPy / SciPy
=============

* [:Cookbook/BuildingArrays:Building Arrays] Introduction to numerical arrays.

* [:/Indexing:Indexing] Indexing numpy arrays, from simple to complicated.

* [:/Interpolation:Interpolation] Examples of interpolation (see also [:Cookbook/Matplotlib/Gridding irregularly spaced data:Gridding irregularly spaced data]).

* [:Cookbook/Rebinning:Data rebinning] Examples of rebinning data to produce smaller arrays with and without interpolation.

* [:Cookbook/LinearRegression:Linear regression] Simple Linear regression example.

* [:Cookbook/OLS:Fit statistics] Estimates a multi-variate regression model and provides various fit statistics.

* [:Cookbook/OptimizationDemo1:Optimization] Quick example of fminbound with plot.

* [:Cookbook/OptimizationAndFitDemo1:Optimization with fit] Similar to above with spline fit and chaco plot.

* [:Cookbook/Finding Convex Hull:Convex Hull] Finds the convex hull around a set of data points

* [:Cookbook/MultiDot:Multiplying multiple arguments] Generalizing ``dot(a,b)`` to the case of N arguments.

* [:Cookbook/KalmanFiltering:Kalman Filtering] Example from the Welch & Bishop [`http://www.cs.unc.edu/~welch/kalman/kalmanIntro.html`_ Introduction to the Kalman Filter].

* [:`/FittingData`_:Fitting Data] Day to day work in the lab: fitting experimental data.

* [:Cookbook/CommTheory:Comm Theory] Example of BPSK simulation.

* [:Cookbook/SignalSmooth:Smoothing a signal] Performing smoothing of 1D and 2D signals by convolving them with a window.

* [:Cookbook/FiltFilt:A zero phase delay filter] Sample code for a null phase delay filter that processes the signal in the forward and backward direction removing the phase delay.

* [:Cookbook/RANSAC:RANSAC algorithm] Implementation of the robust estimation method.

* [:Cookbook/SavitzkyGolay:Savitzky Golay filtering of data] Sample code for Savitzky Golay filtering.

* [:/Multithreading:Multithreading] Easy multithreading for embarrassingly parallel problems

* [:`/SphericalBesselZeros`_:Spherical Bessel Zeros] Finding the zeros of the spherical Bessel functions and its derivative

* [:`/RadialBasisFunctions`_:Radial Basis Functions] Using radial basis functions for smoothing/interpolation

* [:`/SegmentAxis`_:Segment axis] Devious trick using strides to allow general operations (like convolution) on successive, overlapping pieces of an array

* [:`/MetaArray`_:MetaArray_] Class for storing per-axis meta information with an array (axis names, column names, units, etc.)

* [:/Obarray:Obarray] Trick for avoiding object arrays when dealing with arrays of objects.

* [:/Recarray:Recarray] Accessing array columns with structured arrays and recarrays.

* [:/KDTree:KDTree] Searching multidimensional space using kd-trees.

* [:Cookbook/ParticleFilter:Particle Filter] A simple particle filter algorithm for tracking objects in a video sequence.

* [:LoktaVolterraTutorial:Lotka-Volterra Tutorial] Solving ordinary differential equations with Scipy

* [:Cookbook/CoupledSpringMassSystem:A coupled spring-mass system] Another example of solving differential equations. 

* [:Cookbook/Solving Large Markov Chains:Large Markov Chains] Find the stationary distribution of a large Markov chain; the M/M/1 tandem queue

* [:Cookbook/Watershed:Watershed algorithm] Apply the watershed algorithm in order to split an array into distinct components (e.g. for the segmentation of an image into objects).

* [:Cookbook/Intersection:Intersection of functions] Compute the points at which two given functions intersect.

Advanced topics
---------------

* [:Cookbook/ViewsVsCopies:Views vs Copies] A quick introduction to array views and some caveats on situations where you should expect a data view or a data copy.

Compiling Extensions
====================

* [:Cookbook/CompilingExtensionsOnWindowsWithMinGW:Compiling Extensions on Windows] A quick tutorial on how to compile extension modules on Windows using MinGW

SciKits
=======

* [`http://scipy.org/scipy/scikits/wiki/OpenOpt`_ OpenOpt_] numerical optimization example for [`http://projects.scipy.org/scipy/scikits/browser/trunk/openopt/scikits/openopt/examples/nlp_ALGENCAN.py`_ NLP] (non-linear problem), [`http://projects.scipy.org/scipy/scikits/browser/trunk/openopt/scikits/openopt/examples/nsp_1.py`_ NSP] (non-smooth), [`http://projects.scipy.org/scipy/scikits/browser/trunk/openopt/scikits/openopt/examples/qp_1.py`_ QP] (quadratic), [`http://projects.scipy.org/scipy/scikits/browser/trunk/openopt/scikits/openopt/examples/lp_1.py`_ LP] (linear), [`http://projects.scipy.org/scipy/scikits/browser/trunk/openopt/scikits/openopt/examples/milp_1.py`_ MILP] (mixed-integer LP)

* [`http://pytseries.sourceforge.net`_ timeseries] Includes examples for plotting, reporting, frequency conversion, and more. Some recipies at ["/TimeSeries/FAQ"].

Scientific Scripts
==================

* [:Cookbook/Theoretical Ecology:Theoretical Ecology]

* [:Cookbook/SchrodingerFDTD:Schrödinger's equation]: a 1-d FDTD solver that animates the time evolution of a gaussian wave packet interacting with simple potentials.

Input Output
============

* [:Cookbook/ASTER:Reading ASTER files]

* [:Cookbook/hdf5 in Matlab:Loading hdf5 in Matlab]

* [:Cookbook/Reading mat files:Reading Matlab .mat files]

* [:Cookbook/DataFrame:DataFrames] A useful class for storing alphanumerical data, similar to GNU R's data frames.

* [:Cookbook/Data Acquisition with PyUL:Data acquisition with PyUniversalLibrary_] A series of examples using an inexpensive USB data acquisition device from Measurement Computing.

* [:Cookbook/Data Acquisition with NIDAQmx:Data acquisition with Ni-DAQmx] A simple example of using ctypes and numpy to access data acquisition devices from National Instruments.

* [:Cookbook/InputOutput:input/output] Reading and writing a NumPy array from/to an ascii/binary file.

* [:/FortranIO:Fortran I/O] Reading FORTRAN record-structured binary files (if you don't know what these are, thank your stars and you don't need this).

* [:Cookbook/Reading_SPE_files:Reading SPE files] Reading SPE binary files produced by CCD cameras (Princeton and like).

Graphics
========

There are several packages available to produce interactive screen graphics (use the mouse to zoom, orient, and fine-tune) and publication-quality printed plots, in 2D, 3D, and 4D (animations).  These packages have releases more frequently than SciPy_.  Rather than bundling out-of-date packages with SciPy_, the plotting packages are released separately.  However, their developers work closely with the SciPy_ developers to ensure compatibility.

* ["Plotting Tutorial"].

.. THIS IS A BROKEN LINK!  Anyone have the page?

.. See also the [http://www.scipy.org/documentation/plottutorial.html old version].

* [:Cookbook/Matplotlib:Matplotlib cookbook].  Matplotlib is the preferred package for 2D graphics.

* [:Cookbook/Matplotlib/mplot3D:3D Plotting with Matplotlib]. Simple 3D plots using matplotlib and its now-included 3D capabilities.

* [:Cookbook/xplt:Plotting with xplt].  xplt is very fast but less flexible than matplotlib.  It allows simple 3-d surface visualizations as well. It is based on pygist (included) and is available under the sandbox directory in SVN scipy.

* [:Cookbook/MayaVi:MayaVi/TVTK cookbook]. 3D plotting and data visualization with MayaVi2 (and TVTK): a very powerful interactive scientific data visualizer.

* [:Cookbook/PIL:Python Imaging Library]. Create/manipulate images as numpy array's.

* [:WilnaDuToit:Mat3d]. Simple 3D plotting using an OpenGL backend.

* [:Cookbook/LineIntegralConvolution:Line Integral Convolution] code in cython for visualizing vector fields

* [:vtkVolumeRendering:VTK volume rendering]. This is a simple example that show how to use VTK to volume render your three dimensional numpy arrays.

Using NumPy With Other Languages (Advanced)
===========================================

* A [:PerformancePython:comparison] of Weave with NumPy, Pyrex, Psyco, Fortran and C++ using Laplace's equation as an example.

* Using [:Cookbook/Pyrex and NumPy:Pyrex and NumPy_] to share data between your Pyrex/C extension module and NumPy.

* Using [:Cookbook/ArrayStruct and Pyrex:Pyrex and the array_struct interface] to access array data without requiring a C dependency on Numeric, numarray, or NumPy.

* **NumInd**: [:Cookbook/A Numerical Agnostic Pyrex Class:A Numerical Agnostic Pyrex Class] to access Numeric/numarray/!NumPy_ arrays in an uniform way from both C and Pyrex space.

* Using [:Cookbook/SWIG and NumPy:SWIG and NumPy_] to access and modify NumPy arrays in C libraries.

* **numpy.i**: A few [:Cookbook/SWIG NumPy_ examples:SWIG and numpy.i] basic examples.

* **numpy.i**: Using [:Cookbook/SWIG Memory Deallocation:SWIG and numpy.i] to handle automatic C memory deallocation from Python (using a modified numpy.i).

* Using [:Cookbook/F2Py:f2py] to wrap Fortran codes.

* Using [:Cookbook/f2py and NumPy:f2py and Numpy] to wrap C codes.

* Writing [:Cookbook/C Extensions:C Extensions].

* Using [:Cookbook/Ctypes:ctypes with NumPy_].

* Using ["/Weave"] and **iterators** for fast, generalized code.

Scientific GUIs
===============

* Using [:Cookbook/wxPython dialogs:wxPython dialogs] for simple user interaction.

* Using ["TraitsUI"] to build interactive applications.

-------------------------



  **List of all pages in the category "Cookbook":**

  `FullSearch(regex:(----(-*)(\r)?\n)(.*)CategoryCookbook\b)`_

-------------------------



  CategoryCookbook_

-------------------------



  CategoryCookbook_ CategoryCookbook_ CategoryCookbook_ CategoryCookbook_ CategoryCookbook_

.. ############################################################################

.. _MetaArray: ../MetaArray

.. _OpenOpt: ../OpenOpt

.. _PyUniversalLibrary: ../PyUniversalLibrary

.. _SciPy: ../SciPy

.. _NumPy: ../NumPy

.. _`FullSearch(regex:(----(-*)(\r)?\n)(.*)CategoryCookbook\b)`: ../FullSearch(regex:(----(-*)(\r)?\n)(.*)CategoryCookbook\b)

.. _CategoryCookbook: ../CategoryCookbook

