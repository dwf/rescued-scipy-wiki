#format rst

Abstracts of EuroScipy2008
==========================

`Anchor(kmueller)`_

SimPy, a discrete event simulation package in Python
----------------------------------------------------

 **by: Klaus G. Müller** 

The presentation will address SimPy (Simulation in Python), an Open Source discrete event simulation package. It is written completely in Python. SimPy is released under a LGPL license and can be downloaded free of charge from `http://sourceforge.net/project/showfiles.php?group_id=62366`_. The SimPy website `http://simpy.sourceforge.net`_ describes the package in detail and provides extensive user documentation.

SimPy is being used for teaching and research purposes at universities in several countries. Many companies and institutes also use it for simulation studies.

The talk describes the basic philosophy and design of SimPy. SimPy is modeled after the Simula67 simulation language, but goes beyond that language’s capabilities in terms of simulation constructs and extensibility.  It is a process-oriented simulation package, i.e., the lifecycle of a simulation entity and all its events are described in one method (called the Process Execution Method). Processes are implemented as Python generators.  Process scheduling is done by yield statements with parameters. This provides semi-coroutines, light-weight threads which run in pseudo-concurrency. 

Various small examples of SimPy programs will be presented and run to show the range of process control constructs, and also to illustrate how concisely and descriptively models can be programmed in SimPy.

The various run-modes of SimPy (which include event tracing, event-by-event execution, and synchronization between wall-clock and simulation time) will be described and run, as will be the GUI and plotting libraries included.

The talk will conclude with a few words about the relationship between SimPy and SciPy. 

`Anchor(jmartinek1)`_

Coefficient of restitution measurement using a soundcard
--------------------------------------------------------

 **by: Jan Martinek** 

Coefficient of restitution (COR) is a measure of elasticity of collision between two bodies. This article presents a method for measurement of the coefficient of restitution between bouncing a rubber ball and a hard surface. Each impact makes a sound which is detected by a microphone connected to computer's sound card and the recorded sound is analysed. Coefficient of restitution is calculated from the delays between each two consecutive impacts. Programs listed and commented in the article utilises Python with the python‑alsaaudio library for sound recording, !Scipy for data processing and matplotlib for waveform visualisation. It runs under the Linux operating system and a whole experiment is meant primarily for students and education purposes.

`Anchor(jmartinek2)`_

Musical instrument tuner and tone analysis
------------------------------------------

 **by: Jan Martinek** 

This article presents an implementation of well known method for fundamental frequency measurement. The algorithm uses FFT and searches for a peak in spectrum. Dominant frequency is then recalculated to tone name used in music. The presented computer program basically works in similar way to commercially sold tuners for musical instruments and also many other software tuners widely available in the internet, but what makes it unique is the peak search algorithm and reliable matching of higher harmonics. Moreover, the programme is written in Python programming language with a great help of !Scipy. This makes it surprisingly simple to implement and easy to understand and modify. It runs under Linux and uses alsa for sound recording.

`Anchor(bvoigt)`_

Searching High Energy Neutrinos with IceCube and Python
-------------------------------------------------------

**by: Bernhard Voigt**

The IceCube neutrino telescope is currently constructed in the deep ice near the geographic South Pole. At completion IceCube will consist of more than 4500 photomultiplier tubes which record the Cherenkov light from secondary charged particles produced in neutrino nucleon interactions, in order to detect high energy neutrinos coming from cosmological objects. The recorded signals are used to reconstruct the energy and direction of the incident neutrino. The core of the custom made software components, ranging from simulation to data compression and likelihood reconstruction is written in C++. The program flow structures are exposed to Python using Boost.Python. This allows to control the data processing flow in Python which offers a great flexibility. Data analyses can be performed using Python and libraries like numpy, scipy, matplotlib, pytables and pyROOT. For this purpose the main data structures are exposed to Python, as well. The talk will give an overview about the control flow of the IceCube software chain, driven by Python, and how reconstructed data is analysed using Python and extension libraries.

`Anchor(ppeterson)`_

On providing a Computer Algebra System for Python
-------------------------------------------------

**by: Pearu Peterson**

