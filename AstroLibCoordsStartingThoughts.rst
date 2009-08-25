The following outlines some discussions and thoughts we have had at STScI regarding how sky coordinates should be handled. It isn't complete and is intended to get some comments about whether there are better approaches to solving the problem. We welcome the inputs of those more expert than us regarding coordinate systems.

There had been previous discussion in our group that suggested that we should review the VO metadata specification for Space-Time Coordinates that is very complete and consider basing a library on that (having  one good side benefit in that it makes using the VO simpler).  The problem is that the specification is almost entirely oriented towards ensuring that all relevant aspects of **state** are recorded and described, but it says nothing about the behavior or capabilities of such entities. It is all  about description, and virtually nothing about what is allowed to be  manipulated. It is likely that one would have a very hard time  developing classes that had simply described capabilities as far as transformation go. How will errors (those specified for the coordinates) be handled? It seems to be potentially intractable from this point of view. (For reference, here is a link to the relevant [`http://hea-www.harvard.edu/~arots/nvometa/SpaceTime.html`_ VO documentation)

Instead, I argue for trying to take the simplest concept, making that work and  then building on it. We could get going much sooner, and use it sooner for our applications.

How to get started
------------------

  What follows are some thoughts about how to handle coordinate

systems. This isn't completely thought out, and rather than try to polish it, I thought getting it out there for comments and ideas early was more important than polishing it internally. I also welcome input from those much more expert in the topic than we are.

Note: I have looked a bit for other OO implementations, but haven't found much.  Ivo Busko suggested looking at JSky, which I did, but most of the coordinate issues it  faces appear to relate to how to transform pixel coordinates to sky and visa versa (in other words, WCS issues). I didn't see much on mapping different  global coordinate systems to each other. There was a reference to the NCSA  horizon project. But that didn't appear to address it either, and seems pretty  stale to boot (i.e., old). If anyone else is aware of other efforts along this  line, please let me know.

Initially we'll address only directions and not 3d coordinates. In other, words,  how to handle apparent positions on the sky without regard to distance, or any effects of parallax.

Perhaps a brief digression is in order. Why not generalize and use 3 dimensional coordinates? I'd argue that the primary reason is that they do not map well to the most common observables. Telescopes routinely measure directions. Distances are often completely unknown. How does one handle that in a 3d coordinate system? The choice of limiting coordinates to direction eliminates that problem. And when 3 dimensions are needed, they are most naturally created by associating a direction with a distance and an origin since the distance is often determined by completely different means than direction. It's a very natural partioning of the dimensions. So I argue that direction is easily and usefully extended to 3 dimensions.

Objects
-------

**Spherical coordinates:** a location on a unit sphere. These coordinates  have no implicit frame of reference with regard to the "real world".  Coordinates use the usual theta, phi coordinates (e.g., ra, dec) as attributes in radians(degrees?) (double precision).

**World Spherical Coordinates:** Same, except there is an implied absolute, inertial frame of reference with regard to orientation (but not with regard to the origin).

It is important to note in this scheme that all coordinates are fixed in relation to inertial frames. For example, if I want to use a moving frame of reference (say, the earth) I must also specify a time associated with that coordinate that relates it to a fixed inertial direction. So a giving a latitude and longitude at a specific time identifies a direction in the inertial frame. Using a different time results in a different position. This scheme doesn't consider fixed coordinates in moving frames to be fixed in any way, and is only concerned with coordinates at specific times as they relate to inertial coordinates. One just views these frames as alternate means of specifying inertial coordinates that require time as part of the specification.

At the very least, we presume that different frames of reference know how to relate to a common inertial frame of reference to facilitate conversions. (Rather than trying to handle all pair combinations)

Some proposed assumptions
-------------------------

  1 Everywhere a simple single point is allowed, so will an arbitrary-dimension array of points be permitted (allowing for the fact that that array of points may be represented as a pair of separate arrays.

  2 for sky based coordinates, J2000 FK5 is a good interchange inertial frame of reference (or is ICRS more suitable?). 3 Time as referred to here does not refer to the time of a measurement, rather the time as related to a frame of reference. In some cases this may be the same thing (current ra, dec) but the distinction is  important. What we are relating is the coordinates of the same position in different frames, not trying to characterize moving objects

Crude class outline (names chosen for clarity over convenience for now):

::

    class SphericalCoordinate: # is this class necessary or is there just
                               # the inerital coordinate class needed?
         # defines basic operations (distance, relative position
         # angle, any sense in defining any other arithmetic operations?)
         def as_angles(self) # return tuple of component angles
         def as_unitvector(self)
         def distancefrom(self, coord)
         def positionangleof(self, coord)
         def offset(self, dist, positionangle)
         def.rotate(self, rotationaxis, rotation)
         ...and many possible others
    class WorldSphericalCoordinate(SphericalCoordinate):
         def inframe(self, frame)
         # other methods compute relative to this object's frame of
         #  reference
    class FrameOfReference: # abstract class
         # main purpose is to provide the machinery for converting to
         # and from the common inertial frame of reference. I'm not
         # sure what the best interface for that should be. In some
         # respects they may not need any persistent attributes if
         # their job is just to generate an inertial coordinate
         # object (And the reverse), and thus be mostly functional
         # in nature (perhaps objects are not needed at all).
         def asJ2000(self):
         def fromJ2000(self, coord):

derived classes from FrameOfReference will have customized constructors that will require specific info. e.g., (though for most common cases, I would think that 3 parameters, two angular and a time) are all that are needed)::

::

    dateobs="1990-5-3:21:13:17"
    frame = RADEC(dateobs)
    coord1 = WorldSphericalCoordinate("12h15m5s", "-4d5m17s", frame)
    coord2 = WorldSphericalCoordinate(120., 10.5)  # default degrees/J2000
    obsframe = EarthFrame(latitude=35.7, longitude=80, date=dateobs)
    print coord1.inframe(obsframe) # to get alt-az values
    print coord1  # J2000 by default
    print coord1.inframe(Galactic())
    print coord2.distancefrom(coord1) # the separation (degrees or radians?)
    print coord1.positionangleof(coord2) # relative to ?
    print coord1.offset(dist=0.5, positionangle=45)
    print coord1.rotate(rotationaxis=(120. 45), rotation=4.3)

Note that a different date could have been used for the earth frame than that used for the ra and dec.

Lots of details regarding what formats are permitted for angular measures, names, are being glossed over. I'm more interested in what operations are permitted.

There are a couple of issues regarding implementation that I have left open. One is what the internal frame of reference is. Two approaches appear possible here. One is for all objects to use J2000 FK5 for the internal representation. If you create a direction in another coordinate system, it is immediately converted to J2000. But that isn't the only way of dealing with it. One can store the coordinates in the frame given (along with the frame used and any other information such as time). When comparing between objects that use the same internal representation, no conversions are needed; this also prevents the need for round-trip conversions if one is only interested in coordinates in that frame. Only when this object is compared to another that uses a different frame of reference, is the conversion done (and since each frame of reference object knows how to convert to and from J2000, it is always possible to convert to a common frame of reference. The drawback of this approach is that conversions may be done many times if the object is compared to others several times.

Another issue is whether to store the angles or the components of the corresponding unit vector. The latter facilitates vector computations, which can be simpler to implement in many cases.

At the moment, I leave these two issues open to discussion.

Implementation can be gradual. Not all frames need support immediately; not all methods need to be provided immediately to make this useful. At the very least, if the framework is defined, then other tasks can start using these objects as part of their interface (as well as for the conversion capabilities). Others in the community may be willing to implement many of the holes once we provide a framework.

It seems that slalib routines give a good idea of the functionality that the coordinate object should provide. It also has many useful routines not directly relating to the coordinate concept itself that I suggest should be kept separate. Examples are: string decoding (but these may be used by the constructors for coordinates), sexagesimal conversions (likewise), calendars (but useful for specifying dates provided as arguments to constructors), timescales, proper motion, aberrations, refraction and airmass, ephemerides, and astrometry (these look like distortion and projection routines) [note I am using the categories used by our stsdas help pages for this library]. I see many of these other routines being usefully combined with coordinate objects, but not intrinsic to the idea of coordinate representation.

Should we use the scipy traits package for these objects (and the utility library in general)? [see `http://old.scipy.org/site_content/traits/":http://old.scipy.org/site_content/traits/`_ for somewhat dated documentation for what traits provide; essentially they provide a means of type and value checking user input)

I see these coordinate objects as being components of more complex computations. One can combine a velocity vector with a coordinate to determine aberrations or correct for aberrations. Or combine two directions with a 3-d vector to determine parallax. And so forth.

**License issues.** If we allow ourselves to be infected with GPL code, we perhaps can save much work by layering much on  slalib and wcslib (the former is a bit more troublesome since only the Fortran version is public and we have to deal with making that easy to distribute). Perhaps it is much more sensible to go with the flow here rather than re-implement much code that is already well tested [in my local inquiries, GPL may be problematic for STScI; I'm not aware of any previous precedents for STScI releasing GPL'ed software (if anyone is, please let me know); thus it raises the spectre of lawyers getting involved--just that alone will prevent us from using the license since it will mean several months of delay. We will continue looking at it but at this point I'm more reluctant to use GPL'ed code.]

**Testing.** If we re-implement, we should set up extensive cross checks with wrapped versions of slalib and wcslib that are part of a validation test suite. We can also do the same with many of the IDL astron routines though for those we need to run those from IDL rather than Python. This will give us and the community some confidence that the routines are well tested since we are comparing them to well-accepted standards.

If we decide to re-implement wcslib we likely only have to implement a small subset of the WCS models, at least initially (again, once in place others may contribute if they have a special need).

Comments and ideas?

