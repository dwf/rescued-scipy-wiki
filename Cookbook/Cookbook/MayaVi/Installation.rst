#format rst

TableOfContents_

Introduction
============

MayaVi2 and TVTK are part of the [`https://svn.enthought.com/enthought`_ enthought tool suite].

**These instructions are out of date**, see the [`https://svn.enthought.com/enthought/wiki/MayaVi`_ Mayavi2 homepage]

-------------------------



Installation information is detailed here [`http://code.enthought.com/enstaller/eggs/debian/etch`_] for all UN*X flavours.

Installation on a Linux box
===========================

Debian etch distro
------------------

Read installation information at [`http://code.enthought.com/enstaller/eggs/debian/etch`_]

RedHat Enterprise (3/4/5) distro
--------------------------------

Read installation information above (Debian etch distro) and grab the eggs at [`http://code.enthought.com/enstaller/eggs/rhel`_]

Suse v10.2 distro
-----------------

Read installation information above (Debian etch distro) and grab the eggs at [`http://code.enthought.com/enstaller/eggs/suse`_]

Ubuntu (edgy & feisty) distro
-----------------------------

Read installation information above (Debian etch distro) and grab the eggs at [`http://code.enthought.com/enstaller/eggs/ubuntu`_]

Installation on a FreeBSD box
=============================

The procedure to install the complete stuff is somewhat similar to [:Cookbook/MayaVi/InstallPythonStuffFromSource: Installation of vtk/python stuff from source] because FreeBSD system is based on building your own packages (got from "ports") rather than downloading precompiled binary packages (it's only my own point of view ;-). Thus, some binary packages could lack on the FreeBSD repository. If so, you have to build some ports to install MayaVi2 on your FreeBSD box. As ports are more up-to-date than binary packages, only ports will be used here.

Note1: Until now, there is no python eggs for FreeBSD. Someone interested ? |;-)|

Note2: FreeBSD 6.2-STABLE is used here.

Note3: You may have to update your ports tree to build the required packages. See cvsup(1) to make it up-to-date.

You can install ports using portinstall(1) or the "classic" way: cd /usr/ports/category/portname && make install clean.

Thus, you have to install the following ports:

* lang/python24;

* devel/py-setuptools;

* science/py-scipy; you have to install math/atlas port (more than 4 hours are required to build it on my Pentium D 3 GHz...) with WITH_STATICLIB flag enabled or math/blas and math/lapack ports (much faster to build) for scipy to build.

* x11-toolkits/py-wxPython26;

* math/vtk-python (release 4.4); for now, VTK 5 is not yet included in the ports tree |:-(| Still waiting...

* devel/swig13.

You will also need to install subversion(1) (devel/subversion port) to fetch MayaVi2 source code.

Once you have installed all the required stuff, and because pre-built python eggs do not exist yet, you have to build them on your own:

* download the source with svn:

::

   svn co https://svn.enthought.com/svn/enthought/branches enthought-2.0

  This will create for you a directory named "enthought-2.0". "branches" stands for "stable". If you are a enthought dev, a traits guru, or brave, and only in this case ;-), you can get a try with the trunk, but you have been warned |;-)| :

::

   svn co https://svn.enthought.com/svn/enthought/trunk enthought-2.1

* go to your source directory (i.e. enthought-2.0) and build eggs with the python script named egg_builder.py:

::

   ./egg_builder.py enthought.*

  This will build all the eggs in the "dist" directory.

* install MayaVi2 with the easy_install command:

::

   easy_install -f dist enthought.mayavi

* you're done |;-)|

Installation on a MacOS X box
=============================

Read installation information above (Debian etch distro) and grab the eggs at [`http://code.enthought.com/enstaller/eggs/macosx`_]

Installation on a Windows box
=============================

**Installation with Enthon:** For Windows, you can download the enthought edition at `http://code.enthought.com/enthon`_ (>=0.9.3).  This includes Python itself along with MayaVi2 and many other tools.

**Installation with easy_install:** The enthought tools are now also available via individual [`http://peak.telecommunity.com/DevCenter/PythonEggs`_ eggs] that can be installed on top of an existing Python using [`http://peak.telecommunity.com/DevCenter/EasyInstall#installing-easy-install`_ easy_install].  Assuming you've already [`http://peak.telecommunity.com/DevCenter/EasyInstall#installing-easy-install`_ installed easy_install] the following command will do it:

::

     easy_install -f http://code.enthought.com/enstaller/eggs enthought

The enthought egg contains the whole [`http://code.enthought.com/ets/`_ Enthought Tool Suite], which includes MayaVi2.  You may also need to install a few other things that MayaVi2 depends on, like VTK, numpy, scipy, and Enthought's precompiled version of wxWidgets *(can someone verify these are all really dependencies?)*:

::

     easy_install -f http://code.enthought.com/enstaller/eggs numpy scipy wx VTK

**Installation with Enstaller:** Enthought has also written a graphical front end to easy_install called [`http://code.enthought.com/enstaller/`_ Enstaller].  You can install Enstaller by running this script: [`http://code.enthought.com/enstaller/run_enstaller.py`_ run_enstaller.py].  Enstaller is still quite new, so you may or may not find it an improvement over the easy_install method at this time.

Creation of a Live CD (based on Debian) including MV2
=====================================================

A step-by-step guide to creating your own bootable CD-ROM, running [`http://www.debian.org`_ Debian] and containing mayavi2 is given [:Cookbook/MayaVi/Installation/DebianLiveCD: here].

-------------------------

 CategoryInstallation_

