#format rst

1. What is AstroAsciiData
-------------------------

ASCII tables are one of the major data exchange formats used in science. In astronomy we use ASCII tables e.g. for object lists, line lists or even spectra.

Every person working with astronomy data has to deal with ASCII data, however there are various ways to do so. Some use the awk scripting language, some transfer the ASCII tables to FITS tables and then work on the FITS data, some use IDL routines. Most of those approaches need individual efforts (such as preparing a format file for the transformation to FITS) whenever there is a new kind of ASCII table with e.g. a different number of columns.

Within the AstroAsciiData project we envision a Python module which easily can be used to work on all kinds of ASCII tables. The class should provide a convenient tool such that the user can easily:

* read in ASCII tables;

* manipulate table elements;

* save the modified ASCII table;

* combine several tables;

* delete/add rows and columns;

* to sort along column values;

The AstroAsciiData module may be used interactively, within small scripts, in data reduction tasks and even in data bases.

In general, the ASCII tables used in astronomy have a rather small size. As an example, the size of the Wide Field Camera catalogue  of Hubble Ultra Deep Field is 2.2MB. Handling those amounts of data is not a time consuming task for modern day computers. As a consequence, computational speed is not a prime issue in software design and construction. The focus is rather to maximize the convenience for the user, such that using the class requires only to overcome a small threshold.

2. Software release
-------------------

The project started with a design paper, which was published on this wiki. This paper as well as the feedback to this draft were the main guidelines in the implementation of the module.

Although all conversation based on the design dratft remains still valid, the information in this discussion is now, after the first releases, somewhat outdated, and all content was moved to the ["AstroAsciiDatahistory"] page.

In October 2006 version 1.0 of the AstroAsciiData module was released. The project webpages are at:  http://www.stecf.org/software/PYTHONtools/astroasciidata/

On this page you will find some introduction on how to use the module, the source code for download and the manual.

3. Release notes for version 1.0
--------------------------------

After the initial release (which was version 0.01), version 1.0 of the module comprises all the features we originally had envisioned for the project. We took particular care that

* a fair amount of Unit Tests comes together with the software. Running these tests will assure the proper working of the code;

* the module was tested by the developer and within their working group in real projects;

* there is a manual which covers all aspects of the module.

If you have the feeling that the AstroAsciiData module might be the answer to some of your problems, then go to the `AstroAsciiData project webpage <http://www.stecf.org/software/PYTHONtools/astroasciidata/>`_ and download the software.

In case that the module does **not** meet your expectations or is just disapointing, give a short feedback why, either on the wiki here or via email at AstroAsciiData@stecf.org.

4. Next steps and outlook
-------------------------

As mentioned above the released version 1.0 already contains everything we wanted the module to do. So from our side, their is no big pressure anymore to do further, substantial development. Certainly we will now and then add some features in case that we miss them in our daily work with the module, but this will not touch or extend the core functionality of the package.

Feedback from the users and from potential users who just miss a key functionality for their benefit would be very important to motivate and trigger the further development and improvement of the AstroAsciiData module. Any kind of feedback either directly here in this wiki or to AstroAsciiData@stecf.org is welcome.

