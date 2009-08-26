#format rst

Parallel Programming with numpy and scipy
=========================================

Multiprocessor and multicore machines are becoming more common, and it would be nice to take advantage of them to make your code run faster. numpy/scipy are not perfect in this area, but there are some things you can do. The best way to make use of a parallel processing system depend on the task you're doing and on the parallel system you're using. If you have a big complicated job or a cluster of machines, taking full advantage will require much thought. But many tasks can be parallelized in a fairly simple way.

As the saying goes, "[`http://www.acm.org/ubiquity/views/v7i24_fallacy.html`_ premature optimization is the root of all evil]". Using a multicore machine will provide at best a speedup by a factor of the number of cores available. Get your code working first, before even thinking about parallelization. Then ask yourself whether your code actually needs to be any faster. Don't embark on the bug-strewn path of parallelization unless you have to.

Simple parallelization
----------------------

Break your job into smaller jobs and run them simultaneously
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For example, if you are analyzing data from a pulsar survey, and you have thousands of beams to analyze, each taking a day, the simplest (and probably most efficient) way to parallelize the task is to simply run each beam as a job. Machines with two processors can just run two jobs. No need to worry about locking or communication; no need to write code that knows it's running in parallel. You can have issues if the processes each need as much memory as your machine has, or if they are both IO heavy, but in general this is a simple and efficient way to parallelize your code - if it works. Not all tasks divide up this nicely. If your goal is to process a single image, it's not clear how to do this without a lot of work.

Use parallel primitives
~~~~~~~~~~~~~~~~~~~~~~~

One of the great strengths of numpy is that you can express array operations very cleanly. For example to compute the product of the matrix A and the matrix B, you just do:

::

   >>> C = numpy.dot(A,B)

Not only is this simple and clear to read and write, since numpy knows you want to do a matrix dot product it can use an optimized implementation obtained as part of "BLAS" (the Basic Linear Algebra Subroutines). This will normally be a library carefully tuned to run as fast as possible on your hardware by taking advantage of cache memory and assembler implementation. But many architectures now have a BLAS that also takes advantage of a multicore machine. If your numpy/scipy is compiled using one of these, then dot() will be computed in parallel (if this is faster) without you doing anything. Similarly for other matrix operations, like inversion, singular value decomposition, determinant, and so on. For example, the open source library `ATLAS <http://math-atlas.sourceforge.net/>`_ allows compile time selection of the level of parallelism (number of threads). The proprietary `MKL <http://www.intel.com/cd/software/products/asmo-na/eng/307757.htm>`_ library from Intel offers the possibility to chose the level of parallelism at runtime.  There is also the `GOTO <http://www.tacc.utexas.edu/resources/software/software_downloads.php>`_ library that allow run-time selection of the level of parallelism. This is a commercial product but the source code is distributed free for academic use.

Finally, scipy/numpy does not parallelize operations like

::

   >>> A = B + C
   >>> A = numpy.sin(B)
   >>> A = scipy.stats.norm.isf(B)

These operations run sequentially, taking no advantage of multicore machines (but see below). In principle, this could be changed without too much work. OpenMP is an extension to the C language which allows compilers to produce parallelizing code for appropriately-annotated loops (and other things). If someone sat down and annotated a few core loops in numpy (and possibly in scipy), and if one then compiled numpy/scipy with OpenMP turned on, all three of the above would automatically be run in parallel. Of course, in reality one would want to have some runtime control - for example, one might want to turn off automatic parallelization if one were planning to run several jobs on the same multiprocessor machine.

Write multithreaded or multiprocess code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes you can see how to break your problem into several parallel tasks, but those tasks need some kind of synchronization or communication. For example, you might have a list of jobs that can be run in parallel, but you need to gather all their results, do some summary calculation, then launch another batch of parallel jobs. There are two approaches to doing this in Python, using either multiple [`http://en.wikipedia.org/wiki/Thread_(computer_science`_) threads] or [`http://en.wikipedia.org/wiki/Process_(computing`_) processes].

Threads
:::::::

