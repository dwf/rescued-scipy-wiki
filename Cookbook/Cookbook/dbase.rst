#format rst

Update - 1/18/2007
==================

* Added a function to convert a data-dictionary to a rec-array (Pierre GM).

Update - 1/14/2007
==================

* Replaces missing values with 'nan'

* Loads non-numeric data from csv

Dbase
=====

The [attachment:dbase.0.7.py dbase.py] class, can be used to read/write/summarize/plot time-series data.

To summarize the functionality:

1. data and variable names stored in a dictionary - accessible using variable names

#. load/save from/to csv/pickle format, including date information (shelve format to be added)

#. plotting and descriptive statistics, with dates if provided

#. adding/deleting variables, including trends/(seasonal)dummies

#. selecting observations based on dates or other variable values (e.g., > 1/1/2003)

#. copying instance data

Attached also the [attachment:dbase_pydoc.0.2.txt dbase_pydoc.txt] information for the class.

Example Usage
-------------

To see the class in action download the file and run it (python dbase.py). This will create an example data file (./dbase_test_files/data.csv) that will be processed by the class.

To import the module:

::

   import dbase

After running the class you can load the example data using

::

   data = dbase.dbase("./dbase_test_files/data.csv", date = 0)

In the above command '0' is the index of the column containing dates.

You can plot series 'b' and 'c' in the file using

::

   data.dataplot('b','c')

attachment:ex_plot.0.1.png

You get descriptive statistics for series 'a','b', and 'c' by using

::

   data.info('a','b','c')

Since there is date information in [attachment:data.0.3.csv data.csv] this information will be added automatically when calling dataplot() or info().

There is an extensive set of examples at the bottom of the code file that demonstrates the functionality of the class.

-------------------------

 CategoryCookbook_

