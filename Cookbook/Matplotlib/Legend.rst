#format rst

Cookbook/Matplotlib/Legend
==========================

Legends for overlaid lines and markers
--------------------------------------

If you have a lot of points to plot, you may want to set a marker only once every *n* points, e.g.

::

   plot(x, y, '-r')
   plot(x[::20], y[::20], 'ro')

Then the automatic legend sees this as two different plots. One approach is to create an extra line object that is not plotted anywhere but used only for the legend:

::

   from matplotlib.lines import Line2D
   line = Line2D(range(10), range(10), linestyle='-', marker='o')
   legend((line,), (label,))

Another possibility is to modify the line object within the legend:

::

   line = plot(x, y, '-r')
   markers = plot(x[::20], y[::20], 'ro')
   lgd = legend([line], ['data'], numpoints=3)
   lgd.get_lines()[0].set_marker('o')
   draw()

Legend outside plot
-------------------

There is no nice easy way to add a legend outside (to the right of) your plot, but if you set the axes right in the first place, it works OK:

::

   figure()
   axes([0.1,0.1,0.71,0.8])
   plot([0,1],[0,1],label="line 1")
   hold(1)
   plot([0,1],[1,0.5],label="line 2")
   legend(loc=(1.03,0.2))
   show()

Removing a legend from a plot
-----------------------------

One can simply set the ``legend_`` attribute of the axes to ``None`` and redraw:

::

   ax = gca()
   ax.legend_ = None
   draw()

If you find yourself doing this often use a function such as

::

   def remove_legend(ax=None):
       """Remove legend for ax or the current axes."""
       from pylab import gca, draw
       if ax is None:
           ax = gca()
       ax.legend_ = None
       draw()

(Source: `Re: How to delete legend with matplotlib OO from a graph? <http://osdir.com/ml/python.matplotlib.general/2005-07/msg00285.html>`_)

