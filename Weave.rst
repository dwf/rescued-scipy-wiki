#format rst

The weave package allows the inclusion of C/C++ within Python code and is useful in accelerating Python code.

* Weave is a subpackage of scipy. (I.e. you have it already if you installed SciPy)

* Alternatively, you can check-out and install weave separately using

::

   svn co http://svn.scipy.org/svn/scipy/trunk/scipy/weave weave
   cd weave
   sudo python setup.py install

* Current documentation (which is still being updated to reflect the move to NumPy) can be seen `here <http://projects.scipy.org/scipy/scipy/browser/trunk/scipy/weave/doc/tutorial.txt?format=raw>`_

* PerformancePython: A comparison of various ways to improve the performance of Python code using Numeric,  weave, Pyrex, Psyco and Fortran (f2py) for solving Laplace's equation.  These are compared with code written in C++.

* [:Cookbook/Weave] Some cookbook examples of using low level Numpy C-API

If you have scipy installed, weave includes several examples here:

::

   site-packages/scipy/weave/examples

And the above tutorial is on your installation also:

::

   site-packages/scipy/weave/doc

To find where your site-packages directory holding scipy is, run this python command in a terminal:

::

   python -c "from scipy import weave; print weave.__path__"

some random notes
-----------------

when is code compiled
~~~~~~~~~~~~~~~~~~~~~

a) Is it possible to distribute modules using weave to other people who might *NOT* have a C compiler installed ?  b)  when I (or someone who does not have a C compiler !) change parts of that module that should not require a recompiling of the C part - is weave smart enough to recognise this ?

::

   > It's my understanding that a re-compile is triggered by a mismatch to a
   > MD5 generated on the C string that is to be compiled and the cached MD5
   > for the expression.  This would mean that only changes to that string
   > would force a re-compile.  However, even formatting changes (even to
   > whitespace) in the C string force a recompile.

   > The types of the inputs are also taken into account.

   > And (to be pedantic :) ) the version the numpy API.

how to distribute code to people w/o a C compiler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   You can make weave generate an extension module of your choosing.
   Look at examples/fibonacci.py which builds a
   fibonacci_ext.cpp/fibonacci_ext.so pair in the current directory.

Weave and Numpy array arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   >> if I pass a numpy array 'arr' as argument
   >> a) how does the C code get arr.ndim ?
   >> b) how does the C code get arr.shape[0],... ?
   >> c) if the C code changes elements of arr, are those changes *on the
   >> original data* ?

   Yes.

   >> In other words, is weave.inline making a copy of arr ?

   No.

   >> I searched through
   >> http://projects.scipy.org/scipy/scipy/browser/trunk/scipy/weave/doc/tutorial.
   >> html?format=raw but did not find a definite answer. From
   >> the 'array3d.py' example in weave in looks like Narr would contain the
   >> shape !?

   Yes. Specifically:

   arr_array is the actual ``PyArrayObject``* corresponding to the Python object.

   Narr = arr_array->dimensions
   Sarr = arr_array->strides
   Darr = arr_array->nd
   arr = arr_array->data

   > > Oh, and I forgot: How about non-contiguous arrays !?

   Passed straight on through, just like contiguous arrays.

   >> In the case that these are handled - does that slow things down for proper
   >> aligned arrays,  too !?

   You will have to take the strides into account in your code.


-------------------------

 CategorySciPyPackages

.. ############################################################################

.. _NumPy: ../NumPy

.. _PerformancePython: ../PerformancePython

.. _CategorySciPyPackages: ../CategorySciPyPackages

