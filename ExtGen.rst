ExtGen - Python Extension module Generator
==========================================

Author:: Pearu Peterson < `pearu.peterson@gmail.com`_ >

Introduction
------------

ExtGen is a pure Python package that provides a high-level tool for constructing and building Python extension modules.

**Warning:** *ExtGen is a very new project and is not ready for production use. But if you like the idea of ExtGen then help in any form (feedback, bug reports, feature requests, patches, etc) is welcome.*

Hello example
-------------

::

   >>> from numpy.f2py.lib.extgen import *
   >>> f = PyCFunction('say', PyCArgument('word', output_intent='return'))
   >>> m = PyCModule('foo', f)
   >>> foo = m.build()
   >>> print foo.__doc__
   This module "foo" is generated with ExtGen from NumPy version ...

   :Functions:
     say(word) -> (word)
   >>> foo.say('Hello')
   'Hello'
   >>> print m.generate() # this will print the extension module source that ExtGen generated, useful for debugging

Documentation
-------------

* [`http://docs.python.org/ext/`_ "Extending and Embedding the Python Interpreter"]

* [`http://docs.python.org/api/`_ "Python/C API Reference Manual"]

* [`http://projects.scipy.org/scipy/numpy/wiki/G3F2PY/ExtGenDoc`_ "ExtGen Reference Manual"]

For more examples and documentation, see the documentation strings of the component classes such as PyCModule, PyCFunction, etc.

Getting and installing ExtGen
-----------------------------

Get and install NumPy_ from SVN. ExtGen is currently a subpackage of numpy.f2py.lib package.

.. ############################################################################

.. _pearu.peterson@gmail.com: mailto:pearu.peterson@gmail.com

.. _NumPy: ../NumPy

