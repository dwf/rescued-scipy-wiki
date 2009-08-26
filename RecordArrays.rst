#format rst

Table of Contents
=================

TableOfContents_

Overview
========

What is a Record Array?
-----------------------

A Record Array allows access to its data using named fields.  In other words, instead of referring to the first dimension of a matrix ``x`` as ``x[0]``, one might name that dimension 'space', and use ``x['space']`` instead.  Imagine your data being a spreadsheet, then the field names would be the column headings.

Example
-------

We would like to represent a small colour image. The image is two pixels high and two pixels wide.  Each pixel has a red, green and blue colour component, which is represented by a 32-bit floating point number between 0 and 1.

Intuitively, we could represent the image as a 3x2x2 array, where the first dimension represents the color, and the last two the pixel positions, i.e.

::

   In [1]: from numpy import *
   In [2]: img = array([ [[0,1], [0,0]], [[0,0], [1,0]], [[0,0], [0,1]] ], dtype=float32)
   In [3]: img
   Out[3]:
   array([[[ 0.,  1.],
           [ 0.,  0.]],
          [[ 0.,  0.],
           [ 1.,  0.]],
          [[ 0.,  0.],
           [ 0.,  1.]]], dtype=float32)

This image has a black pixel in the upper-left corner, a red pixel in the upper-right corner, a green pixel in the bottom-left corner and a blue pixel in the bottom-right corner.  We can examine the red components

::

   In [4]: img[0]
   Out[4]:
   array([[ 0.,  1.],
          [ 0.,  0.]], dtype=float32)

or view the colour components of the red pixel in the upper-righthand corner

::

   In [5]: img[:,0,1]
   Out[5]: array([ 1.,  0.,  0.], dtype=float32)

This works, but requires us to keep track of the dimensions and what they represent.  It would be simpler to access the colour components by name.  For that purpose, we use record arrays:

::

   In [6]: img = array([[(0,0,0), (1,0,0)], [(0,1,0), (0,0,1)]], [('r',float32),('g',float32),('b',float32)])
   or
   In [6]: img = array([[(0,0,0), (1,0,0)], [(0,1,0), (0,0,1)]], {'names': ('r','g','b'), 'formats': ('f4', 'f4', 'f4')})
   or
   In [6]: img = zeros((2,2), [('r',float32),('g',float32),('b',float32)])
   In [7]: img.flat = [(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
   In [8]: img
   Out[8]:
   array([[(0.0, 0.0, 0.0), (1.0, 0.0, 0.0)],
          [(0.0, 1.0, 0.0), (0.0, 0.0, 1.0)]],
         dtype=[('r','<f4'),('g','<f4'),('b','<f4')])

Note the descriptor type here, which is given in the array interface format as a list of tuples where each tuple is (<name>, <data-type>).

Again, we can examine the colour components, but this time by name, e.g.

::

   In [9]: img['r']
   Out[9]:
   array([[ 0.,  1.],
          [ 0.,  0.]], dtype=float32)

or view the colour components of the red pixel in the upper-righthand corner

::

   In [10]: img[0,1]
   Out[10]: (1.0, 0.0, 0.0)

But what if we would still like to view the data as a 3x2x2 matrix?

::

   In [11]: img_mat = img.view((float32, 3))
   In [12]: img_mat
   Out[12]:
   array([[[ 0.,  0.,  0.],
           [ 1.,  0.,  0.]],
          [[ 0.,  1.,  0.],
           [ 0.,  0.,  1.]]], dtype=float32)
   In [13]: img_mat = img_mat.swapaxes(0,2)
   In [14]: img_mat
   Out[14]:
   array([[[ 0.,  1.],
           [ 0.,  0.]],
          [[ 0.,  0.],
           [ 1.,  0.]],
          [[ 0.,  0.],
           [ 0.,  1.]]], dtype=float32)

Note that ``img_mat`` is simply a view on the data in ``img``, which means that you can still manipulate ``img`` via ``img_mat``.

Finally, the ``recarray`` class allows us to view named fields as properties.

::

   In [15]: rimg = img.view(recarray)
   In [16]: rimg.r
   Out[16]:
   array([[ 0.,  1.],
          [ 0.,  0.]], dtype=float32)

Usage summary
=============

Creating
--------

::

   img = zeros((2,2), {'names': ('r','g','b'), 'formats': (float32, float32, float32)})

or

::

   img = zeros((2,2), [('r','f4'),('g','f4'),('b','f4')])

Accessing fields
----------------

::

   img['r'], img['g'], img['b']
   rimg = img.view(recarray)
   r.r, r.g, r.b

Viewing the underlying data
---------------------------

::

   img.view((float32, 3))

.. ############################################################################

.. _TableOfContents: ../TableOfContents

