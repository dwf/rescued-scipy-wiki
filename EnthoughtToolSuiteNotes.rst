#format rst

Getting into ETS: A Newbies Experience
======================================

I'm keeping a personal ETS "actions list" at ["ETSToDoList"].

A note on my point-of-view
--------------------------

I've just starting working with the Enthought Tool Suite (ETS), after a number of years experience of working with Python/numpy/matplotlib/scipy as a tool for scientific data analysis. I am used to building data acquisition applications with wxPython, VTK and the in-house libraries developed at my workplace. ETS is a real revelation and I'm really enjoying learning it. Here are some notes on my experiences on learning and using it "in anger".

enthought namespace
-------------------

The large and fine-grained enthought namespace is quite off-putting. What do all these components do? Few of them have any documentation. Installing everything as eggs means that stuff which sits in the same python namespace may, in fact, be in a quite different part of the filesystem tree. For example, where can I find enthought.traits.ui.editors.py ? Is it in the traits egg or is it in the traits.ui egg? Maybe it's in both, but having to hunt around all the eggs to find stuff is not nice.

(p.s. I found it in the end)

A further problem with the egg installation is that is doesn't play nicely with code-completion in eclipse/pydev. After some playing around with project paths etc. I got it to partially work but it doesn't seem to reliable. For a large library, code-completion is a huge productivity boost and I'm really missing it. Instead, I keep an IPython window open with just about everything imported just so I can probe the namespaces and pop up doc-strings. Oh how I wish for eclipse-integration...

Traits / TraitsUI
-----------------

The Traits documentation is not too bad. There's enough to get going. Here's some of the quirks I ran into

* Just about the first thing I tried with Traits/TraitsUI was to subclass a trait-object to give it a different default editor. I soon discovered this is not possible (you need to use the Trait factory function). Not being able to subclass to add/change functionality is quite jarring to the seasoned python programmer. However, it seems this will be addressed with the upcoming Traits-3 release.

* Pickling traited objects. I spent some time wondering why I couldn't pickle traited object before discovering that this is a peculiarity of IPython. Pickling traited objects works fine, just not within the ipython shell (is this issue known?).

* The default editor for Array traits is a grid of text-control widgets. The first time I tried configure_traits() on an object with some arrays in it, my PC locked up for 20 minutes while wxPython tried to render 4096 text-controls! This is a poor choice of defult editor for arrays. A new scientific users is quite likely want to view/edit arrays and it's quite likely these arrays may bve big. Thus, the default editor should handle this gracefully. I'd like to see an ArrayEditor_ based on a "virtual" wxGrid control, which has a default maximum size of say 10 rows and ~4 cols (so as not to hog the entire display). The ArrayEditor_ should obviously be a scrolled window so all parts of the array can be accessed. To handle arrays with dimensions>2, there shouls be a control bar where the user can select which 2D slices of a N>2 dims array to display. The columns should be labeled by index number, like the rows.

PlotItems
~~~~~~~~~

The MVC concept for building applications is a fantastic one for on-the-fly scientific data analysis and particularly so for interactive anaylsis. My experience of promoting python for data analysis is that people can get the hang of writing simple linear scripts to process their data. Matplotlib does an excellent job of making plotting simple and provides excellent output quality. However, when users want to do more interactive analysis, they get scared off at the prospect of learning a GUI-toolkit like wxPython. At this point, they just give up and install Matlab or Labview or Origin or even Excell, where the documentation is good and the sales reps are happy to show you how things work (dealer analogy here...).

Traits/TraitsUI could change this. It lets the user focus on their Model (the data and equations they are working with) without having to worry about the user-interface. You define your model, and them an interactive GUI is created automagically! Instant gratification.

The key feature is to give the user a brain-dead simple way of visualising their data. In the context of Traits MVC architecture, this means having a set of ready-to-go PlotItems which can be dropped into View definitions to get a plot based on one or more data-arrays. The Chaco2PlotItem is the only thing available out-the-box and is (frankly) a bit crap. It provides a basic level of zooming and panning but nothing else. Here's what I think is required of a universal plot component:

* For line- or scatter plots, the PlotItem_ constructor should take a seris of tuples as it's input (+keyword args). The first two components of the tuple give the names of the x-data and y-data traits to use and the third (optional) component should be a format string (like matplab/matplotlib) specifying the format of the plot (line-type, marker-type etc.). The forth (optional) component should give the data series label.

* The PlotEditor should provide a control toolbar with buttons to save the figure. Save formats should include bitmap and vector output formats. Where bitmap output is chosen, a magnification factor of at least 2x should automatically be used such that the results are print-quality. SVG output would be useful: it's quite common to want to add annotations or otherwise edit figures afterwards. This is tricky with PDF, but easy with SVG.

* The control bar should provide a button to pop up a configuration dialog for the plot. This should, at a minimum, allow the user to enter the plot title and the axis labels. Selecting the fonts and fontsizes would be nice. This recognises that we scientists think about our data first and foremost and things like formatting tend to occur to us after-the-fact. It gets me every time I write a matplotlib script, I run the script, tweak the zoom/pan levels to get the view of my data I want, and *only then* realise I've forgotten to set the title and axis labels of the plot, so I must kill the program, edit my script and re-run it. I want see my data first, *then* tweak the format and save the output.

