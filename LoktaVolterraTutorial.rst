#format rst

This example describes how to integrate ODEs with the scipy.integrate module, and how to use the matplotlib module to plot trajectories, direction fields and other information.

You can get the source code for this tutorial here: attachment:tutorial_lokta-voltera_v4.py .

Presentation of the Lotka-Volterra Model
----------------------------------------

We will have a look at the Lotka-Volterra model, also known as the predator-prey equations, which is a pair of first order, non-linear, differential equations frequently used to describe the dynamics of biological systems in which two species interact, one a predator and the other its prey. The model was proposed independently by Alfred J. Lotka in 1925 and Vito Volterra in 1926, and can be described by

::

   du/dt =  a*u -   b*u*v
   dv/dt = -c*v + d*b*u*v

