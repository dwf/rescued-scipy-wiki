#format rst

Exercise 1:
-----------

::

    >>> import pyfits
    >>> tab = pyfits.getdata('fuse.fits')
    >>> tab.info()
    >>> flux =  10.**12*tab.field('flux')
    >>> error = 10.**12*tab.field('flux')
    >>> plot(flux, error,'.')

Exercise 2, 3:
--------------

::

    >>> im = pyfits.getdata('pix.fits')
    >>> from numarray.convolve import boxcar
    >>> sim = boxcar(im, (31, 31))
    >>> sim = 100*sim/sim.max()
    >>> contour(sim, contours= [90, 70, 50, 30, 10])
    >>> imshow(im, vmax=500)
    >>> contour(sim, [90,70,50,30,10],hold=True)

Exercise 4:
-----------

::

    >>> imshow(im, vmax=500)
    >>> gray()
    >>> text(380,72,'my hometown!',color='yellow'
    >>> savefig('fluxerror.ps')

Exercise 5:
-----------

  This example wasn't really doable with the level of knowledge given but  a solution is given anyway (turned out overplotting with a transparent background on an image is not quite so simple).

::

    >>> ax = subplot(111, frameon=False) # leads to a clear plot background so images show through
    >>> imshow(im, vmax=500)
    >>> sim = 500.*im/8000. # scale image to prevent shrinking image when plot value is larger than 512
    >>>                     # no matter, image will still rescale due to auto ticking
    >>> def buttonclick(event):
    ...     # left button, note use of int() to make position acceptable for indexing
    ...     if event.button==1: plot(sim[int(event.ydata)], hold=True)
    ...     if event.button==2: plot(sim[:,int(event.xdata)], hold=True)
    ...
    >>> cid=connect('button_press_event',buttonclick)
    >>> # click away. Note that old overplot remain. More work is needed to make this more useful,
    >>> # particularly with regard to plot scaling and keeping the image size unchanged.
    >>> disconnect(cid)