During the last ten years there has been many attempts to provide a Computer Algebra System (CAS) for Python that have important applications in code generation tools, for example.  In most cases, one of the following approaches has been proposed: wrap existing CAS libraries to Python, create Python interfaces to existing CAS programs, or implement pure Python CAS from scratch.  In this talk I will discuss pros and cons of these approaches as well as try to give an overview of what is the current state with CAS-s for Python. Finally, a pure Python package, sympycore, will be introduced as sufficiently efficient and robust implementation of a CAS for Python. For example, the sympycore speed is comparable with the speed of many CAS-s that are implemented using a compiled language.

`Anchor(jmrohwer)`_   

Python, Systems Biology and PySCeS
----------------------------------

by: Johann M. Rohwer, Brett G. Olivier, and Jan-Hendrik S. Hofmeyr

**Introduction**

Computer modelling has become an integral tool in the analysis and understanding of the reaction networks that underlie cellular processes. Programs such as the Systems [`http://dx.doi.org/10.1089/153623103322637670`_ BiologyWorkbench_] (SBW) and [`http://bioinformatics.oxfordjournals.org/cgi/content/abstract/22/24/3067`_ COPASI] allow us to simulate the behaviour of these reaction networks; each has its advantages and limitations. The need to adapt modelling software to our specific needs prompted the development of [`http://pysces.sourceforge.ne`_ PySCeS], the Python Simulator for Cellular Systems, which we present here. PySCeS is an extremely exible, user-extensible, open-source modelling tool. Development started in 2000, with the first public release following in 2004. PySCeS is written in Python and makes extensive use of the highly successful IPython, NumPy, SciPy, Matplotlib stack. It has been developed to run on both Microsoft Windows and Linux (with a Mac OS X port possible in principle) and is currently released under the GNU GPL licence.

**PySCeS: core**

Models are initially described as PySCeS input files in a human readable model description language (MDL). We have implemented a MDL parser using David Beazley's PLY. Alternatively, PySCeS supports translation to and from the [`http://www.sbml.org`_ Systems Biology Markup Language (SBML)], the de facto standard for model exchange. Once a PySCeS model object has been instantiated with an input file, all model properties are represented by attributes. Specifically, the kinetic rate equations are represented by rate equation objects. During the load process a stoichiometric analysis is automatically performed, thus generating the ordinary differential equations (ODEs) describing the system. After translation into ODEs the system can be analysed with a number of algorithms in terms of its time-dependent (LSODA, CVODE) and steady-state (HYBRD, NLEQ2, KINSOL) solutions. PySCeS also allows higher level system properties to be analysed using Metabolic Control Analysis, a theoretical framework for the study of the control and regulatory properties of a cellular reaction network at steady state. The stability of the system can be evaluated by automatic computation of the eigenvalues of the Jacobian matrix.

**PySCeS in operation**

