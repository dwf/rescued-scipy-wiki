#format rst

* ["Moin configuration"] - configuration requests for this wiki

* ["Navigation bar draft"] - what links hould be listed on the navigation bar (navi bar will appear on the left once the theme is changed to sinorca)

* ["Site content types"] - list of different content types that may appear on this site

* ["Site user types"]

* ["Tests of wiki features"]

-------------------------

 Contents: TableOfContents_

Planning the future
===================

Related posts on the mailing list
---------------------------------

We need to think about the organization of this website, as it will be with us for a long time.  Here are some recent emails concerning the site-structure:

* http://www.scipy.org/documentation/mailman?fn=scipy-dev/2005-December/004532.html

* http://www.scipy.org/documentation/mailman?fn=scipy-dev/2005-December/004534.html

Andrew Straws layout suggestion
-------------------------------

Andrew Straw suggested to make the website function more as a portal to scientific-computing-using-Python-in-general and not just SciPy and thus proposed a site structure something more like:

::

   Home
           executive summary
           sidebar with brief news summary
   News
           (e.g. scipy_core and full scipy nearing end of heavy re-structuring)
   Getting started
           simple demos using scipy_core and matplotlib, for example
           pointers to individual packages, both scipy and external
   Screenshots
           made with matplotlib and scipy_core and/or full scipy
           made with MayaVi
           made with raw VTK
           benchmarks from 64 CPU 64 bit Itanium system
   scipy_core
           About
           Installation
           Intro demos
           Download page with links to source and binary releases
           FAQ
           Documentation
           Info about svn, link to Trac
   (full) scipy
           About
           Installation
           Intro demos
           Download page with links to source and binary releases
           FAQ
           Documentation
           Info about svn, link to Trac
   Cookbook
           we should
           think about
           some organization
           for code receipes
   Download
           point to (or include) scipy_core/Download and scipy/Download

Another structure suggestion looking for simplicity
---------------------------------------------------

::

   Home
           executive summary
           sidebar with brief news summary

   News
           (e.g. scipy_core and full scipy nearing end of heavy re-structuring)

   Screenshoots
           screenshoots
           demos

   Documentation
           getting started
           install
           tutorial
           cookbook
           reference
           FAQ

   Download
           packages
           docs

   Community
           mailing lists
           events
           presentations

   Developers
           bug reports
           SVN

Yet another structure suggestion (a mix of the 2 above)
-------------------------------------------------------

The main idea here is:

1. To create an impression that this site represents a tool called SciPy rather than a mix of interrelated software. The impression of a "mix" is very confusing for newbies.

#. Still give a proper representation to scipy_core and other tools for scientific computing with Python.

-------------------------



* Home

  * executive summary

  * sidebar with brief news summary

  * pic with nice graphics made with SciPy

* News

  * Maybe omit the link to news page from navigation bar and only leave it as "More news" at the bottom of News sidebar.

* About SciPy

  * Somewhat longer explanation of what's SciPy and what's it good for,

  * mention that SciPy is based on scipy_core which is usable separately and that scypy_core is intended to replace numarray and numeric.

  * Some pointers for new users.

* Screenshoots

  * screenshoots

  * demos

* Documentation

  * FAQ

  * Getting started - several versions optimized for different user types.

  * Various other docs

  * Docs downloads

* Getting SciPy

  * Directions on what to download and pre-requisites

  * packages

  * Link to installation instructions

  * Link to "Getting started"

  * Sources - (very briefly, link to "Development" for details)

* Community

  * mailing lists

  * events

  * presentations

* scipy_core

  * (All about scipy_core)

  * It's good to have a link to scipy_core on the front page since we want to convince the developers of other packages currently based on numeric and numarray to move to scipy_core, so we need to give it a good representation.

* Related projects

  * What was "Topical software"

* Development

  * bug reports

  * Developer docs

  * SVN

-------------------------



.. ############################################################################

.. _TableOfContents: ../TableOfContents

