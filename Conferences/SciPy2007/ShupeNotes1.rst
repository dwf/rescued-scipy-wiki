#format rst

Tutorial Day 1 Notes
====================

by David Shupe

::

   SciPy 2007

   Tutorial, Fernando Perez and Brian Granger, 14 Aug

   Resources page; Py4Science repository (F. Perez and J. Hunter), lots of
   examples
   STScI tutorial has been updated for numpy!

   I've started with
   Python 2.4.1
   numpy 1.0.1
   IPython 0.8.1
   matplotlib 0.90.1
   SciPy 0.5.2

   Had to install from Fernando's tarballs
   zope interface in Twisted subdirectory
   Twisted 2.5.0 from tarball
   setuptools from tarball
   ipython1 from tarball

   ipython dutil.py

   %rundemo demo1_basic

   logstart -o -r -t

   ,concat Ladies Gentlemen # automatically quotes the arguments

   %run is the most important command in IPython!

   [I can't run qt4 because no PyQt4 installed -- demo3_qt4.py]
   [have to install SIP and PyQt4]

   Break - moved to Beckman Institute Auditorium!!

   Fernando continues...

   wallis example

   qsort exercise (we filled in code ourselves!)

   schrod_fdtd nice example in examples directory

   Brian Granger
   -------------

   Serial example of "wordfreq" : run wordfreq, print_wordfreq(freq)

   Startup scripts
     ipcontroller
         Used to start the Controller
         The Controller listens on a number of ports and must be
            started first
     ipengine
         Used to start a single Engine after the Controller is running
         This script can be started using mpirun
     ipcluster
         Starts on Controller and N Engines on localhost or an ssh-based
           cluster


   Within IPython:
   import ipython1.kernel.api as kernel
   ipc = kernel.RemoteController(('127.0.0.1', 10105))

   ipc.getIDs()

   autopx # Auto Parallel -- for e.g. defining fcns on all engines

   ipc.pushAll(a=10,b=set())
   ipc.push(0,b={'a':range(10)})
   px print b

   ipc.pullAll('a')

   # Fernando tip: _26 returns result of computation #26 in IPython

   ipc['b'] = 10  # shorthand for push
   ipc['b']       # shorthand for pull

   ipc.keysAll()

   import numpy

   ipc.scatterAll('a',a)  # Divides up the sequence
   px import time
   px time.sleep(3) # takes 3 sec on controlling ipython session

   ipc.block = False

   ipc.execute('time.sleep(5)')  # Returns instantly, a pendingResult object

   pr = _
   pr.getResult()  #same as pr.r


   ipc.map?  # Parallelized verion of Python's builtin map

   Another interface - Task Controller - does some load balancing

   Back to Fernando: Iterators

   Numpy iterators - there's a chapter in a book, on how Travis did it for numpy.

   Python cookbook: n-way mergesort

   In IPython: run nwmerge.py

   Back to Brian:
   MPI - can use mpi-2-py(?) in IPython

   More examples - link on Fernando's resource page
     parallel_pylab.py

   Intro to the TaskController
    Dynamically load-balanced, fault-tolerant task farming using the engines.
     Controller = task master, engines = workers.
     More powerful but less general than the RemoteController interface.
     Details of specific engines are hidden.
     RemoteController and TaskController interfaces can be used together
      at the same time to great effect.

   Example: mcdriver, mcpricer  Monte-Carlo options pricer in parallel

   tc.run?

   run mcdriver.py
   # Can add or kill engines on the fly!! (didn't quite work when I tried it)

   plot_options(K_vals, sigma_vals, vp) # vanilla put
   plot_options(K_vals, sigma_vals, vc) # vanilla call

   Warning! Have to think about how to parallelize your arrays.  Can easily
   make parallel version slower than serial version.  If you're pushing and
   pulling large arrays, it will be slower.

   Fernando: This is an open-source effort!  Help needed.  If this is useful
   for your work, then please do participate and contribute.

   IPython has 4-5 steady developers and a few occasional contributors.
   Numpy has maybe 10 active.  Same for SciPy.  Matplotlib has 5-6
   steady developers. 


   Titus Brown: Idiommatic Python
   (need to get a handout)

   Iterators, enumerate
   for i, item in enumerate(z):
      print i, item

   Python cookbook: recommended!  explore corners of Python.

   Remember __getattr__ to find out about all special methods.

   Modules vs. scripts:
   put in a '-' into script names because it can't be imported!
   PEP-8 suggests keeping module names to one word.

   Titus likes to use packages to organize files, not symbols.  Better
   to keep all symbols at top-level as in Python stdlib.

   PEP 8 - Style Guide for Python Code

   my_package
   my_module
   my_function

   ThisIsMyClass

   _my_variable (private)

   How modules are loaded (and when code is executed)

   Easy Install
   Part of setuptools (which I had to install for ipython1)
   See the "easy_install" command

   (coffee break)

   sets

   "any" and "all" in Python 2.5

   Exceptions and exception hierarchies

   Function decorators

   subprocess replaces os.system, os.popen, os.popen2....

   Audience suggestion: pexpect module (pipes don't get full)

   Unit test: should only work with code, not the filesystem or the database.
   Tests should emit no output when they succeed.

   doctest allows tests to be embedded inside docstrings or elsewhere in file.

   Titus's document is written in Restructured Text


