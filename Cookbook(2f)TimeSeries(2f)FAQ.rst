#format rst

**Recipies and FAQ for the Timeseries Scikit**

`TableOfContents(4)`_

NOTE: The official documentation and important remarks from the developers can be found at the [`http://pytseries.sourceforge.net`_ timseries scikit sourceforge page].

FAQ
===

General threads
---------------

1. time series analysis - `http://article.gmane.org/gmane.comp.python.scientific.user/13949`_

#. time series: Python vs. R URL missing!!!

#. roadmap/plans for timeseries package -  `http://permalink.gmane.org/gmane.comp.python.scientific.user/14599`_

Reading data and creating timeseries objects
--------------------------------------------

masking NoData values
~~~~~~~~~~~~~~~~~~~~~

Question
::::::::

In my original data nodata values are marked with "-999". How can I import the data or create the time series and exclude these no  data points from further processing? (flagging no data in timeseries  - `http://permalink.gmane.org/gmane.comp.python.scientific.user/14455`_)

Answer
::::::

* use masked_where from maskedarray

::

   myvalues_ts_hourly = masked_where(myvalues_ts_hourly , -999)

* Use indexing

::

   myvalues_ts_hourly[myvalues_ts_hourly==-999] = M.masked

More extensive answer
:::::::::::::::::::::

*** START SAMPLE DATA (tmp.txt) ***