* Automatic storing of plot formatting traits. The user should not have to worry about plot formatting in their python script. Thus, when the application is run, the user can tweak the formatting (labels, annotations fonts etc) using the GUI. However, once the format is set, the user should not have to re-create it every time the program is run. The program should automagically pickle and save the plot state and attempt to re-load this on the next run.

* A comprehensive set of PlotItem classes to cover the common types of plot: Line/Scaller plots, colormap/contour plots, bar-charts, surface plots (3D) etc. (and probably many more but these are what I use on a regular basis).

* Cursor support. This one is a bit domain specific, but I want a draggable plot cursor widget which the user can use to select a point on a line graph or a point on an image. The chaco RangeSelect tools is quite close to this, but I need to select a point rather than a range.

Note, I recognise that chaco is capable of alot more than a set of PlotItems could provide. My point is that PlotItems provide a really easy-to-understand method of deploying chaco/Traits.

Traits 3
~~~~~~~~

It looks like Traits-3 will address a number of weaknesses in the current traits-2 implementation. I struggled to get traits-3 installed: there's no install docs. In the end

VET and TraitsUI demo
~~~~~~~~~~~~~~~~~~~~~

The TraitsUI demo is really great. It's clearly inspired by the wxPython one and is a great way to show off the GUI features of traitsui to new users. This deserves to have an Application Menu entry so users can find it easily.

VET, the View Editing Tool, also has the potential to be a big hit with non-programmer users. The fact is people like to edit graphical things graphically. Integration with the aforementioned library of PlotItems would be great for the scientist-user. The key thing is providing a visual "palette" of tools the user can select from to achieve their goal. I couldn't figure out what all the windows in the VET application did, so some documentation would be helpful.

Both of these applications are a little rudimentary so, although they have huge potential, they could use some polish.

Chaco
-----

In the language of chaco, the "X-data" (as I would call it) is refered to as the "index" data. The "Y-data" are the "values". The architecture of chaco is quite different from matplotlib but, after a couple of days working with it, I think I prefer it. It's certainly more flexible and easier to work with internally.

Class Inheritance Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~

Here's a class tree for the Chaco API:

attachment:ChacoClassTreeSmall_.png

The anatomy of a chaco plot comprises the following:

* PlotRenderers_ - these are the actual plot/points/image plotted on the screen

* PlotContainers_ - These layout PlotRenders_ spatially

* Mappers - these map data coorinates to screen coordinates, based on ...

* Ranges - define the bounds of the data coordinates to display (i.e. xaxis range, yaxis range etc.)

* Overlays - these are all the other visual components of a plot, like axes, grids, labels etc.

* DataSources_ - these are the "plot pipeline" entry point for the input data.

For example, a simple line plot has the following structure (internally).

attachment:ChacoPlotRelationships_.png

PlotRenderers
~~~~~~~~~~~~~

PlotRenderers (subclasses of AbstractPlotRenderer) are the object that closest resembles the "core" item in a plot. It is the visual representation of your data on the screen. E.g. for a line-plot, the line is drawn by a LinePlot instance. Similarly, the bars of a barchart are drawn by a BarPlot instance.

Note, however, there is a one-to-one relationship between a plot item (line, bar etc.) and PlotRenderer object. If you want multiple lines/series on your chart, you need one PlotRenderer per series. For multiline plots, the PlotRenderer instances are contained by a PlotContainer object. In the case of a multiline plot, this would probably be an OverlayPlotContainer, which, as it's name suggests, draws all it's contained components on top of each other.

Note also, that a bare PlotRenderer_ does not include any axes or grids or any other annotation. These are handled by other objects. (PlotAxis and PlotGrid objects, appropriately enough)

PlotContainer
~~~~~~~~~~~~~

These are container objects used to layout PlotRenderers or other PlotContainers (any subclass of PlotComponent in fact), using a box-model. As menioned above, the OverlayPlotContainer is used for multiline plots. Plots can be laid side-by-side using StackedPlotContainer or in a grid using GridPlotContainer etc.

DataSources
~~~~~~~~~~~

The DataSources (i.e. subclasses of AbstractDataSource) are how your data gets into the chaco "plotting pipeline" (clear inspiration from VTK evident in this aspect of the architecture). Which DataSource you use depends on your data type (1D arrays, multi-dimensional arrays, points or grids). You can usually create the DataSources from some numpy arrays. If you give the DataSource a different array, the object notifies the other parts of the chaco pipeline and your plot updates accordingly. Other than that, DataSources don't do much.

DataRanges
~~~~~~~~~~

These define the visual extent of the source data to be plotted. I.e. these represent the axis ranges. Thus, to change the scales on your plot, you need to access/edit the Range objects. These usually a Range object for each index and value object respectively. Note, however, that PlotComponents_ can share Ranges.

Mappers
~~~~~~~

