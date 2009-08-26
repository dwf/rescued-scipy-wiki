#format rst

This package contains various functions for any-dimensional image processing.

See also `numarray.ndimage documentation <http://stsdas.stsci.edu/numarray/numarray-1.5.html/module-numarray.ndimage.html>`_.

Filters
-------

**Common parameters**

* *mode* - determines boundary conditions. Can be one of *nearest*, *wrap*, *reflect*, *constant* (from site-packages/scipy/ndimage/_ni_support.py).

* *cval* - (guessing/generalizing from a hint below) the value used when specifying the constant boundary condition

* *origin* - (guessing/generalizing from a hint below) controls the alignment of the weights with the image

* *axis* - the axis along which 1-D operations are performed.

-------------------------



  **correlate1d**(input, weights, axis=-1, output=None, mode='reflect', cval=0.0, origin=0)

  Calculate a one-dimensional correlation along the given axis. The lines of the array along the given axis are correlated with the given weights. The weights parameter must be a one-dimensional sequence of numbers.

**convolve1d**(input, weights, axis=-1, output=None, mode='reflect', cval=0.0, origin=0)

  Calculate a one-dimensional convolution along the given axis. The lines of the array along the given axis are convolved with the given weights. The weights parameter must be a one-dimensional sequence of numbers.

**gaussian_filter1d**(input, sigma, axis=-1, order=0, output=None, mode='reflect', cval=0.0)

  One-dimensional Gaussian filter. The standard-deviation of the Gaussian filter is given by sigma. An order of 0 corresponds to convolution with a Gaussian kernel. An order of 1, 2, or 3 corresponds to convolution with the first, second or third derivatives of a Gaussian. Higher order derivatives are not implemented.

**gaussian_filter**(input, sigma, order=0, output=None, mode='reflect', cval=0.0)

  Multi-dimensional Gaussian filter. The standard-deviations of the Gaussian filter are given for each axis as a sequence, or as a single number, in which case it is equal for all axes. The order of the filter along each axis is given as a sequence of integers, or as a single number. An order of 0 corresponds to convolution with a Gaussian kernel. An order of 1, 2, or 3 corresponds to convolution with the first, second or third derivatives of a Gaussian. Higher order derivatives are not implemented. Note: The multi-dimensional filter is implemented as a sequence of one-dimensional convolution filters. The intermediate arrays are stored in the same data type as the output. Therefore, for output types with a limited precision, the results may be imprecise because intermediate results may be stored with insufficient precision.

**prewitt**(input, axis=-1, output=None, mode='reflect', cval=0.0)

  Calculate a Prewitt filter.

**sobel**(input, axis=-1, output=None, mode='reflect', cval=0.0)

  Applies a Sobel filter to the input array. The result is stored in output, output needs to have the same shape as input. The axis parameter allows to define the orientation of the sobel filter, axis must not be larger than the dimensions or the input array (input.ndim):

  In the 2D case

  * axis = 1 uses

    |-1 0 1|

    |-2 0 2|

    |-1 0 1|

    . which is also the default behavior

  * axis = 0 uses

    |-1 -2 -1 |

    | 0    0   0 |

    | 1    2   1 |



**generic_laplace**(input, derivative2, output=None, mode='reflect', cval=0.0, extra_arguments=(), extra_keywords={})

  Calculate a multidimensional laplace filter using the provided second derivative function.  The derivative2 parameter must be a callable with the following signature:

    derivative2(input, axis, output, mode, cval, *extra_arguments, **extra_keywords)

  The extra_arguments and extra_keywords arguments can be used to pass extra arguments and keywords that are passed to derivative2 at each call.

**laplace**(input, output=None, mode='reflect', cval=0.0)

  Calculate a multidimensional laplace filter using an estimation for the second derivative based on differences.

**gaussian_laplace**(input, sigma, output=None, mode='reflect', cval=0.0)

  Calculate a multidimensional laplace filter using gaussian second derivatives. The standard-deviations of the Gaussian filter are given for each axis as a sequence, or as a single number, in which case it is equal for all axes.

