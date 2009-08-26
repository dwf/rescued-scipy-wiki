#format rst

PyTrilinos
----------

-------------------------

 PyTrilinos_**: A Python Interface to Trilinos, a Set of Object-Oriented Solver Packages**

*Bill Spotz, Sandia National Laboratories*

PyTrilinos_ is a python interface to selected Trilinos solver packages. Trilinos is a publicly available, open source set of largely independent yet interoperable object-oriented solver packages designed at Sandia National Laboratories for parallel and serial scientific computing. These packages include linear algebra services, direct and iterative linear solvers for dense and sparse matrices, algebraic and multi-level preconditioners, eigensolvers, nonlinear and continuation solvers, and a wide variety of utilities, ranging from graph coloring to I/O and matrix factories. With Release 5.0 in March 2005, Trilinos included the PyTrilinos_ package, which provides a python interface to a selected set of Trilinos packages: Epetra, the linear agebra services package; EpetraExt_, an extension of Epetra that provides graph coloring algorithms, transforms and other utilities; and NOX, the nonlinear solver package, including an interface to Epetra. Trilinos Release 6.0, slated for September 2005, should include significant improvements to the first release of PyTrilinos_, including more extensive wrappers for Epetra (including MPI), and additional wrapped packages. These packages will include AztecOO, for sparse iterative solvers; Amesos, for sparse direct solvers; IFPACK, for algebraic preconditioning; ML, for multi-level preconditioning; LOCA, for continuation algorithms; and TriUtils_, a collection of utilities. This talk will provide an overview of the Trilinos project with a focus on the python interface.

