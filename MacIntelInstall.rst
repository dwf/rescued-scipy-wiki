#format rst

Installing SciPy on the Mac requires a g77-compatible compiler.  Unfortunately, g77 has not been ported to Mac Intel and gfortran (which you can get) does not yet support all the Fortran code used in SciPy.  However, g95, does seem to compile most of the Fortran code correctly and can be used to get SciPy to work.

One way that is known to work to get SciPy installed is to use the Fink package. Here are the instructions from Jeff Whitaker:

* install Xcode

* install the fink 0.8.1 binary installer for intel   http://fink.sourceforge.net/download/index.php?phpLang=en ).

* edit /sw/etc/fink.conf and add 'unstable/main' to the 'Trees:' line.

* run 'fink selfupdate' (this will take a while as it downloads, builds and installs stuff).

* run 'fink install scipy-py24'  (this will also install all the dependencies, like g95 and numpy and python itself).

You can also get svn (fink install svn) and matplotlib (fink install matplotlib-py24) and ipython (fink install ipython-py24) and xemacs (fink install xemacs-sumo-pkg).

The system python is still python but the python with SciPy_ installed will be python2.3

sudo gcc_select 4.0  will select gcc 4.0 to use as the compiler.  This is the configuration I've used and found to work, but gcc 3.3 may also work.

-Travis Oliphant

.. ############################################################################

.. _SciPy: ../SciPy