**generic_gradient_magnitude**(input, derivative, output=None, mode='reflect', cval=0.0, extra_arguments=(), extra_keywords={})

  Calculate a gradient magnitude using the provdide function for the gradient. The derivative parameter must be a callable with the following signature:

    derivative(input, axis, output, mode, cval, *extra_arguments, **extra_keywords)

  The extra_arguments and extra_keywords arguments can be used to pass extra arguments and keywords that are passed to derivative2 at each call.

**gaussian_gradient_magnitude**(input, sigma, output=None, mode='reflect', cval=0.0)

  Calculate a multidimensional gradient magnitude using gaussian derivatives. The standard-deviations of the Gaussian filter are given for each axis as a sequence, or as a single number, in which case it is equal for all axes.

**correlate**(input, weights, output=None, mode='reflect', cval=0.0, origin=0)

  Multi-dimensional correlation of the two arrays *input* and *weights*. The array is correlated with the given kernel using exact calculation (i.e. not FFT). Method uses a numarray intermediate in ndimage/filters.py->_correlate_or_convolve library function.

**convolve**(input, weights, output=None, mode='reflect', cval=0.0, origin=0)

  Multi-dimensional convolution.The array is convolved with the given kernel.

**uniform_filter1d**(input, size, axis=-1, output=None, mode='reflect', cval=0.0, origin=0)

  Calculate a one-dimensional uniform filter along the given axis. The lines of the array along the given axis are filtered with a uniform filter of given size.

**uniform_filter**(input, size=3, output=None, mode='reflect', cval=0.0, origin=0)

  Multi-dimensional uniform filter. The sizes of the uniform filter are given for each axis as a sequence, or as a single number, in which case the size is equal for all axes. The multi-dimensional filter is implemented as a sequence of one-dimensional uniform filters. The intermediate arrays are stored in the same data type as the output. Therefore, for output types with a limited precision, the results may be imprecise because intermediate results may be stored with insufficient precision.

**minimum_filter1d**(input, size, axis=-1, output=None, mode='reflect', cval=0.0, origin=0)

  Calculate a one-dimensional minimum filter along the given axis. The lines of the array along the given axis are filtered with a minimum filter of given size.

**maximum_filter1d**(input, size, axis=-1, output=None, mode='reflect', cval=0.0, origin=0)

  Calculate a one-dimensional maximum filter along the given axis. The lines of the array along the given axis are filtered with a maximum filter of given size.

**minimum_filter**(input, size=None, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)

  Calculates a multi-dimensional minimum filter. Either a size or a footprint with the filter must be provided. An output array can optionally be provided. The origin parameter controls the placement of the filter. The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to 'constant'.

**maximum_filter**(input, size=None, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)

  Calculates a multi-dimensional maximum filter. Either a size or a footprint with the filter must be provided. An output array can optionally be provided. The origin parameter controls the placement of the filter. The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to 'constant'.

**rank_filter**(input, rank, size=None, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)

  Calculates a multi-dimensional rank filter. The rank parameter may be less then zero, i.e., rank = -1 indicates the larges element. Either a size or a footprint with the filter must be provided. An output array can optionally be provided. The origin parameter controls the placement of the filter. The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to 'constant'.

**median_filter**(input, size=None, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)

  Calculates a multi-dimensional median filter. Either a size or a footprint with the filter must be provided. An output array can optionally be provided. The origin parameter controls the placement of the filter. The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to 'constant'.

**percentile_filter**(input, percentile, size=None, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)

  Calculates a multi-dimensional percentile filter. The percentile parameter may be less then zero, i.e., percentile = -20 equals percentile = 80. Either a size or a footprint with the filter must be provided. An output array can optionally be provided. The origin parameter controls the placement of the filter. The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to 'constant'.

**generic_filter1d**(input, function, filter_size, axis=-1, output=None, mode='reflect', cval=0.0, origin=0, extra_arguments=(), extra_keywords={})

  Calculate a one-dimensional filter along the given axis. The function iterates over the lines of the array, calling the given function at each line. The arguments of the line are the input line, and the output line. The input and output lines are 1D double arrays. The input line is extended appropiately according to the filter size and  origin. The output line must be modified in-place with the result. The origin parameter controls  the placement of the filter. The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to 'constant'. The extra_arguments and extra_keywords arguments can be used to pass extra arguments and keywords that are passed to the function at each call.

