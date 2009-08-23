#format rst

Mlabwrap is a high-level python-to-matlab bridge. This wikipage is currently intended for developers and not for users. Please have a look at [`http://mlabwrap.sf.net`_ the sourceforge page] to get a quick overview.

Infrastructure
--------------

* code is [`https://projects.scipy.org/scipy/scikits/browser/trunk/mlabwrap`_ here] 

* use

  ::

     svn co http://scipy.org/svn/scikits/trunk/mlabwrap/

   to get the development version

* webpage is ??? (actually right [MlabWrap here] in all likelihood; this developer info will be moved)

* low-volume user mailing list specific to mlabwrap seems desirable (so keep `mlabwrap@sourceforge.net`_ for the time being)

* developer discussions on [projects.scipy.org/mailman/listinfo/scipy-dev scipy-dev] list; make sure ``subject:`` contains 'mlabwrap'

Design Goals
------------

Mlabwrap strives to 

1. be painless to install and use (and upgrade)

#. (where possible) come close to giving the user the impression to be using a python library rather than calling into a different language 

#. meet the needs of [`http://neuroimaging.scipy.org/`_ NIPY]

One reason for 2. (rather than say striving to emulate the look and feel of matlab as closely as possible) is that it should make it easier to gradually replace legacy matlab code with python code and for python (only) programmers to maintain and understand code that uses mlabwrap to leverage an existing matlab code base. The downside is that there is enough semantic difference between matlab and python (see below) to make this goal fully attainable -- trade-offs will have to be made.

I think it's therefore important that these trade-offs are informed by actual usage patterns, which is why 3. is likely to be vital for arriving at a good design; deriving things from first principles is unlikely to be an adequate substitute.

Principles
----------

* Design approach: First consider the most common use-cases and how they can be made most natural and convenient. Next consider if the contemplated solution results in any violations of intuitively expected behavior for edge cases, and how grave the violations are and whether they'll be detected and diagnosed immediately; violations of expected behavior that don't immediately result in an obvious error are to be avoided if at all possible.

* test-driven development or at least no code checkins without adding/running the necessary tests to/in ``test_mlabwrap.py``.

* root-of-all-evil: it looks like matlab's engine interface is inherently slow (FIXME elaborate), so there seems little point in complicating code with optimizations unless there is a clear demonstrated need for them. Getting the API design right should be the first priority.

Some concrete goals and plans for v. 1.0 and immediate future
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compatibility
:::::::::::::

