#format rst

Here is a preliminary list of use cases, in various categories. This is a working document - please comment!

Potential cases are presently grouped by functionality, and may not all be in scope for the first build.

A. Atomic operations for interactive use
----------------------------------------

1. Transform alpha, delta to l,b

#. Transform B1950 to J2000

#. Transform hmsdms to decimal degrees

#. Transform decimal degrees to hmsdms

Comments on category A: 

These would be basic items I would look for in a coord library. If I can't do these things, I'll look for another toolkit.

B. Working with a list of objects
---------------------------------

1. Sort a list of coords by RA, then dec

#. Find isolated objects in a list (nearest neighbor > r)

#. Find objects isolated in one coordinate (NN separation in RA > d)

Comments on category B:

These are common tasks for planning observing runs, trying to find clean objects to generate PSFs or perform other analysis, and planning some types of spectroscopic observations.

C. Working with pairs of objects
--------------------------------

1. Measure the distance between two points

#. Determine whether a pair of objects are co-incident within their errors

Comments on category C: 

The first item might nicely hook into a matplotlib clicker function. The second would be very useful for matching observations taken at different resolutions.

D. Working with two lists of objects, or an object and a list
-------------------------------------------------------------

1. Match one object to a list of objects within a radius

#. Match one object to a list of objects within an annulus

#. Match two lists of objects within a radius

     3a. Handle multiple matches

     3b. Handle no matches 3c. Distinguish A->B, B->A, A<->B match cases

#. Match two lists of objects within their errors

Comments on category D:

Catalog matching strikes me as an application that would use the coord library and the AstroAsciiData_ library. The goal here *really* would be to develop the two libraries, but the application provides complex use cases and an immediate user draw once the basic functionality is complete.

E. Working with polygons and/or ellipses
----------------------------------------

1. Determine whether an object is within a field

#. Determine whether two polygons overlap

#. Determine whether two ellipses overlap

Comments on category E:

"Is my object in this image?" is a common question. Overlapping polygons or ellipses has applications to finding isolated objects if you actually have their extents as well as their positions, which is not uncommon.

Added by Joe Harrington:

Planetary users will want to be able to add FITS keywords to an image of a planet that specify the location, distance, radii and/or oblateness, and orientation of the planet and have interactive displays like:

* longitude, latitude (planetocentric or planetodetic/planetographic), and oblate planetary radius at the point under the cursor

* X, Y, and Z in another coordinate system including:

* sky-plane coords (axes aligned with RA and DEC but origin at

    center of planet)

* planetary rectilinear coords (axes aligned with equator and

    pole, one axis at a specified zero of longitude, origin at center of planet)

* "planetary sky-plane" coords (axes aligned with projected

    pole, equatorial ansae, and line of sight, origin at center of planet)

* observer coords (axes defined by spacecraft orientation

    keywords, origin at spacecraft, values calculated for surface of an ellipsoid in space)

Also, FITS files containing various map projections should be supported for interactive readout of lon, lat, radius.

I know you won't be writing the interactive part, but the functions to convert image X,Y into the quantities above based on header values would be important.

From laidler Mon May 2 13:28:17 -0500 2005 From: laidler Date: Mon, 02 May 2005 13:28:17 -0500 Subject: Planetary use cases Message-ID: <`20050502132817-0500@www.scipy.org`_>

Most of these sound like cases for the ["AstroLibWCS"] library to me, as they convert image (X,Y) coordinates to sky or planetary coordinates. 

Are there cases of interest to planetary astronomers that involve transformations between coordinate systems that **don't** involve images? Some of these look like they might but I can't quite tell.

When I think of "coordinates" and "planets", I think of moving target considerations and ephemerides to identify the location of a planet in the sky on a particular date. 

.. ############################################################################

.. _AstroAsciiData: ../AstroAsciiData

.. _20050502132817-0500@www.scipy.org: mailto:20050502132817-0500@www.scipy.org

