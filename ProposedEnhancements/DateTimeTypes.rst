#format rst

.. raw:: html
   <h1>A (third) proposal for implementing some date/time types in NumPy</h1>


<table class="docinfo" frame="void" rules="none">
<col class="docinfo-name" />
<col class="docinfo-content" />
<tbody valign="top">
<tr><th class="docinfo-name">Author:</th>
<td>Francesc Alted i Abad</td></tr>
<tr><th class="docinfo-name">Contact:</th>
<td><a class="first last mailto reference external" href="mailto:faltet&#64;pytables.com">faltet&#64;pytables.com</a></td></tr>
<tr><th class="docinfo-name">Author:</th>
<td>Ivan Vilata i Balaguer</td></tr>
<tr><th class="docinfo-name">Contact:</th>
<td><a class="first last mailto reference external" href="mailto:ivan&#64;selidor.net">ivan&#64;selidor.net</a></td></tr>
<tr><th class="docinfo-name">Date:</th>
<td>2008-07-30</td></tr>
</tbody>
</table>

<div class="section" id="executive-summary">
<h3>Executive summary</h3>
<p>A date/time mark is something very handy to have in many fields where
one has to deal with data sets.  While Python has several modules that
define a date/time type (like the integrated datetime <a class="footnote-reference" href="#id10" id="id1">[1]</a> or
mx.DateTime <a class="footnote-reference" href="#id11" id="id2">[2]</a>), NumPy has a lack of them.</p>
<p>In this document, we are proposing the addition of a series of date/time
types to fill this gap.  The requirements for the proposed types are
two-folded: 1) they have to be fast to operate with and 2) they have to
be as compatible as possible with the existing datetime module that
comes with Python.</p>
</div>
<div class="section" id="types-proposed">
<h3>Types proposed</h3>
<p>To start with, it is virtually impossible to come up with a single
date/time type that fills the needs of every case of use.  So, after
pondering about different possibilities, we have stuck with two
different types, namely datetime64 and timedelta64 (these names
are preliminary and can be changed), that can have different time units
so as to cover different needs.</p>
<div class="important">
<p class="first admonition-title">Important</p>
<p class="last">the time unit is conceived here as metadata that
complements a date/time dtype, without changing the base type.  It
provides information about the meaning of the stored numbers, not
about their structure.</p>
</div>
<p>Now follows a detailed description of the proposed types.</p>
<div class="section" id="datetime64">
<h4>datetime64</h4>
<p>It represents a time that is absolute (i.e. not relative).  It is
implemented internally as an int64 type.  The internal epoch is the
POSIX epoch (see <a class="footnote-reference" href="#id12" id="id3">[3]</a>).  Like POSIX, the representation of a date
doesn't take leap seconds into account.</p>
<p>In time unit conversions and time representations (but not in other
time computations), the value -2**63 (0x8000000000000000) is interpreted
as an invalid or unknown date, Not a Time or NaT.  See the section
on time unit conversions for more information.</p>
<div class="section" id="time-units">
<h5>Time units</h5>
<p>It accepts different time units, each of them implying a different time
span.  The table below describes the time units supported with their
corresponding time spans.</p>
<table border="1" class="docutils">
<colgroup>
<col width="16%" />
<col width="32%" />
<col width="52%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head" colspan="2">Time unit</th>
<th class="head">Time span (years)</th>
</tr>
<tr><th class="head">Code</th>
<th class="head">Meaning</th>
<th class="head">&nbsp;</th>
</tr>
</thead>
<tbody valign="top">
<tr><td>Y</td>
<td>year</td>
<td>[9.2e18 BC, 9.2e18 AC]</td>
</tr>
<tr><td>M</td>
<td>month</td>
<td>[7.6e17 BC, 7.6e17 AC]</td>
</tr>
<tr><td>W</td>
<td>week</td>
<td>[1.7e17 BC, 1.7e17 AC]</td>
</tr>
<tr><td>B</td>
<td>business day</td>
<td>[3.5e16 BC, 3.5e16 AC]</td>
</tr>
<tr><td>D</td>
<td>day</td>
<td>[2.5e16 BC, 2.5e16 AC]</td>
</tr>
<tr><td>h</td>
<td>hour</td>
<td>[1.0e15 BC, 1.0e15 AC]</td>
</tr>
<tr><td>m</td>
<td>minute</td>
<td>[1.7e13 BC, 1.7e13 AC]</td>
</tr>
<tr><td>s</td>
<td>second</td>
<td>[ 2.9e9 BC,  2.9e9 AC]</td>
</tr>
<tr><td>ms</td>
<td>millisecond</td>
<td>[ 2.9e6 BC,  2.9e6 AC]</td>
</tr>
<tr><td>us</td>
<td>microsecond</td>
<td>[290301 BC, 294241 AC]</td>
</tr>
<tr><td>ns</td>
<td>nanosecond</td>
<td>[  1678 AC,   2262 AC]</td>
</tr>
</tbody>
</table>
<p>The value of an absolute date is thus an integer number of units of the
chosen time unit passed since the internal epoch.  When working with
business days, Saturdays and Sundays are simply ignored from the count
(i.e. day 3 in business days is not Saturday 1970-01-03, but Monday
1970-01-05).</p>
</div>
<div class="section" id="building-a-datetime64-dtype">
<h5>Building a datetime64 dtype</h5>
<p>The proposed ways to specify the time unit in the dtype constructor are:</p>
<p>Using the long string notation:</p>
::

