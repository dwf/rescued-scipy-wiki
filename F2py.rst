#format rst

F2PY - Fortran to Python interface generator
============================================

Author:: Pearu Peterson < `pearu.peterson@gmail.com`_ >

Introduction
------------

F2PY is a tool that provides an easy connection between Python and Fortran languages. F2PY is part of NumPy.

F2PY creates extension modules from (handwritten or F2PY generated) signature files or directly from Fortran sources.

The generated extension modules facilitate:

* Calling Fortran 77/90/95, Fortran 90/95 module, and C functions from Python.

* Accessing Fortran 77 COMMON blocks and Fortran 90/95 module data (including allocatable arrays) from Python.

* Calling Python functions from Fortran or C (call-backs).

* Automatically handling the difference in the data storage order of multi-dimensional Fortran and Numerical Python (i.e. C) arrays.

In addition, F2PY can build the generated extension modules to shared libraries with only one command. F2PY uses the ``numpy.distutils`` module from NumPy that supports a number of major Fortran compilers. F2PY generated extension modules depend on NumPy that provides a fast multi-dimensional array language facility to Python. For building extension modules with Numeric or Numarray array backend, one can use the older and unmaintained version of F2PY: `f2py2e <http://cens.ioc.ee/projects/f2py2e/>`_.

Main features
-------------

Here follows a more detailed list of F2PY features:

* F2PY scans real Fortran codes to produce the so-called signature files (.pyf files). The signature files contain all the information (function names, arguments and their types, etc.)  that is needed to construct Python bindings to Fortran (or C) functions.

The syntax of signature files is borrowed from the Fortran 90/95 language specification and has some F2PY specific extensions. The signature files can be modified to dictate how Fortran (or C) programs are called from Python:

* F2PY solves dependencies between arguments (this is relevant for the order of initializing variables in extension modules).

* Arguments can be specified to be optional or hidden that simplifies calling Fortran programs from Python considerably.

* In principle, one can design any Python signature for a given Fortran function, e.g. change the order arguments, introduce auxiliary arguments, hide the arguments, process the arguments before passing to Fortran, return arguments as output of F2PY generated functions, etc.

* F2PY automatically generates ``__doc__`` strings for extension modules.

* F2PY generated functions accept arbitrary (but sensible) Python objects as arguments. The F2PY interface automatically takes care of type-casting and handling of non-contiguous arrays.

* The following Fortran constructs are recognized by F2PY:

  * All basic Fortran types:



      ::

         integer[ | *1 | *2 | *4 | *8 ], logical[ | *1 | *2 | *4 | *8 ]
         integer*([ -1 | -2 | -4 | -8 ])
         character[ | *(*) | *1 | *2 | *3 | ... ]
         real[ | *4 | *8 | *16 ], double precision
         complex[ | *8 | *16 | *32 ]

      Negative integer kinds are used to wrap unsigned integers for C codes.

  * Multi-dimensional arrays of all basic types with the following dimension specifications:

      ``<dim> | <start>:<end> | * | :``

  * Attributes and statements:



      ::

         intent([ in | inout | out | hide | in,out | inout,out | c |
                copy | cache | callback | inplace | aux ])
         dimension(<dimspec>)
         common, parameter
         allocatable
         optional, required, external
         depend([<names>])
         check([<C-booleanexpr>])
         note(<LaTeX text>)
         usercode, callstatement, callprotoargument, threadsafe, fortranname
         pymethoddef
         entry

    * Because there are only little (and easily handleable) differences between calling C and Fortran functions from F2PY generated extension modules, then F2PY is also well suited for wrapping C libraries to Python.

    * Practice has shown that F2PY generated interfaces (to C or Fortran functions) are less error prone and even more efficient than handwritten extension modules. The F2PY generated interfaces are easy to maintain and any future optimization of F2PY generated interfaces transparently apply to extension modules by just regenerating them with the latest version of F2PY.

    * `F2PY Users Guide and Reference Manual <http://cens.ioc.ee/projects/f2py2e/usersguide/index.html>`_ --- it is based on f2py2e but most of it is valid for F2PY.

Prerequisites
-------------

Since F2PY is a part of NumPy, the same prerequisites apply, that is, Python 2.3 or newer with ``distutils`` package must be installed.

Of course, to build extension modules, one also needs a working C and/or Fortran compilers installed.

Download and installation
-------------------------

`Download <http://www.scipy.org/Download>`_ and install NumPy in the usual way: ``python setup.py install``.

Usage
-----

To check if F2PY is installed correctly, run

.. ############################################################################

.. _pearu.peterson@gmail.com: mailto:pearu.peterson@gmail.com

.. _NumPy: ../NumPy

