#format rst

In 1950, Taylor published two papers ([`http://adsabs.harvard.edu/abs/1950RSPSA.201..159T`_ The Formation of a Blast Wave by a Very Intense Explosion. I. Theoretical Discussion] and [`http://adsabs.harvard.edu/abs/1950RSPSA.201..175T`_ The Formation of a Blast Wave by a Very Intense Explosion. II. The Atomic Explosion of 1945], both of which I will follow closely). The first describes numerically the evolution of a blast wave, and the second uses declassified photographs to compute the energy released by the Trinity atomic bomb test. Evaluating the required integrals numerically was a laborious process in 1950, but it can be done quite straightforwardly now.

attachment:Trinity_explosion.jpg

A blast wave is a spherical shock that arises when a large amount of energy is deposited more or less instantaneously in a small volume of a homogeneous medium. The heated medium then expands, causing a spherical shock wave to propagate outward. The external pressure is assumed to be negligible compared to the density of kinetic energy near the shock front, and the Mach number of the shock is assumed to be high (a "strong shock"). These conditions are reasonably well satisfied by the explosion of a nuclear weapon, and they are also satisfied by a supernova explosion during certain phases of its evolution.

I will not go into the details of the solution any more than necessary. It proceeds by assuming the blast wave's evolution is self-similar, that is, the pressure (P), density (d), and velocity (v) profiles remain the same, simply scaling as the wave evolves. Specifically, when the blast has radius R, we assume that

  P(r/R)/P0 = R**(-3)*f1(r/R)

  d(r/R)/d0 = psi(r/R)

and

  u(r/R) = R**(-3./2)*phi1(r/R).

Let eta = r/R. We can rescale f1 and phi1 to make them unitless by defining

  f(eta) = f1(eta)*a**2/A**2

and

  phi(eta) = phi1(eta)/A,

where a is the speed of sound in the medium and A is a constant whose value depends on the energy of the explosion. These assumptions mean that the blast wave's pressure, density, and velocity profiles at all times are given by f, psi, and phi respectively; the actual values simply scale with R. The point of all this is that we can derive differential equations for f, psi, and phi depending only on the parameter gamma (the ratio of specific heats in the medium):

  phi'(eta) = (f'(eta)/(gamma*psi(eta)) - (3./2)*phi(eta))/(eta-phi(eta)) psi'(eta) = psi(eta)*(phi'(eta)+2*phi(eta)/eta)/(eta-phi(eta))

and

  f'(eta) = f(eta)*(-3*eta+phi(eta)*(3+gamma/2)-2*gamma*phi(eta)**2/eta)/((eta-phi(eta))**2-f/psi).

Given our assumptions, we can compute the following boundary conditions:

  psi(1) = (gamma+1)/(gamma-1) phi(1) = 2/(gamma+1)

and

  f(1) = 2*gamma/(gamma+1).

We can use scipy's odeint to integrate this system of ordinary differential equations inward from one to zero. First we must construct a "right-hand side" function that takes an eta and phi(eta), psi(eta), and f(eta) and returns the derivatives of each function:

::

   def RHS(eta,(phi, psi, f),gamma):
       fp = (f*
           (-3*eta+phi*(3+gamma/2)-2*gamma*phi**2/eta)/
           ((eta-phi)**2-f/psi))
       phip = (fp/(gamma*psi) - (3./2)*phi)/(eta-phi)
       psip = psi*(phip+2*phi/eta)/(eta-phi)
       return (phip, psip, fp)

Now we choose a gamma - for air, 1.4 is appropriate - and set up our code:

::

   import numpy as N
   import scipy.integrate
   gamma = 1.4
   etas = N.linspace(1,0,1000,endpoint=False)
   psi1 = (gamma+1)/(gamma-1)
   phi1 = 2/(gamma+1)
   f1 = 2*gamma/(gamma+1)

Now we ask scipy to integrate the differential equation for us. scipy.integrate.odeint takes a right-hand-side function and a set of initial conditions, and returns the solution to the ODE evaluated at each of the values of eta we supply. Note that our right-hand side takes an extra argument, gamma, so I will use a lambda expression to create a function with the correct calling conventions:

::

   ys = scipy.integrate.odeint(lambda y, eta: RHS(eta, y, gamma),
       (phi1, psi1, f1),
       etas)

odeint takes many more arguments than this - use help(scipy.integrate.odeint) to see them all - but they are for things like controlling how it decides when convergence has happened, or supplying an analytic derivative of the right-hand side to make the integrator more efficient. None are necessary for us.

The result returned by odeint is an array, three by a thousand. Each row is a value of psi, phi, and f corresponding to a particular eta. Let's plot the results:

