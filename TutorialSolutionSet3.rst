#format rst

Exercise 1:
-----------

::

    >>> import pyfits
    >>> from pylab import *
    >>> fo = pyfits.open('tut3f1.fits')
    >>> fo.info()
    [shows 10 Int32 extensions with 400x400 images]
    >>> cube = zeros((10,400,400))
    >>> for i in range(len(fo)-1): cube[i] = fo[i+1].data
    >>> s = cube.sum(axis=0)
    >>> imshow(s)

Exercise 2 (using PyRAF so that iraf tools can be used):
--------------------------------------------------------

::

    --> import pyfits
    --> imhead tut3f1.fits[1] l+
    tut3f1.fits[1][400,400][int]:
    No bad pixels, min=0., max=0. (old)
    Line storage mode, physdim [400,400], length of user area 162 s.u.
    Created Fri 12:19:29 22-Jul-2005, Last modified Fri 12:19:29 22-Jul-2005
    Pixel file "fff.fits" [ok]
    PCOUNT  =                    0 / number of parameters
    GCOUNT  =                    1 / number of groups
    TARGET  = 'cosmic background'
    PURPOSE = 'none that I can think of'
    --> fo = pyfits.open('tut3f1.fits', mode='update')
    --> for i in range(10):
    ...     fo[i+1].header.update('imnum', i+1, after='target')
    ...     fo[i+1].header.add_history('added imnum value')
    ...
    --> fo.flush()
    --> imhead tut3f1.fits[3] l+
    tut3f1.fits[3][400,400][int]:
    No bad pixels, min=0., max=0. (old)
    Line storage mode, physdim [400,400], length of user area 243 s.u.
    Created Fri 14:05:36 22-Jul-2005, Last modified Fri 14:05:36 22-Jul-2005
    Pixel file "xxx.fits" [ok]
    PCOUNT  =                    0 / number of parameters
    GCOUNT  =                    1 / number of groups
    TARGET  = 'cosmic background'
    IMNUM   =                    3
    PURPOSE = 'none that I can think of'
    HISTORY added imnum value

Exercise 3:
-----------

::

    >>> import numpy.random as nr
    >>> rx = nr.random(1000000)
    >>> ry = nr.random(1000000)
    >>> r = sqrt(rx**2 + ry**2)
    >>> float(len(where(r<1)[0]))/len(r)
    0.785991 # your answer will vary!
    >>> pi/4
    0.78539816339744828

Exercise 4:
-----------

  First generate some data, N time values, and M frequency values to be sampled (between 0 and 2pi), pick 100 for N and 147 for M, and generate random numbers. Note that these frequency sampling points are neither uniform, nor in any order.

::

    >>> import numpy.random as nr
    >>> ts = nr.random(100)
    >>> freqsamp = nr.random(147)*2*pi
    >>> n = arange(100)
    >>> earg = multiply.outer(n, freqsamp) # generate array for exponential  argument
    >>> expval = exp(-1.j*earg) # evaluated exponential
    >>> ts.shape = (100, 1) # to make broadcasting work properly; can use NewAxis too (see docs).
    >>> sprod = ts*expval
    >>> freqvals = sprod.sum(axis=0) # perform summation

