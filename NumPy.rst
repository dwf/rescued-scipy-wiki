#format rst

NumPy
=====

The fundamental package needed for scientific computing with Python is called NumPy. This package contains:

* a powerful N-dimensional array object

* sophisticated (broadcasting) functions

* tools for integrating C/C++ and Fortran code

* useful linear algebra, Fourier transform, and random number capabilities.

It derives from the old Numeric code base and can be used as a replacement for Numeric. It also adds the features introduced by numarray and can be used to replace numarray.

Numeric users should find the transition very easy.  There is a module (import numpy.lib.convertcode --- see the convertall and fromfile functions in that module) that can make (most of) the necessary changes to your Python code that used Numeric to make it work with the new NumPy.  Users of numarray currently need to do a bit more work (mostly import changes) to work with the new system because nobody has yet written an equivalent to convertcode.py

Although Sourceforge is used to distribute releases, bugs and feature-requests should **not** be placed there.  Instead use the Trac pages for NumPy at http://projects.scipy.org/scipy/numpy .  You will need to create an account and login to file a ticket (this is to avoid trouble with SPAM).  A ticket is a bug-report, feature-request, or patch.

Other links:

* ` Sourceforge download site <http://sourceforge.net/project/showfiles.php?group_id=1369&package_id=175103>`_

* `Documentation <http://www.trelgol.com/>`_ (fee-based) and `Sample Chapters <http://www.tramy.us/numpybooksample.pdf>`_

Much of the documentation for Numeric and Numarray is applicable to the new NumPy package.  However, there are `significant feature improvements <http://numeric.scipy.org/new_features.html>`_.  A complete guide to the new system is being written by the primary developer, Travis Oliphant.  If you want to fully understand the new system, or you just want to encourage further development on NumPy (or SciPy), you should purchase the documentation which is being sold for a relatively brief period of time to help offset the cost of producing the Numeric/numarray hybrid and to help raise money for future development.   If you have further questions about the fee-based documentation, Travis has written some `responses <http://www.tramy.us/FAQ.html>`_ to FAQs.

* An extensive and free ["Numpy Example List"] illustrates the use of most of the Numpy features.

* `Free documentation for Numeric <http://numeric.scipy.org/numpydoc/numdoc.htm>`_ (most of which is still valid) is available, or `as a pdf file <http://numeric.scipy.org/numpy.pdf>`_.   Obviously you should replace references to Numeric in that document with numpy (i.e. instead of import Numeric, use import numpy).

* `New Features of NumPy <http://numeric.scipy.org/new_features.html>`_

* A presentation of the new system was also made at SciPy 2005.  You can `download <http://www.scipy.org/wikis/scipy05/presentations/scipy_core_2005.ppt/download>`_ the presentation (or in `pdf <http://www.scipy.org/wikis/scipy05/presentations/scipy_2005_bas.pdf/download>`_ format)

For about 6 months, the new package was called SciPy Core, and so you will occasionally see references to SciPy Core.   It was decided in January 2006 to go with the historical name of NumPy for the new package.  Realize that NumPy (module name numpy) is the new name.   Do not be confused by references to scipy_core.  These should all be replaced by numpy.  Also, because of the name-change, there were a lot of dicussions that took place on `scipy-dev@scipy.org`_ and `scipy-user@scipy.org`_.  If you have a question about the new system, you may wish to run a search on those mailing lists.

See also http://numeric.scipy.org  and http://numpy.scipy.org

.. ############################################################################

.. _SciPy: ../SciPy

.. _scipy-dev@scipy.org: mailto:scipy-dev@scipy.org

.. _scipy-user@scipy.org: mailto:scipy-user@scipy.org

