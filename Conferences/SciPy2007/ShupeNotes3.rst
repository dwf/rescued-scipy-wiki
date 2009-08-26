#format rst

SciPy 2007 Conference Day 1 Notes
=================================

by David Shupe

::

   SciPy 2007 Conference - 16 Aug 2007

   [Note: my editorial comments are in square brackets.]

   Ivan Krstic - OLPC, Science, Awesome

   Main point is education.    Before school, learning is curiosity-driven,
   all-day, peer-based, happens everywhere.  Then, learning is
   authority-driven, select hours, unidrectional, in a particular place.

   Works with a great teacher.  Not at all with no teacher.  1.2 billion
   kids, 75% with inadequate access to education.

   Top down fixing of schools? takes 50-100 yr and others are working on it.
   Try a peer-based approach.  Can do laptops now.
   AMD Geode LX 0.8Wh, 433 MHz, 256 MB RAM, 1GB flash.  Like a desktop
   machine around 2000.  Readable in sunlight!
   Mesh networking: self-contained ARM processor on separate power
   rail, operational during suspend.  802.11s pre-implementation (also
   exising b and g).

   Touchpad: capacitive (normal) and resistive (thermal?).
   Open source, new gui called Sugar, optimized for kids, emphasizes
   collaboration and simplicity.  New security platform called Bitfrost,
   very high security w/o user involvement.  Tried and true stack mostly,
   perturbed in strange ways.
   LinuxBIOS, OpenFirmware, Linux, HAL, X.org, D-BUS, GTK+, HippoCanvas,
   NetworkManager, Telepathy, Jabber/XMPP, Mozilla XULRunner, Python,
   AbiWord, SQLite, OHM, Matchbox, CSound...

   Beta-4 / C-test machines.  Mostly a delta from PyCon.  New processor
   has more L1/L2 cache, runs Python much, much better.

   E Jones: How did you choose this stack?
   A: Has to be small. OS has to fit in 100-150 MB. Don't want to have
   to recharge every 3-4 hr when just reading.  Aggressive approach to
   power management.  Want to suspend in 150msec and resume in 150msec,
   every few seconds -- very challenging for software.

   Q: How much space left over after infrastructure? A: TBD.
   OS takes 200-250 MB, want 100-150 MB.
   Q: Who writes children's s/w?  A: Anyone can contribute, can play with Sugar.
   Q: Is everything Python? A: Biggest chunks (e.g. Sugar).

   Fernando: Why Python?
   A: Allen Kaye, Seymour Papert are constructionists.  Wanted something
   kids can take apart and see how it works, without CS degree.  Python
   is one of the friendliest languages that you can write production code.
   Ivan is one of the drivers for using Python.  Reduces complexity.

   Perry: How do you know this is what is really needed?  Trying out
   prototypes?
   A: Not listening well!  Have had them with 100's of kids, can see
   reports on our wiki, e.g. Nigeria, Brazil?  Ivan suprised there hasn't
   been more resistance or backlash, working surprisingly well.

   Q: Did kids play with Python?
   A: Africa: CS professor visited, kids started asking him questions, one
   kid asked permission to install programming environment on school PC.

   Personal opinion territory now!
   Science: an obvious question that no one asks me at my talks:
   Assuming kids use these to learn learning, what should they use
   learning to learn?  If you now can teach yourself things, what to learn?
   Why is learning important?
   Literature, history and the arts are crucial....but most pressing need
   is for scientific knowledge.  Health, power (electrical), home and communal
   e.g. 14-yr-old William Kamkwamba from Malawi, built a windmill from rough
   plans from a library book.  Imagine if he had all of Wikipedia/Project
   Gutenberg/Google.

   Something you (in audience) could build:
   MetaSci.  In hacker community, MetaSploit reduces overhead in writing
   Proof of Concept exploits.  Boilerplate is included.
   In scientific community, you learn about discoveries either from
   mainstream publications or from the real papers if you can afford
   the journals.  [ What about arXiv.org?  Free physics and astronomy preprints.]
   It'd be awesome to read about a discovery and get a partial dataset
   and visualizations that highlight what the researchers found.  Ivan's
   half-baked idea.  But it's an enormous hassle for scientists to build
   a cross-platform demo.  Choose a vis. toolkit and API, and make
   simple HyperCardish notecards, tables and a way to break into the
   Python shell...couple of hours of work for a scientist.  Ivan is
   confident enough people could be convinced to roll demo sets.
   [ my thoughts: takes a Ph.D. to understand "jargon".  Mainstream
   journalism explanations of science take a lot of work. ]

   Demo
   Measure activity.  Response to lighter flame.
   Australia: water leak from PVC pipe.  Set up XO with a motion detector
   and camera.  After a few days had photos of 10 different species of birds.
   Buttons: Measure A, Set bias o, Show Deta, Stop, Show FFT.
   Can attach cheap $1 sensors, waterproof.

   Next talk:
   Travis Oliphant: will be joining Enthought!  Will be moving to
   Austin on Monday.  Will double the number of kids at
   the Enthought Christmas party! :)

   Average attendee - 1st three eigenfaces from yesterday!

   Numpy in Python:
   - a long-term goal.  We haven't wanted to commit to the release
   schedule.  No one has stepped up to argue our case with other Python
   developers.  Now NumPy is even "bigger" than it was in the past.

   Tactical change:  Get the structure of NumPy into Python 3.0
   via the buffer interface.  Start with changes to Python 3.0 and
   then backport additions to Python 2.6.  Eventually, the demand for
   some of the rest of NumPy will increase.  (PEP for Python 3.0 gets
   more attention from Python developers.  May take 10 yr??)

   Array interface:
   Numeric, numarray, NumPy all use to share data.
   Hatched idea after talking to Guido last SciPy (2006), of buffer
   protocol.  With help of Carl Banks and Greg Ewing and others on
   py3k-dev, PEP 3118 grew out of TO's early efforts. (harder than
   writing a paper!  requires a lot of attention, peer review)

   PEP 3118 Overview
   - redefines tp_as_buffer fcn ptr table for every PyTypeObject
   - Adds PyMemoryViewObject (memoryview in Python) -- will be the 1st
   object in Python to support multi-D slicing.
   - expands struct module with new character-based syntax.
   - creates new C-API fcns to make common things simple for extension
   writer.  Python user won't see much change.

   Timeline: happening now.  Goggle Sprint is next week.  MemoryViewObject
   needs work.  Struct module needs work.  Bug fixes on what's already
   implemented.  Python 3.0 alpha release at end of August.

   tp_as_buffer:
   old: 4 items,get buffer, write buffer, get seg, get charbug.
   couldn't share the data.
   new: 2 items: get_buffer, release_buffer.  Introduces a way to
   lock buffer.  In Python 2.x, always got a new pointer to get around
   the pointer.  New, requires users to release buffer when not needed
   anymore, to allow e.g. allocating more memory.

   Getbuffer
   ojb, view, flags, return

   Pybuffer structure [I can't really follow these slides]

   New C_API:
   PyObject_CheckBuffer (make sure is present)
   PyObject_GetBuffer
   PyObject_ReleaseBuffer
   PyBuffer_FromContiguous, ToContiguous
   PyObject_CopyData
   PyBuffer_IsContiguous
   PyBuffer_FillContiguousStrides
   PyBuffer_FillInfo
   PyMemoryView_Check
   PyMemoryView_GetContiguous,FromObject, FromMemory

   If you have ideas, now is the time!  Can get into Python 3.0.

   MemoryView Object

   Struct-string syntax.

   Implications:
   - standard way to share data among media libraries
   - standard way to share arrays among GUIs
   - increase adoption on NumPy-like features by wider Python community
   - Powerful struct/ctypes connection
   - maybe automatic compiled function call-backs using function-pointer
   data.

   Interested?  Google code Sprints (Aug 22-25), contact Travis before
   Aug 21 AM for guidance.


   Chris Mueller - "CorePy: Using Python on IBM's Cell/B.E."

   Cell/B.E. : high performance processor, in Playstation, Toshiba products
   Cell is whole platform.  B.E. is broadband engine.
   Heterogeneous multicore processors (have different fcns)
   SPE - Synergeistic Processing Element (SPE) cores (8)
   two general PPC cores
   -In-order execution on all cores.
   - Programmer-managed local store on SPUs
   -3 instr sets: PowerPC (PPE), VMX/AltiVec (PPE/SIM), SPU(SPE/SIMD)

   Linux:
    - IBM or Mercury Blades (2 Cell/BE, 16 SPUs, 1 GM RAM)
    - Sony PS3 (1 Cell/BE, 6 SPUs enabled)

   PPU details
   - Full PowerPC and VMX instruc. sets
   - 2 h/w threads, 2 levels of cache,
   - very minimal hardware implementation
      use PPU's as little as possible, disappointing perfomrance

   SPEs are more interesting
    SIMD instr set with.  256k local store.  lots of registers (128).
    Single Instruction, Multiple Data - one add works on 4 pieces of data.

   Cell programmming models
    - Manager/Worker (PPE's dispatch work to SPEs)
    - Pipelined execution (each SPE is a stage in a pipeline)
    - SPE Threads
       treat each SPE as a thread in the program, minimal use of PPE,
         processor in memory: move code in and out more often than data.

   Cell/Python Programming Model
    - Use Python for low-performance tasks
    - Use native kernels for high-perf. tasks
    - Pass pointers from Python-allocated data to SPE kernels
    - Process data in blocks when possible

   CorePy
    library for creating and executing PowerPC, VMX, and SPU programs
         from Python.
    Execute arbitrary SPE programs from Python
    Talk to SPE programs using libspe wrappers
    Create new SPE or PPE programs directly from Python

   CorePy Components
   Example:
     Population counts (popc) counts number of 1 bits in a bit vector
     Assembly-level.
     spu_popc: Pop. count in C.

   Exposed pthread-like interface so can use all cores.

   Python examples.

   iterator examples.
   auto-parallelization for embarrassingly parallel problems.

   CorePy pop counts, Take 3 - works on any length of vector.

   PS3 example: Lyapunov Fractals.
    3.65 FPS, ~21 GOps, ~10 GFlops. Video rendered to a framebuffer in
      main memory.

   Source distribution, evaluation license.
   Tested on IBM Cell Blades, PS3, Apple G4/G5 Macs

   http://www.corepy.org

   Michele [ pronounced "meekala"]  Vallisneri (JPL),
   "Python and the Mock LISA Data Challenges"

   ligo.caltech.edu, www.ligo.org, lisa.nasa.gov

   Gravitational-wave basics
   Measured in amplitude (1/R); do not form images; detectors are
   quasi-omnidirectional.  f < 10 kHz.  Difficult to absorb and scatter.
   Emitted coherently by the bulk motion of matter.  Emitted by massive
   and compact objects: strong gravity.  4.8e-20 ((m/Msun)/(r/Mpc))*(v/c)**2
   [lots of time spent on this slide, intro to gravitational-wave astronomy.
   As an astronomer I really dig this, but what of the rest of the audience?]

   LISA: a constellation, solaar orbit 20 deg from Earth.  (Movie from MPifGP)
   Laser Interferometry can detect small changes (5e6 km baseline).

   Supermassive black holes in active galactic nuclei.
   70% of local galaxies show evidence of mergers.
   Inspiral, merger, and ringdown (of BHs).

   Measurements are hard.  Statistical theory of detection:
   Strategies: Orthogonality and Coincidence.

   Mock Lisa Data Challenges:
    why: encourage development of tools and techniques
    how: compete in analysis of synthetic data sets w/ instrument noise
      and GW source of undisclosed parameters.
    Challenge 1: some Galactic binaries, isolated SMBH binaries
       posted June 2006, evaluated Dec 2006
    Challenge 2: [didn't catch]

   tasks
   compute random GW source parms   -  Python script
   -> lisaXML file

   compute grav. waveforms - standalone C/C++ code w/ Python wrappers
   -> lisaXML file

   compute LISA response & noises - Python module, legacy C w/ Python wrappers
   -> lisaXML file

   Put everything together - Python script
   -> lisaXML file

   Python made it possible. in 3 months
   - intuitive IO library for XML format.
   - steering scripts with easy access to OS.
   - efficiently & simply wrap C/C++ GW codes using SWIG
   - Wrap legacy app with "set-file" IO
   - Write master installer script that calls various setup.py and
      configure/make within SVN.
       need a one-step install for end users and verification on new platforms...
       Installs all the needed packages (numpy, SWIG, etc.) in non-system
          directory.

   Data format:
      Python & XML make a very strong pair.
      Text-based format reassuring (parsed by humans, less dependent on
             I/O libraries or formats like HDF & FITS)
      XML promising

     But....binary file performance would have been nice:
        datasets contain big arrays (130 Mbytes)

     XSIL (Extensible Scientific Interchange Language)
      developed by Roy Williams et al at Caltech's CACR
      based on eight simple XML elements

   Building a natural Python interface for lisaXML
     Everything in XML is mapped into Python.

   SWIG interface module.  Inherits from lisaXML

   Thanks to Python, numpy, pyRXP....


   MLDC: astrogravs.nasa.gov/docs/mldc
   Code:
   sourceforge.net/projects/lisatools

   - Lunch -

   Peter Wang - Interactive Plotting for Fun and Profit
   (Enthought)

   House assessment data.  Interactive demo of Chaco.
   YearBuilt, Mkt_Value, SqFtCost.
   Scatter plot + color/symbol code.  Select data, linear regression
   to selected data.  Got a pretty good deal on his house assessment.

   Prosper.com.  Peer-to-peer lending.  3-yr loans, not collateralized,
   up to $25k.
   Plot lender rate history for different borrower credit ratings.
   Can get a dump of Prosper credit data.
   1. Get data.
   2. Get Robert Kern to write code.
   3. Get a pile of data.
   Turning items into numpy record arrays.
   DebtToIncomeRatio vs. LoanStatus
   CurrentRating vs. LoanStatus
   Conclusion: Prosper is a little more dangerous than other places
   [for lenders, or borrowers?  Lenders?]

   Multitouch scatter plot.  IR illumination blasting screen from behind.
   Camera reads finger spots.  Image processing of spots, which moved
   between frames and which did not.  60 fps camera, can keep up with
   processing.

   Chris Lee - "PyGr: The Python Graph Database Framework for Bioinformatics"
   (UCLA, Ctr for Computational Biology)

   What is PyGr?
   - sequence analysis & comparative genomics tools.
   - Python, plus Pyrex / C extensions where crucial.

   Competing models of languages:

   - Scripting for piping results from one program to another, parsing
   output formats, etc.
   - A model of core properties of the data, its inter-relationships,
   and how we formulate questions about it (eg. sequences, mappings).
   [ I love this slide!!]

   What should our goal be?
   - Bioperl dominates bioinformatics, so we often have to answer
   "Why bother with Python".
   - Should we just replicate same functionality w/ better syntax?
   - Or take beyond scripting? make modeling data easy and natural

   Thesis: Python's core models are already a good model of Bioinfo. data
   - Sequence:
   - Mapping/ Graphs
   - Attributes

   e.g scripts typically store a sequence as a string.
   - this ignores our need for a representation.
   e.g. Python sequences: can be sliced.  Any slice is a slice.
   String: str(s).  Could come from file, SQL...
   Add Allen interval logic: union, intersection, before, after, etc.
   Add orientation to handle DNA sequences. (strand orientation)

   Multiple Storages, Same Interface
   - Sequence: Python object in memory
   - SQLSequence: slice query to relational dB
   - BlastSequence: slice query to NCBI fastacmd
   - FileDBSequence: slice query via fseek to disk
   All follow same interface, interchangeable.  Only needs
   two customizations: __len__(), __str()__

   Hypergraphs: A General Model for Bioinformatics
   Sequence Alignment: Nodes: sequence letters or intervals.
           Edges: links between sequences.

   Python Mapping
     M[node1] -> node2
   Need Graph:
     M[node1][node2] -> edgeinfo
   node 1 is a source node, node 2 is a target node, edge connects
   the two.

   Alternative Splicing Example:
   in SQL, requires a 6-way JOIN, for a simple example.
   In Python,
     q = {1: {2:None, 3:None},2:{3:None}} # no edge info
    for d in GraphQuery(g,q): print 'exons',d[1],d[2],d[3]
   Simpler because the data really is a graph; SQL schema is
   not a good prepresentation of that.

   Benefits of Graph Query
   - Data is actually a graph.  Query is also a graph.
   - The SQL is a mess, unusable except by experts.

   "Everything in Python is a dictionary" (mapping)
   All Python Data (Already) IS a Graph Database!

   Intervals.  Intervals are sorted by xstart, ystart, xend, yend.
   Can stop search at first non-overlapping interval.
   Query time is millisec: proportional to number of items that
   will be returned.
   10-500 times faster than R-Tree.  Published.

   Pygr.Data: A Namespace for Scientific Data & Schema
   - Would like obtaining complex database + dependencies as easy as:
   Python import foo.bar.you.  All you need is "name".
   - The ultimate graph database: all bioinformatics data and their relations
   could be available.

   - Object marked with its pygr.Data ID
   - Automatically saves any dependencies (again by ID).
   - Uses Python pickle: objects must be picklable.

   Demo
   import pygr.Data defaults to XMLRPC server at UCLA.

   http://www.bioinformatics.ucla.edu/pygr

   [This was a fabulous talk!  It made me think a lot about modeling the
    data for my own area.]

   BREAK

   Lightning Talks

   **Fernando Perez - TConfig - Traits-based declarative configuration for programs.
   Traits: typed variables with validation and automatic GUI generation.

   from enthought.traits.api import HasTraits,Int,Float

   class C(HasTraits):
     n = Int(10)
     x = Float(2.5)

   TConfig = Traits + ConfigObj

   Written 2 weeks ago, in ipython/saw/sandbox.

   **Len Reder - Mars Science Laboratory at JPL

   Mars rover.  140 threads that are constantly running.

   Formal interface specs (XML).
   Python tools generate tested and well-understood patterns.
   Template "Cheetah" in Python

   No Python interpreter on rover.  Everything is C code that looks
   like it is from 20 yr ago.

   **Climate Data Analysis Tools (CDAT) - Charles Doutriaux

   Goal: Provide scientific community with tools to allow them to focus
   on science NOT technical aspects.

   Current Version: 4.3 (Numeric), 5.0beta (NumPy)
   Contributed packages-- mix of Python and Fortran, most built on top of
     SciPy/f2py.
   One environment, several hundred users.

   http://cdat.sf.net

   **Platform for Intelligent Computing (NuPIC) - Charlie Curry
   Numenta - startup in Menlo Park in NoCal
   Hierarchicaal Temporal Memory (HTM)

   Can break up local computations.

   **Bill Spotz: Numpy.i
   Officially released.  Prabhu says, documentation is awesome!
   It's in the doc directory of every numpy source distribution.

   Trelino: will be available end of August.  Lots of solvers.
   PyTrelinos package.

   **Rick Wagner: Taught intro to scientific computation for high schoolers.
   Kids know computers (Windows) but not programming.
   If you never leave the interpreter, you're not doing scientific computing.
   Borrowed heavily from Software carpentry course by Greg Wilson.
   Had to make it "shinier" for high-schoolers.
   e.g. Quakenator.  Downloads earthquake data and plots.

   Fernando: please put on scipy.org so we'll have a repository of
   courses that people have taught.

   **Brian Granger: PyStream: Stream & GPU computing in Python
   - New emphasis on performance per watt.
   - multicpu, multicore,etc
   Ex. NVidia GPU ($600) 128 cores.
   Ex. Folding@Home - more GFlops on 30k PS3s, more than supercomputers

   NVIDIA CUDA SDK - makes programming GPUs easy for you.
   CUDA makes easier, but in C and lots of boilerplate.
   PyStream - Python can be used for everything but the actual GPU kernel.
    - fully interactive (or not), and lightning fast.
    - integrated with NumPy.  e.g. send FFT to GPUs.
   http://pystream.googlecode.com, BSD license.

   **Prabhu Ramachandran: TVTK and MayaVi2
   Goal: x-platform 2D/3D visualization for scientists and engineers.
   Almost all 2D plotting: matplotlib and Chaco

   TVTK: VTK + Traits + Numpy supportt = Pythonic VTK

   Now MayaVi is standalone outside Envisage.  Now resuable.

   ** Gael Varoquaux - mlab: a pylab-like interface to Mayavi2

   Mayavi Pros
     Interactive, uses VTK= high-quality, feature-rich.
   Limitations;
     Creating VTK data is too involved.  I don't want to learn VTK.

   Run script inside Mayavi,  or run with ipython -wthread.

   API is still changing -> we need feedback.

   enthought.mayavi.tools.new_mlab in Enthought Tools Suite 2.5
     https://svn.enthought.com/enthought/wiki/install

   **Michel Sanner: What's new in MGL Tools

   molecular interactions
   InstallJammer on Linux, Windows,  PackageMaker on Mac OS X.
   Send everything incl. Python.  Can rollback to initial installation.
   Can download nightly build with fix.  Next install of tested version
   invalidates rollback of in-between nightly builds.

   Matplotlib in Vision.

   **Robert Kern: Spectral color maps.
   Spectral color maps  are confusing, RK has color deficiency.
   Colormap viewer in 3D.
   Allows interesting analysis of colormaps.
   Any that Robert likes? Grey, Heat, some diverging that have white
   at center and diverge smoothly to two different colors at the extremes.

   End of lighning talks.

   BASIN - Dept of Physics, Drexel University, Enrico Vesperini

   Stellar Dynamics, Cosmology

   Another can come in, and share data with me!

   IPython Engines.

   BASIN kernel: classes and fcns for data distribution and parallel data
   operations (C++/MPI)

   Packages for: Cosmology, Stellar dynamics, Statistics,
   FFT (FFTW), Coordinate Transformations.

   BASIN Python interface created with Boost Python.

   A remote Python client can invoke BASIN commands to be executed
   by the Data Analysis Engine.

   Multiple distributed clients can connect to same BASIN engine and
   share data (based on IPython1, terrific tool!)

   Visualization: VisIt (www.llnl.gov/visit)
   Visualization of large distributed datasets
   Also plotting based on GnuPlot API.  Or can use whatever you
   want on the client machine after data are transferred.

   Goals: Ease access to parallel data analysis.
   Avoid redundant developement.
   Interactive and multi-user parallel data analysis.

   What we have:
   Kernel for parallel data mgmt and operations
   Scientific packages
   A few visualization packages

   Next up:
   Increase science scope beyond astrophysics
   Extend visualization options
   2-way communication with visualization packages
   Improve ease of use and installation

