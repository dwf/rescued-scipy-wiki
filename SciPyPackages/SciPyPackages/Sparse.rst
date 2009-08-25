#format rst

`TableOfContents(2)`_

Introduction
============

  This guide provides an overview of the sparse matrix support in SciPy_ version 0.7.  The following topics are covered:

* Constructing sparse matrices

* Handling sparse matrices efficiently

* Solving sparse linear systems and eigenproblems with ``scipy.sparse.linalg``

* Using ``scipy.io`` to read and write sparse matrices

What is a sparse matrix?
------------------------

  A **sparse matrix** is simply a matrix with a large number of zero values.  In contrast, a matrix where many or most entries are non-zero is said to be **dense**.  There are no strict rules for what constitutes a sparse matrix, so we'll say that a matrix is sparse if there is some benefit to exploiting its sparsity.  Additionally, there are a variety of **sparse matrix formats** which are designed to exploit different **sparsity patterns** (the structure of non-zero values in a sparse matrix) and different methods for accessing and manipulating matrix entries.

Where do sparse matrices arise?
-------------------------------

* briefly mention FD and FEM methods

* show a 2D triangle mesh and associated graph Laplacian (nonzeros only exist when two vertices share and edge, typically 6-7 neighbors, therefore sparse)

* briefly mention existence of non-physical examples (PageRank_, LinearProgramming_)

Sparsity Patterns
=================

1. Diagonal

#. Block

#. Unstructured

#. Sensitivity of pattern to ordering, and use of reordering for locality (e.g. direct solvers)

Sparse Formats
==============

  The ``scipy.sparse`` module provides data structures for 2D sparse matrices. There are seven available sparse matrix formats:

* ``csc_matrix``: **C**ompressed **S**parse **C**olumn

* ``csr_matrix``: **C**ompressed **S**parse **R**ow

* ``bsr_matrix``: **B**lock **S**parse **R**ow

* ``lil_matrix``: **Li**st of **L**ists

* ``dok_matrix``: **D**ictionary **o**f **K**eys

* ``coo_matrix``: **Coo**rdinate

* ``dia_matrix``: **Dia**gonal

If you've handled sparse matrices before, then some of these formats will be familiar to you.  If not, don't be overwhelmed by the abundance of sparse matrix formats!

  Each sparse format has certain advantages and disadvantages.  For instance, adding new non-zero entries to a ``lil_matrix`` is fast, however changing the sparsity pattern of a ``csr_matrix`` requires a significant amount of work.  On the other hand, operations such as matrix-vector multiplication and matrix-matrix arithmetic are much faster with ``csr_matrix`` than ``lil_matrix``.  A good strategy is to construct matrices using one format and then convert them to another that is better suited for efficient computation.

Constructing Sparse Matrices
----------------------------

sparse from dense
~~~~~~~~~~~~~~~~~

  There are several ways to construct a sparse matrices in SciPy_.  The simplest method is to pass a dense NumPy_ ``matrix`` or two-dimensional ``ndarray`` to the desired sparse matrix constructor:

  ::

     >>> from numpy import array, matrix
     >>> from scipy.sparse import csr_matrix, lil_matrix
     >>> A = array([[1,0,2],[0,3,0]])
     >>> csr_matrix(A)
     <2x3 sparse matrix of type '<type 'numpy.int64'>'
             with 3 stored elements in Compressed Sparse Row format>
     >>> M = matrix([[1.0,0.0],[0.0,2.0]])
     >>> lil_matrix(M)
     <2x2 sparse matrix of type '<type 'numpy.float64'>'
             with 2 stored elements in LInked List format>

  You can also construct matrices directly from lists, ::

     >>> csr_matrix([[1,0,2],[0,3,0]])
     <2x3 sparse matrix of type '<type 'numpy.int64'>'
             with 3 stored elements in Compressed Sparse Row format>

  and empty matrices are created as follows ::

     >>> lil_matrix((3,4))
     <3x4 sparse matrix of type '<type 'numpy.float64'>'
             with 0 stored elements in LInked List format>
     >>> csr_matrix((3,4), dtype='int8')
     <3x4 sparse matrix of type '<type 'numpy.int8'>'
             with 0 stored elements in Compressed Sparse Row format>

  As you can see, the sparse formats store only the non-zero entries of a matrix.  This value is stored in the ``nnz`` attribute,

  ::

     >>> from scipy.sparse import *
     >>> A = csr_matrix([[1,0,2],[0,3,0]])
     >>> A.nnz
     3

  However, some sparse formats (e.g. ``dia_matrix``, ``csr_matrix``) can contain explicit zero entries. In this situation ``A.nnz`` overestimates the true number of non-zero values in the matrix.

  |/!/| ``scipy.sparse`` now supports most NumPy_ data types (e.g. ``unit8``, ``int32``, ``complex128``, etc.) with the exception of the ``object`` and ``bool`` dtypes.

