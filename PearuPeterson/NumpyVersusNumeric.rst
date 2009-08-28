#format rst

Numpy versus Numeric
====================

While converting Numeric based codes to numpy, I have noticed number of differences how their corresponding functions behave on some corner usage cases. Some of these may be bugs, incompatibilities, or features (of either packages).

Length of scalar array
----------------------

In Numeric the lenght of a scalar is 1:

::

   >>> len(array(1))
   1

In numpy a TypeError is raised:

::

   >>> len(array(1))
   Traceback (most recent call last):
     File "<stdin>", line 1, in ?
   TypeError: len() of unsized object