**generic_filter**input, function, size=None, footprint=None, output=None, mode='reflect', cval=0.0, origin=0, extra_arguments=(), extra_keywords={})

  Calculates a multi-dimensional filter using the given function. At each element the provided function is called. The input values within the filter footprint at that element are passed to the function as a 1D array of double values. Either a size or a footprint with the filter must be provided. An output array can optionally be provided. The origin parameter controls the placement of the filter. The mode parameter

Fourier
-------

**fourier_gaussian**(input, sigma, n=-1, axis=-1, output=None)

  Multi-dimensional Gaussian fourier filter. The array is multiplied with the fourier transform of a Gaussian kernel. If the parameter n is negative, then the input is assumed to be the result of a complex fft. If n is larger or equal to zero, the input is assumed to be the result of a real fft, and n gives the length of the of the array before transformation along the the real transform direction. The axis of the real transform is given by the axis parameter.

**fourier_uniform**(input, size, n=-1, axis=-1, output=None)

  Multi-dimensional Uniform fourier filter. The array is multiplied with the fourier transform of a box of given sizes. If the parameter n is negative, then the input is assumed to be the result of a complex fft. If n is larger or equal to zero, the input is assumed to be the result of a real fft, and n gives the length of the of the array before transformation along the the real transform direction. The axis of the real transform is given by the axis parameter.

**fourier_ellipsoid**(input, size, n=-1, axis=-1, output=None)

  Multi-dimensional ellipsoid fourier filter. The array is multiplied with the fourier transform of a ellipsoid of given sizes. If the parameter n is negative, then the input is assumed to be the result of a complex fft. If n is larger or equal to zero, the input is assumed to be the result of a real fft, and n gives the length of the of the array before transformation along the the real transform direction. The axis of the real transform is given by the axis parameter. This function is implemented for arrays of rank 1, 2, or 3.

**fourier_shift**(input, shift, n=-1, axis=-1, output=None)

  Multi-dimensional fourier shift filter. The array is multiplied with the fourier transform of a shift operation. If the parameter n is negative, then the input is assumed to be the result of a complex fft. If n is larger or equal to zero, the input is assumed to be the result of a real fft, and n gives the length of the of the array before transformation along the the real transform direction. The axis of the real transform is given by the axis parameter.

Interpolation
-------------

**spline_filter1d**(input, order=3, axis=-1, output=<type 'numpy.float64'>, output_type=None)

  Calculates a one-dimensional spline filter along the given axis. The lines of the array along the given axis are filtered by a spline filter. The order of the spline must be >= 2 and <= 5.

**spline_filter**(input, order=3, output=<type 'numpy.float64'>, output_type=None)

  Multi-dimensional spline filter. Note: The multi-dimensional filter is implemented as a sequence of one-dimensional spline filters. The intermediate arrays are stored in the same data type as the output. Therefore, for output types with a limited precision, the results may be imprecise because intermediate results may be stored with insufficient precision.

**geometric_transform**(input, mapping, output_shape=None, output_type=None, output=None, order=3, mode='constant', cval=0.0, prefilter=True, extra_arguments=(), extra_keywords={})

  Apply an arbritrary geometric transform. The given mapping function is used to find, for each point in the output, the corresponding coordinates in the input. The value of the input at those coordinates is determined by spline interpolation of the requested order. *mapping* must be a callable object that accepts a tuple of length equal to the output array rank and returns the corresponding input coordinates as a tuple of length equal to the input array rank. Points outside the boundaries of the input are filled according to the given *mode* ('constant', 'nearest', 'reflect' or 'wrap'). The output shape can optionally be given. If not given, it is equal to the input shape. The parameter *prefilter* determines if the input is pre-filtered before interpolation (necessary for spline interpolation of order > 1).  If False it is assumed that the input is already filtered. The extra_arguments and extra_keywords arguments can be used to provide extra arguments and keywords that are passed to the mapping function at each call. Example usage:



    ::

       >>> a = arange(12.).reshape((4,3))
       >>> def shift_func(output_coordinates):
       ...     return (output_coordinates[0]-0.5, output_coordinates[1]-0.5)
       ...
       >>> print geometric_transform(a,shift_func)
       array([[ 0.    ,  0.    ,  0.    ],
              [ 0.    ,  1.3625,  2.7375],
              [ 0.    ,  4.8125,  6.1875],
              [ 0.    ,  8.2625,  9.6375]])

