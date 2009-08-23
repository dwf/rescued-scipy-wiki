#format rst

SciPy Tutorial Day 2 Notes
==========================

by David Shupe

{{{SciPy_ Tutorials

Eric Jones - Python as "Glue" (we were given a PDF of Eric's slides)

Modernizing code -- commonly taken to be, slap a GUI on it. But then can't drive it by a text file.

To take an object-oriented view of the problem - circle all the nouns!

"advisor test" - can your advisor read the API calls?  (meaning someone more interested in the physics and not the computer science)

Bill Spotz - SWIG tutorial

See SWIG tutorial directory for PPT and complete example.

Eric Jones - f2py

Numpy now has the ability to allocate array in column-major order (Fortran ordering).

============

Travis Oliphant - Signal and Image Processing

Reading and writing

  - scipy.io.read_array - use csv module - "roll your own"

NetCDF reader in SciPy_ opens the arrays as memory-mapped arrays....Travis says this is nice, encouraged for other readers (like PyFITS?).

Makewav.py - plays notes.  Use Audacity to play.

Travis got excited about nd_image -- but it was written for numarray. That got him interested in writing Numpy.

ndimage.affine_transform: prefilter=True if inputting an image.  For efficiency can pre-filter (calculate B-spline coefficients) and set prefilter=False.

Filtering examples on photo of kids in cornfield. run -i ndmorph.py

Interpolation:

  scipy.interpolate scipy.nd_image.map_coordinates scipy.sandbox.delaunay

Break

Filtering

  run -i edge.py

  part2.py

[Interesting: Travis starts python with "ipython -gthread"]

Eigenimages - of 15 photos of faces of SciPy_ attendees.

scipy.signal -- more needed for wavelets.

}}}

