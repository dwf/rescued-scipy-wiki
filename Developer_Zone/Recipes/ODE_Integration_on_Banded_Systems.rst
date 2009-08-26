#format rst

This was sent in an email from Jesper Friis to the scipy-dev mailing list on 2006-03-06 titled "Test case for integrate/ode.py: banded systems"

-------------------------

 I hope this is the correct place to post messages like this. Last Friday I submitted a small patch for integrate/ode.py making it working for banded systems. I have now successfully applied the solver to the banded example problem included in the cvode package. The attached script might both work as a test and as an example on how to solve banded systems.

I think, especially the following comment considering the Jacobian might be of general interest:

::

       # The Jacobian.
       # For banded systems this function returns a matrix pd of
       # size ml+mu*2+1 by neq containing the partial derivatives
       # df[k]/du[u]. Here f is the right hand side function in
       # udot=f(t,u), ml and mu are the lower and upper half bandwidths
       # and neq the number of equations.  The derivatives df[k]/du[l]
       # are loaded into pd[mu+k-l,k], i.e. the diagonals are loaded into
       # the rows of pd from top down (fortran indexing).
       #
       # Confusingly, the number of rows VODE expect is not ml+mu+1, but
       # given by a parameter nrowpd, which unfortunately is left out in
       # the python interface. However, it seems that VODE expect that
       # nrowpd = ml+2*mu+1. E.g. for our system with ml=mu=5 VODE expect
       # 16 rows. Fortunately the f2py interface prints out an error if
       # the number of rows is wrong, so as long ml and mu are known in
       # beforehand one can always determine nrowpd by trial and error...

Regards /Jesper

