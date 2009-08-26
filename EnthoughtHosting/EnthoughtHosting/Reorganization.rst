#format rst

SciPy Server Reorganization
===========================

Please comment on these ideas. If you have others, please add them.

There is also a mailing list at ``administration@scipy.org` <http://projects.scipy.org/mailman/listinfo/administration>`_.

Goals
-----

* Improve reliability

* Ease management

Prioritized List of Problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are some of the biggest problems that need to be addressed to meet the goals.

1. httpd stops responding spontaneously.

#. server load average is frequently too high.

#. setting up new projects with virtualmin breaks the system.

#. SSL is only available for one virtual host for SVN.

#. People have to maintain different passwords for different projects, trac, moin, and svn.

Strategies
~~~~~~~~~~

Unified logins for Trac, Subversion, Moin, etc.
:::::::::::::::::::::::::::::::::::::::::::::::

* Store in LDAP

* Allow project owners to grant permissions to users

When merging the password files, we will encounter multiple passwords for many usernames. I propose the following hierarchy for determining which password to use:

1. Passwords currently in Enthought's LDAP system

#. Scipy Trac

#. Numpy Trac

#. Enthought Trac

#. Other Tracs in alphabetical order

Enable and require SSL for all logins
:::::::::::::::::::::::::::::::::::::

* Requires one domain for all SVN repos and Trac instances

Use MySQL instead of SQLite for Trac
::::::::::::::::::::::::::::::::::::

Replace Virtualmin
::::::::::::::::::

* GForge may be more suitable

* Something new that just manages user accounts at first may be better

Trac improvements
:::::::::::::::::

* Create a global trac.ini that is merged with a project specific trac.ini nightly or more often

* Nightly static sites with links that modify Trac pointing to the real Tracs

Replace full service email with aliases and mailing lists
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

* Does anyone use a scipy.org email address?

Unified logging to a separate server
::::::::::::::::::::::::::::::::::::

* Webalizer can still generate seperate reports for each domain

Moin improvements
:::::::::::::::::

* Use Multimoin to reduce load

* Nightly static sites with links that modify Moin pointing to the real wikis

* Use LDAP for access control

More hardware
:::::::::::::

* Load average has increased 4 to 5 times in the last year

* Should we utilize it by putting different services or different projects on separate servers?

Prerequisites
~~~~~~~~~~~~~

* Web based service for adding and managing users in the LDAP system

  * Must be accessible and separated for project owners to manage

* Decide if GForge is useful

* Write scripts to manage trac configurations

* Set up log server

* Spec out and purchase server

Notes
:::::

I think the most time consuming will be writing the web based system for account management. I have written a python library to do some interaction with our LDAP server. I would appreciate help designing and writing the web interface.

.. ############################################################################

.. _administration@scipy.org: mailto:administration@scipy.org

