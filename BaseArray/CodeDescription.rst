#format rst

The proposed basearray type does not have a fully-filled type-object structure. In other words, basearray is above all a place-holder and base-type, of which other, more capable array objects can be subtypes of. Besides serving as a base type, the object exports and consumes the array interface.

Alongside basearray and datatype (a descriptor of the type an array carries), an array iterator type is defined to facilitate some procedures. There are also two auxialliary structures and a number of C-API functions.

Ultimately, there are two files to be added: [`http://svn.scipy.org/svn/PEP/basearray.c`_ basearray.c] and [`http://svn.scipy.org/svn/PEP/basearray.h`_ basearray.h].

C structures defined
--------------------

PyBaseArrayObject
~~~~~~~~~~~~~~~~~

[Table not converted]

The flags variable is the bit-wise OR of:

  CONTIGUOUS - set if array is c-style contiguous in memory, with the last dimension varying the fastest.

  FORTRAN - set if array is fortran-style contiguous in memory, with the first dimension varying the fastest.  OWN_DATA - set if this array owns the data buffer and should de-allocate it when the array is deallocated. WRITEABLE - the memory can be written to.  ALIGNED - the memory (for each stride) is aligned properly for the type.

PyDataTypeObject
~~~~~~~~~~~~~~~~

Describes the type of data the array carries. There are instances of this object for a fixed set of built-in Python types.

[Table not converted]

PyDataTypeFuncs
~~~~~~~~~~~~~~~

Carries pointers to functions specific to a given datatype object. Currently two such function are included in this structure:

* PyDataType__GetItemFunc_ *getitem;

* PyDataType__SetItemFunc_ *setitem;

PyBaseArrayIterObject
~~~~~~~~~~~~~~~~~~~~~

This iterator structure is usefull for looping over a basearray.

[Table not converted]

PyBaseArrayDims
~~~~~~~~~~~~~~~

Auxiliary structure used for interpreting the shape and stride of Python objects when they are converted to useful C objects.

[Table not converted]

PyBaseArrayChunk
~~~~~~~~~~~~~~~~

Auxiliary structure for representing a memory segment, the equivalent of the Python buffer object.

[Table not converted]

