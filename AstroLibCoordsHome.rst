#format rst

This will serve as the project home page for the AstroLibCoords_ project. We invite comments and contributions from the community at all stages of the project.

There is also a [`http://projects.scipy.org/astropy/astrolib/wiki/WikiStart`_ Subversion repository] for this project.

**v0.3 release now available!** Download it [`http://stsdas.stsci.edu/astrolib/`_ here]

* [`http://stsdas.stsci.edu/astrolib/coords_api/index.html`_ Documentation], including examples demonstrating "snapshot" of current functionality

* Background material:

  * AstroLibCoordsLiteratureSurvey_ collects links to academic papers and other useful resources discussing astronomical coordinate issues at various levels of detail.

  * AstroLibCoordsSoftwareSurvey_ discusses and links to some existing software packages and libraries that either provide functionality similar to what we hope to provide, or provide some underlying machinery that might be wrapped.

  * AstroLibCoordsStartingThoughts_ contains some material written by Perry when he first started thinking about what this object should be able to do. 

* Users, scope, use cases:

  * AstroLibCoordsScope_ discusses who the users will be, what functionality the Coords object should provide, and what it should not provide.

  * AstroLibCoordsUseCases_ suggests and discusses some specific use cases. We intend to develop the project scope from the desired use cases, rather than the other way around.

It's worth noting up front that any functionality to convert from sky coordinates to image coordinates (RA, Dec <-> x,y) will **not** be part of the Coords functionality. Instead, these operations will be handled by the AstroLibWCS library. The interface between these two libraries will be well-defined.

.. ############################################################################

.. _AstroLibCoords: ../AstroLibCoords

.. _AstroLibCoordsLiteratureSurvey: ../AstroLibCoordsLiteratureSurvey

.. _AstroLibCoordsSoftwareSurvey: ../AstroLibCoordsSoftwareSurvey

.. _AstroLibCoordsStartingThoughts: ../AstroLibCoordsStartingThoughts

.. _AstroLibCoordsScope: ../AstroLibCoordsScope

.. _AstroLibCoordsUseCases: ../AstroLibCoordsUseCases