sparse to dense
~~~~~~~~~~~~~~~

  As you might expect, you can also convert sparse matrices to the dense format.

  ::

     >>> from scipy.sparse import csr_matrix
     >>> A = csr_matrix([[1,0,2],[0,3,0]])
     >>> A
     <2x3 sparse matrix of type '<type 'numpy.int64'>'
             with 3 stored elements in Compressed Sparse Row format>
     >>> A.todense()
     matrix([[1, 0, 2],
             [0, 3, 0]])
     >>> A.toarray()
     array([[1, 0, 2],
            [0, 3, 0]])

  This feature is useful for debugging and for using functions in NumPy_ and SciPy_ that don't support sparse matrices directly.

sparse to sparse conversions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Since the whole purpose of sparse matrices is to avoid the dense format, there are several other methods.  Another way is to convert one sparse format to another:

  ::

     >>> from scipy.sparse import csr_matrix, coo_matrix
     >>> A = csr_matrix([[1,0,2],[0,3,0]])
     >>> coo_matrix(A)
     <2x3 sparse matrix of type '<type 'numpy.int64'>'
             with 3 stored elements in COOrdinate format>
     >>> A.tolil()
     <2x3 sparse matrix of type '<type 'numpy.int64'>'
             with 3 stored elements in LInked List format>
     >>> A.asformat('dok')
     <2x3 sparse matrix of type '<type 'numpy.int64'>'
             with 3 stored elements in Dictionary Of Keys format>

  Any sparse format in ``scipy.sparse`` can be converted to any other using any of the previous methods.  Since formats like ``dia_matrix`` are inappropriate for certain sparsity patterns, some caution must be exercised.  However, in general conversions among sparse formats are implemented efficiently so that you choose the best format for your application.

constructing from scratch
-------------------------

  So far, we've shown how to construct sparse matrices from dense matrices and from other sparse matrices.  Clearly we also need a way to construct matrices from scratch.  Since the ``lil_matrix`` (recommended) and ``dok_matrix`` allow new entries to be entered into the matrix, they are a convenient way to build sparse matrices.

  ::

     >>> from scipy.sparse import lil_matrix
     >>> A = lil_matrix((4,3), dtype='float32')
     >>> A[1,0] = 3.0
     >>> A[2,2] = 7.0
     >>> A[3,1] = -2.0
     >>> A
     <4x3 sparse matrix of type '<type 'numpy.float32'>'
             with 3 stored elements in LInked List format>
     >>> A.todense()
     matrix([[ 0.,  0.,  0.],
             [ 3.,  0.,  0.],
             [ 0.,  0.,  7.],
             [ 0., -2.,  0.]], dtype=float32)

  As expected, explicitly setting an entry to zero removes it from the matrix structure: ::

     >>> A[2,2] = 0
     >>> A
     <4x3 sparse matrix of type '<type 'numpy.float32'>'
             with 2 stored elements in LInked List format>
     >>> A.todense()
     matrix([[ 0.,  0.,  0.],
             [ 3.,  0.,  0.],
             [ 0.,  0.,  0.],
             [ 0., -2.,  0.]], dtype=float32)

  |/!/| For the sake of efficiency, this same behavior does not hold for other formats (e.g. ``csr_matrix``).

implementation considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  As the name suggests, the underlying data structure of ``lil_matrix`` is a list (actually an ``ndarray``) of Python lists.  Each row of the matrix is stored in a separate (sorted) list, so adding new elements requires a relatively small number of operations.  Similarly, ``dok_matrix`` is a Python dictionary that maps (row,column) keys to their nonzero values.  While the precise details of these data structures are subject to change, you can rely on the fact that changes to the sparsity structure of these formats will be handled efficiently.

