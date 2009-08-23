#format rst

<div class="section" id="abstract">
<h3>Abstract</h3>
<p>When building numpy and scipy, we are limited to a quite restricted set of
warning compilers, thus missing a large class of potential bugs which could
bedetected with stronger warning flags. The goal of this PEP is to clean the
code and implements some policy to have a warning free numpy and scipy build</p>
</div>
<div class="section" id="warning-flags">
<h3>Warning flags</h3>
<p>Each compiler detects a diffferent set of potential errors. The reference
will be gcc -Wall -W -Wextra. Ideally, a complete set would be nice:</p>
<p>-W -Wall -Wextra -Wstrict-prototypes -Wmissing-prototypes -Waggregate-return
-Wcast-align -Wcast-qual -Wnested-externs -Wshadow -Wbad-function-cast
-Wwrite-strings</p>
<p>Intel compiler, VS with /W3 /Wall, Sun compilers have extra warnings too.</p>
</div>
<div class="section" id="kind-of-warnings">
<h3>Kind of warnings</h3>
<p>C Python extension code tends to naturally generate a lot of spurious
warnings. The goal is to have some facilities to tag some typical C-Python
code so that the compilers do not generate warnings; the tag process has to
be clean, readable, and be robust.</p>
<div class="section" id="unused-parameter">
<h4>unused parameter</h4>
<p>This one appears often: any python-callable C function takes two arguments,
of which the first is not used for functions (only for methods). One way to
solve it is to tag the function argument with a macro NPY_UNUSED. This macro
uses compiler specific code to tag the variable, and mangle it such as it is
not possible to use it accidentally once it is tagged.</p>
<p>The code to apply compiler specific option could be:</p>
<dt>#if defined(__GNUC__)</dt>
<dd>#define __COMP_NPY_UNUSED __attribute__ ((__unused__))</dd>
<dt># elif defined(__ICC)</dt>
<dd>#define __COMP_NPY_UNUSED __attribute__ ((__unused__))</dd>
<dt>#else</dt>
<dd>#define __COMP_NPY_UNUSED</dd>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">&lt;string&gt;</tt>, line 46)</p>
Definition list ends without a blank line; unexpected unindent.</div>
<p>#endif</p>
<p>The variable mangling would be:</p>
<p>#define NPY_UNUSED(x) (__NPY_UNUSED_TAGGED ## x) __COMP_NPY_UNUSED</p>
<p>When applied to a variable, one would get:</p>
<p>int foo(int * NPY_UNUSED(dummy))</p>
<p>expanded to</p>
<p>int foo(int * __NPY_UNUSED_TAGGEDdummy __COMP_NPY_UNUSED)</p>
</div>
<div class="section" id="signed-unsigned-comparison">
<h4>signed/unsigned comparison</h4>
<p>More tricky: not always clear what to do</p>
</div>
<div class="section" id="half-initialized-structures">
<h4>half-initialized structures</h4>
<p>Just put the elements with NULL in it.
&quot;warnfix_pep.txt&quot; 68L, 2125C written</p>
</div>
</div>
-------------------------

 ProposedEnhancements_

.. ############################################################################

.. _ProposedEnhancements: ../ProposedEnhancements

