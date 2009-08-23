#format rst

Exercise 2:
-----------

::

    import pyfits
    >>> im = pyfits.getdata('pix.fits')
    >>> hdr = pyfits.getheader('pix.fits')
    # or >>> data, hdr = pyfits.getdata('pix.fits', header=True)
    >>> print hdr['object']
    m51  B  600s
    >>> print im[:,9]
    [37 41 37...
    ...
    50 49 55 53 55 54]

Exercise3:
----------

::

    >>> scaledim = 2.3*im
    >>> print scaledim.sum()/scaledim.nelements()
    256.927575684

Exercise 4:
-----------

::

    >>> pyfits.writeto('pix2.fits',scaledim[192:-192,192:-192], hdr)
    >>> pyfits.info('pix2.fits')
    Filename: pix2.fits
    No.    Name         Type      Cards    Dimensions   Format
    0    PRIMARY     PrimaryHDU      68   (128, 128)    Float64

Exercise 5:
-----------

::

    >>> from numarray import *
    >>> y, x = indices((500,500)) # ints, next statements makes floats
    >>> y = y - 250.
    >>> x = x - 250.
    >>> im = sin(x/pi)*exp(-(x**2+y**)/2500.)
    >>> from numarray.fft import *
    >>> fim = fft2d(im)
    >>> import numdisplay
    >>> numdisplay.display(abs(fim))

