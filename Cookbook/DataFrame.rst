#format rst

Data Frames
===========

The attachment:DataFrame.py class, posted by Andrew Straw on the scipy-user mailing list[ http://thread.gmane.org/gmane.comp.python.scientific.user/6860 , original link], is an extremely useful tool for using alphanumerical tabular data, as often found in databases. Some data which might be ingested into a data frame could be:

[Table not converted]

The attachment:DataFrame.py class can be populated from data from a CSV file (comman-separated values). In its current implementation, these files are read with Python's own CSV module, which allows for a great deal of customisation.

Example Usage
-------------

A sample file CSV file from Access2000 is in attachment:CSVSample.csv .  We first import the module:

::

   import DataFrame

and read the file in using our desired CVS dialect:

::

   df=DataFrame.read_csv ("CSVSample.csv",dialect=DataFrame.access2000)

(note that the dialect is actually defined in the DataFrame class). It is often useful to filter the data according to some criterion.

-------------------------



  CategoryCookbook

