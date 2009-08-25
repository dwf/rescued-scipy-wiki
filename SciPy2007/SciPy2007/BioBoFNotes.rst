#format rst

Biology Birds of a Feather (BoF) Session
========================================

The Biology BoF was organized by Titus Brown.

-------------------------

 The following text was scraped from: `http://lists.idyll.org/pipermail/biology-in-python/2007-August/000059.html`_

The mailing list posting has been duplicated here with slight formatting changes.

-------------------------

 Hi All,

Last night we had a biology birds of a feather meeting as part of SciPy_  2007. I have included notes below from both Diane and myself. To  summarize, there were two general trends during the evening:

1. Need to establish python/biology community, via website,

     biology-in-python mailing list, rss, blogs, etc.

#. Having a core set of "interfaces" for handling basic

     bioinformatics objects would allow independent projects to share these basic objects. I am sure others will describe this better and in more detail in the near future.

I have agreed to setup the python/biology community site. There are some  ideas in the notes below and I will also be posting ideas and requesting  ideas for this in a future post.

Enthought has agreed to host our community site. We have the option of  using scipy.org sub-domain such as bio.scipy.org or we can choose a  domain name like biologyinpython.org. Any thoughts or preferences on  which one we should use?

I will let others jump and provide some of the details/interests from  the meeting in more detail.

-Brandon King

Brandon King's Notes
====================

Birds of a Feather: Biology

Chris: We could use some core package where all Biology Python packages can build off of, but still do there own thing. This would allow for the  packages to pass data around in a compatible way.

Share [complex] functionality.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* graph db/pygr

  * common interface

    * sequence

    * sequence DB

    * alignment (--> annotation)

    * (BioPython_ seq_io)

Parsing (Only need one / format).

Large analysis management / parallel / cluster processing.

* map / reduce impl?

    l = [ x, y, ... ] map(fn, l) reduce( l )

* Parallelization in Python... mailing list.

Other people's databases.

Problems with BioPython_:

* big, sprawling, interconnected.

* poor ... ???

Parsing Issues:
~~~~~~~~~~~~~~~

* Blast

* Hmmer

Where is the community?

* mailing list

* wiki / website

* RSS / blog / planet

  * extract?

  * use SciPy_

* "Don't suck." / easy_install

  * If you are interested in post datasets.

* Coding standards

  * testing (

  * testing buildbot

  * PEP 8 compliance

  *

Tutorials / entry documentation:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Redoing analysis.

* How to distribute/write/host small projects (eggs)

Common Theme:
~~~~~~~~~~~~~

Core interface so programs can play well together, while the implementations can change. This allows the interface to be independent from the storage.

Databases:

* NCBI eutils, etc.

* Gene ontology

* mammalian PO

* UCSC/Ensembl

* Integr8

* Textspresso?

Agreements:
~~~~~~~~~~~

* Brandon has agreed to setup the biology-in-python community website, etc.

Diane Trout's Notes
===================

* Introductions...

  * Industry, 2

  * Academic, 10

  * Unknown, 1

* What should we do?

  * Work on a common software

  * Work on a common api, or at least define a common api

* Sharing complex functionality

  * Graph Database

  * Sequence Databse, common API

    * common interface to the standard bioinformatics types

      * Like sequence

* parsing (only need once per format)

  * BLAST

  * HMMER

  *

  * Biopython too monolithic

* Large Analysis Management Parallel/Cluster processing

  * Map/Reduce impl

* Other peoples databases

  * NCBI Eutils

  * Gene Ontology

  * mammalian phenotype ontology

  * UCSC/ENSEMBL

  * integr8

  * raw textpresso database available (lexicons)

* Missing Data

* Microarray Formats

  * R-BioConductor_

* Problems with BioPython_

  * Big, Sprawling, Interconnected

  * Poor Automated Testing

  * unpythonic

  * seems low-hanging fruit

* Python software

* Where is the community

  * Mailing List  

  * Wiki

  * Rss/Planet/Blog/planet 

    * bioinformatics.org

    * use scipy

  * Inclusivity

  * how to distribute/write/share small projects

  * "Dont Suck"

    * Coding standards

      * testing

      * PEP8 compliance & docstrings 

      * setup.py distutils

      * make sure they're easy installable

    * if you want to publish your scripts & data, we will be willing

        to help you host it

  * Tutorials

    * Entry documentation

    * Good thing in BioPython_

      * Intro to how to use their blast parser

      * Cookbook

      * How to do the analysis of the paper in python

* One person argues that we shouldn't split things into too many fragments

