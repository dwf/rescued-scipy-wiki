#format rst

Matrix Specification
====================

A design specification for a new matrix class could serve as a guide for making changes to the current matrix class. Or, if the final design breaks too much with current matrix behavior, it could serve as a guide to making a new matrix class.

The most basic, and the most contentious, design decision of a new matrix class is matrix indexing. Several possible approaches have been discussed, as documented at  http://www.scipy.org/MatrixIndexing . What follows is a summary of options.

1. Matrices should be more like arrays
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

The matrix class should be more like the array class:

* iteration over a matrix should yield 1d arrays

* x[0] should yield a 1d array

* x[0,:] and x[\:,0] should return 1d arrays (this is more controversial: it matches ndarray behavior but loses simple extraction of rows and columns as submatrices)

Variant: instead of a 1d array, return a 1d array-like object that contains the orientation (row or column) as an attribute.

Question: is x.sum(1) also 1d array?

2. Operations on matrices should return a matrix or a scalar
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

All operations on a matrix, including all permissible indexing, should return either a matrix or a scalar.

Variant: scalar indexes raise an error except when a matrix has a single row or single column, like in Gauss.

Question: If dimensions are not reduced, what mechanism will allow matrices to be correctly handled by routines that expect that reduction during iteration?

3. Matrices should behave like Octave/Matlab matrices
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

Similar to the previous approach except that matrix operations should only return matrices and never return scalars. Thus a scalar becomes a 1x1 matrix. This would make the matrix class similar to Octave and Matlab.

Question: should scalar indexing index elements, as in Matlab? If so, should iteration be across elements? Or should scalar indexing of a matrix with multiple rows and columns be illegal, like in Gauss?

General Questions
,,,,,,,,,,,,,,,,,

Indexing questions: What is x[0]? What is x[0][0]? What is x[0,:]? What is x[\:,0]?

