#format rst

Exercise 1:
-----------

  extra methods for SDict as defined in tutorial:

::

       def has_key(self, key):
           if type(key) != type(''):
               raise TypeError
           return dict.has_key(self, key.lower())
       def update(self, odict):
           keys = odict.keys()
           values = odict.values()
           for i in range(len(keys)):
               if type(keys[i]) != type(''):
                   raise TypeError
               keys[i] = keys[i].lower()
           for key, value in zip(keys, values):
               self[key] = value
       def get(self, key, value=None):
           if type(key) != type(''):
               raise TypeError
           return dict.get(self, key.lower(), value)
       def setdefault(self, key, value):
           if type(key) != type(''):
               raise TypeError
           return dict.setdefault(self, key.lower(), value)

Exercise 2:
-----------

::

    # Code for transmission function is nearly identical (most of it would be place into
    # functions called by each).

    class TabularSource(SourceFunction):
        def __init__(self, filename, wavecol, fluxcol):
            '''Assumes use of data in FITS table. wavecol and fluxcol are strings
            identifying the columns that contain the wavelengths and fluxes
            '''
            tab = pyfits.getdata(filename)
            self.wave = tab.field(wavecol)
            self.flux = tab.field(fluxcol)
            # could add much error checking (e.g., monotonic wavelengths, etc)
        def __call__(self, wave):
            '''Use simple linear interpolation'''
            # Error if wave has values outside of tabulated range
            # Following to handle case of wave being a simple scalar
            if type(wave) != type(n.array(0)):
                awave = n.array([wave])
            else:
                awave = wave
            if ((awave.min() < self.wave.min()) or
                (awave.max() > self.wave.max())):
                    print 'wavelengths out of tabulated range'
                    raise ValueError
            return interpolate(self.wave, self.flux, wave)

    def interpolate(xtab, ytab, xsamp):
        # from example in tutorial section 3.7.3
        xind = n.searchsorted(xtab, xsamp)
        xfract = (xsamp-xtab[xind])/(xtab[xind+1]-xtab[xind])
        return ytab[xind] + xfract*(ytab[xind+1]-ytab[xind])

