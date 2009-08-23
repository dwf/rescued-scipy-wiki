#format rst

Proposal of New Solver Classes for SciPy
----------------------------------------

TODO
~~~~

1. agree upon the arguments and their names, see below

#. implement the linear solvers first, as they are the most used, as a proof of concept

#. eigenvalue solvers

#. nonlinear solvers

#. ...

Argument names
~~~~~~~~~~~~~~

*Conventions:* lowercase letters with words connected using underscores, as it is usual in SciPy.

*Examples:*

<strong class="highlight">.. raw:: html

</strong>[Table not converted]

Examples of Usage
~~~~~~~~~~~~~~~~~

"Script" usage
::::::::::::::

Suppose we have:

::

   class Umfpack( LinearSolver ):
       name = 'ls.umfpack'
       ...
   class ScipyIterative( LinearSolver ):
       name = 'ls.scipy_iterative'
       ...

Then:

::

   s = ScipyIterative( tol_abs = 1e-6, mtx = A, method = 'cg' )
   x = s( rhs )
   x2 = s( rhs2, abs_tol = 1e-8 )
   conf = {'tol_abs' : 1e-5, 'tol_rel' : 1e-5, 'method' : 'bicg'}
   s = ScipyIterative( conf = conf )
   x = s( rhs, conf = conf, mtx = B )
   ds = Umfpack( mtx = A )
   x = ds( rhs )

"Framework" Usage
:::::::::::::::::

For example, any linear solver (e.g. umfpack, scipy iterative solvers, ...) can be used like:

::

   # Use a SciPy iterative solver configuration.
   iconf = {
       'name' : 'ls',
       'kind' : 'ls.scipy_iterative',
       'method'   : 'cg',
       'max_iter' : 1000,
       'tol_abs'  : 1e-12,
   }
   # Or a direct solver configuration.
   dconf = {
       'name' : 'ls',
       'kind' : 'ls.umfpack',
   }
   s = Solver.any_from_conf( conf = dconf, mtx = A ) # Possibly pre-solves by LU.
   x1 = s( rhs1 )
   x2 = s( rhs2 )
   ...
   x = s( rhs, mtx = B )

The proper solver class is chosen automatically according to the 'kind' attribute of the configuration.

Abstract classes
~~~~~~~~~~~~~~~~

Something to start with (ignore the argument names for now...):

::

   class Solver( Struct ):
        def __init__( self, conf, **kwargs ):
            Struct.__init__( self, conf = conf, **kwargs )
        def __call__( self, **kwargs ):
            print 'called an abstract Solver instance!'
            raise ValueError
   class LinearSolver( Solver ):
        def __init__( self, conf, mtx = None, status = None, **kwargs ):
            Solver.__init__( self, conf = conf, mtx = mtx, status = status,
                             **kwargs )
        def __call__( self, rhs, conf = None, mtx = None, status = None ):
            print 'called an abstract LinearSolver instance!'
            raise ValueError
   class NonlinearSolver( Solver ):
        def __init__( self, conf, evaluator = None, linSolver = None,
                      status = None, **kwargs ):
            Solver.__init__( self, conf = conf, evaluator = evaluator,
                             linSolver = linSolver, status = status,
                             **kwargs )
        def __call__( self, state0, conf = None, evaluator = None,
                      linSolver = None, status = None ):
            print 'called an abstract NonlinearSolver instance!'
            raise ValueError
   class EigenvalueSolver( Solver ):
        def __init__( self, conf, mtxA = None, mtxB = None, nEigs = None,
                      eigenvectors = None, status = None ):
            Solver.__init__( self, conf = conf, mtxA = mtxA, mtxB = mtxB,
                             nEigs = nEigs, eigenvectors = eigenvectors,
                             status = status )
        def __call__( self, mtxA, mtxB = None, nEigs = None,
                      eigenvectors = None, status = None, conf = None ):
            print 'called an abstract EigenvalueSolver instance!'
            raise ValueError

-------------------------

 ProposedEnhancements_

.. ############################################################################

.. _LinearOperator: ../LinearOperator

.. _ProposedEnhancements: ../ProposedEnhancements

