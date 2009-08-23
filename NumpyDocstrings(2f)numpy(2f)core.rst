#format rst

<p>Defines a multi-dimensional array and useful procedures for Numerical computation.</p>
<div class="section" id="functions">
<h3>Functions</h3>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field"><th class="field-name">array:</th><td class="field-body">NumPy Array construction</td>
</tr>
<tr class="field"><th class="field-name">zeros:</th><td class="field-body">Return an array of all zeros</td>
</tr>
<tr class="field"><th class="field-name">empty:</th><td class="field-body">Return an unitialized array</td>
</tr>
<tr class="field"><th class="field-name">shape:</th><td class="field-body">Return shape of sequence or array</td>
</tr>
<tr class="field"><th class="field-name">rank:</th><td class="field-body">Return number of dimensions</td>
</tr>
<tr class="field"><th class="field-name">size:</th><td class="field-body">Return number of elements in entire array or a certain dimension</td>
</tr>
<tr class="field"><th class="field-name">fromstring:</th><td class="field-body">Construct array from (byte) string</td>
</tr>
<tr class="field"><th class="field-name">take:</th><td class="field-body">Select sub-arrays using sequence of indices</td>
</tr>
<tr class="field"><th class="field-name">put:</th><td class="field-body">Set sub-arrays using sequence of 1-D indices</td>
</tr>
<tr class="field"><th class="field-name">putmask:</th><td class="field-body">Set portion of arrays using a mask</td>
</tr>
<tr class="field"><th class="field-name">reshape:</th><td class="field-body">Return array with new shape</td>
</tr>
<tr class="field"><th class="field-name">repeat:</th><td class="field-body">Repeat elements of array</td>
</tr>
<tr class="field"><th class="field-name">choose:</th><td class="field-body">Construct new array from indexed array tuple</td>
</tr>
<tr class="field"><th class="field-name">correlate:</th><td class="field-body">Correlate two 1-d arrays</td>
</tr>
<tr class="field"><th class="field-name">searchsorted:</th><td class="field-body">Search for element in 1-d array</td>
</tr>
<tr class="field"><th class="field-name">sum:</th><td class="field-body">Total sum over a specified dimension</td>
</tr>
<tr class="field"><th class="field-name">average:</th><td class="field-body">Average, possibly weighted, over axis or array.</td>
</tr>
<tr class="field"><th class="field-name">cumsum:</th><td class="field-body">Cumulative sum over a specified dimension</td>
</tr>
<tr class="field"><th class="field-name">product:</th><td class="field-body">Total product over a specified dimension</td>
</tr>
<tr class="field"><th class="field-name">cumproduct:</th><td class="field-body">Cumulative product over a specified dimension</td>
</tr>
<tr class="field"><th class="field-name">alltrue:</th><td class="field-body">Logical and over an entire axis</td>
</tr>
<tr class="field"><th class="field-name">sometrue:</th><td class="field-body">Logical or over an entire axis</td>
</tr>
<tr class="field"><th class="field-name">allclose:</th><td class="field-body">Tests if sequences are essentially equal</td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="more-functions">
<h3>More Functions:</h3>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field"><th class="field-name">arange:</th><td class="field-body">Return regularly spaced array</td>
</tr>
<tr class="field"><th class="field-name">asarray:</th><td class="field-body">Guarantee NumPy array</td>
</tr>
<tr class="field"><th class="field-name">convolve:</th><td class="field-body">Convolve two 1-d arrays</td>
</tr>
<tr class="field"><th class="field-name">swapaxes:</th><td class="field-body">Exchange axes</td>
</tr>
<tr class="field"><th class="field-name">concatenate:</th><td class="field-body">Join arrays together</td>
</tr>
<tr class="field"><th class="field-name">transpose:</th><td class="field-body">Permute axes</td>
</tr>
<tr class="field"><th class="field-name">sort:</th><td class="field-body">Sort elements of array</td>
</tr>
<tr class="field"><th class="field-name">argsort:</th><td class="field-body">Indices of sorted array</td>
</tr>
<tr class="field"><th class="field-name">argmax:</th><td class="field-body">Index of largest value</td>
</tr>
<tr class="field"><th class="field-name">argmin:</th><td class="field-body">Index of smallest value</td>
</tr>
<tr class="field"><th class="field-name">inner:</th><td class="field-body">Innerproduct of two arrays</td>
</tr>
<tr class="field"><th class="field-name">dot:</th><td class="field-body">Dot product (matrix multiplication)</td>
</tr>
<tr class="field"><th class="field-name">outer:</th><td class="field-body">Outerproduct of two arrays</td>
</tr>
<tr class="field"><th class="field-name">resize:</th><td class="field-body">Return array with arbitrary new shape</td>
</tr>
<tr class="field"><th class="field-name">indices:</th><td class="field-body">Tuple of indices</td>
</tr>
<tr class="field"><th class="field-name">fromfunction:</th><td class="field-body">Construct array from universal function</td>
</tr>
<tr class="field"><th class="field-name">diagonal:</th><td class="field-body">Return diagonal array</td>
</tr>
<tr class="field"><th class="field-name">trace:</th><td class="field-body">Trace of array</td>
</tr>
<tr class="field"><th class="field-name">dump:</th><td class="field-body">Dump array to file object (pickle)</td>
</tr>
<tr class="field"><th class="field-name">dumps:</th><td class="field-body">Return pickled string representing data</td>
</tr>
<tr class="field"><th class="field-name">load:</th><td class="field-body">Return array stored in file object</td>
</tr>
<tr class="field"><th class="field-name">loads:</th><td class="field-body">Return array from pickled string</td>
</tr>
<tr class="field"><th class="field-name">ravel:</th><td class="field-body">Return array as 1-D</td>
</tr>
<tr class="field"><th class="field-name">nonzero:</th><td class="field-body">Indices of nonzero elements for 1-D array</td>
</tr>
<tr class="field"><th class="field-name">shape:</th><td class="field-body">Shape of array</td>
</tr>
<tr class="field"><th class="field-name">where:</th><td class="field-body">Construct array from binary result</td>
</tr>
<tr class="field"><th class="field-name">compress:</th><td class="field-body">Elements of array where condition is true</td>
</tr>
<tr class="field"><th class="field-name">clip:</th><td class="field-body">Clip array between two values</td>
</tr>
<tr class="field"><th class="field-name">ones:</th><td class="field-body">Array of all ones</td>
</tr>
<tr class="field"><th class="field-name">identity:</th><td class="field-body">2-D identity array (matrix)</td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="universal-math-functions">
<h3>(Universal) Math Functions</h3>
::

add                    logical_or             exp
subtract               logical_xor            log
multiply               logical_not            log10
divide                 maximum                sin
divide_safe            minimum                sinh
conjugate              bitwise_and            sqrt
power                  bitwise_or             tan
absolute               bitwise_xor            tanh
negative               invert                 ceil
greater                left_shift             fabs
greater_equal          right_shift            floor
less                   arccos                 arctan2
less_equal             arcsin                 fmod
equal                  arctan                 hypot
not_equal              cos                    around
logical_and            cosh                   sign
arccosh                arcsinh                arctanh</div>
