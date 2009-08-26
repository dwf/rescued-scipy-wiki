#format rst

Preparing the interface was part of a `Google Summer Of Code 2006 <http://code.google.com/soc>`_ project (`list of PSF projects <http://wiki.python.org/moin/SummerOfCode>`_) by KarolLangner_ - *Base multidimensional array type for Python core*. The project was not successfull, and is not being currently worked on. A proposed revision of the buffer protocol in Python, however, is outlined in `a PEP by Travis Oliphant <http://svn.scipy.org/svn/numpy/trunk/numpy/doc/pep_buffer.txt>`_.

**Proposal title**: Base multidimensional array type for Python core

**Author**: Karol Marek Langner

**Mentor**: Travis Oliphant

Goals
~~~~~

The goal is to prepare a simple, generic multidimensional array interface that can be readily placed in the Python core as a new built-in base type (called, for instance, "dimarray"), and possibly included in a future Python distribution (maybe 2.6?). This new base type will have the same C-structure as the current array implementation in numpy and will be based on a interface recently formulated by Travis Oliphant within a Python Enhancement Proposal (`http://svn.scipy.org/svn/PEP/`_). After preparing a "ready to insert" version of the array interface, it will be applied to numpy and several other packages that work with multidimensional data, and possibly modified in order to work out an optimal scope.

Rationale and impact
~~~~~~~~~~~~~~~~~~~~

Multidimensional arrays are used throughout science and engineering, and many relevant applications written in Python are not an exception. To date, the optional Numeric package (later numarray and numpy/scipy core) has provided such array objects for Python modules. The structure of the array object implemented in the Numeric package has been stable for about ten years, and it is now obvious the community would benefit from including at least its most basic fragments in the core Python distribution.

While this process has already been started, it apparantly needs to be revived, and more time needs to be dedicated. My involvement would therefore be a continuation of up-to-date efforts, which have outlined an N-dimensional array type and data-type-descriptor object. The last changes I have found for the related PEP (see `http://svn.scipy.org/svn/PEP/`_) date from late 2005.

Such an inclusion has a potential impact on all modules that handle multidimensional data. The existence of a base type would allow other applications utilize a fundamental multidimensional data array object, without depending on a third-party package such as Numeric. Furthermore, such a base type will facilitate the development of more complex array types for specialized needs (Numeric being the most obvious example), and ease their intercompatibility if they inherit from the same type. In the long run, this may also be a precedent to include a more advanced array type in the Python core in the future.

Deliverables
~~~~~~~~~~~~

Besides a ready-to-include N-D array interface, the project aims to deliver several patches or additions to common packages that operate on multidimensional data. These enhancements will enable the use of the new base type for specific versions of these packages. At the same time, they will illustrate the differences compared to native implementations and/or provide a basis for using the new interface in future releases, when it actually is published as part of Python core.

Project details and tentative schedule
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After looking at the current state of the PEP, I plan to divide my possible work on this project into three stages. First, I would need to spend some time (max. two weeks) on becoming more familiar with how the present numpy code implements its array object and what has been done to date. Hopefully, I could get some support from the developers in this.

Using as a starting point the "array_interface" description for a Python object as provided by the existing PEP (`http://numeric.scipy.org/array_interface.html`_), I will finalize an interface suitable for inclusion as a base type. The most important improvement needed is a C-interface for objects to avoid Python attributes. I estimate that this stage would take approximately two weeks, effectively ending at least a couple of days before the mid-program evaluation deadline (a buffer for the mentor).

After creating a working interface for a N-D array object, I will proceed to attempt to apply it to several common packages that operate on multidimensional data. This will allow the new interface to be observed in action, and possible modifications to be made. Each package will be focused on seperately in time (max. two weeks for each), and more may be added within the framework of the program if time permits. The initial choices for targets are:

* NumPy_ (the present N-D array implementation, successor of Numeric and numarry) - this is the first and most obvious target, in which the native array interface will be simply replaced by the new built-in interface,

* `wxPython <http://www.wxpython.org/>`_ - the parts of this module that use data stored in array-like objects will be patched to use the new array interface,

* [`http://www.pythonware.com/products/pil/`_ Python Imaging Library (PIL)] - using a base array type will allow image data to be represented in a natural way, and for some applications perhaps this will be efficient. A means to transfer data from the current image type to an instance carrying the new array object will be provided, along with examples of how to use the array interface.

During the course of the program, the progress made and current state of the project will be published on a public site - one of the python wikis or a personal web page. Besides seeking technical comments and suggestions on channels related to numpy, the idea of including an array interface in the Python core will be further promoted and the current PEP pushed forward.

Collaborators
~~~~~~~~~~~~~

Potentially, I would be working with all the people involved in developing the numpy and scipy projects. Foremost Travis Oliphant, who is the author of the current PEP, and maintainer of the numpy project, and Tim Hochberg, who has recently been working on a version of the array_interface. One of them would be the most obvious choice for a mentor for this project.

