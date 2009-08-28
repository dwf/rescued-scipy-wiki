AstroLib
========

.. image:: http://stsdas.stsci.edu/perry/astroliblogo.png


This page is intended to serve as a means for coordinating ideas about how astronomical utility libraries should be built for Python analogous to the ASTRON library for IDL. This project also has a `Trac Site <http://astropy.scipy.org/astropy/astrolib/wiki/WikiStart>`_ , and discussion also occurs on the `Astropy mailing list <http://lists.astropy.scipy.org/mailman/listinfo/astropy>`_. **Note: both the astrolib repository and trac site were relocated to STScI on February 13, 2009.**  The links to the new repository and trac site are:

svn:  https://www.stsci.edu/svn/ssb/astrolib/

trac: https://www.stsci.edu/trac/ssb/astrolib

We (STScI) would like to help develop an ASTRON-like library for Python.  We have some resources to devote to it now and are starting work on building such tools. (for reference; here is the link to the documentation for the IDL "ASTRON library": http://idlastro.gsfc.nasa.gov/contents.html)

But we also want to keep this an open project so that others can contribute (either existing code or contribute to the development), and have some sense of where we are going early enough to give us feedback before we do it (rather than after the fact). The software will be kept on an STScI  repository (https://www.stsci.edu/svn/ssb/astrolib). We  also want to float our ideas about what we would like to see in such a library so that others can contribute suggestions and alternatives. Naturally, we will tend to focus on capabilities that are important to the work we are doing, but we want to keep things flexible and open enough that it is useful for others, or at least sets a framework that allows others to build on what we contribute.

It may well be that multiple approaches are warranted. Those with good ideas and (especially) time to contribute should not feel that we or any other organization has a monopoly on defining how things are to be done (well, with the exception that some documentation and test standards be met; more on suggestions regarding that below)

* Related Efforts underway: AstroLibAssociatedEfforts

* Approaches to consider: AstroLibPhilosophy

* Array package: AstroLib will use the `numpy <http://numpy.scipy.org/>`_ package (that was intended to replace both Numeric and numarray). Some existing code presently uses numarray , but it will be ported as soon as resources permit. Some existing pages specify numarray; these pages are out of date and will be updated as soon as resources permit.

Specific Library Functionality:
-------------------------------

* FITS WCS standards: AstroLibWCS:

* Astronomical Coordinate Systems: AstroLibCoordsHome

* Dates and Times: AstroLibDatesTimes:

* Photometric utilities: AstroLibPhotometry:

* Utilities to read and write ascii data from and to arrays: AstroAsciiData:

* Others?

Standards
---------

* Documentation Standards: AstroLibDocStandards

* Testing Standards: AstroLibTestStandards

The logo was designed by Nadia Dencheva. Thanks to Bill Love for permission to use the Python image in the Astrolib logo (http://www.bluechameleon.org)

.. ############################################################################

.. _AstroLibAssociatedEfforts: ../AstroLibAssociatedEfforts

.. _AstroLibPhilosophy: ../AstroLibPhilosophy

.. _AstroLibCoordsHome: ../AstroLibCoordsHome

.. _AstroLibDatesTimes: ../AstroLibDatesTimes

.. _AstroLibPhotometry: ../AstroLibPhotometry

.. _AstroAsciiData: ../AstroAsciiData

.. _AstroLibDocStandards: ../AstroLibDocStandards

.. _AstroLibTestStandards: ../AstroLibTestStandards

