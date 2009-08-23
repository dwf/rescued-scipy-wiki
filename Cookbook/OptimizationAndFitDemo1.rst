#format rst

This is a quick example of creating data from several [`http://www.scipy.org/doc/api_docs/scipy.special.info.html`_ Bessel functions] and finding local maxima, then fitting a curve using some spline functions from the [`http://www.scipy.org/doc/api_docs/scipy.interpolate.info.html`_ scipy.interpolate] module.  The [`http://code.enthought.com/chaco/`_ enthought.chaco] package and [`http://www.wxpython.org/`_ wxpython] are used for creating the plot.  [`http://wiki.wxpython.org/index.cgi/PyCrust`_ PyCrust_] (which comes with wxpython) was used as the python shell.

::

   from enthought.chaco.wx import plt
   from scipy import arange, optimize, special
   plt.figure()
   plt.hold()
   w = []
   z = []
   x = arange(0,10,.01)
   for k in arange(1,5,.5):
      y = special.jv(k,x)
      plt.plot(x,y)
      f = lambda x: -special.jv(k,x)
      x_max = optimize.fminbound(f,0,6)
      w.append(x_max)
      z.append(special.jv(k,x_max))
   plt.plot(w,z, 'ro')
   from scipy import interpolate
   t = interpolate.splrep(w, z, k=3)
   s_fit3 = interpolate.splev(x,t)
   plt.plot(x,s_fit3, 'g-')
   t5 = interpolate.splrep(w, z, k=5)
   s_fit5 = interpolate.splev(x,t5)
   plt.plot(x,s_fit5, 'y-')

::

   #class left

   inline:chacoscreenshot.png
   Optimization Example

