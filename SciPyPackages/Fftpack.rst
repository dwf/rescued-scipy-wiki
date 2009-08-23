#format rst

scipy.fftpack
-------------

The package ``scipy.fftpack`` does two things: fast Fourier transforms, and differentiation and integration of periodic sequences.

Fast Fourier Transforms
-----------------------

The fft() function can be used by importing scipy, ie import scipy * However, other functions such as fft2 and the helper functions require the import of fftpack explicitly.  

fft(a)
  performs an Fourier transform on the array **a** and returns a complex array

ifft()
  Inverse of fft

fftn()
  Multi-dimensional FFT

ifftn()
  Inverse of fftn

fft2()
  2D FFT

ifft2()
  Inverse of fft2

rfft()
  FFT of real periodic sequences

irfft()
  Inverse of rfft

Differential and pseudo-differential operators
----------------------------------------------

Helper functions
----------------

The helper functions have to be imported explicitly to be able to use them. That is import scipy * is not enough, import scipy.fftpack is required

fftshift()
  Shift zero-frequency component to the centre of the spectrum

ifftshift()
  Inverse of fftshift

dftfreq()

rfftfreq()

Extension modules
-----------------