**map_coordinates**(input, coordinates, output_type=None, output=None, order=3, mode='constant', cval=0.0, prefilter=True)

  Apply an arbritrary coordinate transformation. The array of coordinates is used to find, for each point in the output, the corresponding coordinates in the input. The value of the input at that coordinates is determined by spline interpolation of the requested order. The shape of the output is derived from that of the coordinate array by dropping the first axis. The values of the array along the first axis are the coordinates in the input array at which the output value is found.  For example, if the input has dimensions (100,200,3), then the shape of coordinates will be (3,100,200,3), where ``coordinates[:,1,2,3]`` specify the input coordinate at which ``output[1,2,3]`` is found. Points outside the boundaries of the input are filled according to the given mode ('constant', 'nearest', 'reflect' or 'wrap'). The parameter prefilter determines if the input is pre-filtered before interpolation (necessary for spline interpolation of order > 1). If False it is assumed that the input is already filtered. Example usage:



    ::

       >>> a = arange(12.).reshape((4,3))
       >>> print a
       [[  0.   1.   2.]
        [  3.   4.   5.]
        [  6.   7.   8.]
        [  9.  10.  11.]]
       >>> output = map_coordinates(a,[[0.5, 2], [0.5, 1]],order=1)
       >>> print output
       [ 2. 7.]

  Here, the interpolated value of ``a[0.5,0.5]`` gives ``output[0]``, while ``a[2,1]`` is ``output[1]``.

**affine_transform**(input, matrix, offset=0.0, output_shape=None, output_type=None, output=None, order=3, mode='constant', cval=0.0, prefilter=True)

  Apply an affine transformation. The given matrix and offset are used to find for each point in the output the corresponding coordinates in the input by an affine transformation. The value of the input at those coordinates is determined by spline interpolation of the requested order. Points outside the boundaries of the input are filled according to the given mode. The output shape can optionally be given. If not given it is equal to the input shape. The parameter prefilter determines if the input is pre-filtered before interpolation, if False it is assumed that the input is already filtered. The matrix must be two-dimensional or can also be given as a one-dimensional sequence or array. In the latter case, it is assumed that the matrix is diagonal. A more efficient algorithms is then applied that exploits the separability of the problem.

**shift**(input, shift, output_type=None, output=None, order=3, mode='constant', cval=0.0, prefilter=True)

  Shift an array. The array is shifted using spline interpolation of the requested order. Points outside the boundaries of the input are filled according to the given mode. The parameter prefilter determines if the input is pre-filtered before interpolation, if False it is assumed that the input is already filtered.

**zoom**(input, zoom, output_type=None, output=None, order=3, mode='constant', cval=0.0, prefilter=True)

  Zoom an array. The array is zoomed using spline interpolation of the requested order. Points outside the boundaries of the input are filled according to the given mode. The parameter prefilter determines if the input is pre-filtered before interpolation, if False it is assumed that the input is already filtered.

**rotate**(input, angle, axes=(-1, -2), reshape=True, output_type=None, output=None, order=3, mode='constant', cval=0.0, prefilter=True)

  Rotate an array. The array is rotated in the plane defined by the two axes given by the axes parameter using spline interpolation of the requested order. The angle is given in degrees. Points outside the boundaries of the input are filled according to the given mode. If reshape is true, the output shape is adapted so that the input array is contained completely in the output. The parameter prefilter determines if the input is pre-filtered before interpolation, if False it is assumed that the input is already filtered.

Measurements
------------

**Common parameters**

* *index* - The index parameter is a single label number or a sequence of label numbers of the objects to be measured.

* *labels* - If index is None, all values are used where labels is larger than zero.

-------------------------



  **label**(input, structure=None, output=None)

  Label an array of objects. The structure that defines the object connections must be symmetric.  If no structuring element is provided an element is generated with a squared connectivity equal to one. This function returns a tuple consisting of the array of labels and the number of objects found. If an output array is provided only the number of objects found is returned.