sparsity structure changes can be expensive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  It is **very inefficient** to change the sparsity structure of other formats in ``scipy.sparse``!  Indeed, most sparse formats in SciPy_ do not even support setting matrix entries.  Notable exceptions are ``csr_matrix`` and ``csc_matrix`` which do permit such modifications. Nevertheless, don't do it!  If you do, you'll be greeted with a ``SparseEfficiencyWarning`` the first time you try.

  ::

     >>> from scipy.sparse import csr_matrix
     >>> A = csr_matrix((4,3), dtype='float32')
     >>> A[1,0] = 3.0
     /usr/lib/python2.5/site-packages/scipy/sparse/compressed.py:623: SparseEfficiencyWarning: changing the sparsity structure of a csr_matrix is expensive. lil_matrix is more efficient.
       SparseEfficiencyWarning)
     >>> A[2,2] = 7.0
     >>> A[3,1] = -2.0
ERROR: EOF in multi-line statement


  You have been warned.  If you insist on abusing ``csr_matrix`` and ``csc_matrix`` in this way, and don't want to be warned, the ``warnings`` module permits filtering,

  ::

     >>> from scipy.sparse import csr_matrix, SparseEfficiencyWarning
     >>> import warnings
     >>> warnings.simplefilter('ignore',SparseEfficiencyWarning)
     >>> A = csr_matrix((4,3), dtype='float32')
     >>> A[1,0] = 3.0
     >>> A[2,2] = 7.0
     >>> A[3,1] = -2.0

  but you should still feel guilty. The justification for the warning is that, in general, changes to the structure of a ``csr_matrix`` require the **entire** data structure to be altered.  The cost of such alterations is proportional to the number of non-zero entries in the matrix.  In contrast, the cost of adding a new value to a ``lil_matrix`` is proportional to the number of non-zero values in that row, while a ``dok_matrix`` typically does the update in constant time.

constructing from scratch faster, with coo_matrix
-------------------------------------------------

  As discussed in the previous section ``lil_matrix`` and ``dok_matrix`` can be used to insert elements into a matrix efficiently.  However, when dealing with sparse matrices with **millions** of non-zeros, a faster method is required.  Behold, the coordinate matrix format.

  The coordinate matrix format is arguably the simplest of all sparse formats: it consists of three arrays ``row``, ``col``, and ``data`` which record the row index, column index, and value of each entry in the matrix respectively.  Using these three arrays, the ``coo_matrix`` is constructed as follows:

  ::

     >>> from scipy.sparse import coo_matrix
     >>> from numpy import array
     >>> row = array([1,2,3])
     >>> col = array([0,2,1])
     >>> data = array([3.0,7.0,-2.0])
     >>> A = coo_matrix((data,(row,col)), shape=(4,3))
     >>> A
     <4x3 sparse matrix of type '<type 'numpy.float64'>'
             with 3 stored elements in COOrdinate format>
     >>> A.todense()
     matrix([[ 0.,  0.,  0.],
             [ 3.,  0.,  0.],
             [ 0.,  0.,  7.],
             [ 0., -2.,  0.]])

  Here we have used the ``shape`` parameter of the constructor to inform ``coo_matrix`` of the matrix dimension.  If ``shape`` is not defined, then ``coo_matrix`` will attempt to infer the matrix dimensions from ``row`` and ``col`` arrays.  Therefore, in this particular example, the shape parameter is not necessary.  However, if the last row or column contains no values, then it is necessary to supply a ``shape`` parameter.  If you happen to forget any of this information, you can always use the ``help`` command within Python to retrieve the documentation

  At this point, you might be questioning the utility of the humble ``coo_matrix``: you will be forgiven for that prejudice.  As a simple test, suppose we want a function that returns an identity matrix of a given size.  Consider the three functions in the code sample below which construct identity matrices using the COO, LIL, and DOK formats.

  ::

     from time import clock
     from numpy import arange, ones
     from scipy.sparse import coo_matrix, dok_matrix, lil_matrix
     def identity_coo(N):
         row = arange(N, dtype='intc')
         col = arange(N, dtype='intc')
         data = ones(N)
         I = coo_matrix((data,(row,col)), shape=(N,N))
         return I
     def identity_lil(N):
         I = lil_matrix((N,N))
         for i in range(N):
             I[i,i] = 1.0
         return I
     def identity_dok(N):
         I = dok_matrix((N,N))
         for i in range(N):
             I[i,i] = 1.0
         return I
     N = 1000 * 1000
     start = clock(); I = identity_coo(N); end = clock();
     print "COO: %6.3f seconds" % (end - start)
     start = clock(); I = identity_lil(N); end = clock()
     print "LIL: %6.3f seconds" % (end - start)
     start = clock(); I = identity_dok(N); end = clock()
     print "DOK: %6.3f seconds" % (end - start)

