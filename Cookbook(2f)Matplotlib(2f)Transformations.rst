#format rst

Whenever you pass coordinates to matplotlib, the question arises, what kind of coordinates you mean. Consider the following example

::

   axes.text(x,y, "my label")

A label 'my label' is added to the axes at the coordinates x,y, or stated more clearly: The text is placed at the theoretical position of a data point (x,y). Thus we would speak of "data coords".  There are however other coordinates one can think of. You might e.g. want to put a label in the exact middle of your graph.  If you specified this by the method above, then you would need to determine the minimum and maximum values of x and y to determine the middle.  However, using transforms, you can simply use

::

   axes.text(0.5, 0.5, "middle of graph", transform=axes.transAxes)

There are four built-in transforms that you should be aware of (let ax be an Axes instance and fig a Figure instance):

::

   matplotlib.transforms.identity_transform()  # display coords
   ax.transData     # data coords
   ax.transAxes     # 0,0 is bottom,left of axes and 1,1 is top,right
   fig.transFigure  # 0,0 is bottom,left of figure and 1,1 is top,right

These transformations can be used for any kind of Artist, not just for text objects.

The default transformation for ax.text is ax.transData and the default transformation for fig.text is fig.transFigure.

Of course, you can define more general transformations, e.g. matplotlib.transforms.Affine, but the four listed above arise in a lot of applications.

To manually apply a transformation t to coordinates x,y, you can use t.xy_tup(x,y). To reverse this transformation, use t.inverse_xy_tup(x,y).  It is very important to use these functions and not to convert coordinates by hand.  Only this way you can be sure that your calculations work for non-linear coordinate systems as well (e.g. logarithmic or polar plots).

Example: tick label like annotations
------------------------------------

If you find that the built-in tick labels of Matplotlib are not enough for you, you can use transformations to implement something similar. Here is an example that draws annotations below the tick labels, and uses a transformation to guarantee that the x coordinates of the annotation correspond to the x coordinates of the plot, but the y coordinates are at a fixed position, independent of the scale of the plot:

::

   import matplotlib as M
   import Numeric as N
   import pylab as P
   blend = M.transforms.blend_xy_sep_transform
   def doplot(fig, subplot, function):
       ax = fig.add_subplot(subplot)
       x = N.arange(0, 2*N.pi, 0.05)
       ax.plot(x, function(x))
       trans = blend(ax.transData, ax.transAxes)
       for x,text in [(0.0, '|'), (N.pi/2, r'$\rm{zero\ to\ }\pi$'),
                      (N.pi, '|'), (N.pi*1.5, r'$\pi\rm{\ to\ }2\pi$'),
                      (2*N.pi, '|')]:
           ax.text(x, -0.1, text, transform=trans,
                   horizontalalignment='center')
   fig = P.figure()
   doplot(fig, 121, N.sin)
   doplot(fig, 122, lambda x: 10*N.sin(x))
   P.show()

Example: adding a pixel offset to data coords
---------------------------------------------

Sometimes you want to specify that a label is shown a fixed *pixel* offset from the corresponding data point, regardless of zooming. Here is one way to do it; try running this in an interactive backend, and zooming and panning the figure.

The way this works is by first taking a shallow copy of ``transData`` and then adding an offset to it. All transformations can have an offset which can be modified with ``set_offset``, and the copying is necessary to avoid modifying the transform of the data itself. New enough versions of matplotlib (currently only the svn version) have an ``offset_copy`` function which does this automatically.

::

   import matplotlib
   import matplotlib.transforms
   from pylab import figure, show
   # New enough versions have offset_copy by Eric Firing:
   if 'offset_copy' in dir(matplotlib.transforms):
       from matplotlib.transforms import offset_copy
       def offset(ax, x, y):
           return offset_copy(ax.transData, x=x, y=y, units='dots')
   else: # Without offset_copy we have to do some black transform magic
       from matplotlib.transforms import blend_xy_sep_transform, identity_transform
       def offset(ax, x, y):
           # This trick makes a shallow copy of ax.transData (but fails for polar plots):
           trans = blend_xy_sep_transform(ax.transData, ax.transData)
           # Now we set the offset in pixels
           trans.set_offset((x,y), identity_transform())
           return trans
   fig=figure()
   ax=fig.add_subplot(111)
   # plot some data
   x = (3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3)
   y = (2,7,1,8,2,8,1,8,2,8,4,5,9,0,4,5)
   ax.plot(x,y,'.')
   # add labels
   trans=offset(ax, 10, 5)
   for a,b in zip(x,y):
       ax.text(a, b, '(%d,%d)'%(a,b), transform=trans)
   show()

-------------------------

 CategoryCookbookMatplotlib_

