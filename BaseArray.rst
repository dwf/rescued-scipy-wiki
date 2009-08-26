#format rst

**BaseArray** was a proposed base multidimensional array type, ready-to-include in the Python core sometime in the future. This page aims at summarizing the various efforts that have gone in this direction. The long-term outcome of these is [`http://www.python.org/dev/peps/pep-3118`_ PEP 3118], *Revising the buffer protocol*. Note that alot of the text on this page is taken directly from [`http://svn.scipy.org/svn/PEP/PEP_basearray.txt`_ the text description of the PEP].

Introduction
============

Multidimensional arrays are often used in scientific and engineering programming, but they have uses in other areas as well, as evidenced by the popularity of spreadsheets and image-processing applications. Python, however, has no default multidimensional array object.

Since 1995, Numeric has been filling the need for multidimensional arrays for many users as a standard optional Python library. The only thing holding it back from the standard library has been stability, and, in particular, a desire on the part of the user community to have a faster release cycle for the array. While some changes have occurred in the functionality of the array object as it has progressed from Numeric to numarray to scipy core (numpy), what has not changed significantly is the interface, which allows Python users to interact with an array of bytes described by a certain shape, memory layout, and type description.

In fact, this interface has recently been formalized by the creation of a description called the "array_interface", which any Python object can consume and/or export. To improve the usefullness of array_interface, however, it would be usefull to have a mechanism via which objects could use the interface quickly on the C-level.

It would be beneficial to the community as a whole to place this common interface into Python itself. This would allow a wider Python community to quickly interact with and use the data in multidimension arrays without requiring or depending on a third-party package. It would also allow Python to work seamlessly with more capable multidimensional array objects that scientific users could install.

The PEP proposes adding a new builtin type to the Python language, a generic multi-dimensional array type (**basearray**), and an associated type dsecribing the type of data it carries (**datatype**). The basearray type would have a C-structure similar to that which has been constant in Numeric and few other features. Together, these objects would implement the array interface specification introduced to Numeric and numarray in April 2005, and encourage the use of this interface both in extensions and Python code in general.

Purpose of basearray
====================

The obvious purpose of basearray is to provide a base multidimensional array type for the Python distribution. This, however, is also the means by which other goals, more important in the long run, can be achieved.

* By providing a "minimal" base type, more capable array types can be created as subtypes of basearray (such as that contained in numpy). Other Python users could write extensions modules that enhance the basic structure of basearray, without having to install an entire scientific computing package.

* Standardized allocation and interpretation of memory for multidimensional arrays, combined with a generic way to share information about arrays and the memory they are stored in (such as the array_interface), will allow all objects dealing with multidimensional data to communicate, even if they are not subtypes of basearray. For example, the inclusion of basearray would allow extension modules such as PyOpenGL, wxPython, and PIL to make use of array-like data stored in a multidimensional array object, without making unnecessary copies.

* Finally, the addition of basearray would pave the way for a more capable multidimensional array object to be gradually added to the Python distribution, if specific features were deemed desireable by the broader community.

Code description
================

  *This is a general description of the basearray code. A more comprehensive description can be found at* `BaseArray/CodeDescription`_*.*

The proposed basearray type does not have a fully-filled type-object structure. In other words, basearray is above all a place-holder and base-type, of which other, more capable array objects can be subtypes of. Besides serving as a base type, the object exports and consumes the array interface.

Alongside basearray and datatype (a descriptor of the type an array carries), an array iterator type is defined to facilitate some procedures. There are also two auxialliary structures and a number of C-API functions.

Ultimately, there are two files to be added: [`http://svn.scipy.org/svn/PEP/basearray.c`_ basearray.c] and [`http://svn.scipy.org/svn/PEP/basearray.h`_ basearray.h].

C structures defined
--------------------

* PyBaseArrayObject_

* PyDataTypeObject_ describes the type of data the array carries. There are instances of this object for a fixed set of built-in Python types.

* PyDataTypeFuncs_ carries pointers to functions specific to a given datatype object. Currently two such function pointers are included in this structure: *getitem and *setitem.

* PyBaseArrayIterObject_ is a structure useful for looping over a basearray.

* PyBaseArrayDims_ is an auxiliary structure used for interpreting the shape and stride of Python objects when they are converted to useful C objects.

* PyBaseArrayChunk_ is an auxiliary structure for representing a memory segment, the equivalent of the Python buffer object.

Related projects
================

* NumPy_, the successor of Numeric and `NumArray <http://www.stsci.edu/resources/software_hardware/numarray>`_, is the starting point -  basearray is in fact a modification of the essential fragments of the numpy core source code. Naturally, the array type in numpy will be the first target to use basearray as a subtype for.

* [`http://numeric.scipy.org/array_interface.html`_ Array interface] - a mechanism for a Python object (or PyCObject) to share information about its multidimensional data. This is like a "protocol", which sets the ground rules for objects that wish to be interpreted through this interface by code written to understand it. Interestingly, this array interface surfaced from discussion between developers of Numeric, Numarray, and numpy.

* `Arraykit <http://svn.scipy.org/svn/numpy/branches/arraykit/>`_ - a similar project by Tim Hochberg, which can be used to create custom array-like objects.

Summer of Code Project
======================

Preparing the interface is formally part of a [`http://code.google.com/soc`_ Google Summer Of Code] project ([`http://wiki.python.org/moin/SummerOfCode`_ list of PSF projects]), currently being worked on by KarolLangner_ - *Base multidimensional array type for Python core*.

Original application
--------------------

**Proposal title**: Base multidimensional array type for Python core

**Author**: Karol Marek Langner

**Mentor**: Travis E. Oliphant

Goals
~~~~~

The goal is to prepare a simple, generic multidimensional array interface that can be readily placed in the Python core as a new built-in base type (called, for instance, "dimarray"), and possibly included in a future Python distribution (maybe 2.6?). This new base type will have the same C-structure as the current array implementation in numpy and will be based on a interface recently formulated by Travis Oliphant within a Python Enhancement Proposal (`http://svn.scipy.org/svn/PEP/`_). After preparing a "ready to insert" version of the array interface, it will be applied to numpy and several other packages that work with multidimensional data, and possibly modified in order to work out an optimal scope.

**Entire application**: ["BaseArray/Application"]

Changes in schedule
-------------------

Due to a late start, the planned realization dates for the project need to be changed. The objective now is to have a complete, minimum base type by roughly July 10th. After that, work will be focused on using it packages that utilize multidimensional data (as described in the application), with roughly two weeks for each package.

.. ############################################################################

.. _BaseArray/CodeDescription: /CodeDescription

.. _PyBaseArrayObject: ../PyBaseArrayObject

.. _PyDataTypeObject: ../PyDataTypeObject

.. _PyDataTypeFuncs: ../PyDataTypeFuncs

.. _PyBaseArrayIterObject: ../PyBaseArrayIterObject

.. _PyBaseArrayDims: ../PyBaseArrayDims

.. _PyBaseArrayChunk: ../PyBaseArrayChunk

.. _NumPy: ../NumPy

.. _NumArray: ../NumArray

.. _KarolLangner: ../KarolLangner

