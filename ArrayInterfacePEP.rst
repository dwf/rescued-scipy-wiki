#format rst

The Array and Buffer interface PEPs
===================================

This page is meant to summarize the issues related to the PEPs (Python Enhancement Proposals) which Travis Oliphant has presented to the core Python team for support of a multidimensional array and an enhanced buffer interface in the language.

The purpose of this page is to present a reasonably organized view of the main points, usage cases and technical issues.  While the mailing lists are an excellent place for back-and-forth arguments, it is time-consuming to get an overview of a topic from a mailing list archive.  This page should provide such organized information in one easy to find location.

*This page is currently mostly a placeholder, please contribute by fillng in useful information.*

Overview
--------

[ Provide a reasonably concise overview of the main idea and its need. ]

Usage Cases
-----------

[ Specific examples of problems where this could help ]

Technical Issues
----------------

[ Summarize here technical points as they get hashed out in the mailing list discussion, so that they don't need to be repeated over and over ]

Resources
---------

[ Put here relevant links to the PEPs themselves, related projects, mailing list threads, etc. ]

Here are the threads related to the PEPs in Gmane:  [`http://news.gmane.org/group/gmane.comp.python.devel/`_]

PEP: Adding data-type objects to the standard library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Author: Travis Oliphant <oliphant <at> ee.byu.edu>

Status: Draft

Type: Standards Track

Created: 05-Sep-2006

Python-Version: 2.6

Abstract

  This PEP proposes adapting the data-type objects from NumPy_ for inclusion in standard Python, to provide a consistent and standard way to discuss the format of binary data.

Rationale

  There are many situations crossing multiple areas where an interpretation is needed of binary data in terms of fundamental data-types such as integers, floating-point, and complex floating-point values.  Having a common object that carries information about binary data would be beneficial to many people. The creation of data-type objects in NumPy_ to carry the load of describing what each element of the array contains represents an evolution of a solution that began with the PyArray__Descr structure in Python's own array object.  These data-type objects can represent arbitrary byte data.  Currently such information is usually constructed using strings and character codes which is unwieldy when a data-type consists of nested structures.

Proposal

  Add a PyDatatypeObject_ in Python (adapted from NumPy_'s dtype object which evolved from the PyArray__Descr structure in Python's array module) that holds information about a data-type.  This object will allow packages to exchange information about binary data in a uniform way (see the extended buffer protocol PEP for an application to exchanging information about array data).

Specification

  The datatype is an object that specifies how a certain block of memory should be interpreted as a basic data-type. In addition to being able to describe basic data-types, the data-type object can describe a data-type that is itself an array of other data-types as well as a data-type that contains arbitrary "fields" (structure members) which are located at specific offsets. In its most basic form, however, a data-type is of a particular kind (bit, bool, int, uint, float, complex, object, string, unicode, void) and size.

  Datatype objects can be created using either a type-object, a string, a tuple, a list, or a dictionary according to the following constructors: Type-object:

    For a select set of type-objects a data-type object describing that basic type can be described:

    Examples:  >>> datatype(float) datatype('float64')

    >>> datatype(int) datatype('int32')  # on 32-bit platform (64 if c-long is 64-bits)

  Tuple-object

    A tuple of length 2 can be used to specify a data-type that is an array of another kind of basic data-type (this array always describes a C-contiguous array).

    Examples:  >>> datatype((int, 5)) datatype(('int32', (5,))) # describes a 5*4=20-byte block of memory laid out as  #  a[0], a[1], a[2], a[3], a[4]

    >>> datatype((float, (3,2)) datatype(('float64', (3,2))    # describes a 3*2*8=48 byte block of memory that should be # interpreted as 6 doubles laid out as arr[0,0], arr[0,1], # ... a[2,0], a[1,2]

  String-object:

    The basic format is '%s%s%s%d' % (endian, shape, kind, itemsize)

      kind     : one of the basic array kinds given below.

      itemsize : the nubmer of bytes (or bits for 't' kind) for

        this data-type.

      endian   : either *, '=' (native), '|' (doesn't matter),

        '>' (big-endian) or '<' (little-endian).

      shape    : either* , or a shape-tuple describing a data-type that

        is an array of the given shape.

    A string can also be a comma-separated sequence of basic formats. The result will be a data-type with default field names: 'f0', 'f1', ..., 'fn'. Examples:  >>> datatype('u4') datatype('uint32')

    >>> datatype('f4') datatype('float32')

    >>> datatype('(3,2)f4') datatype(('float32', (3,2))

    >>> datatype('(5,)i4, (3,2)f4, S5') datatype([('f0', '<i4', (5,)), ('f1', '<f4', (3, 2)), ('f2', '|S5')])

  List-object:

    A list should be a list of tuples where each tuple describes a field. Each tuple should contain (name, datatype{, shape}) or ((meta-info, name), datatype{, shape}) in order to specify the data-type.

    This list must fully specify the data-type (no memory holes). If would would like to return a data-type with memory holes where the compiler would place them, then pass the keyword align=1 to this construction.  This will result in un-named fields of Void kind of the correct size interspersed where needed. Examples:  datatype([( ([1,2],'coords'), 'f4', (3,6)), ('address', 'S30')]) A data-type that could represent the structure float coords[3*6]   Has [1,2] associated with this field char  address[30]

    datatype([( 'simple', 'i4'), ('nested', [('name', 'S30'),

      ('addr', 'S45'),     ('amount', 'i4')])])

    Can represent the memory layout of  struct { int  simple; struct nested {

      char name[30]; char addr[45]; int  amount;

    } There is no formal limit to the nesting that is possible.  datatype('i2, i4, i1, f8', align=1) datatype([('f0', '<i2'), (*, '|V2'), ('f1', '<i4'),

        ('f2', '|i1'), (*, '|V3'), ('f3', '<f8')])

    # Notice the padding bytes placed in the structure to make sure #  f1 and f8 are aligned correctly for the 32-bit system.

  Dictionary-object:

    Sometimes, you are only concerned about a few fields in a larger memory structure.  The dictionary object allows specification of   a data-type with fields using a dictionary with names as keys and tuples as values.  The value tuples are  (data-type, offset{, meta-info}).  The offset is the offset in    bytes (or bits when data-type is 't') from the beginning of the  structure to the field data-type.

    Example: datatype({'f3' : ('f8', 12), 'f2': ('i1', 8)}) type([(*, '|V8'), ('f2', '|i1'), (*, '|V3'), ('f3', '<f8')])

  Attributes

    byteorder --  returns the byte-order of this data-type

    isnative  --  returns True if this data-type is in correct byte-order

      for the platform.

    descr     --  returns an description of this data-type as a list of

      tuples (name or (name, meta), datatype{, shape})

    itemsize  --  returns the total size of the data-type.  kind      --  returns the basic "kind" of the data-type. The basic kinds

      are:

        't' - bit,  'b' - bool,  'i' - signed integer,  'u' - unsigned integer, 'f' - floating point,                   'c' - complex floating point,  'S' - string (fixed-length sequence of char), 'U' - fixed length sequence of UCS4, 'O' - pointer to PyObject_, 'V' - Void (anything else).

    names     --  returns a list of names (keys to the fields dictionary) in

      offset-order.

    fields    --  returns a read-only dictionary indicating the fields or

      None if this data-type has no fields.  The dictionary is keyed by the field name and each entry contains a tuple of (data-type, offset{, meta-object}). The offset indicates the byte-offset (or bit-offset for 't') from the beginning of the data-type to the data-type  indicated.

    hasobject --  returns True if this data-type is an "object" data-type

      or  has "object" fields.

    name      --  returns a 'name'-bitwidth description of data-type. base      --  returns self unless this data-type is an array of some

      other data-type and then it returns that basic data-type.

    shape     --  returns the shape of this data-type (for data-types

      that are arrays of other data-types) or () if there is no array.

    str       --  returns the type-string of this data-type which is the

      basic kind followed by the number of bytes (or bits  for 't')

    alignment --  returns alignment needed for this data-type on platform

      as determined by the compiler.

  Methods

    newbyteorder ({endian})

      create a new data-type with byte-order changed in any and all fields (including deeply nested ones), to {endian}.  If endian is not given, then swap all byte-orders.

    :underline:`len`(self)

      equivalent to len(self.field)

    :underline:`getitem`(self, name)

      get the field named [name].  Equivalent to self.field[name].

  C-functions :  These are function pointers attached in a C-structure

    connected with the data-type object that perform specific  functions.

    setitem  (PyObject_ *datatype, void *data, PyObject_ *obj)

      set a Python object into memory of this data-type

        at the given memory location.

    getitem  (PyObject_ *datatype, void *data)

      get a Python object from memory of this data-type.

Implementation

  A reference implementation (with more features than are proposed here) is available in NumPy_ and will be adapted if this PEP is accepted.

Questions:

  There should probably be a limited C-API so that data-type objects can be returned and sent through the extended buffer protocol (see  extended buffer protocol PEP).

  Should bit-fields be handled by re-interpreting the offsets as bit-values, use some other mechanism for handling the offset, or should they be unsupported? NumPy_ supports "string" and "unicode" data-types.  The unicode data-type in NumPy_ always means UCS4 (but it is translated back-and forth to Python unicode scalars as needed for narrow builds).  With Python 3.0 looming, we should probably support different encodings as data-types and drop the string type for a bytes type.  Some help in understanding what to do here is appreciated.

Copyright

  This PEP is placed in the public domain

PEP: Extending the buffer protocol to include the array interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Author: Travis Oliphant <`oliphant@ee.byu.edu`_>

Status: Draft

Type: Standards Track

Created: 28-Aug-2006

Python-Version: 2.6

Abstract

  This PEP proposes extending the tp_as_buffer structure to include  function pointers that incorporate information about the intended shape and data-format of the provided buffer.  In essence this will place something akin to the array interface directly into Python.

Rationale

  Several extensions to Python utilize the buffer protocol to share the location of a data-buffer that is really an N-dimensional array.  However, there is no standard way to exchange the additional N-dimensional array information so that the data-buffer is interpreted correctly.  The NumPy_ project introduced an array interface  http://numpy.scipy.org/array_interface.shtml ) through a set of attributes on the object itself.  While this approach works, it requires attribute lookups which can be expensive when sharing many small arrays.

  One of the key reasons that users often request to place something like NumPy_ into the standard library is so that it can be used as standard for other packages that deal with arrays.  This PEP provides a mechanism for extending the buffer protocol (which already allows data sharing) to add the additional information needed to understand the data.  This should be of benefit to all third-party modules that want to share memory through the buffer protocol such as GUI toolkits, PIL, PyGame_, CVXOPT, PyVoxel_, PyMedia_, audio libraries, video libraries etc.

Proposal

  Add a bf_getarrayinfo function pointer to the buffer protocol to allow objects to share additional information about the returned memory pointer.  Add the TP_HAS_EXT_BUFFER flag to types that define the extended buffer protocol.

Specification:

  static int

  bf_getarrayinfo (PyObject_ *obj, Py_intptr_t **shape,

    Py_intptr_t **strides, PyObject_ **dataformat)

  Inputs:

    obj -- The Python object being questioned.

  Outputs:

    [function result] -- the number of dimensions (n)

  * shape -- A C-array of 'n' integers indicating the

      shape of the array. Can be NULL if n==0.

  * strides -- A C-array of 'n' integers indicating

      the number of bytes to jump to get to the next element in each dimension. Can be NULL if the  array is C-contiguous (or n==0).

  * dataformat -- A Python object describing the data-format

      each element of the array should be interpreted as.

Discussion Questions:

  1) How is data-format information supposed to be shared?  A companion proposal suggests returning a data-format object which carries the information about the buffer area.

  2) Should the single function pointer call be extended into multiple calls or should it's arguments be compressed into a structure that is filled? 3) Should a C-API function(s) be created which wraps calls to this function pointer much like is done now with the buffer protocol?  What should the interface of this function (or these functions) be. 4) Should a mask (for missing values) be shared as well?

Reference Implementation

  Supplied when the PEP is accepted.

Copyright

  This document is placed in the public domain.

.. ############################################################################

.. _NumPy: ../NumPy

.. _PyArray: ../PyArray

.. _PyDatatypeObject: ../PyDatatypeObject

.. _PyObject: ../PyObject

.. _oliphant@ee.byu.edu: mailto:oliphant@ee.byu.edu

.. _PyGame: ../PyGame

.. _PyVoxel: ../PyVoxel

.. _PyMedia: ../PyMedia

