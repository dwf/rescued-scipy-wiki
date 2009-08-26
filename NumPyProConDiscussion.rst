#format rst

NumPy_ (and associated packages) can be used as an alternative to packages such as MATLAB, Octave, Yorick, and tela; the advantages and disadvantages are summarized at NumPyProConPage_. This page is for a more free-form discussion. Take its contents with even more than the usual Wiki-sized grain of salt.

Some aspects of PyLab_ can only be expected to measure up once some package reaches a stable state. See PyLabAwaits_.

Integration
-----------

* Having a mass of separate packages complicates every bug-tracking operation, as many of them are version skew.

* Presenting a single, more-or-less uniform UI to the user would make their life much easier

* Putting the pieces together in one package would allow developers to focus on making the pieces fit together well - for example, will pylab plot Matrix objects without complaining?

* Providing a canonical bundle would resolve the "which package do I want?" problem for users, and focus developer attention on a smaller number of packages. (Of course, this isn't so good if one chooses *bad* packages for the bundle...)

* A canonical distribution would make a task-oriented ScientificCalculationHowto_ much easier to write (although the ["Cookbook"] is a good start)

UI
--

* For the command-line Linux wonks, the UI seems quite satisfactory - ipython+editor of choice seems more or less adequate

  * Can the editor communicate with a running ipython? ("put a breakpoint here and run the file again" or "take me to the line where the exception occurred")

* Under windows, the terminal seems to be pretty ugly, so people using ipython feel unhappy. (A better terminal program?)

  * **GV =** GaelVaroquaux_ Once IPython gets its new front end this will be easy, maybe by reussing some of the work of enthought.

  * For a better terminal on windows, takes a look at Console: `http://sourceforge.net/projects/console/`_. It looks like it can work with ipython, and it gives you a terminal with easy cut/copy/past, many fonts, tabbed terminals, etc...

* A unified IDE-type environment might be handy

  * Are we interested in xmaple-style "worksheets" with embedded plots and (possibly) pretty-printed results?

    * **GV** I have tryed to offer part of this functionality throught `pyreport <http://gael-varoquaux.info/computers/pyreport>`_, eventhought it does not offer the interactive part of the notebooks. At least it ease editor agnostic and uses files that are still standard python files.

* OpenMath_ cut-and-paste?

* A source level profiling tool would be great. That's something I miss a lot from matlab (profile on - run matlab code - profile report;  gives you the time spent in each function, and at each line. I don't know if it is doable in python)

  * **AMA** - have you tried the python profiler? If you have it installed and are using ipython, it's as easy as %run -p myfile.py (or profile expression() ) and it prints out the time per function (but not per line, unfortunately; I'm not sure that's feasible with python's bytecode design).

Symbolic computation
--------------------

* Even quite simple symbolic computation would be useful; for example, one often needs to compute derivatives, and trying to solve an ODE or integral analytically before bringing out the numerical solvers is often a good idea.

* There seem to be a number of choices:

  * `sympy <http://code.google.com/p/sympy/>`_ - written in python, extremely simple

  * `PyDSTool <http://www.cam.cornell.edu/~rclewley/cgi-bin/moin.cgi/Symbolic>`_'s Symbolic - written in python and based on the Maple syntax model.

  * `swiginac <http://swik.net/swiginac>`_ - automatic wrapper around `ginac <http://www.ginac.de/>`_ (a fast, well-tested C++ library for computer algebra)

  * `pythonica <http://www.tildesoft.com/Pythonica.html>`_ - older code (last web update 2004) based on the Mathematica syntax model.

    * **AMA** My personal feeling is that symbolic computation is a very big job to get right, and we're better off using a system that's been pounded on a bit. It's akin to using ODEPACK or LAPACK instead of writing our own DE solver or LU factorization system. "It's python, of course it's slow" is a bit disingenuous - when the hard work is done by somebody else's optimized library, python need not be slow.

      * **MMF =** MichaelMcNeilForbes_ Some of the need for symbolic computations may be relieved if a good, easy to use automatic differentiation package existed.  In particular, for solvers that require jacobians etc. automatic differentiation can work very nicely.

        * **AMA** I agree, symbolic differentiation is relatively easy and would cover a lot of what people need. In fact, if we want symbolic derivatives of everything in scipy.special, we will probably need to implement them more-or-less by hand no matter which tool we choose.

        * **OC** SymPy_ can differentiate symbolically. Please report everything, that you find not working, or too difficult to use. It can also solve some differential equations symbolically, if you need more, please write into the Issues on the sympy webpage what functionality you need and sympy developers will help you implement it.

