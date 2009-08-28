#format rst

MYMPI
-----

-------------------------

 **Using a generalized MPI interface for Python, MYMPI**

*Authors: Timothy H. Kaiser University of California San Diego - San Diego Supercomputer Center*

*Sarah Healy University of California San Diego - Biology Department*

*Leesa Brieger University of California San Diego - San Diego Supercomputer Center*

**Abstract:**

-------------------------

 We introduce an MPI Python module, MYMPI, for parallel programming of Python with the Message Passing Interface (MPI). This is a true Python module which runs with a standard Python interpreter.

In this paper we discuss the motivation for creating the MYMPI module, along with differences between MYMPI and pyMPI, the familiar MPI Python interpreter. Additionally, we discuss two projects that have used the MYMPI module: Continuity, in computational biology, and Montage, for astronomical mosaicking.

The main difference between pyMPI and MYMPI is that pyMPI is actually a custom version of the Python interpreter along with a module. Our version, MYMPI, is a module only that can be used with a normal Python interpreter.

There is also a fundamental difference in the semantics of the two packages. With pyMPI the Python interpreter is the parallel application. With MYMPI the code executed by the interpreter is the parallel application.

For C and Fortran MPI, the routine MPI_Init is used to initialize a MPI program. That is, every process in the parallel job must call MPI_Init. pyMPI departs from this standard operating procedure. pyMPI programs do not call MPI_Init because the interpreter is the MPI application and it calls MPI_Init on startup. In MYMPI, programs explicitly call MPI_Init. One of the reasons why MYMPI was created was to provide better control of how and when MPI_Init is called.

As much as practical, MYMPI follows the syntax and semantics of C and Fortran MPI. pyMPI has a more OOP flavor. We chose to match C and Fortran more closely because we intended from the start that we would be writing programs that mixed Python with the other languages. Also, the training materials we have developed for teaching standard MPI can be used with MYMPI. All our training examples have been rewritten in Python and work in combination with the Fortran and C examples.

MYMPI is much smaller since it is only a module not a full interpreter. It is also smaller because it only implements about 30 of the 120+ MPI calls. MYMPI builds in seconds and has been installed using, vendor, MPICH, and LAM versions of MPI under AIX, OSX, Redhat, and SuSiE.

Continuity is a computational tool for continuum problems in bioengineering and physiology, especially those related to cardiac mechanics and electrocardiology research. Python is employed for user interfaces, communication, object-oriented component integration and wrapping of computationally efficient FORTRAN functions.

Currently Continuity uses the MYMPI module to allow communication between a root Python process and multiple Fortran processes that perform compute-intensive ODE integration over the order of tens or hundreds of thousands of timesteps. Simulating the spread of electrical activation in a 3D finite element model of part of the rabbit heart (1024 elements, 1377 nodes, 8192 gauss points) resulted in a maximum speedup over the serial code of 15x on 32 nodes. We expect the parallel efficiency to improve with larger problems. The use of the MYMPI module has made possible investigations into biological phenomena that take place of timescales exceeding one beat, e.g. the effect of sympathetic nervous system activation.

Larger simulations will be limited by root process memory. We plan to extend our use of SuperLU, a linear solver, to the distributed version of the package. We will make use of MPI-specific communicator splitting in order to separated the linear solve processes and ODE integration processes.

The MYMPI module has served as part of the workflow management software developed for the Montage astronomical mosaicking project. The MYMPI module facilitated managing in a single parallel job submission, the production of many mosaics. In this project, the three-band infrared Two Micron All Sky Survey (2MASS) is being mosaicked with the Montage software into 6-degree squares. 5202 such mosaics cover the entire sky for the three bands and will serve as pages in the HyperAtlas, now under construction as part of the National Virtual Observatory (NVO) project to federate disparate astronomical surveys. The MYMPI module enabled us flexibility in managing job steps on many CPUs of a parallel machine. During the execution we alternated easily between two levels of granularity, that is, a collection of independent single processor tasks and whole machine MPI parallel applications.

