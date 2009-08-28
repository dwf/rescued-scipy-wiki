#format rst

FiPy
----

-------------------------

 **A finite volume PDE solver written in Python (FiPy)**

*Daniel Wheeler, Jonathon E. Guyer and James A. Warren*

*National Institute of Standards and Technology, Gaithersburg, MD.*

FiPy website: http://www.ctcms.nist.gov/fipy

We will present a description of an object-oriented PDE solver based on a standard finite volume (FV) approach. We will describe how the Numeric and SciPy modules have been used in the design and development of FiPy and the efficiency issues that still need to be addressed.

FiPy has been developed mainly for materials science continuum models that broadly involve material interfaces and phase transformations. Such phase transformations generally describe solid-solid and liquid-solid interactions in phenomena such as polycrystalline reorientation, dendrite formation, electrodeposition and spinodal decomposition. FiPy aims to address the difficulties materials scientists face in quickly developing new models without specialized knowledge, while avoiding the trap of continually developing limited tools for specific problems.

Our approach, combining the FV method and Python, provides a tool that is extensible, powerful and freely available. The framework allows arbitrary combinations of equations to be coupled and solved, while program flow is entirely under user control. This is a different approach from traditional numerical codes written in FORTRAN or C where the program flow is hardwired into the main body of the code.

A few examples will be presented highlighting how one poses problems and then obtains results in FiPy for simple as well as complex systems. We will also describe and quantify FiPy efficiency data relating to the Numeric and weave modules. Furthermore, we will discuss issues relating to sparse solvers (PySparse, scipy.linalg) and viewing capabilities.

.. ############################################################################

.. _SciPy: ../SciPy

.. _PySparse: ../PySparse

