#format rst

The presence of Guido van Rossum as keynote speaker at the Scipy'06 conference is a good opportunity to have an open discussion with him on the needs, ideas, interests and concerns of the scientific python community.  Hopefully this will provide useful both to the scientific users, and to Guido in making decisions for future versions of the language.

This page will serve as a central point to gather ideas on topics for such a discussion.  This will allow those who can't come to the conference to still contribute ideas, as well as letting those who will be there organize the most important topics so the session is an effective one.  Finally, we'll contact Guido shortly before the conference to let him know about this, so that he can have a look at the page before coming to prepare the discussion better.

Feel free to either contribute to a topic below or add a new one.

Data type descriptors
---------------------

There seems to be a lot of duplication of effort in finding ways of describing raw binary data ... *(needs filling more...)*

Existing solutions
~~~~~~~~~~~~~~~~~~

1. array.arrays notation for types ['i'. 'f', etc]

#. ctypes notation for types [c_int, c_float, etc]

#. numpy's notation for types [dtype('<i4'), dtype('<f8')]

#.  the struct module (similar to #1, but not exactly the same)

Getting some part of NumPy into Python 2.6
------------------------------------------

We need to decide and explain to Guido what part of NumPy we would like to see get into Python 2.6.  Basically, we want a base-class with the C-structure of NumPy with few or no methods defined.   This could serve as a data-transfer object.  Coupled with a proper data-descriptor object, it could allow many extensions to communicate easily with each other about raw bytes. 

Raw memory allocator
--------------------

The problems with the buffer protocol exposed by the array object could be alleviated by defining a simple Python object that simply holds a pointer to memory (perhaps with its size stored).   This pointer to memory could then be properly reference counted and all objects that use the buffer protocol be required (or strongly advised) to use  this object instead of raw memory.   A simple C-API implementing the equivalent of malloc, free (simply a DECREF), and realloc would be all that was needed.   This would help ctypes by defining a standard for a void * pointer object. 

