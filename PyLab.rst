#format rst

Currently this page reflects the vision of KeirMierle_, and not necessarily the community as a whole. By integrating consensus from mailing list discussions, I will refine and polish this vision and form a plan of action such that the community can move the numpy+scipy+ipython+matplotlib ensemble closer to the vision outlined below.

THIS IS NOT COMPLETE YET

See the following post for further discussion of the difference between the vision for a new PyLab expressed on this page, and the existing pylab package which is part of matplotlib:

  `http://www.nabble.com/pylab-td24910613.html`_

The PyLab Vision
================

To make PyLab an easy to use, well packaged, well integrated, and well documented, numeric computation environment so compelling that instead of having people go to Python and discovering that it is suitable for numeric computation, *they will find PyLab first and then fall in love with Python.*

The philosophy behind this vision is to consider Rails and Ruby; while Ruby was somewhat popular beforehand, it was Rails which propelled it to the forefront.

At the moment, the current combination of Python, NumPy_**,** SciPy_**, Matplotlib, and IPython** provide a compelling environment for numerical analysis and computation.  **Unfortunately**, for those who are not already familiar with Python and the intricacies of how to build your own Python environment, or for those not familiar with the details of how there are conflicting names exported by different modules, or how the best list of NumPy_ examples is found on the wiki in a non-obvious place (and that the docstrings are not the best documentation), or that the speed of linear algebra operators is dependent on a carefully compiled combination of LAPACK, ATLAS, and Goto BLAS, or a host of other reasons (some outlined below), **the picture is not nearly so rosy.**

Short-term Goals
~~~~~~~~~~~~~~~~

1. **Documentation** - Dramatically enhance the standard documentation by consistently adopting the new DocstringStandard_ for all functions in the NumPy_ API.

#. **API Consistency** - Create an official API for the PyLab system such that there is an official way to import the PyLab packages, and such that there are not multiple functions with very similar names in different packages.

#. **Installation** - Make the installation process trivial, especially for, e.g. people without root access or spare time.

#. **Build Process** - Make the build process simple for the combination of the five core components (Python, NumPy_, SciPy_, Matplotlib, and IPython).

A simple user story
~~~~~~~~~~~~~~~~~~~

Joe is frustrated with Matlab, because he finds it is slow when running his neural network experiments. He hears about PyLab from a friend, who recommends it as an alternative.

1. He finds PyLab as the first search result on Google

#. He finds a page with **minimal clutter**, showing a couple pictures of PyLab, and a direct download link to a binary for his operating system. He notes that pylab.org must have determined he is running Linux automatically. The page also has a small number of **big, clear links** to promotional materials (screencasts, testimonials), documentation, and community information (how to get involved).

#. After downloading, the program installs with no hassles, and Joe can launch Pylab by typing 'pylab' and pressing enter in a terminal. Joe is happy that there was no hassle over dependencies on his older university computer, and that installing directly into his home directory (he does not have root access on the university computers) is not a problem.

#. PyLab notices that it is the first time it is run, and suggests he read the tutorial, and provides a link.

#. Joe clicks the tutorial link, which his terminal automatically pops up in a browser. The tutorial covers the basics of PyLab, explaining some of the philosophy. The tutorial is clearly written, and covers the basics of array computation and 2D graphing.

#. When Joe is implementing code, he finds the interactive help invaluable, provided by typing any object or function with a '?' after it in the interactive prompt. The documentation has **copious examples and helpful pointers** to other functions which may be useful (See also:).

#. Joe implements and runs his neural network simulations, and manages to speed them up by using one of the several methods of optimizing computation in the tutorial. He is so pleased with the results he suggests to his instructor that the entire class should switch to PyLab, as it is free and as far as Joe can tell, **superior in almost every way to MATLAB.**

There are some details omitted here (such as in step 3, does Joe untar the downloaded file or is it an executable?), but those are not the point. The point is that PyLab is a compelling, integrated, usable and superior alternative to MATLAB.

