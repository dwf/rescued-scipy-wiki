#format rst

Working on Scipy
================

Anne Archibald's workflow
-------------------------

This is on Linux.

The first time
~~~~~~~~~~~~~~

Check out the current SVN version
:::::::::::::::::::::::::::::::::

svn co to some local directory

Set things up so compilation doesn't break anything
:::::::::::::::::::::::::::::::::::::::::::::::::::

write compile.sh to do a setuptools install to some arcane local directory; write develop.sh to source when you want that directory on your PYTHONPATH

Compile the current version
:::::::::::::::::::::::::::

run compile.sh

Run the tests
:::::::::::::

::

   python -c "import scipy; scipy.test()"

Unfortunately, there are often some failing tests before you even start. Usually I just check that nothing looks too suspicious and remember that these ones are still going to fail when I'm done.

Second and later times
~~~~~~~~~~~~~~~~~~~~~~

Update SVN
::::::::::

::

   svn update

Compile and test
::::::::::::::::

::

   . develop.sh
   ./compile.sh
   python -c "import scipy; scipy.test()"

Making changes
~~~~~~~~~~~~~~

Write some tests
::::::::::::::::

How to test the module you're working on, say scipy.interpolate:

::

   ./compile.sh && python -c "import scipy.interpolate; scipy.interpolate.test()"

How to write a test:

How to make sure it's getting run: I usually just add "assert False" and make sure it fails.

How to run just one test and bring up a debugger if it fails:

Fix the bug/implement the feature
:::::::::::::::::::::::::::::::::

This is usually surprisingly easy by this point.

Run all scipy tests
:::::::::::::::::::

::

   ./compile.sh
   python -c "import scipy; scipy.test()"

Document the change
:::::::::::::::::::

Just write some docstrings. I usually just format them like other docstrings in similar functions, but there's a prescribed format somewhere.

Committing
~~~~~~~~~~

::

   svn commit

Force an autobuild:

