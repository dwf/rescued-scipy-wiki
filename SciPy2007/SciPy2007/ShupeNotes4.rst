#format rst

SciPy 2007 Conference Day 2 Notes
=================================

by David Shupe

::

   **Terence Yeoh, Evolving Wavelets using SciPy: Analysis of Controlled
      Plasma Transients  (The Aerospace Corporation)
   w/ Gary Stupian, Maribeth Mason, Genghmun Eng, Matthew Begert

   The Era of "Power User" Computing
   -Powerful interpreted code running at near-compiled speed
   -Re-use of other people's code no longer limited to the computer scientist
   (thanks to SciPy!)

   SciPy Tomography
   Used SciPy Array packages to calculate sinogram and backprojections.
   Code written in a matter of days, first program written by user w/minimal
   programming experience.

   Plasma - tin whiskers

   Why are Wavelets important?
   -wavelet decomposition breaks the complex waveforms into manageable bites
     frequency/time maps
     separates random noise without throwing out noise enveloples
   Many uses where FT not applicable
    - single events
    - image compression (jpeg 2000)
    - pattern recognition

   Use of SciPy's GA code for automated signal processing
   - Thousands of plasma events are recorded
   - Self-sorting of signals into self-designated bins are desirable
   - Events are highly variable, "random" noise could be important
   - Standard waveform fitting not iefficitn
   - clustering algorithms needed to sort the dadta

   13 Intel Xeion dual-processor 3 GHz (26 nodes)
   Python 2.3 w/ SciPy 0.3.2 (older version for GA code compatibility)
   Ka-Ping Yee's Delegate.py for hassle-free forking
   Filip Wasilewski PyWavelets code for wavelets
   Armin Rigo's Psyco for "Just iN Time" compliled code

   Openmosix: Moshe Bar's single system image (SSI) clustering
   solution (http://www.openmosix.org)
   -Cluster acts as one large multiprocessor system
      "fork and forget"
   -Useful for MonteCarlo simulations or GA code with independent processes.
   -Compatible with Python forking (Delegate.py)

   SciPy's Genetic Algorithm code
   - Scipy 0.3.2 standard genetic algorithm packages
     populations size, islanding, migrants
     determine fitness fcn
            (rules of the game: whoever does best gets to play again)
   -Fitness fcn in Python

   Used GA code for automated alignment.
   2,500 slices through a semiconductor material.


   Titus Brown - Regulatory Genomics

   Introduction to regulatory genomics
   Most organisms: 20,000 - 45,000 genes (incl. humans)
   It's the architectural plans that make the difference.  Stored
   in our genomes, both in genes and the regulatory regions that
   control gene expression.

   Cartwheel -
     allows biologists to establish sequence analysises, on someone
      else's compute server, visualize and intercact via a client GUI.
     Aimed at "bench biologists" (2-4 yr behind computing trends)
     Intended to be extensible.

   Client GUI connects to Cartwheel Server via XML-RPC
   Cartwheel server talks to batching & queuing system by
      database connection; compute nodes run 3rd-party s/w

   Server:
   Linux, Python, Quixote (for structuring simple websites)
   SCGI to serve Quixote stuff
   PostgreSQL db, psycopg
   Home-grown O/R adapter "cucumber"
   Several subpackages (paircomp, motility) w/Python interfaces
   Client:
   Started with Jython; switch to FLTK (C++).  Cross Platform.
   (Troubles with Jython: distribution a challenge (randomness),
     couldn't get it to run fast, fell behind Python.)
   Uses XML-RPC to communicate with server.

   Comparative Sequence Analysis has turned regulatory region search
   from a 2-yr technically difficult task into a 3-month summer
   student project.  (Lots of money in biology, lots of interesting
   questions to answer, just need analysis ability!)

   Maintenance digression:
   Need to test Web sites -> built twill.
   Need to run tests flexibly -> use nose.
   Need to target more tests -> built figleaf.
   Need to record web tests -> built scotch

   Automated testing rocks! 30% of Web app covered.

   Sociological digression:
   -User pop'n is computationally naive.
   -Existing tools either very simple oor impossible to use.
   -We provided simple Web interface, and intuitive GUI interface,
      and a tutorial.
   -Biologists prefer making their own judgements...and they hate
       high false positives.  They don't like being handed a bunch
        of results and a confidence estimate.

   No one uses Titus' code.  Exception: paircomp, motility (small libraries).

   QT or KWWidgets allow testing!
   ExtJS javascript toolkit.
   SQLAlchemy is a very nice O/R mapping system.

   Emphasize end-user usefulness over flexibility.
   Need tutorials and intuitive interfaces.

   80-90% of what Titus did was at the request of users.
   Most users underestimate what is possible so they under-request features.


   -----
   James Taylor - Galaxy, regulatory genomics

   Computational biology textbooks always mention Perl.

   What is Galaxy?
   - An open-source framework for integrating various computational tools.

   Workflows.
   Explicit workflow construction and editing.
   Workflow construction by example.  Want to be able to pull out
      portions of workflow to run again.

   Python 2.4 + some C extensions
   WSGI Web framework
   love SQLAlchemy for database abstraction
   love jQuery

   Can use Galaxy without javaScript.  Can turn on javaScript to get
   progressively more features.

   Just checkout from subversion and run!

   [Sorry, I had to leave the conference after the morning break....]

