#format rst

A Submillisecond Pulsar?
========================

Pulsars are rapidly-rotating neutron stars. The fastest of them spin `many hundreds of times per second <http://www.nrao.edu/pr/2006/mspulsar/>`_, indicating that they must be extremely small. Since they are known to have masses a bit more than the sun, these inferred radii of tens of kilometers indicate that they must be extremely dense. Understanding the matter they are made of poses a considerable theoretical challenge. Discovering a pulsar spinning at more than a thousand times a second would pose extremely stringent constraints on theories of neutron-star matter. In 2007, `Kaaret et. al <http://adsabs.harvard.edu/abs/2007ApJ...657L..97K>`_ published a paper claiming to have detected pulsations at 1122 Hz coming from a neutron star. If these pulsations are real, and if they represent the rotation of the star, this would be an amazing discovery. `Over 20 papers <http://adsabs.harvard.edu/cgi-bin/nph-ref_query?bibcode=2007ApJ...657L..97K&amp;refs=CITATIONS&amp;db_key=AST>`_ have since been published discussing its theoretical implications. But is it real? We will download the original data and analyze it ourselves; I leave the conclusion up to you.

The neutron star they looked at, XTE J1739-285, is a Low-Mass X-ray Binary (LMXB). That is, it is in a close binary orbit with another, low-mass, star. The orbit is so close that the neutron star siphons mass off its companion, filling an accretion disc with gas. We think that the accreted material forms a layer on the star, which from time to time ignites and "burns", fusing the accreted mater (mostly hydrogen and helium) into heavier elements and releasing a great deal of energy, which we observe in X-rays. This is called a Type I X-ray burst. The star XTE J1739-285 underwent a number of these Type I X-ray bursts during the observations. In a single such burst, as the X-ray emission was falling back to its normal levels, Kaaret et al. detected a brief oscillation at 1122 Hz. The oscillation lasted only a few seconds, but was stable in frequency. We might expect such a signal if the burning on the surface of the star was nonuniform (producing oscillations) but the accreting material screened it from view most of the time. (Other explanations are possible, of course.) So let us look for this oscillation.

Getting the data
----------------

Observations were conducted with the Rossi X-ray Timing Explorer, an X-ray timing satellite. Data taken by satellite observatories is normally kept proprietary for one year, so that the astronomers who requested the data can have exclusive access, but after a year it becomes publicly available. The burst which showed the oscillations occurred on Nov. 4 2005. Thus the data should be available.

First, go to `HEASARC <http://heasarc.gsfc.nasa.gov/db-perl/W3Browse/w3browse.pl>`_, NASA's online database access tool. If we ask for observations of XTE J1739-285, we find many. Select "XTE Master Catalog", and you obtain a list of observations done with XTE. We want the observation on 2007-11-04, which has observation ID 91015-03-04-00. Click on the "D" in this row, for "list data products", select them all, and request a tar file of the lot. (X-ray data is not especially large; the tar file is 50 MB.)

Expand the tar file in a new directory. All its contents should go in a directory P91015, apart from the abstract.

Reading the data
----------------

The data we are interested in is taken with RXTE's Proportional Counter Array (PCA). This instrument simply collects individual X-ray photons, recording their arrival time and energy. It has a very broad field of view - one degree - and can't do imaging, but it has a large collecting area and a good time resolution. For more information on RXTE instruments and data formats see `The ABC of XTE <http://heasarc.gsfc.nasa.gov/docs/xte/abc/contents.html>`_.

We will use `PyFITS <http://www.stsci.edu/resources/software_hardware/pyfits>`_ to access the data, rather than rely on NASA's FTOOLS.

The data we want are stored in the directory P91015/91015-03-04-00/pca/, and are gzipped. Copy them to your working directory and extract them. Their names are, as you can see, unhelpful, but the ones beginning with "FH" are housekeeping and the ones beginning with "FS" are science. The single observation is broken up into a number of pieces, so we will want to extract all photon arrival times from all the "FS" files.

::

   >>> import glob
   >>> glob.glob("FS*")
   ['FS46_164681ea-1646ac2f',
    'FS4f_164681d0-16468f54',
    'FS4f_164697d0-1646a55b',
    'FS4a_164681ea-1646ac2f',
    'FS3b_164697d0-1646a55c',
    'FS3b_164681d0-16468f54']
   >>> import pyfits
   >>> fitsfiles = [pyfits.open(f) for f in glob.glob("FS*")]

