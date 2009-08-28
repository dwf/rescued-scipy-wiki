#format rst

AutoDockTools
-------------

-------------------------

 **Using** AutoDock **with** AutoDockTools**: A Tutorial**

*Ruth Huey, Garrett M. Morris, Michel Sanner*

*Molecular Biology, The Scripps Research Institute, La Jolla, CA 92037*

AutoDock is a computational chemistry program for automated docking of flexible ligands to proteins (Morris et al., 1998). It has applications in computer-aided drug design, protein crystallography and even protein-protein docking. It uses a hybrid search algorithm combining a global search using a genetic algorithm with a local search method. The search attempts to find docked conformations at the global minimum of an empirical free energy scoring function.

AutoDockTools (ADT) is a Python-based graphical user interface for setting up input files for AutoDock and analyzing results of docking experiments. It extends the Python Molecular Viewer (PMV). ADT simplifies setting up the flexibility of the ligand by allowing the user to point and click on bonds in the molecule. The extent and location of the 3-D search space can be defined visually and interactively. Subsequent AutoDock searches result in low energy conformations of the ligand in favourable binding pockets on the macromolecule. ADT facilitates the analysis and visualization of not just these docked structures in a variety of useful ways, but also isocontours the underlying affinity maps for various atom types, thus helping to guide synthetic chemists in the next iteration of drug design.