Why the PyLab name? Isn't that already taken by Matplotlib?
-----------------------------------------------------------

PyLab should be the name of the entire suite, and I feel strongly that the correct way to import the entire core PyLab API should be via

::

   from pylab import *

This should include the core parts of numpy, scipy, and matplotlib. This should also be the default namespace set up when the program is launched interactively via 'pylab'. Whether the other components (such as numpy.linalg.*) should be included in this import is up for debate.

1. Revamping the Documentation
==============================

For now this section only talks about docstrings, and ignores the other forms of documentation (tutorial, guide, etc). If you want to fill out this section please do!

Docstring standard
~~~~~~~~~~~~~~~~~~

Travis Oliphant posted a `draft docstring standard on January 10th 2007 <http://article.gmane.org/gmane.comp.python.scientific.devel/5572>`_ which is the basis for the following proposed standard, which is now the DocstringStandard_ page. Please look at it.

Available modules in docstrings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Examples in docstrings are extremely valuable. However, it is currently never the case that the docstrings in either NumPy_ or SciPy_ use any of the functionality offered by matplotlib. This in unfortunate, especially in the case of SciPy_, because often the clearest way of demonstrating a function is to plot something.

While it is true that there is an argument which says that SciPy_ should not become dependent on matplotlib, it appears that this dependence already exists for all intents and purposes. It is likely that only in the most extreme cases one would want to use SciPy_ without matplotlib. Furthermore, the dependency would only be in the case where a user is executing docstrings in the interactive interpreter; in this case, it is highly likely that the user is doing something which requires some sort of plotting package regardless.

2. Fixing API consistency
=========================

The current PyLab ensemble has issues with API consistency, mainly stemming from Matplotlib's compatability layer. For example, **consider the load function**, which exists in both NumPy_ and Matplotlib:

::

   >>> from pylab import *
   >>> load.__doc__
   '\n    Load ASCII data from fname into an array and return the array.\n\n ....'
   >>> from numpy import *
   >>> load.__doc__
   'Wrapper around cPickle.load which accepts either a file-like object or\n    a filename.\n    '

This function isn't matched! They are clearly different, yet each accepts a filename, and each will break in mysterious ways when one is expecting the functionality of the other. This is especially hard to track down when one is editing a script and running it where the script's import order causes numpy.load to be present, but in the interactive terminal the user has open pylab.load is the exposed function. **This is bad.**

Another example is the confusion around the min and max functions overwriting the builtins, then breaking in weird and unexpected ways. It appears this is now sorted out, with numpy.amax and numpy.amin being the array versions, with numpy.min and numpy.max new names for numpy.amin/amax. I feel as though from numpy import * should import min and max, but import a min and a max that throw an exception!

Here's a list of conflicts between SciPy_ and Matplotlib:

::

   In [12]: import pylab
   In [13]: import scipy
   In [14]: p=set(dir(pylab))
   In [15]: s=set(dir(scipy))
   In [16]: k=p.intersection(s)
   In [17]: conflicts = [f for f in k if id(scipy.__dict__[f]) != id(pylab.__dict__[f])]
   In [18]: import matplotlib
   In [19]: matplotlib.__version__
   Out[19]: '0.87.7'     <--- this was a pre 0.90 svn IIRC
   In [20]: conflicts[0]
   Out[20]: 'cumsum'
   In [21]: pylab.cumsum?
   Type:           function
   Base Class:     <type 'function'>
   String Form:    <function cumsum at 0xb6731924>
   Namespace:      Interactive
   File:           /usr/lib/python2.4/site-packages/numpy/oldnumeric/functions.py
   Definition:     pylab.cumsum(x, axis=0)
   Docstring:
       <no docstring>
   In [22]: scipy.cumsum?
   Type:           function
   Base Class:     <type 'function'>
   String Form:    <function cumsum at 0xb774d5a4>
   Namespace:      Interactive
   File:           /usr/lib/python2.4/site-packages/numpy/core/fromnumeric.py
   Definition:     scipy.cumsum(x, axis=None, dtype=None, out=None)
   Docstring:
       Sum the array over the given axis.
   In [23]: conflicts
   Out[23]: ['cumsum', 'ptp', 'fix', 'ravel', '__file__', 'ones', 'rank', 'tri',
   'insert', 'arange', 'indices', 'loads', 'where', 'mean', 'argmax', 'nonzero',
   'asarray', 'sum', 'polyfit', 'prod', 'log2', 'power', 'cumproduct', 'corrcoef',
   'meshgrid', '__name__', 'cov', 'cumprod', 'vander', 'arccos', 'load', 'array',
   'iterable', 'eye', 'log', 'sometrue', 'alltrue', 'zeros', 'log10', '__doc__',
   'empty', 'polyval', 'arcsin', 'arctanh', 'linspace', 'typecodes', 'copy',
   'std', 'fromfunction', 'argmin', 'trapz', 'binary_repr', 'sqrt', 'take',
   'product', 'repeat', 'trace', 'compress', 'array2string', 'amax', 'identity',
   'amin', 'fromstring', 'average', 'base_repr', 'reshape']

