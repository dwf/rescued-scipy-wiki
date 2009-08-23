#format rst

::

   >>> import coords as C
   >>> print C.__version__
   0.25

   #Unit conversions
   >>> ob=C.Position('12:34:45.34 -23:42:32.6')
   >>> ob.hmsdms()
   '12:34:45.340 -23:42:32.600'
   >>> ob.dd()
   (188.68891666666667, -23.709055555555555)
   >>> ob.rad()
   (3.2932428578545374, -0.41380108198269777)

   #Angular separations
   >>> p1=C.Position("01:23:45.300 +65:43:31.240")
   >>> p2=C.Position("01:23:45.62 +65:43:31.20")
   >>> p1.angsep(p2)
   0.000548 degrees
   >>> delta=p1.angsep(p2)
   >>> delta.arcsec()
   1.973739377865491
   >>> p1.within(p2,3.0,units='arcsec')
   True

   # Coordinate conversions
   >>> ob.j2000()
   (188.68891666666667, -23.709055555555555)
   >>> ob.b1950()
   (188.03056480942405, -23.433637283819877)
   >>> ob.galactic()
   (298.01638938748795, 39.003358150874568)
   >>> ob.ecliptic()
   (197.58457414028533, -18.294241465720475)

   >>> p3=C.Position("01:23:45 -65:43:21.4",equinox='J2000')
   >>> p4=C.Position("01:23:45 -65:43:21.4",equinox='B1950')
   >>> p3.j2000()
   (20.9375, -65.722611111111107)
   >>> p4.j2000()
   (21.356870704681981, -65.462921080444147)

   >>> p3.angsep(p4)
   0.312199 degrees

   >>> p5=C.Position((0.0,0.0),system='galactic')
   >>> p5.j2000()
   (266.40499571858879, -28.936169261309555)


    >>> #Specify position in hmsdms
    >>> polaris=C.Position("02:31:49.08 +89:15:50.8")
    >>> polaris.dd()
    (37.954500000000003, 89.264111111111106)
    >>> polaris.hmsdms()
    "02:31:49.080 +89:15:50.800"
    >>> print polaris.details()

            System: celestial
           Equinox: J2000

    >>> #Specify position in decimal degrees
    >>> ob=C.Position((52.9860209, -27.7510006))
    >>> ob.hmsdms()
    "03:31:56.645 -27:45:03.602"
    >>> ob.dd()
    (52.9860209, -27.751000600000001)
    >>>
    >>> #Use as calculator without saving the intermediate object
    >>> C.Position("12:34:45.4 -22:21:45.4").dd()
    (188.68916666666667, -22.362611111111111)

