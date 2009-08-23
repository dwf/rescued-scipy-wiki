#format rst

Autovectorization
=================

There are instances where it is very convenient to have a function defined in the language of scalars that can operate on arrays. [`http://docs.scipy.org/doc/numpy/reference/generated/numpy.vectorize.html`_ numpy.vectorize] provides such a conversion.

In simplier language: This function basically makes a functions which calculate single values (e. g. math.sin) operate on array.

Some links and threads on this:

* optimising single value functions for array calculations -  `http://article.gmane.org/gmane.comp.python.numeric.general/26543`_

* vectorized function inside a class -  `http://article.gmane.org/gmane.comp.python.numeric.general/16438`_

* numpy.vectorize performance - `http://article.gmane.org/gmane.comp.python.numeric.general/6867`_

* vectorize() - `http://www.scipy.org/Numpy_Example_List_With_Doc#head-fbff061fdb843209707a8fa537d9b24b6a91245e`_

* NumPy_: vectorization - `http://folk.uio.no/hpl/PyUiT/PyUiT-split/slide218.html`_

* vectorizing loops - `http://article.gmane.org/gmane.comp.python.numeric.general/17266`_

See also
--------

* ["`SciPyPackages/NumExpr`_"]