Here's the result

 

  ::

     COO:  0.030 seconds
     LIL: 19.870 seconds
     DOK: 15.790 seconds

The ``coo_matrix`` method is clearly the fastest, beating the others by a factor of 500.  Interestingly, constructing a matrix in COO first, and then converting to LIL or DOK is still faster than using those formats directly:

 

  ::

     start = clock(); I = identity_coo(N);  I = I.tolil(); end = clock()
     print "COO->LIL: %6.3f seconds" % (end - start)
     start = clock(); I = identity_coo(N);  I = I.todok(); end = clock()
     print "COO->DOK: %6.3f seconds" % (end - start)

  ::

     COO->LIL:  7.990 seconds
     COO->DOK:  4.390 seconds

construction utilities
----------------------

* spdiags

* sparse.kron

* sparse.bmat, sparse.hstack, sparse.vstack

* discuss ``format`` parameter

Handling Sparse Matrices
========================

* Support for slicing and fancy indexing in CSR/CSC formats (but not for assignment)

* Which formats implement efficient matrix-matrix arithmetic and matrix-vector opertions

* why formats are not preserved (CSR.T becomes CSC and LIL * LIL becomes CSR, etc.) and what to do if you care about the format of the result

Solving Sparse Linear Systems
=============================

There are two main classes of solvers for sparse linear systems: **direct** and **iterative**.

Direct method can be thought of as a extension of dense matrix factorizations, like the LU factorization, to sparse matrices.  The goal of such algorithms is to produce factors (e.g. matrices L and U) that are as sparse as possible.  Sophisticated agorithms are used to reorder rows and columns of the input matrix so that the **fill in** of the sparse factors is minimized.

In contrast, iterative methods solve linear systems by iteratively improving an approximation to the solution. Since iterative methods do not require a matrix factorization to be computed they are usually applied to large linear systems where the memory cost of computing such factors is prohibitive.  On the other hand, many iterative methods only work for a specific type of matrix (e.g. symmetric matrices) and have several tuning parameters, so they can be somewhat more difficult to use.

Direct Factorization Methods
----------------------------

* basic intuition and background

* use of reordering to minimize fill

* Further information.... (UMFPACK scikit, others)

* Note: moved from scipy.linsolve to scipy.sparse.linalg, UMFPACK now deprecated

Iterative Methods
-----------------

* basic intuition and background

* explain classes of matrices (e.g. SPD)

* simple examples with cg and gmres

* solve a 2d Poisson problem and plot it w/ pcolor()

* illustrate use of preconditioner

* Further information.... (PyAMG,others)

Solving Sparse Eigenvalue Problems
==================================

* basic intuition and background

* examples with ARPACK and LOBPCG

* find a few eigenmodes of a 2d Poisson problem and plot them w/ pcolor()

* illustrate use of preconditioner

Sparse Matrix File Input/Output
===============================

  The ``scipy.io`` module supports two file formats for reading and writing sparse matrices.

MatrixMarket
------------

  The [`http://math.nist.gov/MatrixMarket/formats.html#MMformat`_ MatrixMarket_] format stores matrices in a simple ASCII file format.  Software for reading and writing MatrixMatrix_ in various programming languages files is [`http://math.nist.gov/MatrixMarket/formats.html#MMformat`_ freely available].  The [`http://bebop.cs.berkeley.edu/smc/`_ BeBOP sparse matrix converter] can be used to convert between the MatrixMarket_ format and other sparse formats (e.g. Harwell-Boeing).

  Reading and writing files in the MatrixMarket_ format is easy:

  ::

     >>> from scipy.sparse import csr_matrix
     >>> from scipy.io import mmread, mmwrite
     >>> A = csr_matrix([[1.0,0.0,2.0],[0.0,3.0,0.0]])
     >>> A
     <2x3 sparse matrix of type '<type 'numpy.float64'>'
             with 3 stored elements in Compressed Sparse Row format>
     >>> mmwrite('my_file.mtx', A)
     >>> B = mmread('my_file.mtx')
     >>> B
     <2x3 sparse matrix of type '<type 'numpy.float64'>'
             with 3 stored elements in COOrdinate format>

  Reading MatrixMarket_ files compressed with ``gzip`` is also supported:

  ::

     >>> B = mmread('my_file.mtx.gz')
     >>> B
     <2x3 sparse matrix of type '<type 'numpy.float64'>'
             with 3 stored elements in COOrdinate format>

