#format rst

The cookbook is a place for community contributions of recipes, howtos and examples.

Complete documentation and tutorials for matplotlib can be found at [`http://matplotlib.sourceforge.net/`_ matplotlib's webpage]

  **Table of Contents**

TableOfContents_

Simple plotting
===============

* [:Cookbook/Matplotlib/SigmoidalFunctions:Sigmoidal Functions] - plotting simple functions

    attachment:sigmoids_small.png

* [:Cookbook/Matplotlib/MultilinePlots:Multiline Plots] - how to plot multiple lines over one another

    attachment:multiline.png

* [:Cookbook/Matplotlib/BarCharts:Bar Charts] - how to make a bar chart

    attachment:barchartscaled.png

* [:Cookbook/Matplotlib/Common Errors:Common Errors] - Compilation of common errors that can cause erroneous behavior. Check before emailing mailing lists.

* ["/Animations"] - how to animate your figures.

* [:Cookbook/Matplotlib/MulticoloredLine:Multicolored Line] - different colors for different parts of a line

    attachment:colored_line.png

* [:Cookbook/Matplotlib/ShadedRegions:Shaded Regions] - how to plot grey shaded regions using transparency.

    attachment:shaded_small.png

* ["/Arrows"] - how to plot arrows

    attachment:plot_arrow_small.png

* [:Cookbook/Matplotlib/UnfilledHistograms:Unfilled Histograms] - how to plot histograms that are un-filled and don't look like bar charts.

    attachment:hist_outline_small.png

* [:Cookbook/Matplotlib/CustomLogLabels:Custom Log Plot Labels] - plotting log plots with custom tick labels that are formatted as integer numbers rather than exponents as is the default.

    attachment:log_labels_small.png

* [:Cookbook/Matplotlib/ThickAxes:Thick Axes] - how to make thick axes lines and bold fonts.

    attachment:thick_axes.png

* ["/Maps"] - how to plot data on map projections

    attachment:basemap1.png

* [:Cookbook/Matplotlib/Plotting values with masked arrays:Plotting values with masked arrays] - How to plot only selected values of an array, because some values are meaningless (detector malfunction), out of range, etc. etc.

* ["/Transformations"] - Using transformations to convert between different coordinate systems.

* TreeMap_ - classic treemap style plots

* ["/Legend"] - Adding a legend to your plot

* [:Cookbook/Matplotlib/HintonDiagrams:Hinton Diagrams] - A way of visualizing weight matrices

    attachment:hinton-small.png

Pseudo color plots
==================

* [:Cookbook/Matplotlib/Loading a colormap dynamically:Loading a colormap dynamically] - How to load a color map from a GMT (Generic Mapping Tools) file.

* [:Cookbook/Matplotlib/Show colormaps:Show colormaps] - Small script to display all of the Matplotlib colormaps, and an exampleshowing how to create a new one.

* [:Cookbook/Matplotlib/converting a matrix to a raster image:Converting a matrix to a raster image] - A replacement for scipy's imsave command

* [:Cookbook/Matplotlib/Gridding irregularly spaced data:Gridding irregularly spaced data] - how to grid scattered data points in order to make a contour or image plot.

* [:Cookbook/Matplotlib/Plotting Images with Special Values:Plotting Images with Special Values] - how to plot an image with special values mapped to specific colors, e.g. missing values or data extrema

    attachment:sentinel.png

* [:Cookbook/Matplotlib/ColormapTransformations:Transformations on Colormaps] - how to apply a function to the look up table of a colormap and turn it into another one.

Typesetting
===========

* [:Cookbook/Matplotlib/UsingTex:Using TeX] - formatting matplotlib text with LaTeX

    attachment:tex_demo.png

* [:Cookbook/Matplotlib/LaTeX Examples:LaTeX Examples] - Complete examples for generating publication quality figures using LaTeX.

3D
==

[Table not converted]

* [:Cookbook/Matplotlib/mplot3D:3D plots] - Simple 3D plots using matplotlibs built-in 3D functions (which were originally provided by John Porter's mplot3d add-on module).

    attachment:contourf3D.jpg

* [:Cookbook/Matplotlib/VTK Integration:VTK Integration] - how to import plots into vtk

    attachment:mpl_vtk.png

Misc
====

* [:Cookbook/Matplotlib/EmbeddingInWx:Embedding in WX] - advice on how to embed matplotlib figures in `wxPython <http://www.wxpython.org>`_ applications

* [:Cookbook/Matplotlib/LoadImage:Load and display an image] - shows a simple way to import a PNG image to a numpy array

* [:Cookbook/Matplotlib/Interactive Plotting:Interactive Plotting] - Adding mouse interaction to identify data annotations.

* [:Cookbook/Matplotlib/Matplotlib and Zope:Matplotlib and Zope] - How to use Matplotlib within the application server `Zope <http://www.zope.org>`_.

* [:Cookbook/Matplotlib/Qt with IPython and Designer:Qt with IPython and Designer] - How to design a GUI using Qt's Designer tool using Matplotlib widgets, and that can be interactively controlled from the IPython command line.

* [:Cookbook/Matplotlib/CompilingMatPlotLibOnSolaris10:Compiling Matplotlib on Solaris 10] - how to compile the thing on Solaris 10, using gcc/g++

* [:Cookbook/Matplotlib/Using MatPlotLib_ in a CGI script:Using MatPlotLib_ in a CGI script] - steps needed to be able to use matplotlib from a python cgi script

* [`http://www.answermysearches.com/index.php/making-dynamic-charts-and-graphs-for-your-webpage/135/`_ Making Dynamic Charts for your Webpage] - Complete CGI script example.

* [`http://www.dalkescientific.com/writings/diary/archive/2005/04/23/matplotlib_without_gui.html`_ matplotlib without GUI] by Andrew Dalke.

* [`http://debs.astraw.com/dapper/`_ Andrew Straw's Apt Repository] - Bleeding edge deb packages for Debian, Ubuntu (also has packages for numpy/scipy etc.).

* [:Cookbook/Matplotlib/AdjustingImageSize:Adjusting Image Size] - a brief discussion of how to adjust the size of figures -- for printing, web, etc.

* [:Cookbook/Matplotlib/DeletingAnExistingDataSeries:Deleting An Existing Data Series] - a quick example showing how to remove one data series from an already existing plot.

* [:Cookbook/Matplotlib/Django:Embedding in Django] - example on how to use matplotlib with Django.

* [`http://pytseries.sourceforge.net`_ timeseries scikit] - The documentation contains a section on plotting ``TimeSeries`` objects using matplotlib

* `/TreeMap`_ - A compact way of showing weighted tree information.

* [:Cookbook/Matplotlib/Multiple Subplots with One Axis Label:Multiple Subplots with One Axis Label] - how to use one centered label to annotate several subplots

* [`http://www.nabble.com/Multiple-Y-axis-td10734643.html`_ Multiple Y-axis] - How to plot different variables on the same plot but different Y-Axis (one left and one right)

* `WxMpl <http://agni.phys.iit.edu/~kmcivor/wxmpl>`_: Integration of matplotlib into WxPython_ GUIs

* [`http://code.enthought.com/projects/traits/docs/html/tutorials/traits_ui_scientific_app.html`_ Gael Varoquax's scientific GUI tutorial] includes an instructive example of embedding matplotlib in a Traits GUI.

-------------------------



  CategoryCookbookMatplotlib_ CategoryCookbook_

