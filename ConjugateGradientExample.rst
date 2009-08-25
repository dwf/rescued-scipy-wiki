<p>The following example is provided as the first example of using matrices and linear algebra in numpy (hopefully others will provide more).  Its intent is to provide a concrete example upon which design decisions can be made with regard to the matrix class and the linalg module.</p>
<div class="section" id="conjugate-gradient">
<h3>Conjugate Gradient</h3>
<p>I wish to return x, which solves A x = b, where A is a matrix, b is a column vector and x is also a column vector.  When A is symmetric and positive definite, then the <a class="http reference external" href="http://en.wikipedia.org/wiki/Conjugate_gradient_algorithm">conjugate gradient method</a> is guaranteed to converge.</p>
<p>This algorithm can be expanded to handle multiple right-hand sides, producing multiple solutions.  In this case, b and x become matrices (collections of column vectors).  For cases where the application allows for simultaneous solutions, it can be a big win: we promote some of our linear algebra from level-2 BLAS to level-3 BLAS, which can be much more efficient.  (I don't actually know if numpy uses level-3 BLAS, but I can assume here that matrix-matrix multiplication does, or someday will.)</p>
<p>The algorithm I came up with is as follows:</p>
::

import numpy as np

def col_vector_norms(a,order=None):
    &quot;&quot;&quot;
    Return an array representing the norms of a set of column vectors.

    Arguments:
      a      - An (n x m) numpy matrix, representing m column vectors of length
               n.
      order  - The order of the norm.  See numpy.linalg.norm for more
               information.
    &quot;&quot;&quot;
    (nrow,ncol) = a.shape
    norms = np.zeros((ncol,),a.dtype)
    for j in range(ncol):
        col = a[:,j].A
        col.shape = (nrow,)
        norms[j] = np.linalg.norm(col,order)
    return norms

def cg(A, b, x=None, tol=1.0e-8, itmax=None, info=False):
    &quot;&quot;&quot;
    Use the conjugate gradient method to return x such that A * x = b.

    Arguments:
      A      - A square numpy matrix representing the linear operator.  If A is
               symmetric, then this algorithm is guaranteed to converge.
      b      - An (n x m) numpy matrix representing the right hand side, where m
               is the number of column vectors and n is the size of A.
      x      - A numpy matrix, same shape as b, that serves as the initial guess
               for the algorithm.  Defaults to the zero matrix.  If given, the
               return matrix is this matrix.
      tol    - Accuracy tolerance for the algorithm stopping criterion.  Default
               1.0e-8.
      itmax  - Maximun allowed iterations.  Default is n, the size of A.
      info   - If info is True, return a tuple (x, k, norms) where x is the
               solution, k is the required iterations and norms is an array of
               the final residual norms.  Default False.
    &quot;&quot;&quot;

    # Sanity checks.  I check the types of A, b and x to ensure that I will get
    # matrix algebra.
    if not isinstance(A,np.matrix):
        raise TypeError, &quot;A must be a matrix&quot;
    (nrow,ncol) = A.shape
    if nrow != ncol:
        raise ValueError, &quot;A must be a square matrix&quot;
    if not isinstance(b,np.matrix):
        raise TypeError, &quot;b must be a matrix&quot;
    if x is None:
        x = np.matrix(np.zeros(b.shape, b.dtype))
    if not isinstance(x,np.matrix):
        raise TypeError, &quot;x must be a matrix&quot;
    if itmax is None:
        itmax = nrow

    # Initialization
    nrhs  = b.shape[1]
    r2    = np.zeros((nrhs,), b.dtype)
    alpha = np.zeros((nrhs,), b.dtype)
    beta  = np.zeros((nrhs,), b.dtype)
    r = b - A * x
    p = r.copy()
    k = 0

    # Main conjugate gradient loop
    while k &lt; itmax:
        for j in range(nrhs):
            r2[j] = r[:,j].T * r[:,j]
        for j in range(nrhs):
            alpha[j] = r2[j] / (p[:,j].T * A * p[:,j])
        x[:] += p.A * alpha
        r[:] -= (A * p).A * alpha
        norms = col_vector_norms(r,2)
        if (norms &lt; tol).all():
            break
        for j in range(nrhs):
            beta[j] = (r[:,j].T * r[:,j]) / r2[j]
        p[:] = r + p.A * beta
        k += 1

    # Return the requested information
    if info:
        return (x, k, norms)
    else:
        return x<p>Here is essentially the same thing written for array operations.  (This time both arrays and matrices are correctly handled.)  Note that the matrix test in col_vector_norms2 would not be necessary if iteration over matrices were to yield 1d arrays (as is under discussion), and that the test then reduces to a single line that could be moved into the algorithm itself:</p>
::

def col_vector_norms2(a,order=None):
    &quot;&quot;&quot;
    See doc for col_vector_norms
    &quot;&quot;&quot;
    if isinstance(a,np.matrix):
        a = a.A
    norms = np.fromiter((np.linalg.norm(col,order) for col in a.T),a.dtype)
    return norms

def cg2(A, b, x=None, tol=1.0e-8, itmax=None, info=False):
    &quot;&quot;&quot;
    See doc string for cg.
    &quot;&quot;&quot;
    matrixout = True if isinstance(A,np.matrix) else False
    A = np.asarray(A)
    b = np.asarray(b)
    nrow, ncol = A.shape
    if nrow != ncol:
        raise ValueError, &quot;A must be square&quot;
    if x is None:
        x = np.zeros(b.shape, b.dtype)
    if itmax is None:
        itmax = nrow

    # Initialization
    nrhs  = b.shape[1]
    alpha = np.zeros((nrhs,), b.dtype)
    beta  = np.zeros((nrhs,), b.dtype)
    r2old = np.zeros((nrhs,), b.dtype)
    r = b - np.dot(A,x)
    r2 = (r * r).sum(axis=0)
    p = r.copy()
    k = 0

    # Main conjugate gradient loop
    while k &lt; itmax:
        for j in range(nrhs):
            alpha[j] = r2[j] / (np.outer(p[:,j],p[:,j]) * A).sum()
        # or replace the loop by:
        # alpha = r2 / (p*np.dot(A,p)).sum(axis=0)
        x[:] += p * alpha
        r[:] -= np.dot(A , p) * alpha
        norms = col_vector_norms2(r,2)
        if (norms &lt; tol).all():
            break
        r2old[:] = r2
        r2[:] = (r * r).sum(axis=0)
        beta = r2 / r2old
        p[:] = r + (p * beta)
        k += 1

    if matrixout:
        x = np.asmatrix(x)
    # Return the requested information
    if info:
        return (x, k, norms)
    else:
        return x</div>
<div class="section" id="discussion">
<h3>Discussion</h3>
<p>The function cg() takes as input right-hand side b, which is passed in as a matrix.  Conceptually, it and x are a collection of independent column vectors, although they need to be matrices to take advantage of level-3 BLAS.</p>
<p>The CG algorithm is considered converged when the norm of the residual r = b - A x is less than some specified tolerance.  For multiple right-hand sides, we actually have an array of residual norms.  Getting this right took more than just a couple of lines of code, so I broke out the computation of these norms into its own function.</p>
<p>This illustrates an example of where row_vector and col_vector classes can provide an advantage.  I am using the numpy.linalg.norm() function, which can compute norms of both &quot;vectors&quot; and &quot;matrices&quot;, which are two different operations.  As near as I can tell, it checks the number of dimensions and interprets 1D arrays as vectors and 2D arrays as matrices.  So I have to extract a column from my matrix, interpret it as an array and then change its shape to be 1D before calling norm().  If there were row_vector and col_vector classes, and they were naturally extracted from matrix objects, and the norm() function checked for these types before proceeding appropriately, this code would be much cleaner and readable.</p>
<p>I first wrote this algorithm for single vectors b and x, but expressed as n x 1 matrices.  In that version of the algorithm, I would compute:</p>
::

r2 = r.T * r<p>which is very readable, but r2 was a 1 x 1 matrix and I couldn't divide by it.  So I had to change it to:</p>
::

r2 = (r.T * r)[0,0]<p>which is less readable.  When I expanded it to handle multiple solutions, I was able to get rid of the indexing:</p>
::

r2[j] = r[:,j].T * r[:,j]<p>because r2 is now a numpy array and I guess the conversion from 1 x 1 matrix to scalar is handled automatically.</p>
<p>I'd be curious to see if anybody can come up with a way to fill up r2, alpha and beta by iterating over columns rather than iterating over column indexes.</p>
<p>The second version of the algorithm provided above suggests that little if anything was gained by the use of matrices.</p>
</div>