MATLAB
------

  The ``scipy.io`` module also supports the MATLAB (tm) file format.  Considerably more sophisticated than the MatrixMarket_ format, MATLAB stores data in a binary format, so reading and writing large matrices is noticably more efficient.  On the other hand, the simplicity of the MatrixMatket_ makes it particularly easy to work with in other software (e.g. using ``fprintf()`` and ``fscanf()``).

  The MATLAB format supports multiple matrices per-file.  These are stored in a Python ``dict`` object as shown in the following example:

  ::

     >>> from scipy.sparse import csr_matrix
     >>> from scipy.io import loadmat, savemat
     >>> A = csr_matrix([[1.0,0.0,2.0],[0.0,3.0,0.0]])
     >>> A
     <2x3 sparse matrix of type '<type 'numpy.float64'>'
             with 3 stored elements in Compressed Sparse Row format>
     >>> savemat('my_file.mat', {'A' : A})
     >>> m_dict = loadmat('my_file.mat')
     >>> m_dict['A']
     <2x3 sparse matrix of type '<type 'numpy.float64'>'
             with 3 stored elements in COOrdinate format>

Additional Resources
====================

Python
------

* [`http://code.google.com/p/sfepy/`_ PyAMG] : Algebraic Multigrid Solvers in Python.

* [`http://code.google.com/p/sfepy/`_ SfePy_] : Simple Finite Elements in Python.

* [`http://www.ctcms.nist.gov/fipy/`_ FiPy_] : A Finite Volume PDE Solver Using Python

* [`http://scipy.org/scipy/scikits/`_ UMFPACK] : Support for the UMFPACK sparse solver library.

* [`http://trilinos.sandia.gov/packages/pytrilinos/`_ Pytrilinos]: High-Performance Distributed-Memory Solvers for Python

Books
-----

* [`http://www-users.cs.umn.edu/~saad/books.html`_ Iterative Methods for Sparse Linear Systems] by Yousef Saad (first edition is freely available)

Other Packages and Libraries
----------------------------

* [`http://www-users.cs.umn.edu/~saad/software/SPARSKIT/sparskit.html`_ SPARSKIT] : A basic tool-kit for sparse matrix computations.

* [`http://trilinos.sandia.gov/`_ Trilinos] : An extensive collection of distributed-memory solvers.

TODO: update and integrate this information where possible
==========================================================

for convenience; the ``lil_matrix`` class supports basic slicing and fancy indexing with a similar syntax to NumPy_ arrays, and is adapted to gradually fill your sparse matrix, while compressed formats are not suited to a progressive filling.

To perform manipulations such as multiplication or inversion, first convert the matrix to either CSC or CSR format. These formats store the sparse matrix in arrays and allow faster computations than the list or dictionary-based formats. The ``lil_matrix`` format is row-based, so conversion to CSR is efficient, whereas conversion to CSC is less so.

Notes:

* CSC format is also called [`http://math.nist.gov/MatrixMarket/formats.html#hb`_ Harwell-Boeing] format, and used in other libraries or software ([`http://www.mathworks.com/access/helpdesk/help/techdoc/math/sparse3.html#12993`_ Matlab] for example).

Examples (TODO: update)
=======================

Example 1
~~~~~~~~~

This is a very simple example illustrating basic usage of ``linsolve``, ``sparse`` and some other useful things (use the latest version of linsolve.py). If you don't know how to get hold of the latest modules, spend some time in the ["Developer Zone"] and see the **SOURCE CODE** section.

We're going to solve a trivial case of ``Ax = b``, where ``A`` is a matrix, ``b`` a vector (the RHS) and ``x`` the unknowns. In this example ``A`` refers to the 'normal' matrix, and ``Asp`` to the **sparse representation** of ``A``, ``x`` for the 'normal' solution and ``xsp`` for the solution arising from using the sparse method. (You'll most probably find it useful to use [`http://ipython.scipy.org`_ IPython] when going through this example, especially if you're used to Matlab®. The normal Python prompt looks like this ``>>>``, IPython's default prompt (one can change it) looks like this ``In [x]:``, where the ``x`` is a number).

Import the necessary commands from the numpy and scipy modules:

::

   from numpy import allclose, arange, eye, linalg, ones
   from scipy import linsolve, sparse

It is of course also possible to import all the commands from the two modules, but in that case it might not be a bad idea to do it as follows (note that this is just one way of doing it):

::

   import numpy as N
   import scipy as S

