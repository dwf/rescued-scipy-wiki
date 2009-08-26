#format rst

Below is a list of various projects which are using Numpy and/or Scipy.

If you're using Numpy/Scipy and would like to let the world know about your project, please add it to the list here.  At a minimum please include a short description of the project or product, how it uses numpy/scipy, and a web link.  If there is interesting output then a screenshot of reasonable size would also be appreciated.

**Index** `TableOfContents(2)`_

Middleware
==========

These are library projects that are primarily intended for use by other developers.

Python Imaging Library
----------------------

The Python Imaging Library (PIL) adds image processing capabilities to your Python interpreter. This library supports many file formats, and provides powerful image processing and graphics capabilities.  The latest PIL supports copy-free interchange of data with Numpy. *Someone please verify this -- I'm just making this up!*

* **Link:** `http://www.pythonware.com/products/pil/`_

Matplotlib
----------

Matplotlib is a python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. matplotlib can be used in python scripts, the python and ipython shell (ala matlab or mathematica), web application servers, and six graphical user interface toolkits.  Matplotlib uses Numpy extensively internally for processing data.

* **Link:** `http://matplotlib.sourceforge.net/`_

PyOpenGL
--------

PyOpenGL is the cross platform Python binding to OpenGL and related APIs.  PyOpenGL supports the use of Numpy arrays as inputs and outputs for OpenGL APIs, which makes for a very efficient interface to the underlying C API.

* **Link:** `http://pyopengl.sourceforge.net/`_

PyTrilinos
----------

Trilinos is a set of object-oriented, sparse solver packages, including linear solvers, preconditioners, nonlinear solvers, eigensolvers and related utilities, usable in serial or parallel.  PyTrilinos_ is a Trilinos package that provides a python interface to selected Trilinos packages.  The fundamental linear algebra services package is called Epetra, and the python interface to Epetra is compatible with NumPy_.

* **Link:** `http://software.sandia.gov/trilinos`_

* **Link:** `http://software.sandia.gov/trilinos/packages/pytrilinos`_

Madagascar
----------

Madagascar is an open-source software package for geophysical data analysis and reproducible numerical experiments. It offers: (1) Programs that implement geophysical algorithms and utilities needed by them (linear algebra/etc), and (2) A programming interface to its library of I/O in geophysical data formats and associated tools. This programming interface has been implemented for C, C++, F77, F90, Matlab and Python. The Python interface uses Numpy arrays and a few of the programs use Numpy and SciPy_.

* **Link:** `http://rsf.sourceforge.net/`_

Applications
============

These are some end-user applications that make use of Numpy and Scipy.

Inkscape
--------

Inkscape is an Open Source vector graphics editor, with capabilities similar to Illustrator, Freehand, CorelDraw_, or Xara X using the  W3C standard Scalable Vector Graphics (SVG) file format.   Inkscape can use effect extensions written in Python, and the latest version includes an extension that uses Numpy to distort an image with a perspective transformation.  There will likely be more of this in Inkscape's future.

* **Link:** `http://www.inkscape.org`_

PyPedal
-------

PyPedal_ (Python Pedigree Analysis) is a tool for analyzing pedigree files. It calculates several quantitative measures of genetic diversity from pedigrees, including average coefficients of inbreeding and relationship, effective founder numbers, and effective ancestor numbers. Checks are performed to catch common mistakes in pedigree files, such as parents with more recent birthdates or smaller ID numbers than their offspring and animals appearing as both sires and dams in the pedigree. Tools for pedigree visualization and report generation are also provided. NumPy_ is used for computation of numerator relationship matrices and for visualization.

* **Link:** `http://pypedal.sourceforge.net/`_

* **Screenshots:** `http://sourceforge.net/project/screenshots.php?group_id=106679`_

PanelCheck
----------