::

   phis = ys[:,0]
   psis = ys[:,1]
   fs = ys[:,2]
   import pylab
   pylab.plot(etas,psis,label="psi")
   pylab.plot(etas,phis,label="phi")
   pylab.plot(etas,fs,label="f")
   pylab.legend(loc="best")
   pylab.xlabel("eta")
   pylab.show()

attachment:trinity-plots-small.png

However, we are interested in more than the shape of these functions; we would also like to be able to relate the total energy in the explosion and the growth of the blast wave. Some further calculation gives that

  E = B*d0*A**2

where B is a unitless constant depending only on gamma given by

  B = 2*pi*int(lambda eta: psi(eta)*phi(eta)**2*eta**2,0,1) + 4*pi/(gamma*(gamma-1))*int(lambda eta: f(eta)*eta**2,0,1).

In particular, we need to compute two integrals. We could go back through the calculation and put the integrals into our differential equation solver: simply introduce quantities I1 and I2. Then the derivative of I1 is just psi(eta)*phi(eta)**2*eta**2, for example. However, if we're lazy, we can simply use the values of psi, phi, and f that we already calculated and use Simpson's rule:

::

   I1 = -scipy.integrate.simps(psis*phis**2*etas**2,etas)
   I2 = -scipy.integrate.simps(fs*etas**2,etas)
   B = 2*N.pi*I1+4*N.pi/(gamma*(gamma-1))*I2

Note that since our etas are in decreasing order we are computing the integrals right-to-left and so we must flip the sign (hence the minus sign in the calculations above). Now, how do we calculate the energy of the Trinity explosion from a series of pictures? Well, the photographs included both time stamps and size marks, so Taylor was able to read off measurements:

::

   tRs = N.array([
   # ms    m
   (0.10, 11.1),
   (0.24, 19.9),
   (0.38, 25.4),
   (0.52, 28.8),
   (0.66, 31.9),
   (0.80, 34.2),
   (0.94, 36.3),
   (1.08, 38.9),
   (1.22, 41.0),
   (1.36, 42.8),
   (1.50, 44.4),
   (1.65, 46.0),
   (1.79, 46.9),
   (1.93, 48.7),
   (3.26, 59.0),
   (3.53, 61.1),
   (3.80, 62.9),
   (4.07, 64.3),
   (4.34, 65.6),
   (4.61, 67.3),
   (15.0, 106.5),
   (25.0, 130.0),
   (34.0, 145.0),
   (53.0, 175.0),
   (62.0, 185.0),
   ])
   ts = tRs[:,0]/1000. # convert to s
   Rs = tRs[:,1]*100 # convert to m

Times are in seconds, radii are in centimeters (the CGS system is endemic in astronomy).

The self-similar solution Taylor proposed predicts that R should grow like t**(2./5.). Let us verify that. First we will fit a straight line to the log t-log R relation. For simple least-squares fitting, we use scipy.linalg.lstsq; for information on its interface use help(scipy.linalg.lstsq). We want to write log10(Rs) as a matrix product A*[m,b], or at least, as closely as possible. The first column of A should be log10(ts), and the second should be all ones:

::

   import scipy.linalg
   A = N.hstack((N.log10(ts)[:,N.newaxis],N.ones(len(ts))[:,N.newaxis]))
   (m,b), resids, rank, s = scipy.linalg.lstsq(A,N.log10(Rs))

We can also try fitting a line of the slope theory predicts:

::

   C = N.mean(5./2 * N.log10(Rs) - N.log10(ts))

Now let's plot the points and the best-fit line:

::

   pylab.plot(N.log10(ts),N.log10(Rs),"+",label="data")
   pylab.plot(N.log10(ts),m*N.log10(ts)+b,label="best-fit line")
   pylab.plot(N.log10(ts),2./5.*N.log10(ts)+2./5.*C,label="prediction")
   pylab.legend(loc="best")
   pylab.xlabel("log10(ts)")
   pylab.ylabel("log10(Rs)")
   pylab.show()

attachment:trinity-data-small.png

Looks like the data fits the model pretty well (better than one would expect, as Taylor points out, since gamma changes significantly with temperature).

Finally, we have that

  A = 2./5.*R**(5./2.)*t**(-1)

in

  E = d0*A**2*B

so

::

   A = 2./5.*10**C
   E = 1.25e-3*A**2*B

in ergs, or

::

   E_tonnes = E/4.25e16

The final result, ``E_tonnes``, is 16075 tonnes of TNT. This is smaller than the usual figure, 20 kilotons, in part because it ignores any energy that was radiated away.

attachment:taylor.py

