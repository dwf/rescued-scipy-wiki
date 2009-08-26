#format rst

Example of using f2py
=====================

*Taken from a message on 2006-06-22 to scipy-user by* ArndBaecker_

Thanks to f2py, wrapping Fortran code is (with a bit of effort) trivial in many cases. For complicated functions requiring many arguments the wrapper can become longish. Fortunately, many things can be learnt from looking at scipy/Lib/linalg/generic_flapack.pyf In particular, the documentation at http://cens.ioc.ee/projects/f2py2e/  is excellent. I also found  the f2py notes by FernandoPerez_ very helpful, http://cens.ioc.ee/pipermail/f2py-users/2003-April/000472.html

Let me try to give some general remarks on how to start (the real authority on all this is of course Pearu, so please correct me if I got things wrong here):

* first find a routine which will do the job you want:

  * If the lapack documentation is installed properly on Linux you could do

      ``apropos  keyword``

  * http://www.netlib.org/  provides a nice decision tree

* make sure that that it does not exist in scipy:

::

     from scipy.lib import lapack
     lapack.clapack.<TAB>         (assuming Ipython)
     lapack.clapack.<routine_name>

  Remark: routines starting with c/z are for double/single complex and routines for d/s for double/single real numbers. The calling sequence for c/z and d/s are (I think always) the same and sometimes they are also the same for the real and complex case.

* Then one has to download the fortran file for the lapack routine of interest.

* Generate wrapper by calling

    ``f2py -m wrap_lap -h wrap_lap.pyf lapack_routine.f``

* Generate library

    ``f2py  -c wrap_lap.pyf  lapack_routine.f -latlas -llapack -lblas``

* You can use this by

::

     import wrap_lap

  Note, that this is not yet polished (this is the part on which has to spent some effort |;-)| ), i.e. one has to tell which variables are input, which are output and which are optional. In addition temporary storage has to be provided with the right dimensions as described in the documentation part of the lapack routine.

Concrete (and very simple) example (non-lapack):

Wrapping Hermite polynomials
----------------------------

Download code (found after hours of googling |;-)| , from http://cdm.unimo.it/home/matematica/funaro.daniele/splib.txt

and extract ``hermite.f``

Generate wrapper framework:

::

     # only run the following line _once_
     # (and never again, otherwise the hand-modified hermite.pyf
     #  goes down the drains)
     f2py -m hermite -h hermite.pyf hermite.f

Then modify ``hermite.pyf``

Create the module:

::

     f2py -c hermite.pyf  hermite.f

     # add this if you want:
     -DF2PY_REPORT_ON_ARRAY_COPY=1 -DF2PY_REPORT_ATEXIT

Simple test:

::

     import hermite
     hermite.vahepo(2,2.0)
     import scipy
     scipy.special.hermite(2)(2.0)

A more complicated example about how to wrap routines for band matrices can be found at http://www.physik.tu-dresden.de/~baecker/comp_talks.html  under "Python and Co - some recent developments".

Step by step wrapping of a simple numerical code
------------------------------------------------

`http://websrv.cs.umt.edu/isis/index.php/F2py_example`_

-------------------------

 CategoryCookbook_ CategoryCookbook_

