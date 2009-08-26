#format rst
## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
## master-page:WikiSandBox

`FullSearch(CategoryCategory)`_ **Feel free to experiment here, after the four dashes below. Please do not create new pages without any meaningful content just to try it out!**

**Tip:** Shift-click "HelpOnEditing_" to open a second window with the help pages.

-------------------------



Formatting
----------

*italic* **bold** ``typewriter``

``backtick typewriter`` (configurable)

:big:`bigger`  :small:`smaller`

::

   preformatted some more
   and some more lines too

::

   def syntax(highlight):
       print "on"
       return None

`Anchor(anchorup)`_

How to disable line numbers
:::::::::::::::::::::::::::

`Anchor(anchordown)`_

::

   >>> from numpy import *
   >>> a = arange(12)
   >>> a = a.reshape(3,2,2)
   >>> print a
   [[[ 0  1]
     [ 2  3]]
    [[ 4  5]
     [ 6  7]]
    [[ 8  9]
     [10 11]]]
   >>> a[...,0]                               # same as a[:,:,0]
   array([[ 0,  2],
          [ 4,  6],
          [ 8, 10]])
   >>> a[1:,...]                              # same as a[1:,:,:]
   array([[[ 4,  5],
           [ 6,  7]],
          [[ 8,  9],
           [10, 11]]])

::

     public void main(String[] args]){
        System.out.println("Hello world!");
     }

