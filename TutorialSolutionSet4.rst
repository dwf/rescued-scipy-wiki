#format rst

Exercise 1:
-----------

::

    [in file refits.py]
    '''function to use regular expression matching on header keyword names
    and print all those that match
    '''

    import re
    import pyfits

    def findkeywords(filename, pattern):
        rekey = re.compile(pattern, flags=re.IGNORECASE)
        fo = pyfits.open(filename)
        extn = 0
        for ext in fo:
            hdrcards = ext.header.ascardlist()
            for card in hdrcards:
                mo = rekey.match(card.key)
                if mo and mo.end()==len(card.key): # to ensure match of entire key
                    print 'ext=%d'% extn, card
            extn += 1

Exercise 2:
-----------

::

    [in file refits_iraf.py]
    from pyraf import iraf
    import refits

    parfile = iraf.osfn('home$scripts/findkey.par')
    t = iraf.IrafTaskFactory(taskname='findkey', value=parfile,   function=refits.findkeywords)

    [in file home$scripts/findkey.par]
    filename,s,a,"",,,"FITS file to search for keywords"
    searchstring,s,a,"",,,"Regular expression pattern"
    mode,s,h,"al"

    Then doing (in pyraf)
    --> pyexecute('refits_iraf.py')
    --> lpar findkey
         filename =               FITS file to search for keywords
     searchstring =               Regular expression pattern
            (mode = al)
    --> findkey pix.fits naxis.*
    ext=0 NAXIS   =                    2 / Number of axes
    ext=0 NAXIS1  =                  512 / Axis length
    ext=0 NAXIS2  =                  512 / Axis length  

