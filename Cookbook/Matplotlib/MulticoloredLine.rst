#format rst

Defining colors manually
========================

attachment:colored_line.py is a simple illustration of how to make the color of each segment of a line depend on some property of the data being plotted.

inline:colored_line.png

Here is the script:

::

   #/usr/bin/env python
   ''' Color parts of a line based on its properties, e.g., slope.
   This is a minimal LineCollection demo.
   With a bit more work we could use a colormap instead of
   the if/elif/else block.  It might make sense to simply modify
   LineCollection to inherit from ScalarMappable, like the other
   collections do.
   '''
   from pylab import *
   from matplotlib.collections import LineCollection
   from matplotlib.colors import colorConverter
   x = arange(0, 10, 0.1)
   y = sin(x)
   z = cos(0.5 * (x[:-1] + x[1:]))  # first derivative
   rr = colorConverter.to_rgba('r')
   gg = colorConverter.to_rgba('g')
   bb = colorConverter.to_rgba('b')
   colors = list()
   for zz in z:
       if zz < -.5:
           colors.append(rr)
       elif zz < .5:
           colors.append(gg)
       else:
           colors.append(bb)
   points = zip(x, y)
   segments = zip(points[:-1], points[1:])
   ax = axes(frameon=True)
   LC = LineCollection(segments, colors = colors)
   LC.set_linewidth(3)
   ax.add_collection(LC)
   axis([0, 10, -1.1, 1.1])
   savefig('colored_line.png', dpi=70)
   show()

Note that the number of segments is one less than the number of points.

An alternative strategy would be to generate one segment for each contiguous region of a given color.

Using a colormap
================

If you have a parametric curve to display, and want to represent the parameter using color.

inline:colored_line2.png

::

   from pylab import *
   from matplotlib.collections import LineCollection
   t = linspace(0,10,200)
   x = cos(pi*t)
   y = sin(t)
   ax = gca()
   points = zip(x,y)
   segments = zip(points[:-1], points[1:])
   colors = cm.copper(linspace(0,1,200))
   LC = LineCollection(segments, colors = colors)
   LC.set_linewidth(3)
   axis([-1, 1, -1, 1])
   ax.add_collection(LC)
   savefig('colored_line2.png', dpi=70)
   show()

-------------------------

 CategoryCookbookMatplotlib_

