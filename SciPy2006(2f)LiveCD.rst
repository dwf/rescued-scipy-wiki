#format rst

SciPy 2006 LiveCD Information
=============================

Bryce Hendrix (Enthought, Inc.) is working on an Ubuntu 6.06 LiveCD with Python 2.4.3 and some other pre-installed libraries for this year's SciPy Conference [:`SciPy2006/TutorialSessions`_:Tutorial Sessions].

We'll also post a link, when available, to a downloadable ISO for those who can't attend and want to test drive things.

Update
------

The i386 torrent can be downloaded here: [`http://code.enthought.com/downloads/scipy2006-i386.iso.torrent`_]

Update 2
--------

The ppc torrent caused no end of problems on the limited hardware we have here. A working ISO was unfortunately not built in time. The builds will be made available as a tar bundle however.

The ppc files can be found [`http://code.enthought.com/downloads/scipy2006-ppc.tar.bz2`_ here]. Simply uncompress them in the root dir and everything should be in place.

To keep the download as small as possible, packages which can be downloaded using apt were omitted. The omitted package include:

* atlas3-base-dev

* fftw3-dev

* gcc

* gcc-3.4

* g77

* g++

* g++-3.4

* libumfpack4-dev

* make

* python-dev

* python-gtk2-dev

* python-numarray

* python-vtk

* python-wxgtk2.6

* python-wxtools

* python-wxversion

* tk8.4-dev

* subversion

* swig

* xlibs-dev

Or, for your cut 'n' paste pleasure:

  sudo apt-get install atlas3-base-dev fftw3-dev gcc gcc-3.4 g77 g++ g++-3.4 libumfpack4-dev make python-dev python-gtk2-dev python-numarray python-vtk python-wxgtk2.6 python-wxtools python-wxversion tk8.4-dev subversion swig xlibs-dev 

.. ############################################################################

.. _SciPy2006/TutorialSessions: ../TutorialSessions

