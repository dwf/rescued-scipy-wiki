Underlying machinery
--------------------

After a survey of the available software (listed below for reference), we selected the TPM (Telescope Pointing Machine) software, which Jeff Percival has graciously made available, as the underlying machinery for the AstroLibCoords_ project.

* The [`http://www.sal.wisc.edu/~jwp/astro/tpm/tpm.html`_ Telescope Pointing Machine] is a coordinate conversion program built around [`http://cadcwww.dao.nrc.ca/ADASS/adass_proc/adass3/papers/percivalj/percivalj.html`_ state machine software]. Its results match both NOVAS and SLALIB, and the underlying engine is also used to point the WIYN telescope.

User tools
----------

  Libraries and applications that provide some of the functionality we hope to provide with the AstroLibCoords_

* ["IDLAstronCoordTasks"]

* ["IRAFCoordTasks"]

* Some ["JSkyPieces"] have similar functionality, although most of JSky seems to be concerned with sky to image manipulations, and so would have more relevance to ["AstroLibWCS"]

Software Packages
-----------------

Packages that provide trusted, accurate astrometric results for these tasks. We may consider wrapping one of these instead of re-implementing. At the minimum, we will use one of these libraries as a test standard.

* [`http://www.starlink.rl.ac.uk/cgi-bin/htxserver/sun67.htx/sun67.html`_ SLALIB] is the positional astronomy library developed by STARLINK in the late 80s.  STARLINK offers a [`http://star-www.rl.ac.uk/static_www/soft_get_PTPH.html`_  variety of other software packages] for positional astronomy as well.

* [`http://aa.usno.navy.mil/software/novas/novas_info.html`_ NOVAS] This is the USNO software that underlies the Astronomical Almanac. Originally in FORTRAN, there is now a C version.

  * There's also a [`http://pynovas.sourceforge.net/`_ PyNOVAS] project at SourceForge_, but it appears to be moribund: created in 2001 and no activity since. There was a slight revival January, 2006.

* The [`http://www.rhodesmill.org/brandon/projects/pyephem.html`_ PyEphem_] software includes support for fixed targets in a package that is primarily aimed at supporting moving targets. Its design and user interface look crisp and clean.

  * It uses [`http://www.clearskyinstitute.com/xephem/`_ XEphem] by Elwood Charles Downey as its computing engine. XEphem is commercial software, with a restrictive license for free use. Its documentation claims "professional accuracy" but doesn't cite any test standards. The AAVSO [`http://www.aavso.org/data/software/xephem.shtml`_ recommends] it for their observers.

* There is a C and Python package for calculation of orbital parameters and ephemeris at [`http://astrolabe.sf.net`_ Astrolabe].  All functions are implemented in C and Python.  I use it for some orbital parameters needed for tidal analysis for my tidal  analysis package at [`http://tappy.sf.net`_ TAPPy].  I have some bug fixes for Astrolabe that have not been applied to the main source which can be found in the TAPPy download.

.. ############################################################################

.. _AstroLibCoords: ../AstroLibCoords

.. _SourceForge: ../SourceForge

.. _PyEphem: ../PyEphem

