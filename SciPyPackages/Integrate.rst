#format rst

scipy.integrate
---------------

The package ``scipy.integrate`` does two things: integration (or quadrature), and solving differential equations.

Quadrature functions
--------------------

quadrature(func, a, b, args=(), tol=1.5e-8, maxiter=50)
  Integrate ``func`` from ``a`` to ``b`` using Gaussian quadrature with absolute tolerance ``tol``. ``args`` is extra arguments to pass to ``func``, and ``maxiter`` is the maximum number of iterations. Returns ``(val, err)``, where ``val`` is the Gaussian quadrature approximation, and ``err`` is the difference between the last two estimates of the integral.

romberg(function, a, b, tol=1.48e-8, show=0, divmax=10)
  Romberg integration of a callable function or method.

dblquad(func, a, b, gfun, hfun, args=(), epsabs=1.5e-8, epsrel=1.5e-8)
  Compute the double (definite) integral of ``func(y,x,*args)`` from x=``a``..``b`` and y=``gfun(x)``..``hfun(x)``. Returns ``(val, err)``.

tplquad(func, a, b, gfun, hfun, qfun, rfun, args=(), epsabs=1.5e-8, epsrel=1.5e-8)
  Compute the triple (definite) integral of ``func(z,y,x,*args)`` from x=``a``..``b``, y=``gfun(x)``..``hfun(x)``, and z=``qfun(x,y)``..``rfun(x,y)``. Returns ``(val, err)``.

quad(func, a, b, args=(), full_output=0, epsabs=1.49e-8, epsrel=1.49e-8, limit=50, points=None, weight=None, wvar=None, wopts=None, maxp1=50, limlst=50)
  Computes an integral using a technique from the Fortan library QUADPACK. The function is integrated from a to b. Run scipy.integrate.quad_explain() for more information on the more esoteric inputs and outputs.

Differential Equations
----------------------

``ode``, ``odeint``.

odeint(func, y0, t, args=(), Dfun=None, col_deriv=0, full_output=0, ml=None, mu=None, rtol=None, atol=None, tcrit=None, h0=0.0, hmax=0.0, hmin=0.0, ixpr=0, mxstep=0, mxhnil=0, mxordn=12, mxords=5, printmessg=0)

    Integrate a system of ordinary differential equations.

    ::

       #class right

       inline:odeint2.png

    ::

       from scipy import *
       from pylab import *
       deriv = lambda y,t : array([y[1],-y[0]])
       # Integration parameters
       start=0
       end=10
       numsteps=10000
       time=linspace(start,end,numsteps)
       from scipy import integrate
       y0=array([0.0005,0.2])
       y=integrate.odeint(deriv,y0,time)
       plot(time,y[:,0])
       show()

Another example of numerical integration of ODEs is given by [:LoktaVolterraTutorial_:"Integrating Lokta-Volterra equations with SciPy_"].

-------------------------

 CategorySciPyPackages_

