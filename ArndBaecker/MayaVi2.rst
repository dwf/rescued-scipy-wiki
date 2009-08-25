#format rst

<strong class="highlight">.. raw:: html

</strong>[Table not converted]

.. raw:: html
   <h1>MayaVi2</h1>


<p><a class="http reference external" href="http://www.enthought.com/enthought/wiki/MayaVi">MayaVi2</a> is the successor of <a class="http reference external" href="http://mayavi.sf.net/">MayaVi</a>
for 3D visualization.</p>
<div class="section" id="get-and-build">
<h3>Get and build</h3>
<p>Most authorative instructions are
here <a class="http reference external" href="http://www.enthought.com/enthought/wiki/GrabbingAndBuilding">http://www.enthought.com/enthought/wiki/GrabbingAndBuilding</a></p>
<p>For the impatient:</p>
::

svn co http://svn.enthought.com/svn/enthought/trunk enthought
cd enthought/src/lib/
ENTHOME=$PWD<p>Note that this imports the whole enthought tree - which is
pretty big, around 260MB because of all the subversion info.</p>
<p>Optional: Before the build you can do the folllowing to skip some packages:</p>
::

cd $ENTHOME/enthought/
$EDITOR setup.py &amp;

#  comment out the following
ext_modules = [#&quot;kiva/agg/setup_agg.py&quot;,
               #&quot;freetype/setup_freetype.py&quot;,
               #&quot;interpolate/setup_interpolate.py&quot;,
               &quot;util/setup_util.py&quot;,
               &quot;traits/setup_traits.py&quot;,
               &quot;tvtk/setup_tvtk.py&quot;,
               #&quot;chaco/setup_chaco.py&quot;
              ]<p>Build with:</p>
::

cd $ENTHOME/enthought/
python setup.py build_src build_clib build_ext --inplace<p>which does not take very long.</p>
<div class="section" id="running-mayavi2">
<h4>Running MayaVi2</h4>
<p>Extend your python path (assuming bash shell syntax):</p>
::

export PYTHONPATH=$ENTHOME:$PYTHONPATH<p>To start:</p>
::

cd $ENTHOME/enthought/mayavi/scripts/
./mayavi2<p>Examples are under:</p>
::

cd $ENTHOME/enthought/mayavi/examples
python nongui.py
python numeric_source.py</div>
<div class="section" id="tvtk-examples">
<h4>tvtk examples</h4>
<p>tvtk stands for traited VTK and provides the whole basis for MayaVi2's visualization,
see <cite>http://www.enthought.com/enthought/wiki/TVTK</cite>
and the excellent <a class="http reference external" href="http://www.enthought.com/enthought/wiki/TVTKIntroduction">tvtk introduction</a>
for more details.</p>
<p>Examples:</p>
::

cd  $ENTHOME/enthought/tvtk/examples
python simple.py
python array_animation.py
python ivtk_example.py<p>In particular, have a look at mlab.py:</p>
::

cd  $ENTHOME/enthought/tvtk/tools
python mlab.py<p>(note that this example has a large number of polygons, so it might feel sluggish on slower machines).</p>
</div>
</div>
A simple example to visualize some function  inline:simple_tvtk_surface.py 

