#format rst

`TraitsUI <http://code.enthought.com/traits/>`_ is a module that allows automatic generation of `WxPython <http://www.wxpython.org>`_ dialogs to edit the properties of objects.

It makes building interactive graphical user interfaces much easier than working directly with the widgets.

This page is nothing but a short introduction. An step-by-step tutorial on building an interactive scientific application with traitsUI is available at: http://gael-varoquaux.info/computers/traits_tutorial/index.html  .

The configure_traits dialog
===========================

A "traited" object is an object whose attributes have been specified beforehand.

::

   from enthought.traits.api import Str, Int, HasTraits
   class Person(HasTraits):
       age = Int
       name = Str

The "HasTrait" metaclass will not allow new attributes to be added to the object, and it will check that the values the attributes are set to correspond to the object's definition.

::

   >>> joe = Person()
   >>> joe.name = "joe"
   >>> joe.age = "1"
   Traceback (most recent call last):
     File "<stdin>", line 1, in ?
     File "/usr/local/lib/python2.4/site-packages/enthought/traits/trait_handlers.py", line 171, in error
       raise TraitError, ( object, name, self.info(), value )
   enthought.traits.trait_errors.TraitError: The 'age' trait of a Person instance must be a value of type 'int', but a value of 1 was specified.

A traited object has a method that can display a dialog to edit its attributes:

::

   >>> joe.configure_traits()

attachment:configure_traits.png

Interactive dialogs
===================

The "configure_traits" method does not fit in a larger UI, it creates a UI, with its event-loop, and closes it once the dialog is closed. It fits in purely sequential batch programming.

Using a few simple modification notifications makes the application interactive:

::

   from enthought.traits.api import Str, Float, HasTraits
   class UnitConverter(HasTraits):
       pounds = Float(0, desc="Weight in pounds")
       kilogrammes  = Float(0, desc="Weight in kilogrammes")
       def _pounds_changed(self, value):
           self.kilogrammes = value/2.2
       def _kilogrammes_changed(self, value):
           self.pounds = value*2.2
   UnitConverter().configure_traits()

attachment:unit_converter.png

An "edit_traits" method is available to create a dialog that will be part of the WxPython event-loop. You can use it in "ipython -wthread", that has the WxPython loop running, or in a larger WxPython  application. The tutorial shows how to integrate traits and matplotlib plots. [:EmbeddingInTraitsGUI:Here's] another recipe for embedding a matplotlib figure in a TraitsUI app.

The examples shown here are very basic, but the traits module provides many more tools and features that help building a fully-fledged application for scientific purposes.

.. ############################################################################

.. _WxPython: ../WxPython