As an example of how we use PySCeS in systems biology we will show how multiple-parameter rate characteristics can be used to investigate bistable regulatory patterns in an example metabolic pathway and how regulatory metabolites can be computationally identified from a  [`http://dx.doi.org/10.1016/j.jtbi.2007.10.032`_ generalised supply-demand analysis]. Exciting bleeding-edge developments include PySCeS/Kraken and PySCeS/Mariner. Kraken is our first attempt at using PySCeS in a distributed environment and employs a single master, multiple client design that allows for the distribution of embarrassingly parallel problems over a heterogeneous grid of CPUs. PySCeS/Mariner provides a web-application framework (using Optio's soaplib) to expose PySCeS functionality on the one hand and consume SOAP-based web-services (e.g. SBW) on the other hand.

`Anchor(adalke)`_

Python Tools in Computational Chemistry
---------------------------------------

**by: Andrew Dahlke**

For the last 13 years I've been a professional software developer in computational chemistry and related fields, and mostly in chemical informatics, molecular modeling, and bioinformatics.  I develop scientific software but it often seems distant from what others do at SciPy.  For example, I import the numeric libraries about every time there's a name change.  The science behind what I work on is more often based on graph theory than on matrices.

Thankfully Python is popular in computational chemistry and there are a good number of chemistry tools for Python available, including the OpenEye toolkits and OpenBabel, so I don't often have to work on the low-level details.  Much of what I do is tool and algorithm integration, which often means wrapping yet another program and figuring out how it breaks, or writing yet another specialized format parser.

In my presentation I'll summarize some of the reasons I think Python became the dominant high-level language in computational chemistry, some of the algorithms and data types which are important to this field, and a few of the key projects.

`Anchor(mmueller)`_

PyModelData - Easy Data Input for Scientific Simulation Models
--------------------------------------------------------------

 **by: Mike Müller and Stefan Schwarzer**

Processing of input data for simulation models can be a major effort. The Python library [`http://www.pymodeldata.org`_ PyModelData_] provides many features to aid the model programmer as well as the model user. User input is transferred directly into data structures of the programming language Python without the need to write code. PyModelData is based on [`http://www.yaml.org`_ YAML] which offers an input format readable by humans and machines alike. PyModelData extends this format to allow nesting of files, thus separating frequently changed from other data. Moreover, the included files can have other formats such as CSV, Excel, dBase or HDF.

An application user writes an input data file in YAML format while an application programmer may add a declarative input description with units, valid ranges and other meta-information which is applied after parsing the user's data.

PyModelData has been used successfully for two simulation models. Users seem to grasp the library quickly and become productive after a short learning period.

It is planned to add a GUI interface that generates its views automatically from the declarative template file. This means getting a simple yet useful GUI without any work except specifying the input data. 

`Anchor(mcroettger)`_ 

How to decide - Machine Learning with Python
--------------------------------------------

**by: Michael C. Röttger and Andreas W. Liehr**

In Reinforcement Learning, one solves optimal control problems without knowledge of the underlying system's dynamics from the following perspective: An agent, who is aware of the current state of his environment, decides in favour of a particular action. The action is performed resulting in a change of the agent's environment. The agent notices the new state, receives a reward and decides again. This process repeats over and over and may be terminated by reaching a terminal state. In the course of time the agent learns from his experience by developing a strategy which maximizes his estimated total reward.

The overall research in Reinforcement Learning concentrates on discrete sets of actions, but for real world problems it would be nice to have methods which are able to find good strategies using actions drawn from continuous sets, e.g. when you have to decide for a spatial direction in order to reach a distant point by going a minimal number of steps.

We're using Python for searching and comparing strategies by evaluating combinations of different Reinforcement Learning algorithms, control tasks and requirements. In this talk, we give an overview of our implementation pointing out the contexts in which SciPy and other Python packages are applied. 

`Anchor(dalbanese)`_ 

mlpy - Machine Learning Py - A High-Performance Python/NumPy Based Package for Machine Learning
-----------------------------------------------------------------------------------------------

**by: Davide Albanese, Stefano Merler, Giuseppe Jurman, Roberto Visintainer, Samantha Riccadonna, Silvano Paoli, Cesare Furlanello, and Fondazione Bruno Kessler**

Obtaining honest performance estimates from a machine learning experiment usually requires fulfilling a complex pipeline of simpler tasks. Those steps can be organized inside a Data Analysis Protocol (DAP) tailored by the researcher as suitable for the investigated problem typically a predictive classification or regression task. As a very basic example, a binary classification experiment can be structured by a k-fold cross-validation with internal feature ranking performed at each split. We propose mlpy as an Open Source package collecting several modules; they implement different flavours of the machine learning functions required in each classification, feature-ranking and feature-listsanalysis experiment. In particular, mlpy provides high level procedures which guarantee high modularity and ease of use. These features allow researchers, even those not particularly inclined to programming, to construct their own methodological procedure still mantaining good computational efficiency. Although mlpy is suited for general-purpose machine learning tasks, its elective application field is bioinformatics and, in particular, the analysis of high-throughput data such as genomics and proteomics, where input data can easily reach dimensions of thousands of samples described up to onemillion of features (e.g. SNPs array data). Furthermore, we can use modularity to alleviate the computational burden by distributing the processes on a HPC facility such as a cluster or a grid infrastructure. The modular structure of mlpy allows easily adding new algorithms in each category. The mlpy package makes an intensive use of the NumPy module: its strong support for integration with C code has allowed us to implement as internal C functions the parts with higher computational costs. The main features of mlpy can be divided into several groups according to their goal, as detailed in the following lists (for beta version 1.2.5):

Classification
  For each classifier, distinct methods are deployed for the training and the testing phases. Whenever possible, the real valued prediction can be obtained. The implemented algorithms are in the families of SVMs-Support Vector Machines (four kernels avaiable), DA-Discriminant Analysis (Fisher and Spectral Regression) and Nearest Neighbours.

Feature weighting
  In addition to feature weights coming directly from classifiers such as SVMs or DAs, classifier-independent methods for weighting features are also implemented: I-RELIEF and Discrete Wavelet Transform (four a total of nine methods).

Feature ranking
  Two main schemas are used for selecting and ranking purposes, belonging either to the Recursive Feature Elimination or the Recursive Forward Selection family (for a total of six variants).

Resampling methods
  The classification and feature ranking operations can be organized within a sampling procedure such as Textbook/Monte-Carlo cross validation, leave-one-out or user-defined train/test split schema. Stratification over lables is also available.

Metric functions
  Performance assessment can be evaluated by a set of different measures with variability assessed by Standard Deviation or Bootstrap Confidence Intervals: among those we mention Error, Accuracy, Matthews Correlation Coefficient, Area Under the ROC Curve.

Feature list analysis
  The ordered lists from the feature ranking experiments can be analyzed in terms of stability (Canberra indicator, extraction/position indicator) and an optimal list can be retrieved [`http://biodcv.fbk.eu/listspy.html`_ Borda count].

Landscaping tools
  The package includes executable scripts to be used off-the-shelf for typical parameter tuning tasks such as SVM-kernel choice and optimization.

[`https://mlpy.fbk.eu`_ mlpy] is a project developed by [`http://mpba.fbk.eu`_ MPBA Group] at [`http://www.fbk.eu`_ Fondazione Bruno Kessler]. It is free software licensed under the GNU General Public License (GPL) version 3.

`Anchor(kzimmermann)`_

Rapid Information Processing Based on Self-Documented Primary Data
------------------------------------------------------------------

**by: Klaus Zimmermann, Michael C. Röttger, Martin Kühne, Kristian Sylvester-Hvid, Rico Schüppel, Moritz Riede, Andreas W. Liehr**

The bottleneck for communicating scientific primary data is the lack of a standard for simple tabular data sets. While complex binary data sets can be stored comfortably with the Hierarchical Data Format (HDF5) or the Network Common Data Format (netCDF) these formats burden too much overhead for small tabular data sets. The consequence is, that most scientists save their data in text files consisting of non-annotated bare columns of numbers. Because these data files are always written in the scientist's personal data format, which is rarely documented, the primary data is very often become lost after finishing the project. This continuously results in the recreation of primary data and thus unnecessary extra work.

In order to overcome this problem, we have invented the Full Metadata Format (FMF), which is a text based format taking into account the most basic needs of the average scientist. The grammar of FMF has been formallyformaly specified  with ANTLR and has been integrated into the Pyphant data analysis framework. This allows us to demonstrate the increase in research performance arising from the simple fact, that primary data is stored in a standardised way together with its meta data. The examples comprise the automatic visualization of data files with publication ready labelled diagrams, analysise of data sets with unit and error propagation, as well as automated data interpretation, which gives rise to new machine learning paradigmsparadigma for natural and engineering sciences. 

`Anchor(avesquivel)`_          

Intensive Python for Meshless Simulation
----------------------------------------

**by: Alcides Viamontes Esquivel**

Meshless methods are an emerging group of techniques for cutting edge PDE simulation, at problems where conventional Finite Element Method (FEM) falls short. In contraposition with FEM, Meshless evolved quite recently, in the Pythonic Age, long decades after the Spread of Fortran which at its moment gave raise to old good FEM. "NOMS", our framework for meshless simulation is built around two basic pillars: first, scientific computing have to be possible and enjoyable for non hard-core programmers, and second, fun should not sacrifice performance. This presentation is about the hat of tricks we have used to achieve those goals:

* Python let us code smarter routines in terms of how they process client input. It’s also the language where the general, outer workflow of the application gets coded. That’s good both for the developers and for the users of the framework.

* As usual, inner and expensive loops are implemented in a compiled language. We use C++ through Boost.Python. The numpy array class is powerful and Python-friendly, so many Python and C++ routines can accept their instances as input. There’s also a simple sparse matrix class implemented in C++ and some bindings for Boost.UBLAS, the TAUCS symmetric solver and the UMFPACK library for sparse systems.

* The nice trick in the realms of interoperability is the use of C++ STL template instantiations from Python. Through some extensions and adaptations of Boost.Python, that’s achieved in a uniform and automatic way. It allows, among other things, to use the ecient STL ordered map from Python, both for fixed combinations of key and value type in C++ or for the scripting Python object. The implementation wrapper exposes the usual dictionary interface and also allows the client to do both range and stabbing unidimensional queries on the map.

* The only missing detail for a good framework would be some mechanism for compiling complex formulas into something fast to calculate. The need arises for certain parts of the numerical model that our framework user should code. They are employed by the inner loops of the simulation algorithms, where performance is absolutely critical. After examining our choices, we decided to design our own, very simple and purpose-fitting functional language. The translator (compiler) for that functional language, including scanner-parser, construction of the internal AST, various optimization stages and code generation was implemented in Python.

Configuration, documentation, construction and deployment is also managed using this language, through SCons, Epydoc and a few custom modules coded by us. In all the cases, Python demonstrated to be a valuable

`Anchor(rcimrman)`_ 

SfePy - Simple Finite Elements in Python
----------------------------------------

**by: Robert Cimrman and  Ondøej Èertík**

[`http://sfepy.org`_ SfePy_] is an open source (BSD license) finite element analysis software designed to provide a flexible general finite element modeling tool which is easily adaptable to solve problems defined in terms of systems of PDEs. It is written almost exclusively in Python programming language, with a few time-demanding parts in C wrapped by the interface generator [`http://www.swig.org`_ SWIG]. Other notable features are its small size (complete sources are just about 1.2 MB, April 2008), fast compilation, problem description files in pure Python and problem description syntax similar to a mathematical description "on paper".

It relies primarily on [`http://scipy.org`_ NumPy/Scipy], [`http://pyparsing.wikispaces.com`_ Pyparsing], and optionally on [`http://matplotlib.sourceforge.net`_ Matplotlib] and [`http://pytables.sourceforge.net`_ Pytables].

Its research applications include: shape optimization of closed channels; multiscale modeling of a strongly heterogeneous porous media (e.g. muscles, bones, brain) by the theory of homogenization; modeling of so-called phononic materials, elastic periodic structures with strong heterogeneities in the elasticity: in the homogenized medium, negative eigenvalues of an effective mass tensor appear for certain frequency ranges, leading to so-called band gaps in acoustic wave propagation; a Schroedinger equation solver, that solves it for any potential in real space.

In the presentation we give a general information on SfePy, show a solution of a simple problem and mention some examples from the fields above. The code verification using the method of manufactured solutions (calculated by SymPy) is also discussed.

.. ############################################################################

.. _Anchor(kmueller): ../Anchor(kmueller)

.. _Anchor(jmartinek1): ../Anchor(jmartinek1)

.. _Anchor(jmartinek2): ../Anchor(jmartinek2)

.. _Anchor(bvoigt): ../Anchor(bvoigt)

.. _Anchor(ppeterson): ../Anchor(ppeterson)

.. _Anchor(jmrohwer): ../Anchor(jmrohwer)

.. _BiologyWorkbench: ../BiologyWorkbench

.. _Anchor(adalke): ../Anchor(adalke)

.. _Anchor(mmueller): ../Anchor(mmueller)

.. _PyModelData: ../PyModelData

.. _Anchor(mcroettger): ../Anchor(mcroettger)

.. _Anchor(dalbanese): ../Anchor(dalbanese)

.. _Anchor(kzimmermann): ../Anchor(kzimmermann)

.. _Anchor(avesquivel): ../Anchor(avesquivel)

.. _Anchor(rcimrman): ../Anchor(rcimrman)

.. _SfePy: ../SfePy

