#format rst

`MayaVi2 <http://code.enthought.com/projects/mayavi/>`_ is the successor of `MayaVi <http://mayavi.sf.net>`_ for 3D visualization. It is a interactive program allowing elaborate plots of scientific data.

MayaVi2 relies on `VTK <http://www.vtk.org>`_, and especially a python interface to it: `TVTK <https://svn.enthought.com/enthought/wiki/TVTK>`_.

<strong class="highlight">.. raw:: html

</strong>[Table not converted]

If you need more help, you are invited to ask questions on the `Enthought-dev <https://mail.enthought.com/mailman/listinfo/enthought-dev>`_ mailing list.

::

   #class right
   ## Snazzy graphics here...
   inline:mayavi2.png

   A mayavi2 session.

MayaVi2 topics
==============

MayaVi2 can be used as an interactive program or not, as it will be presented here.

* For installation of MayaVi2 in the enthought tool suite see the `Mayavi documentation <http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/installation.html>`_

* Using MayaVi2:

    There are (at least) two ways to use MayaVi2:

    * [:Cookbook/MayaVi/RunningMayavi2: Running MayaVi2_] on the command line.

    * [:Cookbook/MayaVi/ScriptingMayavi2: Scripting MayaVi2_] in Python.

* [:Cookbook/MayaVi/Examples: Scripting Examples] (all provided in MayaVi2 svn tree):

  * Using Contour Module (contour.py)

  * Using Glyph Module (glyph.py)

  * Using Mayavi2 without GUI (nongui.py)

  * A 3D array as numerical source (numeric_source.py)

  * Using Streamline Module (streamline.py)

  * Using ImagePlaneWidget Module (test.py)

  * Plotting a surface from a matrix (surf_regular_mlab.py). See also [:Cookbook/MayaVi/Surf: Cookbook/MayaVi/Surf]

* [:Cookbook/MayaVi/Tips: Tips]: General tips for MayaVi2 and around.

TVTK
====

::

   #class inline
   ## Snazzy graphics here...
   inline:mlab.png

   Using the mlab module from ipython

* [:Cookbook/MayaVi/mlab: Mlab]: module allowing to drive VTK from Python to do 3D plots ala matlab.

* [:Cookbook/MayaVi/tvtk: tvtk]: Traited VTK, including iVTK

inline:5_2_1.png

**Visualization of the (5,2,1) orbital of the H-atom using an iso-surface and a semi-transparant scalar cut plane.**

-------------------------

 CategoryCookbook_