Most of these are via oldnumeric, but not all. Either way, all oldnumeric functions exposed via pylab shouldn't be.

The single import statement
---------------------------

What most users want is for a single import statement to get a consistent set of packages which fulfil most of their needs. This should consist of:

::

   from pylab import *

That gets them NumPy_, SciPy_, and Matplotlib. A rough equivalent would be:

::

   from pylab import *
   from numpy import *
   from scipy import *

But there are so many names!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not really. from scipy import * brings in about 20 subpackages (i.e. signal such that you still need to do signal.ifft, but not scipy.signal.ifft) and only 15 new symbols.

How to fix the API
------------------

Fixing the API will involve a discussion between the core maintainers of each of the core modules (excepting IPython): NumPy_, SciPy_, and Matplotlib.

3. Fixing installation process
==============================

The installation process has certainly gotten easier over the years; however, the packages in PyLab core should be bundled in a cohesive whole so that the user is not even aware that there are several packages beneath the PyLab label. Certainly, for the busy undergrad who needs to get his signal processing homework done but can't afford MATLAB and doesn't have root access on his university computers it makes sense to have a monolithic binary which bundles everything (ala SAGE).

4. Fixing the Build process
===========================

Building a basic PyLab setup is straightforward on Debian and Ubuntu thanks to package management, provided one is capable of fishing around for the required build packages. However, a straight forward

::

   python setup.py build

will not produce the most optimized executable; in order to get a highly optimized PyLab system, an elaborate dance is required to compile the BLAS, then Goto BLAS, then LAPACK with that BLAS, then replace a subset of LAPACK with optimized versions from ATLAS. The whole process is entirely unintuitive and, as far as the author can tell, not clearly documented **anywhere**, even for Linux.

Becoming a better foundation for SAGE
=====================================

There is a package called `SAGE <http://sage.math.washington.edu/sage/>`_ which aims for almost exactly the same goals as PyLab. However, it is even more extreme than the PyLab vision outlined here, because SAGE includes many third party programs for cutting-edge support of symbolic computation. It also makes some incompatible changes to the Python syntax.

SAGE is built from a core of Python, IPython, and NumPy_. In a `posting <http://arcknowledge.com/gmane.comp.mathematics.sage.devel/2006-12/msg00111.html>`_ to the SAGE developer list, the lead SAGE developer, William Stein, described how he wishes NumPy_ and SciPy_ would follow more consistent documentation standards. Shortly thereafter Travis Oliphant committed the documentation standard which should be used in NumPy_ and SciPy_. **By slowly working the docstring documentation into a consistent state, PyLab can form a more consistent and usable foundation for SAGE.**

.. ############################################################################

.. _KeirMierle: ../KeirMierle

.. _NumPy: ../NumPy

.. _SciPy: ../SciPy

.. _DocstringStandard: ../DocstringStandard

