#format rst

TConfig
=======

Traits-based declarative configuration for programs
---------------------------------------------------

[`mailto:Fernando.Perez@colorado.edu`_ Fernando Perez]

**Applied Mathematics**

**University of Colorado at Boulder**

Traits
======

*Typed variables* with validation and automatic GUI generation:

::

   from enthought.traits.api import HasTraits, Int, Float

   class C(HasTraits):
       n = Int(10)
       x = Float(5.5)

   a = C()

   a.edit_traits()

ConfigObj
=========

.ini / .conf style file read/write tool with nested sections and comment preservation:

::

   # Top-level of the configuration
   m = 1

   # A section
   [Protocol]
       ptype = 'http'

       # A subsection
       [[Handler]]
           key = 'foo'

TConfig = Traits + ConfigObj
============================

* Changes to the Traited instance propagate back into the ConfigObj.

* A purely declarative interface for describing configurations.

* Auto-generation of valid .conf files.

* Hierarchical inclusion of files.

* Automatic GUI editing of configuration objects.

Where is TConfig?

http://ipython.scipy.org/svn/ipython/ipython/branches/saw/sandbox/tconfig

**DEMO**

