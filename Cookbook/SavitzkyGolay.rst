#format rst

Savitzky Golay Filtering
========================

The Savitzky Golay filter is a particular type of low-pass filter, well adapted for data smoothing. For further information see: http://www.nrbook.com/b/bookcpdf/c14-8.pdf  (or http://www.dalkescientific.com/writings/NBN/data/savitzky_golay.py  for a pre-numpy implementation).

Sample Code
-----------

::

   def savitzky_golay(data, kernel = 11, order = 4):
       """
           applies a Savitzky-Golay filter
           input parameters:
           - data => data as a 1D numpy array
           - kernel => a positiv integer > 2*order giving the kernel size
           - order => order of the polynomal
           returns smoothed data as a numpy array
           invoke like:
           smoothed = savitzky_golay(<rough>, [kernel = value], [order = value]
       """
       try:
               kernel = abs(int(kernel))
               order = abs(int(order))
       except ValueError, msg:
           raise ValueError("kernel and order have to be of type int (floats will be converted).")
       if kernel % 2 != 1 or kernel < 1:
           raise TypeError("kernel size must be a positive odd number, was: %d" % kernel)
       if kernel < order + 2:
           raise TypeError("kernel is to small for the polynomals\nshould be > order + 2")
       # a second order polynomal has 3 coefficients
       order_range = range(order+1)
       half_window = (kernel -1) // 2
       b = numpy.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
       # since we don't want the derivative, else choose [1] or [2], respectively
       m = numpy.linalg.pinv(b).A[0]
       window_size = len(m)
       half_window = (window_size-1) // 2
       # precompute the offset values for better performance
       offsets = range(-half_window, half_window+1)
       offset_data = zip(offsets, m)
       smooth_data = list()
       # temporary data, with padded zeros (since we want the same length after smoothing)
       data = numpy.concatenate((numpy.zeros(half_window), data, numpy.zeros(half_window)))
       for i in range(half_window, len(data) - half_window):
               value = 0.0
               for offset, weight in offset_data:
                   value += weight * data[i + offset]
               smooth_data.append(value)
       return numpy.array(smooth_data)

Figure
------


.. image:: images/Cookbook/SavitzkyGolay/cd_spec.png
 CD-spectrum of a protein. Black: raw data. Red: filter applied

A fix for data which do not start and end at zero
-------------------------------------------------

The above implementation is correct if and only if the input vector starts and ends sufficiently close to 0. When applied to other data, it adds ugly noise at the "non-zero" ending. This problem is caused by padding the data with zeros from both sides. Instead, data may be padded with the first value on the left side and with the last value on the right. That is,

::

   # temporary data, with padded zeros (since we want the same length after smoothing)
   data = numpy.concatenate((numpy.zeros(half_window), data, numpy.zeros(half_window)))

should be changed to:

::

   # temporary data, with padded first/last values (since we want the same length after smoothing)
   firstval=data[0]
   lastval=data[len(data)-1]
   data = numpy.concatenate((numpy.zeros(half_window)+firstval, data, numpy.zeros(half_window)+lastval))

A much better solution would be to extend the signal with its mirror image. It can be shown that such an extension of a smooth function is continuous and smooth at the original end points. The above fragment should then be substituted with:

::

      # temporary data, extended with a mirror image to the left and right
       firstval=data[0]
       lastval=data[len(data)-1]
       #left extension: f(x0-x) = f(x0)-(f(x)-f(x0)) = 2f(x0)-f(x)
       #right extension: f(xl+x) = f(xl)+(f(xl)-f(xl-x)) = 2f(xl)-f(xl-x)
       leftpad=numpy.zeros(half_window)+2*firstval
       rightpad=numpy.zeros(half_window)+2*lastval
       leftchunk=data[1:1+half_window]
       leftpad=leftpad-leftchunk[::-1]
       rightchunk=data[len(data)-half_window-1:len(data)-1]
       rightpad=rightpad-rightchunk[::-1]
       data = numpy.concatenate((leftpad, data))
       data = numpy.concatenate((data, rightpad))

A wrapper for cyclic voltammetry data
-------------------------------------

One of the most popular applications of S-G filter, apart from smoothing UV-VIS and IR spectra, is smoothing of curves obtained in electroanalytical experiments. In cyclic voltammetry, voltage (being the abcissa) changes like a triangle wave. And in the signal there are cusps at the turning points (at switching potentials) which should never be smoothed. In this case, Savitzky-Golay smoothing should be done piecewise, ie. separately on pieces monotonic in x:

::

   def savitzky_golay_piecewise(xvals, data, kernel=11, order =4):
       turnpoint=0
       last=len(xvals)
       if xvals[1]>xvals[0] : #x is increasing?
           for i in range(1,last) : #yes
               if xvals[i]<xvals[i-1] : #search where x starts to fall
                   turnpoint=i
                   break
       else: #no, x is decreasing
           for i in range(1,last) : #search where it starts to rise
               if xvals[i]>xvals[i-1] :
                   turnpoint=i
                   break
       if turnpoint==0 : #no change in direction of x
           return savitzky_golay(data, kernel, order)
       else:
           #smooth the first piece
           firstpart=savitzky_golay(data[0:turnpoint],kernel,order)
           #recursively smooth the rest
           rest=savitzky_golay_piecewise(xvals[turnpoint:], data[turnpoint:], kernel, order)
           return numpy.concatenate((firstpart,rest))

