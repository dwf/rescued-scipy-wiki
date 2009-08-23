#format rst

Compiling Extension Modules on Windows using mingw
==================================================

Pre-reqs
--------

1. Python 2.5 (with earlier versions of Python, it is much more complicated to compile extensions with mingw. Use visual studio 2003 if you cannot upgrade to Python 2.5)

#. Local admin access on your machine

Compiler setup
--------------

1. Go to www.mingw.org and go to the "downloads" section of the web-site. Look for the link to the sourceforge page and go there. Grab the latest version of the "Automated MinGW Installer" and run the installer.

#. When asked "which MinGW package" you would like to install, select "Current" or "Candidate" depending on whether you want to be on the bleeding edge or not.

#. When you get to the section where you need to select the various components you want to install, include the "base tools" and the "g++ compiler", and possibly the g77 compiler too if you are going to be compiling some extensions that use Fortran.

#. Install it to "C:\MinGW" (the default location)

#. Add "C:\MinGW\bin" to your PATH environment variable if the installer did not do this for you. If you are running Vista, you will need to add "C:\MinGW\libexec\gcc\mingw32\3.4.5" to your PATH as well

#. In notepad (or your favourite text editor) create a new text file and enter the following in the file:

     [build]BR_ compiler = mingw32

#. Save the file as "C:\Python25\Lib\distutils\distutils.cfg". This will tell python to use the MinGW compiler when compiling extensions

#. Close down any command prompts you have open (they need to be reopened to see the new environment variable values)

Compiling an extension (through distutils)
------------------------------------------

Note: this will only work for modules which have a setup.py script that uses distutils

1. So lets say you have downloaded code for some module to the folder "xyz". Open a command prompt and cd to this directory (eg. type "c:" then press enter to change to the C drive, then type "cd c:\xyz" to change to directory xyz)

#. To create a binary installer, type "python setup.py bdist_wininst"

#. If everything worked fine, then there should now be a subfolder called "dist" which contains an exe file that you can run to install the module.