dtype('datetime64[us]')<p>Using the short string notation:</p>
::

dtype('T8[us]')<p>Note that a time unit should always be specified, as there is not a
default.</p>
</div>
<div class="section" id="setting-and-getting-values">
<h5>Setting and getting values</h5>
<p>The objects with this dtype can be set in a series of ways:</p>
::

t = numpy.ones(3, dtype='T8[s]')
t[0] = 1199164176    # assign to July 30th, 2008 at 17:31:00
t[1] = datetime.datetime(2008, 7, 30, 17, 31, 01) # with datetime<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">&lt;string&gt;</tt>, line 114)</p>
Literal block ends without a blank line; unexpected unindent.</div>
<dt>module</dt>
<dd>t[2] = '2008-07-30T17:31:02'    # with ISO 8601</dd>
<p>And can be get in different ways too:</p>
::

str(t[0])  --&gt;  2008-07-30T17:31:00
repr(t[1]) --&gt;  datetime64(1199164177, 's')
str(t[0].item()) --&gt; 2008-07-30 17:31:00  # datetime module object
repr(t[0].item()) --&gt; datetime.datetime(2008, 7, 30, 17, 31)  # idem
str(t)  --&gt;  [2008-07-30T17:31:00  2008-07-30T17:31:01<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">&lt;string&gt;</tt>, line 124)</p>
Literal block ends without a blank line; unexpected unindent.</div>
<dt>2008-07-30T17:31:02]</dt>
<dd><dt>repr(t)  --&gt;  array([1199164176, 1199164177, 1199164178],</dt>
<dd>dtype='datetime64[s]')</dd>
</dd>
</div>
<div class="section" id="comparisons">
<h5>Comparisons</h5>
<p>The comparisons will be supported too:</p>
::

numpy.array(['1980'], 'T8[Y]') == numpy.array(['1979'], 'T8[Y]')
--&gt; [False]<p>or by applying broadcasting:</p>
::

numpy.array(['1979', '1980'], 'T8[Y]') == numpy.datetime64<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">&lt;string&gt;</tt>, line 139)</p>
Literal block ends without a blank line; unexpected unindent.</div>
<dt>('1980', 'Y')</dt>
<dd>--&gt; [False, True]</dd>
<p>The next should work too:</p>
::

