\The project scope will most likely emerge from the AstroLibCoordsUseCases_, but we can identify some user communities that we will, or will not, try to serve.

Target Users
------------

Our target user is a typical astronomer who needs to analyze data, work with catalogs, prepare observing proposals,  and prepare for observing runs.

The following areas are not presently planned to be in the project scope:

* Relativistic effects

* Orbital mechanics (eg, satellite tracking)

* High precision astrometry

    We aren't opposed to providing support for these, if someone has the expertise and wants to contribute; but it won't be the primary focus of the library.

Finding the right niche
-----------------------

This project has potential overlaps with other existing projects, and it's worth carefully considering where we fit.

* This library doesn't need to provide the level of precision or detailed modelling provided by astrometric libraries (see SLALIB, NOVAS, TPM on the AstroLibCoordsSoftwareSurvey_ page). But, if the machinery already exists, it may be easier to wrap and provide it.

* If we were to take catalog matching as one of our AstroLibCoordsUseCases_, it's worth noting that this is one of the fundamental problems the Virtual Observatory needs to tackle. The VO, however, needs to consider much larger, more distributed, and more general cases than we do. On the other hand, it would be good to be able to interface with the VO.

Interfaces with other libraries
-------------------------------

* AstroAsciiData_ for getting data

* AstroLibDatesTimes_ (although this may come as part & parcel of some of the external libraries)

* AstroLibFormats_ to handle various representations (decimal, sexagesimal)

* AstroLibUnits_ to handle various units (degrees, hour angle, radians)

.. ############################################################################

.. _AstroLibCoordsUseCases: ../AstroLibCoordsUseCases

.. _AstroLibCoordsSoftwareSurvey: ../AstroLibCoordsSoftwareSurvey

.. _AstroAsciiData: ../AstroAsciiData

.. _AstroLibDatesTimes: ../AstroLibDatesTimes

.. _AstroLibFormats: ../AstroLibFormats

.. _AstroLibUnits: ../AstroLibUnits