::

   #!/usr/bin/env python
   # Test provided provided by Jesper Friis, <jesper.friis@material.ntnu.no>
   from scipy import arange,zeros,exp
   from scipy.integrate import ode
   def test_ode_banded():
       """Banded example copied from CVODE.

       The following is a simple example problem with a banded Jacobian,
       with the program for its solution by CVODE.
       The problem is the semi-discrete form of the advection-diffusion
       equation in 2-D:
         du/dt = d2 u / dx2 + 0.5 du/dx + d2 u / dy2
       on the rectangle 0 <= x <= 2, 0 <= y <= 1, and the time
       interval 0 <= t <= 1.  Homogeneous Dirichlet boundary conditions
       are posed, and the initial condition is
         u(x,y,t=0) = x(2-x)y(1-y)exp(5xy) .
       The PDE is discretized on a uniform MX+2 by MY+2 grid with
       central differencing, and with boundary values eliminated,
       leaving an ODE system of size NEQ = MX*MY.
       Assuming that MY < MX a minimum bandwidth banded system can be
       constructed by arranging the grid points along columns. This
       results in the lower and upper bandwidths ml = mu = MY.
       This function solves the problem with the BDF method, Newton
       iteration with the VODE band linear solver, and a user-supplied
       Jacobian routine. It uses scalar relative and absolute tolerances.
       Output is printed at t = 0., .1, .2, ..., 1.
       """
       # Some constants
       xmax = 2.0              # domain boundaries
       ymax = 1.0
       mx = 10                 # mesh dimensions
       my = 5
       dx = xmax/(mx+1.)       # grid spacing
       dy = ymax/(my+1.)
       neq = mx*my             # number of equations
       mu = my                 # half bandwidths
       ml = my
       atol = 1.e-5            # scalar absolute tolerance
       nrowpd = ml+2*mu+1      # number of rows in storage of banded Jacobian
       x = dx*(arange(mx)+1.0) # inner grid points
       y = dy*(arange(my)+1.0)
       t = 0.1*arange(11)      # the times we want to print the solution
       # The right hand side function in udot = f(t,u)
       def f(t,u):
           for j in range(mx):
               for i in range(my):
                   # Get index of gridpoint i,j in u and udot
                   k = j*my+i
                   # Extract u at x_j, y_i and four neighboring points
                   ult = urt = uup = udn = 0.0
                   uij = u[k]
                   if j>0:    ult = u[k-my]
                   if j<mx-1: urt = u[k+my]
                   if i>0:    uup = u[k-1]
                   if i<my-1: udn = u[k+1]
                   # Set diffusion and advection terms and load into udot
                   hdiff = (ult - 2.0*uij + urt)/(dx*dx)
                   vdiff = (uup - 2.0*uij + udn)/(dy*dy)
                   hadv  = 0.5*(urt - ult)/(2.0*dx)
                   udot[j*my+i] = hdiff + hadv + vdiff
           return udot
       # The Jacobian.
       # For banded systems this function returns a matrix pd of
       # size ml+mu*2+1 by neq containing the partial derivatives
       # df[k]/du[u]. Here f is the right hand side function in
       # udot=f(t,u), ml and mu are the lower and upper half bandwidths
       # and neq the number of equations.  The derivatives df[k]/du[l]
       # are loaded into pd[mu+k-l,k], i.e. the diagonals are loaded into
       # the rows of pd from top down (fortran indexing).
       #
       # Confusingly, the number of rows VODE expect is not ml+mu+1, but
       # given by a parameter nrowpd, which unfortunately is left out in
       # the python interface. However, it seems that VODE expect that
       # nrowpd = ml+2*mu+1. E.g. for our system with ml=mu=5 VODE expect
       # 16 rows. Fortunately the f2py interface prints out an error if
       # the number of rows is wrong, so as long ml and mu are known in
       # beforehand one can always determine nrowpd by trial and error...
       def jac(t,u):
           # The components of u that f[i,j] = udot_ij depends on are:
           # u[i,j], u[i,j-1], u[i,j+1], u[i-1,j] and u[i+1,j], with
           #   df[i,j]/du[i,j]   = -2 (1/dx2 + 1/dy2),          l=k
           #   df[i,j]/du[i,j-1] = 1/dx2 - .25/dx,       j>0,    l=k-my
           #   df[i,j]/du[i,j+1] = 1/dx2 + .25/dx,       j<MX-1, l=k+my
           #   df[i,j]/du[i-1,j] = 1/dy2                 i>0,    l=k-1
           #   df[i,j]/du[i+1,j] = 1/dy2                 i<MY-1, l=k+1
           # where k=j*my+i.
           for j in range(mx):
               for i in range(my):
                   k = j*my+i
                   pd[mu,k] = -2.0*(1.0/(dx*dx) + 1.0/(dy*dy))
                   if j > 0:    pd[mu-my,k] = 1.0/(dx*dx) + 0.25/dx
                   if j < mx-1: pd[mu+my,k] = 1.0/(dx*dx) + 0.25/dx
                   if i > 0:    pd[mu-1,k]  = 1.0/(dy*dy)
                   if k < my-1: pd[mu+1,k]  = 1.0/(dy*dy)
           return pd
       # Initial value
       u = zeros(neq,float)
       for j in range(mx):
           u[j*my:(j+1)*my] = x[j]*(xmax - x[j])*y*(ymax - y)*exp(5*x[j]*y)
       # Allocate global work arrays pd and udot
       pd   = zeros((nrowpd,neq),float)
       udot = zeros(neq,float)
       # Solve the problem
       print "2-D advection-diffusion equation, mesh dimensions =%3d %3d" %(mx,my)
       print "Banded solution, bandwidth = %d" % (ml+mu+1)
       r = ode(f, jac)
       r.set_integrator('vode',atol=atol,lband=ml,uband=mu,method='bdf')
       r.set_initial_value(u, t=t[0])
       print 'At t=%4.2f    max.norm(u) = %-12.4e'%(r.t, max(u))
       for tout in t[1:]:
           u = r.integrate(tout)
           print 'At t=%4.2f    max.norm(u) = %-12.4e'%(r.t, max(u))
           if not r.successful():
               print "An error occurred during integration"
               break
   test_ode_banded()

