#format rst

ETS Issues To be resolved
=========================

These are things I want to see fixed (or fix myself) inorder to make ETS the "ultimate" tool for developing scientific Apps.

* A set of matplotlib-based PlotItems, to give users a simple way to make plots AND get presentation quality output. These should work with the current enthought-python-distribution. This is a tempory measure until chaco is fully ready.

* Make a nicer ArrayViewer, based on a wxGrid control

* Fix up SVG export (this is preferable to PDF) in Chaco/kiva

* High-res bitmap export (fixed in Trunk apparently) in Chaco/kiva

* PlotItem classes based on chaco

* Make a set of CursorTools for chaco

* Py2exe integration. Comments on the mailing lists indicate ETS doesn't play well with py2exe.

* Mlab/TVTK PlotItems

* OpenGL backend for chaco/kiva

* Package distribution. How to get these changes "to the masses" (or to my users, at least!). The release cycle for EPD is long. How about a time-based release schedule: it's well proven for other open-source projects. A local egg-repository may be the best option.

* Documentation. This is the really big issue for ETS. To really get a good userbase going, and glossy textbook is invaluable (and might even prove profitable). VTK and Blender are both examples of OSS projects which have spawned textbook to get effect. A printed book does wonders for the credibility of a project. The Numpy book is a less good example as it is written too much like a reference document and less like a student textbook.

that's all I can think of right now! There's still other areas of ETS I havn't looked into, like Envisage/charm/pyface.