**find_objects**(input, max_label=0)

  Find objects in a labeled array. The input must be an array with labeled objects. A list of slices into the array is returned that contain the objects. The list represents a sequence of the numbered objects. If a number is missing, None is returned instead of a slice. If max_label > 0, it gives the largest object number that is searched for, otherwise all are returned.

**sum**(input, labels=None, index=None)

  Calculate the sum of the values of the array.

**mean**(input, labels=None, index=None)

  Calculate the mean of the values of the array.

**variance**(input, labels=None, index=None)

  Calculate the variance of the values of the array.

**standard_deviation**(input, labels=None, index=None)

  Calculate the standard deviation of the values of the array.

**minimum**(input, labels=None, index=None)

  Calculate the minimum of the values of the array.

**maximum**(input, labels=None, index=None)

  Calculate the maximum of the values of the array.

**minimum_position**(input, labels=None, index=None)

  Find the position of the minimum of the values of the array.

**maximum_position**(input, labels=None, index=None)

  Find the position of the maximum of the values of the array.

**extrema**(input, labels=None, index=None)

  Calculate the minimum, the maximum and their positions of the values of the array.

**center_of_mass**(input, labels=None, index=None)

  Calculate the center of mass of of the array.

**histogram**(input, min, max, bins, labels=None, index=None)

  Calculate a histogram of of the array. The histogram is defined by its minimum and maximum value and the number of bins.

**watershed_ift**(input, markers, structure=None, output=None)

  Apply watershed from markers using a iterative forest transform algorithm. Negative markers are considered background markers which are processed after the other markers. A structuring element defining the connectivity of the object can be provided. If none is provided an element is generated iwth a squared connecitiviy equal to one. An output array can optionally be provided.

Morphology
----------

**Common parameters**

* An *output* array can optionally be provided.

* The *origin* parameter controls the placement of the filter.

* Either a *size* or a *footprint*, or the *structure* must be provided.

* The *mode* parameter determines how the array borders are handled...

* *cval* is the value when mode is equal to 'constant'.

-------------------------



  **iterate_structure**(structure, iterations, origin=None)

  Iterate a structure by dilating it with itself. If origin is None, only the iterated structure is returned. If not, a tuple of the iterated structure and the modified origin is returned.

**generate_binary_structure**(rank, connectivity)

  Generate a binary structure for binary morphological operations. The inputs are the rank of the array to which the structure will be applied and the square of the connectivity of the structure.

**binary_erosion**(input, structure=None, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)

  Multi-dimensional binary erosion with the given structure. If no *structuring* element is provided an element is generated with a squared connectivity equal to one. The *border_value* parameter gives the value of the array outside the border. The erosion operation is repeated *iterations* times. If iterations is less than 1, the erosion is repeated until the result does not change anymore. If a *mask* is given, only those elements with a true value at the corresponding mask element are modified at each iteration.

**binary_dilation**(input, structure=None, iterations=1, mask=None, output=None, border_value=0, origin=0, brute_force=False)

  Multi-dimensional binary dilation with the given structure. If no *structuring* element is provided an element is generated with a squared connectivity equal to one. The dilation operation is repeated *iterations* times.  If iterations is less than 1, the dilation is repeated until the result does not change anymore.  If a *mask* is given, only those elements with a true value at the corresponding mask element are modified at each iteration.

**binary_opening**(input, structure=None, iterations=1, output=None, origin=0)

  Multi-dimensional binary opening with the given structure. If no *structuring* element is provided an element is generated with a squared connectivity equal to one. The *iterations* parameter gives the number of times the erosions and then the dilations are done.

**binary_closing**(input, structure=None, iterations=1, output=None, origin=0)

  Multi-dimensional binary closing with the given structure. An *output* array can optionally be provided. The *origin* parameter controls the placement of the filter. If no *structuring* element is provided an element is generated with a squared connectivity equal to one. The *iterations* parameter gives the number of times the dilations and then the erosions are done.

