#format rst

WE NEED YOUR HELP!
==================

This is a distributed, volunteer project with many contributors. The best way to join our effort is to browse around, read the last section of this page to learn about our vision and plans, and then announce your intent to help on one of the developer ["Mailing Lists"] or contact any of the folks listed on this page.

STEERING COMMITTEE
==================

* Jarrod Millman

* Eric Jones

* Robert Kern

* Travis Oliphant

* Stefan van der Walt

The purpose of this group is to ensure coherency in the SciPy_ library and advocate its progression.  It organizes doc-days, bug-days, coding sprints, and assists with organizing the SciPy_ conference.  It also serves to resolve questions that come up regarding the future of SciPy_.

SOURCE CODE
===========

Make contributions (e.g. code patches), feature requests and file bug reports by submitting a "ticket" on the Trac pages linked below.  Because of spam abuse, you must create an account on our Trac in order to submit a ticket, then click on the "New Ticket" tab that only appears when you have logged in.  Please give as much information as you can in the ticket.  Also specify the component, the version you are referring to and the milestone.  Report bugs to the appropriate Trac instance (there is one for NumPy_ and a different one for SciPy_).  There are [:Mailing Lists:read-only mailing lists] for tracking the status of your bug ticket.

Note that NumPy contains the most basic numerical functionality, and SciPy is layered on top of NumPy to provide a much wider range of capability.  You need NumPy for SciPy to work.

<strong class="highlight">.. raw:: html

</strong>[Table not converted]

Interested people can get repository write access as well.  This usually requires a developer "vouching" for you, which happens more easily if you already made a number of patch contributions.

See Packaging, below, for the process of building and making releases.

Source Code Team
----------------

* Travis Oliphant `MailTo(oliphant.travis at ieee.org)`_

* Robert Kern `MailTo(robert.kern at gmail.com)`_

Affiliated, non-field-specific projects:

* matplotlib - John D. Hunter

* ipython - Fernando Perez

* f2py - Pearu Peterson `MailTo(pearu.peterson AT gmail DOT com)`_

* "unifying extension generation tools" - Pearu Peterson `MailTo(pearu.peterson AT gmail DOT com)`_

FILL IN URLs and emails and more projects

New Code
--------

If you have some new code you'd like to see included in SciPy_, the first thing to do is make a SciKit_.  A SciKit_ is a stand-alone package including your code (including complete reference and user documentation).  SciKits_ are distributed here:

`http://scikits.appspot.com/`_

This site is currently still in early construction phases, and will be moved (and linked) to the main page of this site when it is ready to accept new SciKits_.  Right now users and developers are encouraged to view the site and comment on `MailTo(scipy-dev@scipy.org)`_ to ensure it serves your needs.

Once you get some use experience, the community may decide to include your SciKit_ in SciPy_.  These decisions are based on many factors, including maturity of the code API and the docs, ease of building it on all platforms, how many people use it, how well it is integrated into SciPy_, etc.

Because it must remain small and easy to build, new additions of entire packages to NumPy_ are extremely rare.  Contact the Steering Committee or post on the `MailTo(numpy-discussion@scipy.org)`_ mailing list if you think you have a compelling case.

PACKAGING
=========

For the majority of users who do not want to build the code from source, binary installers that "just work" are the key to using SciPy_.  Producing these after the coding is finished is the Packaging Team's job.

Making Source and Binary Releases
---------------------------------

A releaseable tarball gets made from the sources following a straightforward procedure (see http://projects.scipy.org/numpy/wiki/MakingReleases ).  To make an official release to the community, someone on the packaging team, usually Jarrod Millman, makes a series of test releases and announces them on the mailing lists.  After getting feedback, the team makes a final release, posts it, and announces it on the mailing lists.

FILL IN: Packaging Team, please fill in more detail on how you cut releases and where you need help.  Describe the build system, standards for accepting a release candidate, what systems are tested, who does what, use of Trac for bugs, etc.

Getting Releases Into Distribution
----------------------------------

<p>Linux distributions and many others pick up our packages and deliver them to users as part of larger collections.  To ensure that they are distributing our latest and best, we record on the <a class="reference external" href="./Developer_Zone/Distros">Distros</a> page what's needed to trigger them to pick up a new release.  This could mean contacting an individual, posting on a mailing list, or doing something on a web site.  WE NEED YOUR HELP!  If you know the proper way to get a distro to pick up a new version of a package, please document it under <a class="reference external" href="./Developer_Zone/Distros">Distros</a>.</p>
Packaging Team
--------------

* Debian - Ondrej Certik (`MailTo(ondrej AT certik DOT cz)`_) and `Debian Python Modules Team (DPMT) <http://wiki.debian.org/Teams/PythonModulesTeam>`_

* Ubuntu - [`https://edge.launchpad.net/~kitterman`_ Scott Kitterman] and others

* numpy.distutils - Pearu Peterson