numpy.array(['1979', '1980'], 'T8[Y]') == '1980-01-01'
--&gt; [False, True]<p>because the right hand expression can be broadcasted into an array of 2
elements of dtype 'T8[Y]'.</p>
</div>
<div class="section" id="compatibility-issues">
<h5>Compatibility issues</h5>
<p>This will be fully compatible with the datetime class of the
datetime module of Python only when using a time unit of
microseconds.  For other time units, the conversion process will loose
precision or will overflow as needed.  The conversion from/to a
datetime object doesn't take leap seconds into account.</p>
</div>
</div>
<div class="section" id="timedelta64">
<h4>timedelta64</h4>
<p>It represents a time that is relative (i.e. not absolute).  It is
implemented internally as an int64 type.</p>
<p>In time unit conversions and time representations (but not in other
time computations), the value -2**63 (0x8000000000000000) is interpreted
as an invalid or unknown time, Not a Time or NaT.  See the section
on time unit conversions for more information.</p>
<div class="section" id="id4">
<h5>Time units</h5>
<p>It accepts different time units, each of them implying a different time
span.  The table below describes the time units supported with their
corresponding time spans.</p>
<table border="1" class="docutils">
<colgroup>
<col width="16%" />
<col width="32%" />
<col width="52%" />
</colgroup>
<thead valign="bottom">
<tr><th class="head" colspan="2">Time unit</th>
<th class="head">Time span</th>
</tr>
<tr><th class="head">Code</th>
<th class="head">Meaning</th>
<th class="head">&nbsp;</th>
</tr>
</thead>
<tbody valign="top">
<tr><td>Y</td>
<td>year</td>
<td>+- 9.2e18 years</td>
</tr>
<tr><td>M</td>
<td>month</td>
<td>+- 7.6e17 years</td>
</tr>
<tr><td>W</td>
<td>week</td>
<td>+- 1.7e17 years</td>
</tr>
<tr><td>B</td>
<td>business day</td>
<td>+- 3.5e16 years</td>
</tr>
<tr><td>D</td>
<td>day</td>
<td>+- 2.5e16 years</td>
</tr>
<tr><td>h</td>
<td>hour</td>
<td>+- 1.0e15 years</td>
</tr>
<tr><td>m</td>
<td>minute</td>
<td>+- 1.7e13 years</td>
</tr>
<tr><td>s</td>
<td>second</td>
<td>+- 2.9e12 years</td>
</tr>
<tr><td>ms</td>
<td>millisecond</td>
<td>+- 2.9e9 years</td>
</tr>
<tr><td>us</td>
<td>microsecond</td>
<td>+- 2.9e6 years</td>
</tr>
<tr><td>ns</td>
<td>nanosecond</td>
<td>+- 292 years</td>
</tr>
<tr><td>ps</td>
<td>picosecond</td>
<td>+- 106 days</td>
</tr>
<tr><td>fs</td>
<td>femtosecond</td>
<td>+- 2.6 hours</td>
</tr>
<tr><td>as</td>
<td>attosecond</td>
<td>+- 9.2 seconds</td>
</tr>
</tbody>
</table>
<p>The value of a time delta is thus an integer number of units of the
chosen time unit.</p>
</div>
<div class="section" id="building-a-timedelta64-dtype">
<h5>Building a timedelta64 dtype</h5>
<p>The proposed ways to specify the time unit in the dtype constructor are:</p>
<p>Using the long string notation:</p>
::

dtype('timedelta64[us]')<p>Using the short string notation:</p>
::

dtype('t8[us]')<p>Note that a time unit should always be specified, as there is not a
default.</p>
</div>
<div class="section" id="id5">
<h5>Setting and getting values</h5>
<p>The objects with this dtype can be set in a series of ways:</p>
::

t = numpy.ones(3, dtype='t8[ms]')
t[0] = 12    # assign to 12 ms
t[1] = datetime.timedelta(0, 0, 13000)   # 13 ms
t[2] = '0:00:00.014'    # 14 ms<p>And can be get in different ways too:</p>
::

str(t[0])  --&gt;  0:00:00.012
repr(t[1]) --&gt;  timedelta64(13, 'ms')
str(t[0].item()) --&gt; 0:00:00.012000   # datetime module object
repr(t[0].item()) --&gt; datetime.timedelta(0, 0, 12000)  # idem
str(t)     --&gt;  [0:00:00.012  0:00:00.014  0:00:00.014]
repr(t)    --&gt;  array([12, 13, 14], dtype=&quot;timedelta64[ms]&quot;)</div>
<div class="section" id="id6">
<h5>Comparisons</h5>
<p>The comparisons will be supported too:</p>
::

