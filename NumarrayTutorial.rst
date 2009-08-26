#format rst

This tutorial has been written by Perry Greenfield and Robert Jedrzejewski to illustrate how one can use Python to do interactive data analysis in astronomy (in much the same style as is now popular with IDL). The focus is initially in showing someone how to get going quickly in using Python to do interactive tasks, and only later on teaching details of how to program in Python.

The version of the tutorial available on this page uses the older array package numarray, which is being phased out. **Unless you have a very strong reason to learn using numarray, please use the numpy version of the tutorial!**

`Download tutorial <http://stsdas.stsci.edu/perry/pydatatut_numarray.pdf>`_

Using the tutorial for fields other than astronomy
--------------------------------------------------

Most of the tutorial is pretty generic. The great majority of examples use astronomical data but do not require any astronomical expertise." Those that want to use this tutorial and who aren't in astronomy should skip sections 1.7, 1.8, 3.5 and 4.10.

Comments on how to improve this version of the tutorial are not welcome since it is no longer being maintained. You are encouraged to comment on the numpy version though (hint, hint)

Data and scripts for examples and exercises
-------------------------------------------

The following gzipped tar files contain data files and scripts used by the tutorial examples and exercises. There are two different tar files to choose from. The first is complete, but quite large. The second has everything the first has except the acs.fits file and is considerably smaller.

`Download complete set of data and scripts (120 MB) <http://stsdas.stsci.edu/perry/full_numarray.tar.gz>`_

`Download all except acs.fits (3.2 MB) <http://stsdas.stsci.edu/perry/partial_numarray.tar.gz>`_

Contents of gzipped tar files:

::

    Data for examples and exercises:
     pix.fits (Tutorial 1)
     fuse.fits (Tutorial 2)
     table2.fits (Tutorial 2)
     nicmos.fits (Tutorial 3)
     acs.fits (Tutorial 3), only included in larger download
     tut3f1.fits (Tutorial 3 exercise)
     alpha_boo_iue.fits (for use with Tutorial 5 exercise 2)
    Scripts and modules:
    Examples from Tutorial 3:
      interp.py
      radial.py
      coins.py
      laplace.py
      nearest.py
    Examples from Tutorial 5:
      sortedlist.py
      sdict.py
      spec1.py
      spec2.py

Software needed to run examples:
--------------------------------

* Python  http://www.python.org )

* numarray  http://www.stsci.edu/resources/software_hardware/numarray )

* PyFITS  http://www.stsci.edu/resources/software_hardware/pyfits )

* matplotlib  http://matplotlib.sourceforge.net )

* numdisplay  http://stsdas.stsci.edu/numdisplay/ ) (for displaying images to display programs such as DS9 or ximtool

* DS9  http://hea-www.harvard.edu/RD/ds9/ ) (for non-matplotlib image display examples)

To run the IRAF-related examples one needs to install IRAF and PyRAF as well.

* IRAF  http://iraf.noao.edu/iraf-homepage.html )

* PyRAF  http://www.stsci.edu/resources/software_hardware/pyraf )

Solutions to exercises
----------------------

Note that many approaches are possible with most of the exercises. The following are intended just to show one way they can be done.

* NumarrayTutorialSolutionSet1_

* NumarrayTutorialSolutionSet2_

* NumarrayTutorialSolutionSet3_

* NumarrayTutorialSolutionSet4_

* NumarrayTutorialSolutionSet5_

.. ############################################################################

.. _NumarrayTutorialSolutionSet1: ../NumarrayTutorialSolutionSet1

.. _NumarrayTutorialSolutionSet2: ../NumarrayTutorialSolutionSet2

.. _NumarrayTutorialSolutionSet3: ../NumarrayTutorialSolutionSet3

.. _NumarrayTutorialSolutionSet4: ../NumarrayTutorialSolutionSet4

.. _NumarrayTutorialSolutionSet5: ../NumarrayTutorialSolutionSet5