The Mappers (subclasses of AbstractMapper) do the actual mapping from the data coordinates into screen coordinates for display. The mappers take their input from the DataRange objects (which tell them want range to display). As well as mapping the PlotRenderers, the mappers are also shared by things like the axes and grids (anything which requires appropriate scaling from data coords to screen coords).

Overlays
~~~~~~~~

The Overlays (subclasses of AbstractOverlay) are all other visual (i.e. drawn) items on the plot. These include the axis lines, labels, ticks, ticklabels and grids. These also include annotations like data labels (arrows and text labels etc.).

Interactors/Tools
~~~~~~~~~~~~~~~~~

Interactivity is provided by means of "Tools". These are subclasses of BaseTool. Many predefined tools are provided to provid things like panning, zooming, data-selection etc.

Integrating Chaco into a wxPython Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get a plotting widget into a wxPython application, you need a Window object from the Enable library e.g.

Here's a minimal chaco app. It's doesn't do much (no pan/zoom), no axes, grid, colors etc.

::

   import wx
   import numpy
   from enthought.enable2.wx_backend.api import Window
   from from enthought.chaco2.api import create_line_plot
   app = wx.App(0)
   f = wx.Frame(None, -1, "hello from chaco")
   x = numpy.linspace(-10,10,512)
   y = numpy.cos(x)
   plot = create_line_plot((x,y),add_axis=True,add_grid=True)
   w = Window(f, component=plot)
   s = wx.Sizer(wx.VERTICAL)
   s.Add(w.control,1,wx.EXPAND)
   f.SetSizer(s)
   f.Show()
   app.MainLoop()

Like elsewhere in ETS, wherever a traited object represents a GUI-toolkit widget, the actual gui widget is accessed as the .control attribute (well, Trait actually) of the object.

Putting It All Together
~~~~~~~~~~~~~~~~~~~~~~~

TVTK
----

TVTK has without question cause me the most pain so far. At least part of the problem is that I'm already a regular VTK user, so the subtle renaming of the API requires a mental re-alignment. The good part about TVTK is the ease with which you can pop up a traits-editor to tweak the properties of an object. The downside is a greater disconnect between the tvtk-API and the standard D'Oxygen API docs. Although the standard docs are for C++, the python interface is almost identical and everything has doc-strings which are easy to call up in eclipse or ipython. With TVTK, code-completion is mostly broken in eclipse (see comments on the enthought egg-namespace above). With a library the size of VTK, code-completion is just about essential to avoid constantly refering to the html-docs. TVTK converts all the VTK object Getters and Setters into python properties. This is certainly more puthonic. This problem is, you can view a doc-string on a property.

This documentation problem might be mitigated if TVTK has some traits-aware auto-generated API documentation which would be a substitute for the standard VTK docs. However, this doesn't exist at present; only the core TVTK stuff is included in the endo-docs, presumably because the entire TVTK API is auto-generated at build-time.

Integrating a TVTK Scene into a wxPython Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is another area where TVTK scores over the standard VTK distribution. The canonical wxVTKRenderWindow widget was/is sporidically maintained (I guess because the main author now works at enthought!). For TVTK, you need to use Pyface (I'd like to see a more general description of what pyface is for) to provide a Scene object. e.g.

::

   import wx
   from enthought.tvtk.api import tvtk
   from enthought.pyface.tvtk.api import Scene
   app = wx.App(0)
   frame = wx.Frame(None, -1, "hello from TVTK")
   scene = Scene(frame)
   sizer = wx.BoxSizer(wx.VERTICAL)
   sizer.Add(scene.control, 1, wx.EXPAND)
   frame.SetSizer(sizer)
   cone = tvtk.ConeSource()
   mapper = tvtk.PolyDataMapper(input=cone.output)
   actor = tvtk.Actor(mapper=mapper)
   scene.renderer,add_actor(actor)
   frame.Show()
   app.MainLoop()

Pyface also provides a DecoratedScene_ class which adds a nice toolbar for configuring the camera view, saving a snapshot (with magnification control! yeay!) and a full-screen mode. This is great.

Like other traited components based on wxPython widgets, you access the underlying widget via the .control trait, which returns the wxPython window, for inclusion in parent windows or sizers etc.

The ETS API documentation
-------------------------

The "traits-aware" API documentation generated by a tool called Endo is quite nice. Here's a few suggestions which would hugely increase it's utility (in a manner similar to d'oxygen):

1. For every class listed, provide a link one or more python examples where it is used

2. Provide links to subclasses, as well as the superclass. This would make it easier to track both down as well as up the class tree. NOTE: I just noticed the "Class Hierarchy" link at the top-right of the endo docs; this allows you to browse down the tree.

.. ############################################################################

.. _ArrayEditor: ../ArrayEditor

.. _PlotItem: ../PlotItem

.. _ChacoClassTreeSmall: ../ChacoClassTreeSmall

.. _PlotRenderers: ../PlotRenderers

.. _PlotContainers: ../PlotContainers

.. _PlotRenders: ../PlotRenders

.. _DataSources: ../DataSources

.. _ChacoPlotRelationships: ../ChacoPlotRelationships

.. _PlotRenderer: ../PlotRenderer

.. _PlotComponents: ../PlotComponents

.. _DecoratedScene: ../DecoratedScene