Threads are generally 'lighter' than processes, and can be created, destroyed and switched between faster than processes. They are normally preferred for taking advantage of multicore systems. However, multithreading with python has a key limitation; the [`http://docs.python.org/api/threads.html`_ Global Interpreter Lock] (`GIL <http://effbot.org/pyfaq/what-is-the-global-interpreter-lock.htm>`_). For various reasons (a quick web search will turn up copious `discussion <http://blog.ianbicking.org/gil-of-doom.html>`_, not to say `argument <http://mail.python.org/pipermail/python-3000/2007-May/007414.html>`_, over [`http://www.artima.com/weblogs/viewpost.jsp?thread=214235`_ why this exists] and [`http://blog.snaplogic.org/?p=94`_ whether it's a good idea]), python is implemented in such a way that only one thread can be accessing the interpreter at a time. This basically means only one thread can be running python code at a time. This almost means that you don't take any advantage of parallel processing at all. The exceptions are few but important: while a thread is waiting for IO (for you to type something, say, or for something to come in the network) python releases the GIL so other threads can run. And, more importantly for us, while numpy is doing an array operation, python also releases the GIL. Thus if you tell one thread to do:

::

   >>> print "%s %s %s %s and %s" %( ("spam",) *3 + ("eggs",) + ("spam",) )
   >>> A = B + C
   >>> print A

During the print operations and the % formatting operation, no other thread can execute. But during the A = B + C, another thread can run - and if you've written your code in a numpy style, much of the calculation will be done in a few array operations like A = B + C. Thus you can actually get a speedup from using multiple threads.

The python threading module is part of the standard library and provides tools for multithreading. Given the limitations discussed above, it may not be worth carefully rewriting your code in a multithreaded architecture. But sometimes you can do multithreading with little effort, and in these cases it can be worth it. See ["Cookbook/Multithreading"] for one example. [`http://code.activestate.com/recipes/576519/`_ This recipe] provides a thread Pool() interface with the same API as that found for processes (below) which might also be of interest. There is also the `ThreadPool <http://www.chrisarndt.de/projects/threadpool/>`_ module which is quite similar.

Processes
:::::::::

One way to overcome the limitations of the GIL discussed above is to use multiple full processes instead of threads. Each process has it's own GIL, so they do not block each other in the same way that threads do. From python 2.6, the standard library includes a `multiprocessing <http://docs.python.org/library/multiprocessing.html>`_ module, with the same interface as the threading module. For earlier versions of Python, this is available as the `processing <http://pyprocessing.berlios.de/>`_ module (a backport of the multiprocessing module of python 2.6 for python 2.4 and 2.5 is in the works here: `multiprocessing <http://code.google.com/p/python-multiprocessing>`_ ). It is possible to share memory between processes, including [`http://coding.derkeiler.com/Archive/Python/comp.lang.python/2008-09/msg00937.html`_ numpy arrays]. This allows most of the benefits of threading without the problems of the GIL. It also provides a simple Pool() interface, which features map and apply commands similar to those found in the ["Cookbook/Multithreading"] example.

Comparison
::::::::::

Here is a very basic comparison which illustrates the effect of the GIL (on a dual core machine).

::

   import numpy as np
   import math
   def f(x):
       print x
       y = [1]*10000000
       [math.exp(i) for i in y]
   def g(x):
       print x
       y = np.ones(10000000)
       np.exp(y)

::

   from handythread import foreach
   from processing import Pool
   from timings import f,g
   def fornorm(f,l):
       for i in l:
           f(i)
   time fornorm(g,range(100))
   time fornorm(f,range(10))
   time foreach(g,range(100),threads=2)
   time foreach(f,range(10),threads=2)
   p = Pool(2)
   time p.map(g,range(100))
   time p.map(f,range(100))

[Table not converted]

For function ``f()``, which does not release the GIL, threading actually performs worse than serial code, presumably due to the overhead of context switching. However, using 2 processes does provide a significant speedup. For function ``g()`` which uses numpy and releases the GIL, both threads and processes provide a significant speed up, although multiprocesses is slightly faster.

Sophisticated parallelization
-----------------------------

If you need sophisticated parallelism - you have a computing cluster, say, and your jobs need to communicate with each other frequently - you will need to start thinking about real parallel programming. This is a subject for graduate courses in computer science, and I'm not going to address it here. But there are some python tools you can use to implement the things you learn in that graduate course. (I am perhaps exaggerating - some parallelization is not that difficult, and some of these tools make it fairly easy. But do realize that parallel code is much more difficult to write and debug than serial code.)

* `IPython1 <http://ipython.scipy.org/moin/IPython1>`_

* ["mpi4py"]

* [`http://www.parallelpython.com/`_ parallel python]

* `POSH <http://poshmodule.sourceforge.net/>`_

.. ############################################################################

.. _ThreadPool: ../ThreadPool

