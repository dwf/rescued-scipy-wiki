def RHS(eta,(phi, psi, f),gamma):
    fp = (f*
        (-3*eta+phi*(3+gamma/2)-2*gamma*phi**2/eta)/
        ((eta-phi)**2-f/psi))
    phip = (fp/(gamma*psi) - (3./2)*phi)/(eta-phi)
    psip = psi*(phip+2*phi/eta)/(eta-phi)
    return (phip, psip, fp)

import numpy as N
import scipy.integrate

gamma = 1.4
etas = N.linspace(1,0,1000,endpoint=False)
print "gamma:",gamma

psi1 = (gamma+1)/(gamma-1)
phi1 = 2/(gamma+1)
f1 = 2*gamma/(gamma+1)

ys = scipy.integrate.odeint(lambda y, eta: RHS(eta, y, gamma),
    (phi1, psi1, f1),
    etas)

phis = ys[:,0]
psis = ys[:,1]
fs = ys[:,2]

import pylab
pylab.figure(1)
pylab.plot(etas,psis,label="psi")
pylab.plot(etas,phis,label="phi")
pylab.plot(etas,fs,label="f")
pylab.legend(loc="best")
pylab.xlabel("eta")

I1 = -scipy.integrate.simps(psis*phis**2*etas**2,etas)
I2 = -scipy.integrate.simps(fs*etas**2,etas)
B = 2*N.pi*I1+4*N.pi/(gamma*(gamma-1))*I2
print "B: ",B

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

import scipy.linalg
A = N.hstack((N.log10(ts)[:,N.newaxis],N.ones(len(ts))[:,N.newaxis]))
(m,b), resids, rank, s = scipy.linalg.lstsq(A,N.log10(Rs))

C = N.mean(5./2 * N.log10(Rs) - N.log10(ts))

pylab.figure(2)
pylab.plot(N.log10(ts),N.log10(Rs),"+",label="data")
pylab.plot(N.log10(ts),m*N.log10(ts)+b,label="best-fit line")
pylab.plot(N.log10(ts),2./5.*N.log10(ts)+2./5.*C,label="prediction")
pylab.legend(loc="best")
pylab.xlabel("log10(ts)")
pylab.ylabel("log10(Rs)")

A = 2./5.*10**C
E = 1.25e-3*A**2*B

E_tonnes = E/4.25e16
print "E_tonnes:", E_tonnes
pylab.show()