* 1.0 version should retain compatibility to matlab > 5, python >= 2.3 and

    Numeric as well as numpy (don't break existing code with 1.0 release)

* future versions:

  * Numeric compatibility axed immediately after 1.0

  * compatibility to V >= 6.5 good enough (XXX: when did int types grow arithmetic)?

  * require python 2.5 (gives us relative imports, ctypes, with-statements)?

  * it will be necessary to keep open the option of incompatible interface changes, but newer versions of mlabwrap should offer a way to get old-style behavior (e.g. by using something like ``from mlabwrap.v1 import mlab`` instead of  ``from mlabwrap import mlab``)

  * Prescriptions for writing upward compatible code: always pass in ``float64`` arrays (rather than ``int*`` arrays) and don't use lists (which may convert to ``cell``s in future versions) if you want ``double``s in matlab.

Installation
::::::::::::

Painless Install:

* no setup.py editing required for common scenarios (*XXX* having to set ``LD_LIBRARY_PATH`` is kind of nasty, but I can't see a good way around this)

* no scipy dependency -- only external dependency should be numpy and matlab

* cheeseshop support would be nice (see open questions)

Limitations and issue with current design and implementation
------------------------------------------------------------

* ``mlabraw.cpp`` -- can we use ``ctypes`` instead? This could allow for faster development and easier experimentation and due to the high intrinsic overhead the involved speed-penality might not matter at all.

* no > 2D support and no proper ``cell``/``struct`` marshaling support (not a hard problem as such; but first one ought to see if migration to ctypes is feasible)

* Conversion behavior. When to proxy and how. When to offer the ability to select/fine-tune the default behavior, and how. 

* marshaling behavior (currently: all numeric dtypes to ``double``, all sequences to ``array``); handling of leading/trailing unit dimensions (e.g. ``_flatten_col_vecs`` and ``_flatten_row_vecs``)

* Proxy behavior: in particular

  * ``a.b.c = d`` *doesn't work as a typical user would expect*, although

      this is documented it might well bite unsuspecting users and is the main reason the hybrid-proxying scheme 2. (see below) makes a proxying for convertible types.

  * how should indexing work? 

  * how much should one make matlab containers look like python containers?

    * plain sequence protocol:

      * ``x[0]`` to ``x(1)``

      * ``x[-1]`` to ``x(end)``

      * ``x.flat[0]`` to ``x(1)``

      * ``len(x)`` to ``length(x)`` (or ``size(x,1)``? or ``size(x,2)``? or ``numel(x)``) ``length`` is nasty so ``size(x,1)`` would possibly be best

      * what about ``iter`` and ``in``?

    * 'pseudo-array' protocol

      * ``x[multidimensional_array]`` to ?

      * ``x.shape`` to ``size(x)`` (also ``ndim``, ``imag``, ``real``, ``conj``, ``T``,

          ``flat``, ``ravel``)

      Unfortunately ``ndarray`` is a bit bloated, but things that are ubiquitious in matlab, likely to be overloaded for many user-types and that have a clear ndarray equivalent presumably ought to work (e.g. ``shape``). But what to do about conflicting matlab object properties? Force people to use ``mlab.subsref(thing, substruct('.', 'shape'))``?

  * generally, to what extent should operator overloading work?

  * what about mixed (proxy-pythonobject) arithmetic?

  * how do we handle the intrinsic/extrinsic dimensionality impedence mismatch? Possible solutions include:

    * squeezing leading/trailing unit dimensions. Advantage: automatic and cheap; also applicable to marshaling. Difficulty: which one, leading or trailing? Whilst ``[[1]] -> 1`` will typically not cause issues (1x1 matrices are rare), 1 element vectors *do* commonly occur.

    * copy matlab's behavior (i.e. ``x[i]`` does flat indexing, ``x[i,j]`` treats x as a matrix)

    * inspecting ``size(x)`` on indexing ``x`` in order to compute the result dimensionality.

* Testing

  * mlabwrap 1.0 still depends on the obsolete netcdf package for some tests, but the current development version has already switched to a purpose-built ``@proxyTest`` matlab class

  * mlabwrap relies heavily on test driven development but the python standard library unittest is

    1. ill-suited for testing numpy code (because it doesn't provide sensible ways to compare numpy arrays for equality or similarity) and

    #. generally sup-optimal in not supporting interactive, test-driven development properly (during development I want to run tests in ipython and land in pdb when and where something fails, so I can quickly figure out what's going on; and after correcting the code somehow to address the test-failure I want to retry the failed test *first* and not wait for all the tests that precede it to complete).

    To address 1. ``test_mlabwrap.py`` contains some home-brew code to compare arrays, and to address 2. I've written a drop-in replacement for unittest that gets used when instead by test_mlabwrap if it is available.

    However numpy/scipy also contain their own test structure, so it would be good to convert to that and I think Taylor and Jarrod have already started the process. OTOH, from superficial inspections, whilst numpy.testing seems to address 1. it doesn't seem to address 2. -- but this is something I'd assume would be convenient for other people as well. Maybe there is a chance of getting something into numpy.testing? Or is what I'm looking for maybe even already available?

Differences between numpy and matlab that complicate bridging
-------------------------------------------------------------

more ops
  python lacks the following:

  * ``*``, ``/``, ``^`` (instead offering ``.*``, ``./``, ``.^``)

  * ``\``, ``.\``

  * ``'``, ``.'``

  * ``,``, ``;``

  * ``{}``, ``subsindex``

  * ``kron``

  * ``any`` ``all``

  * set ops: ``union`` (could use '|'), ``unique``, 'intersect' (could use

      '&'), 'setdiff' , 'setxor' , 'ismember' (could use ``in``, but there's a 3 argument version, too)

  * some bit-ops: ``bitget``, ``bitset``, the binary version of ``bitcmp``

  * size (could map to ``.shape``); not quite sure whether ``numel`` is somehow

      relevant for mlabwrap

fastest varying index
  matlab is column major, python is row major; apart from performance penalties when converting this also has implications for how data is preferentially arranged. This also interacts with dimensionality, see below. 

dimensionality
  I can think of two sane and internally consistent ways to handle array dimensionality:

  intrinsic dimensionality
    In numpy dimensionality is intrinsic to an array (e.g. ``a = array(1)`` has dimensionality, i.e. ``numpy.ndims(a)``, 0 and ``a[0,0,0,0]`` will throw an error). 

  sane context dependent dimensionality (scdd)
    In matlab dimensionality is context dependent (e.g. ``a=1; a(1,1,1,1)`` will work fine). A sane way to have done this would be to conceptualize everything as an array with an infinite number of leading (or trailing; if one desires column major) unit dimensions and determine the desired actual dimensionality by context (ignoring leading unit dimensions by default). In other words, under that scheme ``1, [1], [[1]], [[[1]]]`` are all the same object with the same physical representation and when context doesn't determine the dimensionality (e.g. the number of subscripts when indexing), one assumes by default the dimensionality of the arrays sans leading(/trailing) unit dimensions. The (IMO minor) advantage of this scheme is that it is sometimes convenient to regard on and the same object as e.g. a scalar or a 1x1 matrix, depending on context (as is often done in math). The (IMO major) disadvantage is that one looses the ability to regard arrays as nested container types (e.g. in numpy ``a[0]`` is legal and has an obvious meaning for any ``a`` with non-zero dimensions and it holds that ``ndims(a[0]) == ndims(a)-1``. But this equality doesn't hold in scdd and without some arbitrary convention (such as matlab's flat-indexing) ``a[0]`` is not even meaningful when there is more than one non-unit dimension).

  Of course matlab being matlab doesn't implement either of these schemes opting for something more messy instead: I *think* the idea basically is that everything is a matrix, unless it has too many (non-unit trailing) dimensions. As an example, in the 'sane context dependent dimensionality' scheme detailed above ``ndims(a)`` would be ``[]``; in matlab it is ``2``, as is ``ndims(ones(1,1,1))``, ``ndims(ones(2,1,1))``, but *not* ``ndims(ones(1,1,2))`` which is ``3``. Another annoyance is that matlab isn't really consistent in its column-major vantage point: flats (i.e. ``x(:)``) are column vectors, but very basic commands like ``linspace`` and the ``:`` operator return row vectors -- in other words, unlike in numpy there is no 'canonical' vector type; further complicating DWIM conversion attempts.

dereferencing, nullary-call and indexing

    Matlab doesn't syntactically distinguish between dereferencing a variable and calling a  nullary function -- ``a`` in matlab can mean ``a`` in python, or equally ``a()``. Similarly function      call and indexing are syntactically indistinguishable; ``a(1)`` could be either ``a(1)`` or ``a[0]``  in python. One issue where this comes up is determining how ``mlab.some_var`` ought to behave.

indexing and attribute access and modification


  `{}` vs `()`
    currently done with the ``_`` hack; *TODO* maybe add a way to associate ``x[key]`` with ``{}`` indexing when ``x`` belongs to certain set of classes.

  `subsref` and `subsasgn` are non-recursive
    By that I mean that whears in python (only) ``x.y' gets to handle the attribute access to`` z ``in`` x.y.z`, in matlab it's actually ``x``.  Python's behavior becomes an issue with the current (i.e. mlabwrap 1.0) scheme for assigning to.

  1-based indexing and `end` arithmetic
    (Aside ``end`` is pretty nasty; you'd think matlab might just call ``size`` to figure out the ``end`` for a given dimension, but not so, unless you define your own ``end`` method, it just silently uses '1', however *not* for the ``a(:)`` syntax, which one might erroneously assume to resolve to something like ``a(1:end)``. Interestingly although I know how to define an ``end`` method I haven't figured out how to *call* it directly...).

  strict slices (matlab) vs permissive ones (python)
    ``[][1:1000]`` will work fine in python (for arrays and lists), but *not* in matlab. Although it would be possible to try to hide this (e.g. by doing something like ``thing(min(slice_start,end),min(slice_end,end))``, it's presumably not worth the trouble.

dtypes
  Although matlab has ``logical`` (bool) ``{u,}int{8,16,32,64}`` as well as ``single``, ``double`` and ``char`` arrays and therefore a pretty good correspondence to the available numpy dtypes (apart from the fact that {single,double}-floats are conflated with {single,double}-complex floats), the mapping is complicated by the fact that ``double`` takes a very dominant role in matlab (e.g. IIRC the various int types only recently grew even the standard arithmetic operators and have hence largely only been used to represent integral values when using ``double``s was somehow too expensive or otherwise impossible). Currently mlabwrap "solves" this by just converting everything (save strings) to ``double``, but with matlab's growing emancipation of non- 64-bit float matrix datatypes, this may become a less attractive trade-noff.

call-by-value, copy-on write (matlab) vs. proper object identity (python)


multiple value return
  not much of an issue (the ``nout`` arg seems to handle this fine)

broadcasting
  an issue for mixed python/matlab object operations?

Marshaling vs. Proxying
-----------------------

Mlabwrap currently uses two different approaches to make matlab objects available in python: marshaling (i.e. creating an 'equivalent' native python object from a temporary matlab-original) for types (currently matrices and strings)) and proxying (creating a proxy object that delegates to the matlab object, which is kept around). 

Each method has it's downsides and upsides and the key design questions for the next version of mlabwrap is what mix of the two mlabwrap should employ, how the user can fine-tune it. Here's some of the issues with various scenarios:

Problems with a pure-marshaling scheme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* expressiveness: there will always be types that cannot be marshaled, no matter how sophisticated mlabwrap becomes (e.g. anonymous functions and handles to files or other system resources). 

* inefficiencies: deep-copying large structs and in particular objects is quite expensive, especially if one really is only interested in a particular field (struct) or the results of method calls (object). Deep-copying is also not structure preserving, which is not much of a problem in matlab presently since creating shared structure is not straightforward, but this could change as matlab becomes increasingly general purpose.

* breaking interface and encapsulation: marshaling matlab objects to recarrays as suggested in [`https://projects.scipy.org/scipy/scikits/wiki/MlabProxyObjects`_] circumvents matlab's equivalent to python's ``property/__getattr__`` mechanisms and such reliance on implementation details is likely to lead to nasty surprises. Generally converting the constituent parts of an matlab object to python equivalents only really makes sense if one is interested in breaking the encapsulation rather than using the intended interface -- but that is hardly the case one should optimize for. Additionally such a scheme implicitly assumes 100% roundtripability which seems problematic (*XXX: where exactly this assumption might fail is a question worth pondering, irrespective of whether one wants to adopt pure-marshaling*).

Problems with a pure-proxying scheme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* violation of transparency: whilst it might be possible to duck-type ndarrays sufficiently well (possibly autoconverting on certain actions), there are clear limitations, especially for fundamental types such as strings; it is very unlikely that e.g. a proxied matlab ``char`` matrix will be as useful a return value as a ``str`` in most situations. Generally the only way to get complete python semantics is to really use native python types.

* inefficiencies: proxying is only more efficient if one doesn't want to 'use' all the data associated with an object in python. For arrays and strings that typically seems unlikely to me.

Hybrid-scheme 1: pretty much as currently - proxy only objects (and possibly structs), but not arrays, strings etc.

Hybrid-scheme 2: Also proxy object attributes (on access), even if they could be marshaled (largely so that subattribute assignment can be made to work)

(FIXME expand this section)

Problems with hybrid-scheme 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``proxy.a.b = c`` 

Problems with hybrid-scheme 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* surprises: the subtly different behavior of ``proxy.array`` and ``array`` is going to bite someone somewhere eventually; the question is how often and hard. 

* complexity: this scheme is much more complicated than the others proposed here

Summary: I think pure marshaling ought to be available as option (an maybe pure-proxying, too), but I suspect that a hybrid approach will make the best default.

Hacks at our disposal to fine-tune (conversion etc.) behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generally speaking Matlab and python are semantically too different for mlabwrap to be able to offer default behavior that always produces the desired or expected results. Here are ways how fine-tuning behavior is or could be implemented

* leveraging python's richer syntax

  * keyword arguments (e.g. nout)

  * nasty: use the fact that names may not begin with '_' in matlab to give mlab.foo different semantics from mlab._foo; currently this is only used to handle python keywords (e.g. mlab._print) and ``{}`` indexing.

* customization variables (e.g. _array_cast, _flatten_col_vecs)

  * Downside: python's weak support for dynamic scope makes this unattractive (by and large anything governing pervasive behavior (e.g. number of significant digits in computations; printing precision; floating modes etc.) ought to be dynamically scoped; statically scoped global vars as in python suck; however python 2.5's with statement can be used as a (poor man's?) fluid-let). 

    It should also be borne in mind that the more customization switches there are the harder it becomes to read code using mlabwrap because one has to find out which switches are in effect in order to interpret it correctly.

* proxying with transparent auto-conversion

As hinted above too much flexibility can be a bad thing; the less customization possibilities the design needs whilst retaining generality and convenience for the common cases, the better.

Relevant Links
--------------

* [`http://www.scipy.org/Cookbook/Ctypes`_ ctypes]

* [`http://rpy.sourceforge.net/download.html`_ rpy] and other python-x bridges

    should be studied for design ideas

* [`http://mlabwrap.sf.net`_ old mlabwrap sourceforge site]

Open questions
--------------

* does ``setup.py`` work under windows as desired?

* Is guessing the default ``nout`` of builtins via the horrible docstring regexp

    hack (``expound_docstring`` in dev. version) still needed for non-ancient matlab versions?

* distutils vs. [`http://svn.scipy.org/svn/numpy/trunk/numpy/doc/DISTUTILS.txt`_ numpy.distutils] vs. [`http://peak.telecommunity.com/DevCenter/setuptools`_ setuptools] (ADDENDUM: apparently [`http://cheeseshop.python.org/pypi/setuptools`_] is more up-to-date): 

  * version 1.0 will use plain distutils

  * for future versions: 

    * is there a (sane) way to install automatically, even if ``numpy`` is not  already installed? We need ``numpy.get_includes`` (or ``numpy.distutils`` equivalent) for options to pass to ``setup`` but ``setup`` is also the place where the dependency on ``numpy`` is declared (? 

    .. ############################################################################

    .. _mlabwrap@sourceforge.net: mailto:mlabwrap@sourceforge.net