numpy.array([12, 13, 14], 't8[ms]') == numpy.array([12, 13, 13], 't8<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">&lt;string&gt;</tt>, line 243)</p>
Literal block ends without a blank line; unexpected unindent.</div>
<dt>[ms]')</dt>
<dd>--&gt; [True, True, False]</dd>
<p>or by applying broadcasting:</p>
::

numpy.array([12, 13, 14], 't8[ms]') == numpy.timedelta64(13, 'ms')
--&gt; [False, True, False]<p>The next should work too:</p>
::

numpy.array([12, 13, 14], 't8[ms]') == '0:00:00.012'
--&gt; [True, False, False]<p>because the right hand expression can be broadcasted into an array of 3
elements of dtype 't8[ms]'.</p>
</div>
<div class="section" id="id7">
<h5>Compatibility issues</h5>
<p>This will be fully compatible with the timedelta class of the
datetime module of Python only when using a time unit of
microseconds.  For other units, the conversion process will loose
precision or will overflow as needed.</p>
</div>
</div>
</div>
<div class="section" id="examples-of-use">
<h3>Examples of use</h3>
<p>Here it is an example of use for the datetime64:</p>
::

In [5]: numpy.datetime64(42, 'us')
Out[5]: datetime64(42, 'us')

In [6]: print numpy.datetime64(42, 'us')
1970-01-01T00:00:00.000042  # representation in ISO 8601 format

In [7]: print numpy.datetime64(367.7, 'D')  # decimal part is lost
1971-01-02  # still ISO 8601 format

In [8]: numpy.datetime('2008-07-18T12:23:18', 'm')  # from ISO 8601
Out[8]: datetime64(20273063, 'm')

In [9]: print numpy.datetime('2008-07-18T12:23:18', 'm')
Out[9]: 2008-07-18T12:23

In [10]: t = numpy.zeros(5, dtype=&quot;datetime64[ms]&quot;)

In [11]: t[0] = datetime.datetime.now()  # setter in action

In [12]: print t
[2008-07-16T13:39:25.315  1970-01-01T00:00:00.000
 1970-01-01T00:00:00.000  1970-01-01T00:00:00.000
 1970-01-01T00:00:00.000]

In [13]: repr(t)
Out[13]: array([267859210457, 0, 0, 0, 0], dtype=&quot;datetime64[ms]&quot;)

In [14]: t[0].item()     # getter in action
Out[14]: datetime.datetime(2008, 7, 16, 13, 39, 25, 315000)

In [15]: print t.dtype
dtype('datetime64[ms]')<p>And here it goes an example of use for the timedelta64:</p>
::

In [5]: numpy.timedelta64(10, 'us')
Out[5]: timedelta64(10, 'us')

In [6]: print numpy.timedelta64(10, 'us')
0:00:00.000010

In [7]: print numpy.timedelta64(3600.2, 'm')  # decimal part is lost
2 days, 12:00

In [8]: t1 = numpy.zeros(5, dtype=&quot;datetime64[ms]&quot;)

In [9]: t2 = numpy.ones(5, dtype=&quot;datetime64[ms]&quot;)

In [10]: t = t2 - t1

In [11]: t[0] = datetime.timedelta(0, 24)  # setter in action

In [12]: print t
[0:00:24.000  0:00:01.000  0:00:01.000  0:00:01.000  0:00:01.000]

In [13]: print repr(t)
Out[13]: array([24000, 1, 1, 1, 1], dtype=&quot;timedelta64[ms]&quot;)

In [14]: t[0].item()     # getter in action
Out[14]: datetime.timedelta(0, 24)

In [15]: print t.dtype
dtype('timedelta64[s]')</div>
<div class="section" id="operating-with-date-time-arrays">
<h3>Operating with date/time arrays</h3>
<div class="section" id="datetime64-vs-datetime64">
<h4>datetime64 vs datetime64</h4>
<p>The only arithmetic operation allowed between absolute dates is the
subtraction:</p>
::

In [10]: numpy.ones(3, &quot;T8[s]&quot;) - numpy.zeros(3, &quot;T8[s]&quot;)
Out[10]: array([1, 1, 1], dtype=timedelta64[s])<p>But not other operations:</p>
::

In [11]: numpy.ones(3, &quot;T8[s]&quot;) + numpy.zeros(3, &quot;T8[s]&quot;)
TypeError: unsupported operand type(s) for +: 'numpy.ndarray'<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">&lt;string&gt;</tt>, line 354)</p>
Literal block ends without a blank line; unexpected unindent.</div>
<p>and 'numpy.ndarray'</p>
<p>Comparisons between absolute dates are allowed.</p>
<div class="section" id="casting-rules">
<h5>Casting rules</h5>
<p>When operating (basically, only the subtraction will be allowed) two
absolute times with different unit times, the outcome would be to raise
an exception.  This is because the ranges and time-spans of the
different
time units can be very different, and it is not clear at all what time
unit will be preferred for the user.  For example, this should be
allowed:</p>
::

&gt;&gt;&gt; numpy.ones(3, dtype=&quot;T8[Y]&quot;) - numpy.zeros(3, dtype=&quot;T8[Y]&quot;)
array([1, 1, 1], dtype=&quot;timedelta64[Y]&quot;)<p>But the next should not:</p>
::

&gt;&gt;&gt; numpy.ones(3, dtype=&quot;T8[Y]&quot;) - numpy.zeros(3, dtype=&quot;T8[ns]&quot;)
raise numpy.IncompatibleUnitError  # what unit to choose?</div>
</div>
<div class="section" id="datetime64-vs-timedelta64">
<h4>datetime64 vs timedelta64</h4>
<p>It will be possible to add and subtract relative times from absolute
dates:</p>
::

In [10]: numpy.zeros(5, &quot;T8[Y]&quot;) + numpy.ones(5, &quot;t8[Y]&quot;)
Out[10]: array([1971, 1971, 1971, 1971, 1971], dtype=datetime64[Y])

In [11]: numpy.ones(5, &quot;T8[Y]&quot;) - 2 * numpy.ones(5, &quot;t8[Y]&quot;)
Out[11]: array([1969, 1969, 1969, 1969, 1969], dtype=datetime64[Y])<p>But not other operations:</p>
::

In [12]: numpy.ones(5, &quot;T8[Y]&quot;) * numpy.ones(5, &quot;t8[Y]&quot;)
TypeError: unsupported operand type(s) for *: 'numpy.ndarray'<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">&lt;string&gt;</tt>, line 394)</p>
Literal block ends without a blank line; unexpected unindent.</div>
<p>and 'numpy.ndarray'</p>
<div class="section" id="id8">
<h5>Casting rules</h5>
<p>In this case the absolute time should have priority for determining the
time unit of the outcome.  That would represent what the people wants to
do most of the times.  For example, this would allow to do:</p>
::

&gt;&gt;&gt; series = numpy.array(['1970-01-01', '1970-02-01', '1970-09-01'],
dtype='datetime64[D]')
&gt;&gt;&gt; series2 = series + numpy.timedelta(1, 'Y')  # Add 2 relative years
&gt;&gt;&gt; series2
array(['1972-01-01', '1972-02-01', '1972-09-01'],
dtype='datetime64[D]')  # the 'D'ay time unit has been chosen</div>
</div>
<div class="section" id="timedelta64-vs-timedelta64">
<h4>timedelta64 vs timedelta64</h4>
<p>Finally, it will be possible to operate with relative times as if they
were regular int64 dtypes as long as the result can be converted back
into a timedelta64:</p>
::

In [10]: numpy.ones(3, 't8[us]')
Out[10]: array([1, 1, 1], dtype=&quot;timedelta64[us]&quot;)

In [11]: (numpy.ones(3, 't8[M]') + 2) ** 3
Out[11]: array([27, 27, 27], dtype=&quot;timedelta64[M]&quot;)<p>But:</p>
::

In [12]: numpy.ones(5, 't8') + 1j
TypeError: the result cannot be converted into a ``timedelta64``<div class="section" id="id9">
<h5>Casting rules</h5>
<p>When combining two timedelta64 dtypes with different time units the
outcome will be the shorter of both (&quot;keep the precision&quot; rule).  For
example:</p>
::

In [10]: numpy.ones(3, 't8[s]') + numpy.ones(3, 't8[m]')
Out[10]: array([61, 61, 61],  dtype=&quot;timedelta64[s]&quot;)<p>However, due to the impossibility to know the exact duration of a
relative year or a relative month, when these time units appear in one
of the operands, the operation will not be allowed:</p>
::

In [11]: numpy.ones(3, 't8[Y]') + numpy.ones(3, 't8[D]')
raise numpy.IncompatibleUnitError  # how to convert relative years to<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">&lt;string&gt;</tt>, line 445)</p>
Literal block ends without a blank line; unexpected unindent.</div>
<p>days?</p>
<p>In order to being able to perform the above operation a new NumPy
function, called change_timeunit is proposed.  Its signature will
be:</p>
::

change_timeunit(time_object, new_unit, reference)<p>where 'time_object' is the time object whose unit is to be changed,
'new_unit' is the desired new time unit, and 'reference' is an absolute
date (NumPy datetime64 scalar) that will be used to allow the conversion
of relative times in case of using time units with an uncertain number
of smaller time units (relative years or months cannot be expressed in
days).</p>
<p>With this, the above operation can be done as follows:</p>
::

In [10]: t_years = numpy.ones(3, 't8[Y]')

In [11]: t_days = numpy.change_timeunit(t_years, 'D', '2001-01-01')

In [12]: t_days + numpy.ones(3, 't8[D]')
Out[12]: array([366, 366, 366],  dtype=&quot;timedelta64[D]&quot;)</div>
</div>
</div>
<div class="section" id="dtype-vs-time-units-conversions">
<h3>dtype vs time units conversions</h3>
<p>For changing the date/time dtype of an existing array, we propose to use
the .astype() method.  This will be mainly useful for changing time
units.</p>
<p>For example, for absolute dates:</p>
::

In[10]: t1 = numpy.zeros(5, dtype=&quot;datetime64[s]&quot;)

In[11]: print t1
[1970-01-01T00:00:00  1970-01-01T00:00:00  1970-01-01T00:00:00
 1970-01-01T00:00:00  1970-01-01T00:00:00]

In[12]: print t1.astype('datetime64[D]')
[1970-01-01  1970-01-01  1970-01-01  1970-01-01  1970-01-01]<p>For relative times:</p>
::

In[10]: t1 = numpy.ones(5, dtype=&quot;timedelta64[s]&quot;)

In[11]: print t1
[1 1 1 1 1]

In[12]: print t1.astype('timedelta64[ms]')
[1000 1000 1000 1000 1000]<p>Changing directly from/to relative to/from absolute dtypes will not be
supported:</p>
::

In[13]: numpy.zeros(5, dtype=&quot;datetime64[s]&quot;).astype('timedelta64')
TypeError: data type cannot be converted to the desired type<p>Business days have the peculiarity that they do not cover a continuous
line of time (they have gaps at weekends).  Thus, when converting from
any ordinary time to business days, it can happen that the original time
is not representable.  In that case, the result of the conversion is
Not a Time (NaT):</p>
::

In[10]: t1 = numpy.arange(5, dtype=&quot;datetime64[D]&quot;)

In[11]: print t1
[1970-01-01  1970-01-02  1970-01-03  1970-01-04  1970-01-05]

In[12]: t2 = t1.astype(&quot;datetime64[B]&quot;)

In[13]: print t2  # 1970 begins in a Thursday
[1970-01-01  1970-01-02  NaT  NaT  1970-01-05]<p>When converting back to ordinary days, NaT values are left untouched
(this happens in all time unit conversions):</p>
::

In[14]: t3 = t2.astype(&quot;datetime64[D]&quot;)

In[13]: print t3
[1970-01-01  1970-01-02  NaT  NaT  1970-01-05]</div>
<div class="section" id="final-considerations">
<h3>Final considerations</h3>
<div class="section" id="why-the-origin-metadata-disappeared">
<h4>Why the origin metadata disappeared</h4>
<p>During the discussion of the date/time dtypes in the NumPy list, the
idea of having an origin metadata that complemented the definition
of the absolute datetime64 was initially found to be useful.</p>
<p>However, after thinking more about this, we found that the combination
of an absolute datetime64 with a relative timedelta64 does offer
the same functionality while removing the need for the additional
origin metadata.  This is why we have removed it from this proposal.</p>
</div>
<div class="section" id="operations-with-mixed-time-units">
<h4>Operations with mixed time units</h4>
<p>Whenever an operation between two time values of the same dtype with the
same unit is accepted, the same operation with time values of different
units should be possible (e.g. adding a time delta in seconds and one in
microseconds), resulting in an adequate time unit.  The exact semantics
of this kind of operations is defined int the &quot;Casting rules&quot;
subsections of the &quot;Operating with date/time arrays&quot; section.</p>
<p>Due to the peculiarities of business days, it is most probable that
operations mixing business days with other time units will not be
allowed.</p>
</div>
<div class="section" id="why-there-is-not-a-quarter-time-unit">
<h4>Why there is not a quarter time unit?</h4>
<p>This proposal tries to focus on the most common used set of time units
to operate with, and the quarter can be considered more of a derived
unit.  Besides, the use of a quarter normally requires that it can
start at whatever month of the year, and as we are not including support
for a time origin metadata, this is not a viable venue here.
Finally, if we were to add the quarter then people should expect to
find a biweekly, semester or biyearly just to put some
examples of other derived units, and we find this a bit too overwhelming
for this proposal purposes.</p>
<table class="docutils footnote" frame="void" id="id10" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id1">[1]</a></td><td><a class="http reference external" href="http://docs.python.org/lib/module-datetime.html">http://docs.python.org/lib/module-datetime.html</a></td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id11" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id2">[2]</a></td><td><a class="http reference external" href="http://www.egenix.com/products/python/mxBase/mxDateTime">http://www.egenix.com/products/python/mxBase/mxDateTime</a></td></tr>
</tbody>
</table>
<table class="docutils footnote" frame="void" id="id12" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id3">[3]</a></td><td><a class="http reference external" href="http://en.wikipedia.org/wiki/Unix_time">http://en.wikipedia.org/wiki/Unix_time</a></td></tr>
</tbody>
</table>
</div>
</div>
-------------------------

 ProposedEnhancements