If you're working in an IPython session, type ``S.`` and press the <TAB> button, you'll see all the available commands (attributes). The same goes for ``N.``

Construct an identity 1000x1000 ``lil_matrix``. There is a couple of ways of doing this, one method is slow, the other not. A slow method:

::

   A = eye(1000)
   Asp = sparse.lil_matrix(A)

A faster method:

::

   Asp = sparse.lil_matrix((1000,1000))
   Asp.setdiag(ones(1000))

Note that ``Asp`` is still in **LI**nked **L**ist (``lil_matrix``) format - leave it like that for now.

Now create vector ``b``; we choose the entries so that we can easily check the (trivial) solution:

::

   b = arange(1,1001)

To see what ``b`` looks like, type ``b`` or ``print b`` at your prompt.

Now let's solve ``Ax = b``, first using ``A``...

::

   x = linalg.solve(A,b)

... and now using ``Asp``:

::

   xsp = linsolve.spsolve(Asp,b)

Check the result: ``x`` and ``xsp`` should both be equal to ``b``, as one expects. A convenient way of checking this is to make use of ``allclose()``. In IPython you can type ``allclose?`` to get help on it, and at the Python prompt one will type ``help(allclose)`` (this is the case for almost all commands, but some might not have a **Docstring**). The input and resulting output from the command is shown here:

::

   >>> allclose(x,b)
   True
   >>> allclose(b,xsp)
   True

Let's have a look at the difference in solution time between the two methods. In an IPython session, simply type (or scroll back with your arrow keys and just insert the ``time`` in front):

::

   time x = linalg.solve(A,b)
   Itime xsp1 = linsolve.spsolve(Asp,b)

You should see a significant difference (roughly 5 to 6 times faster).

If you're working in the normal Python shell instead, do the following:

::

   from time import time
   t=time(); x = linalg.solve(A,b); time()-t
   t=time(); xsp1 = linsolve.spsolve(Asp,b); time()-t

We saw that we can get the solution to ``Ax = b`` even if ``A`` is in **LIL** format. We'll now inspect the difference in execution speed for the following (assuming that you're using IPython, ``Out [x]:``'s not shown, and in a new session):

::

   from numpy import allclose, arange, eye, linalg, random, ones
   from scipy import linsolve, sparse
   Asp = sparse.lil_matrix((50000,50000))
   Asp.setdiag(ones(50000))
   Asp[20,100:250] = 10*random.rand(150)
   Asp[200:250,30] = 10*random.rand(50)
   b = arange(0,50000)
   time xsp1 = linsolve.spsolve(Asp,b)
   time xsp2 = linsolve.spsolve(Asp.tocsc(),b)
   time xsp3 = linsolve.spsolve(Asp.tocsr(),b)
   allclose(xsp1,xsp2) # Should be True
   allclose(xsp2,xsp3) # Should be True

**Note**: the line that returns xsp3 fails if you don't have a recent enough version of scipy.

The time for the last solution (``xsp3``) should be the fastest by a factor of roughly 1,5 to 2 times compared to the other two solutions (``xsp1`` and ``xsp2``). The benefit in speed when compared to using 'normal' methods for solving sparse systems is obvious.

Example 2
~~~~~~~~~

Construct a 1000x1000 ``lil_matrix`` and add some values to it:

::

   from scipy import sparse, linsolve
   from numpy import random, linalg
   A = sparse.lil_matrix((1000, 1000))
   A[0, :100] = random.rand(100)
   A[1, 100:200] = A[0, :100]
   A.setdiag(random.rand(1000))

Now convert it to CSR format and solve (A A^T) x = b for x:

::

   A = A.tocsr()
   b = random.rand(1000)
   x = linsolve.spsolve(A * A.T, b)

  The ``.T`` bit of ``A.T`` above computes the transpose of ``A``, i.e., it's a shortcut for ``A.transpose()``. It will also work for 'normal' dense (numpy) matrices and currently works for arrays in the latest SVN versions of NumPy. Also take note of the differences between matrices and arrays when working with them. If ``B`` is a matrix and ``C`` an array, both with the same size and entries, then ``B*B`` is **not** the same as ``C*C``. See ["NumPy_ for Matlab Users"] for more details.

Convert it to a dense matrix and solve, and check that the result is the same:

::

   A_ = A.todense()
   x_ = linalg.solve(A_ * A_.T, b)
   err = linalg.norm(x-x_)

Now we can print the error norm with:

::

   print "Norm error =", err

It should be small |:)|

