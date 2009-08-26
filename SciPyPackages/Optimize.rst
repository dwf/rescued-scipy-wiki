#format rst

There are two mainstream optimization packages available:

* `scikits.openopt <http://scipy.org/scipy/scikits/wiki/OpenOpt>`_ (license: BSD)

* `SciPy_.optimize <http://www.scipy.org/doc/api_docs/SciPy.optimize.html>`_ (license: BSD)

* Also you could be interested in `Optimization <http://www.scipy.org/Topical_Software#head-d21a11d2d173826993e03eb937fac7e6347e6d5f>`_ section from `Topical software <http://www.scipy.org/Topical_Software>`_.

scipy.optimize contains only copyleft-free solvers, while scikits.openopt contains connections to any-licensed solvers (BSD, GPL, LGPL etc), as well as some our own Python-written BSD-licensed solvers (numpy required). Using OpenOpt `oofun <http://scipy.org/scipy/scikits/wiki/OOFun>`_ can speedup some non-linear solvers, from or beyond scipy.optimize (see 10X speedup `example <http://projects.scipy.org/scipy/scikits/browser/trunk/openopt/scikits/openopt/examples/oofun/speedup.py>`_).