**binary_hit_or_miss**(input, structure1=None, structure2=None, output=None, origin1=0, origin2=None)

  Multi-dimensional binary hit-or-miss transform. The *origin* parameters controls the placement of the structuring elements. If the first *structuring* element is not given one is generated with a squared connectivity equal to one. If the second *structuring* element is not provided, it set equal to the inverse of the first structuring element. If the *origin* for the second structure is equal to None it is set equal to the *origin* of the first.

**binary_propagation**(input, structure=None, mask=None, output=None, border_value=0, origin=0)

  Multi-dimensional binary propagation with the given structure. If no *structuring* element is provided an element is generated with a squared connectivity equal to one. If a *mask* is given, only those elements with a true value at the corresponding mask element are. This function is functionally equivalent to calling binary_dilation with the number of iterations less then one: iterative dilation until the result does not change anymore.

**binary_fill_holes**(input, structure=None, output=None, origin=0)

  Fill the holes in binary objects. If no *structuring* element is provided an element is generated with a squared connectivity equal to one.

**grey_erosion**(input, size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0)

  Calculate a grey values erosion.

**grey_dilation**(input, size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0)

  Calculate a grey values dilation.

**grey_opening**(input, size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0)

  Multi-dimensional grey valued opening.

**grey_closing**(input, size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0)

  Multi-dimensional grey valued closing.

**morphological_gradient**(input, size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0)

  Multi-dimensional morphological gradient.

**morphological_laplace**(input, size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0)

  Multi-dimensional morphological laplace.

**white_tophat**(input, size=None, footprint=None, structure=None, output=None, mode='reflect', cval=0.0, origin=0)

  Multi-dimensional white tophat filter.

**black_tophat**

**distance_transform_bf**(input, metric='euclidean', sampling=None, return_distances=True, return_indices=False, distances=None, indices=None)

  Distance transform function by a brute force algorithm. This function calculates the distance transform of the input, by replacing each background element (zero values), with its shortest distance to the foreground (any element non-zero). Three types of distance *metric* are supported: 'euclidean', 'city_block' and 'chessboard'. In addition to the distance transform, the feature transform can be calculated. In this case the index of the closest background element is returned along the first axis of the result. The *return_distances*, and *return_indices* flags can be used to indicate if the distance transform, the feature transform, or both must be returned. Optionally the sampling along each axis can be given by the *sampling* parameter which should be a sequence of length equal to the input rank, or a single number in which the sampling is assumed to be equal along all axes. This parameter is only used in the case of the euclidean distance transform. This function employs a slow brute force algorithm, see also the function distance_transform_cdt for more efficient city_block and chessboard algorithms. The *distances* and *indices* arguments can be used to give optional output arrays that must be of the correct size and type (Float64 and Int32).

**distance_transform_cdt**(input, structure='chessboard', return_distances=True, return_indices=False, distances=None, indices=None)

  Distance transform for chamfer type of transforms. The structure determines the type of chamfering that is done. If the *structure* is equal to 'cityblock' a structure is generated using generate_binary_structure with a squared distance equal to 1. If the *structure* is equal to 'chessboard', a structure is generated using generate_binary_structure with a squared distance equal to the rank of the array. These choices correspond to the common interpretations of the cityblock and the chessboard distance metrics in two dimensions. In addition to the distance transform, the feature transform can be calculated. In this case the index of the closest background element is returned along the first axis of the result. The *return_distances*, and *return_indices* flags can be used to indicate if the distance transform, the feature transform, or both must be returned. The *distances* and *indices* arguments can be used to give optional output arrays that must be of the correct size and type (both Int32).

**distance_transform_edt**(input, sampling=None, return_distances=True, return_indices=False, distances=None, indices=None)

  Exact euclidean distance transform. In addition to the distance transform, the feature transform can be calculated. In this case the index of the closest background element is returned along the first axis of the result. The *return_distances*, and *return_indices* flags can be used to indicate if the distance transform, the feature transform, or both must be returned. Optionally the sampling along each axis can be given by the *sampling* parameter which should be a sequence of length equal to the input rank, or a single number in which the sampling is assumed to be equal along all axes. The *distances* and *indices* arguments can be used to give optional output arrays that must be of the correct size and type (Float64 and Int32)

-------------------------



  CategorySciPyPackages_