PanelCheck_ is a tool that allows the user to monitor the performance of sensory panels by means of various types of plots. These plots are based on the results of different univariate and multivariate statistical methods analysing the variation in the data, giving insight in individual differences between assessors as well as panel performance globally. PanelCheck_ is based on: Python, Numpy, Scipy, matplotlib, wxPython.

* **Link:** `http://www.matforsk.no/panelcheck`_

* **Link:** `https://sourceforge.net/projects/sensorytool/`_

* **Screenshots:** `https://sourceforge.net/project/screenshots.php?group_id=163531&ssid=32792=`_

PyMC
----

PyMC is a python module that implements the Metropolis-Hastings algorithm as a python class, and is extremely flexible and applicable to a large suite of problems. PyMC includes methods for summarizing output, plotting, goodness-of-fit and convergence diagnostics. PyMC uses NumPy_ and Matplotlib.

* **Link:** `http://code.google.com/p/pymc/`_

SfePy
-----

SfePy is a finite element solver written in Python, with the time demanding parts implemented in C and interfaced by SWIG. It can be used to solve various problems described by partial differential equations in 2D or 3D, for example the linear elasticity, hyperelasticity, heat conduction, Navier-Stokes, Biot, and other problems. As a research code it is used to implement models derived by the theory of homogenization, with applications in modeling of porous media (for example bones or soft tissue organs) or phononic materials. It relies on !NumPy/!SciPy_ with UMFPACK, Pyparsing, and Matplotlib.

* **Link:** `http://sfepy.kme.zcu.cz`_

* **Development:** `http://sfepy.org`_

Topographica
------------

Topographica is a neural-network modeling package focusing on biologically detailed simulations of large sheets of neurons in the cortex and other brain areas.  Topographica is designed to allow neuroscientists and computational scientists to simulate and understand how topographic maps contribute to brain function.  The simulator uses NumPy_ arrays throughout to represent two-dimensional arrays of neurons, connections, and patterns of neural activity.

* **Link:** `http://topographica.org`_

* **Screenshots:** `http://sourceforge.net/dbimage.php?id=75314`_

PyPIV
-----

PyPIV is a Particle Image Velocimetry (PIV) analysis tool focusing on simple, FFT-based cross-correlation interrogation algorithm to assess the flow velocity fields from the image of flows seeded with tracers.  PyPIV is designed to allow fluid mechanics students and researchers to analyze the PIV realizations.  The algorithm uses NumPy/SciPy/PIL/Matplotlib functions to read images, iteratively cross-correlate through the arbitrary shaped interrogation windows and obtain flow velocity vector maps, shown by a quiver plot. PyPIV is a clone of a popular Matlab(tm) open-source toolbox, abbreviated URAPIV (since 1997).

* **Link:** `http://urapiv.wordpress.com/2006/02/08/i-want-to-break-free/`_

* **Link:** `http://sourceforge.net/projects/pypiv`_

MDP
---

Modular toolkit for Data Processing (MDP) is a Python data processing framework. From the user's perspective, MDP is a collection of supervised and unsupervised learning algorithms and other data processing units that can be combined into data processing sequences and more complex feed-forward network architectures. From the scientific developer's perspective, MDP is a modular framework, which can easily be expanded. The implementation of new algorithms is easy and intuitive. The new implemented units are then automatically integrated with the rest of the library. The base of available algorithms is steadily increasing and includes, to name but the most common, Principal Component Analysis (PCA and NIPALS), several Independent Component Analysis algorithms (CuBICA, FastICA, TDSEP, and JADE), Slow Feature Analysis, Gaussian Classifiers, Restricted Boltzmann Machine, and Locally Linear Embedding.

* **Link:** `http://mdp-toolkit.sourceforge.net`_

.. ############################################################################

.. _TableOfContents(2): ../TableOfContents(2)

.. _PyTrilinos: ../PyTrilinos

.. _NumPy: ../NumPy

.. _SciPy: ../SciPy

.. _CorelDraw: ../CorelDraw

.. _PyPedal: ../PyPedal

.. _PanelCheck: ../PanelCheck

