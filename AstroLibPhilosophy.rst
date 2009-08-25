General issues for an ASTRON-like library:
------------------------------------------

Literal translations of IDL procedures vs redesign (by literal translation we mean primarily a line-by-line translation of IDL code to corresponding Python functionality):

* Advantages of literal approach:

  * Existing familiarity for current IDL users

  * Relatively easy implementation

    * No big design issues to settle on

  * Relatively easy regression tests (in comparison with IDL results) to validate.

* Disadvantages:

  * Somewhat inconsistent interfaces.

  * Redundant functionality

    * E.g., various FITS libraries (contrast with PyFITS)

  * doesn't provide easy means of user and other applications using common machinery (See the Coordinate topic, AstroLibCoordsStartingThoughts_, for an illustration).

  * Many aspects superceeded by more functional libraries (E.g, database functionality)

  * Many of the ASTRON "non-Astronomy" routines not relevant in Python.

Regarding specific ASTRON categories:
-------------------------------------

Some components of the ASTRON library are better suited for literal translation than others. If we remove those categories that no longer seem relevant (non-Astronomy, databases, FITS, plotting) that leaves primarily:

* Astronomical Utilities

* DAOPHOT-type photometry procedures

* FITS Astrometry

* Math and Statistics

* Robust Statistics Procedures

The latter two are likely more suitable for direct translation. The second perhaps (though I wonder how this whole issue would be approached now given the widespread use of tools like SExtractor). The first probably could benefit from a new approach to the utilities. We haven't looked at the FITS astrometry utilities much yet to comment (though decoupling WCS from FITS would seem to be a good idea).

Anything missing from ASTRON that should be in "astropy"?

Issues related to any redesign:
-------------------------------

* All code will be based on numarray. No compatibility with Numeric will be attempted. This is because PyFITS requires numarray (handling tables with Numeric is much more difficult).

* For "Astronomical Utilities", many of the routines deal with time/date, coordinate, or photometric issues that may be better handled with an object-oriented approach.

* If developing an object-oriented foundation is too complex, it will take too long to get in place to serve as a foundation for an ASTRON library equivalent.

* As far as STScI is concerned, we are unlikely to base many applications on literal translations of all the Astronomical Utilities and are looking for components that make handling coordinates, times, and photometry in a more general way.  A subsequent list posting will discuss ideas for how to  handle the beginnings of a coordinate object for Python.

* Yet, we don't want to exclude the possibility (and usefulness) of literal translations. We think that we should allow those that wish to contribute such version to a corresponding Python library. It is likely that there is at least a fairly large subset of Astronomical Utilities procedures that are suitable as literal translations in any case.

* We propose creating an "astron" module to contain all the literal equivalents of IDL routines. Nonliteral versions should go into different modules (astrolib and others?). Any better ideas for categorizing routines? Use a package instead? Any other suggestions for names? Astrolib doesn't to be used within the Python context but there is a Java library of the same name. Some alternatives: astropy, astro 

.. ############################################################################

.. _AstroLibCoordsStartingThoughts: ../AstroLibCoordsStartingThoughts