* None of them seem to support Grobner bases, but probably nobody but AMArchibald minds.

  * **OC** SymPy_ supports Groebner bases

Plotting, particularly 3D
-------------------------

* pylab seems to be a credible substitute for MATLAB's plotting program; I find it hard to find anything, and the manual is just a mass of docstrings (which often do not describe, for example, how to get different line styles or black-and-white output).

  * **GV** The best way to build documentation for scipy & Co is probably to rely a lot on the wiki. Hopefully there is a way off export the info to static pages.

* MayaVis_ seems to be the standard tool to recommend for 3D plotting, but it's (another) separate package.

* SymPy_ supports 3D plotting

Installation
------------

* On Linux, getting an out-of-date version is usually easy using your distribution's package manager; more up-to-date versions may also be available (e.g. astraw's Ubuntu packages). Supporting this will become easier if we reach a point where all packages have compatible stable releases.

* On Windows it seems to be painful and complicated.

  * **GV** Certainly not if you are using the enthought distribution.

  * **AS** Over the long term, the Enthought distribution is definately a good option. But that doesn't solve everyone's problems. I can think of at least 2 scenarios in which Windows users will still want to build from source. Firstly, to test bugfixes only available from SVN. Secondly, to compile NumPy_ with a third party BLAS or LAPACK, like ATLAS tuned for a specific processor, Intel's MKL or AMD's ACML. Remember, [`http://eclipse-projects.blogspot.com/2006/09/open-means-buildable.html`_ open means buildable].

    * **AMA** It should indeed be buildable, but I think for the purposes of this discussion, that's not so important. Here we're looking (I gather) at people trying to use PyLab_ as a MATLAB alternative and who want to just use it. People who want to build it from scratch seem like another category entirel, to me.

* On the Mac?

  * **MMF** It was a pain getting everything installed at first, mainly because there are at least four places that things could get installed.  (Apps. and Frameworks for bundles and standard stuff, darwin-ports, fink, and compiled from source packages.)  I had many problems trying to compile things because I had different version of python, libraries etc. from various different source.  Once I cleaned everything up, however, and installed everything from a single source, things worked fine, but there was quite a steep learning curve.  There is the potential for making everything very easy, but looking through the mailing lists seems to indicate that many people stumble here.

* Are other operating systems important for this discussion?

* Post-"installation" installation issues

  * How to help the user set up a sensible PYTHONPATH, particularly if they want contrib files or code they wrote themselves?

  * How to set up a sensible configuration for everything (for example, ipython works much better with a bit of configuration in the user's .ipythonrc)

User-contributed packages
-------------------------

* Not obviously a sensible notion for a project with such open development, but it makes sense to have a "contrib" collection of less-supported, less-developed or less-generally-useful packages that are nonetheless easy to drop in.

.. ############################################################################

.. _NumPy: ../NumPy

.. _NumPyProConPage: ../NumPyProConPage

.. _PyLab: ../PyLab

.. _PyLabAwaits: ../PyLabAwaits

.. _ScientificCalculationHowto: ../ScientificCalculationHowto

.. _GaelVaroquaux: ../GaelVaroquaux

.. _OpenMath: ../OpenMath

.. _MichaelMcNeilForbes: ../MichaelMcNeilForbes

.. _SymPy: ../SymPy

.. _MayaVis: ../MayaVis

