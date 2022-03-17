'''
_________________________________________________________
|					TABLE 	OF 	CONTENT					|
 -------------------------------------------------------
|	1. Introduction	to Numpy Library					|
|	2. Importing Numpy 									|
|	3. Data type 										|
|	4. Creating Arrays									|
|	5. Indexing and Slicing								|
|	6. 							|
|________________________________________________________
'''

'''			
				1. NumPy library
'''

NumPy = """
# In Scientific computing environment, efficient data structures for working with arrays are provided by the 
NumPy library.

# Difference between NumPy and Python list
- Python lists are generic containers of objects, NumPy arrays are homogenous and typed arrays of fixed size. 
- Homogenous means that all elements in the array have the same data type. 
- Fixed size means that an array cannot be resized

# NumPy provides a large collection of basic operators and functions that act on these data structures, 
as well as submodules with higher-level algorithms such as linear algebra and fast Fourier transform.
"""
'''
					2. Importing the Modules
'''
import numpy as np
'''
					3. The NumPy Array Object
'''
# The main data structure for multidimensional arrays in NumPy is the ndarray class.
# data structure also contains important metadata about the array, such as:
NUMPY_ATTRIBUTES = '''
1. Shape 	-	A tuple that contains the number of elements (i.e., the length) for each dimension (axis) of the array.
2. Size 	-	The total number elements in the array.
3. Ndim		- 	Number of dimensions (axes). 
4. nbytes	- 	Number of bytes used to store the data.
5. dtype 	-	The data type of the elements in the array

'''

data = np.array([[1, 2], [3, 4], [5, 6]])
type(data) 	# <class 'numpy.ndarray'>
print(data)
			# array([[1, 2],
			#        [3, 4],
			#        [5, 6]])

data.ndim 	# 2
data.shape 	# (3, 2)
data.size 	# 6
data.dtype  # dtype('int64')
data.nbytes # 48

'''
					4. Data Types
'''

# dtype attribute of the ndarray object describes the data type of each element in the array. They Include:
NUMPY_DATATYPES = '''
1. int		- (int8, int16, int32, int64) 			- Integers
2. uint 	- (uint8, uint16, uint32, uint64) 		- Unsigned (nonnegative) integers
3. bool 	- (Bool) 								- Boolean (True or False)
4. float 	- (float16, float32, float64, float128) - Floating-point numbers
5. complex 	- (complex64, complex128, complex256) 	- Complex-valued floating-point numbers
'''

# it is often necessary to explicitly choose whether to use arrays of integers, floating-point numbers, or complex values.
np.array([1, 2, 3], dtype=np.int)		# array([1, 2, 3])

np.array([1, 2, 3], dtype=np.float)		# array([ 1.,  2.,  3.])

np.array([1, 2, 3], dtype=np.complex)	# array([ 1.+0.j,  2.+0.j,  3.+0.j])


# Once a NumPy array is created, its dtype cannot be changed, other than by creating a new copy with type-casted array values.
data = np.array([1, 2, 3], dtype=np.float)
print(data)				# array([ 1.,  2.,  3.])
data.dtype 				# dtype('float64')

data = np.array(data, dtype=np.int)
data.dtype 				# dtype('int64')
print(data) 			# array([1, 2, 3])

# creating a new copy with  using the astype method of the ndarray class
data = np.array([1, 2, 3], dtype=np.float)
print(data) 			# array([ 1.,  2.,  3.])
data.astype(np.int)		# array([1, 2, 3])

# When computing with NumPy arrays, the data type might get promoted from one type to another, 
# if required by the operation. For example:
d1 = np.array([1, 2, 3], dtype=float)
d2 = np.array([1, 2, 3], dtype=complex)
d1 + d2 				# array([ 2.+0.j,  4.+0.j,  6.+0.j])
(d1 + d2).dtype 		# dtype('complex128')


'''
Using the np.sqrt function to compute the square root of each element in an array 
gives different results depending on the data type of the array. 
Only when the data type of the array is complex is the square root of –1 resulting in 
the imaginary unit (denoted as 1j in Python).
'''
In [26]: np.sqrt(np.array([-1, 0, 1]))
Out[26]: RuntimeWarning: invalid value encountered in sqrt
         array([ nan,   0.,   1.])
In [27]: np.sqrt(np.array([-1, 0, 1], dtype=complex))
Out[27]: array([ 0.+1.j,  0.+0.j,  1.+0.j])



# Real and Imaginary Parts

# Regardless of the value of the dtype attribute, all NumPy array instances have the attributes
# real and imag for extracting the real and imaginary parts of the array, respectively:
data = np.array([1, 2, 3], dtype=complex)
print(data)		# array([ 1.+0.j,  2.+0.j,  3.+0.j])
data.real 		# array([ 1.,  2.,  3.])
data.imag 		# array([ 0.,  0.,  0.])
# The same functionality is also provided by the functions np.real and np.imag

# Order of Array Data in Memory
# Two-dimensional array, containing rows and columns: possible way to store this array: 

# row-major format
# as a consecutive sequence of values is to store the rows after each other.
# A NumPy array can be specified to be stored in row-major format, using the keyword argument order= 'C', 
# This is the default format.

# column-major format.
# store the columns one after another. The former is
# A NumPy array can be specified to be stored in column-major format, using the keyword argument order= 'F', 

# the NumPy array attribute ndarray.strides defines exactly how mapping is done. 
# The strides attribute is a tuple of the same length as the number of axes (dimensions) of the array.


'''
				5. Creating Arrays
'''
# 5.1 - A summary of frequently used array-generating functions

ARRAY_GENERATING_FUNCTIONS = '''
1. np.array - 	Creates an array for which the elements are given by an array-like object, which, for example, 
				can be a (nested) Python list, a tuple, an iterable sequence, or another ndarray instance.

2. np.zeros -	Creates an array with the specified dimensions and data type that is filled with zeros.

3. np.ones 	-	Creates an array with the specified dimensions and data type that is filled with ones.

4. np.diag 	-	Creates a diagonal array with specified values along the diagonal and zeros elsewhere.

5. np.arange - 	Creates an array with evenly spaced values between the specified start, end, 
				and increment values.

6. np.linspace -	Creates an array with evenly spaced values between specified start and end values, 
					using a specified number of elements.

7. np.logspace	-	Creates an array with values that are logarithmically spaced between the given start 
					and end values.

8. np.meshgrid -	Generates coordinate matrices (and higher-dimensional coordinate arrays) from 
					one-dimensional coordinate vectors.

9. np.fromfunction -	Creates an array and fills it with values specified by a given function, 
						which is evaluated for each combination of indices for the given array size.

10. np.fromfile -	Creates an array with the data from a binary (or text) file. NumPy also provides 
					a corresponding function np.tofile with which NumPy arrays can be stored to disk and 
					later read back using np.fromfile.

11. np.genfromtxt, np. -	Create an array from data read from a text file, for example, a comma-loadtxt
							separated value (CSV) file. The function np.genfromtxt also supports data files 
							with missing values.

12. np.random.rand -	Generates an array with random numbers that are uniformly distributed between 0 and 1. 
						Other types of distributions are also available in the np.random module.
'''


# 5.2 - Arrays Created from Lists and Other Array-Like Objects

# np.array function
np.array([1, 2, 3, 4]) 
				# array([ 1,  2,  3, 4])
data.ndim 		# 1
data.shape 		# (4,)

np.array([[1, 2], [3, 4]]) 
				# array([[1,  2],
              	#		[3, 4]])
data.ndim 		# 2
data.shape 		# (2, 2)


# 5.3 - Arrays Filled with Constant Values

# The functions np.zeros and np.ones create and return arrays filled with zeros and ones, respectively.
np.zeros((2, 3))
				# array([[ 0.,  0.,  0.],
                #		[ 0.,  0.,  0.]])
np.ones(4)		# array([ 1.,  1.,  1., 1.])

data = np.ones(4)
data.dtype 		# dtype('float64')
data = np.ones(4, dtype=np.int64)
data.dtype 		# dtype('int64')

# An array filled with an arbitrary constant value can be generated by first creating an array filled 
# with ones and then multiplying the array with the desired fill value.
x1 = 5.4 * np.ones(10)
print(x1) 		# array([5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4])

# However, NumPy also provides the function np.full that does exactly this in one step. 
x2 = np.full(10, 5.4)
print(x1) 		# array([5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4])

# An already created array can also be filled with constant values using the np.fill function, 
# which takes an array and a value as arguments, and set all elements in the array to the given value.
x1 = np.empty(5)
x1.fill(3.0)
print(x1) 		# array([ 3.,  3.,  3.,  3.,  3.])

x2 = np.full(5, 3.0)
print(x2)   	# array([ 3.,  3.,  3.,  3.,  3.])



# 5.4 - Arrays Filled with Incremental Sequences

# np.arange and np.linspace function - Both functions take three arguments, 
# where the first two arguments are the start and end values. 
# The third argument of np.arange is the increment, 
# while for np.linspace it is the total number of points in the array.
# For example, to generate arrays with values between 1 and 10, with increment 1,:
np.arange(0.0, 10, 1)
# array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])
np.linspace(0, 10, 11)
# array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.,  10.])


# 5.5 Arrays Filled with Logarithmic Sequences

'''The function np.logspace is similar to np.linspace, but the increments between the elements 
in the array are logarithmically distributed, and the first two arguments, for the start and end values, 
are the powers of the optional base keyword argument (which defaults to 10). 
''' 
# For example, to generate an array with logarithmically distributed values between 1 and 100, we can use
np.logspace(0, 2, 5)  # 5 data points between 10**0=1 to 10**2=100
# array([ 1. , 3.16227766, 10. , 31.6227766 , 100.])


# 5.6 Meshgrid Arrays

# Multidimensional coordinate grids can be generated using the function np.meshgrid, 
# Given two one-dimensional coordinate arrays
x = np.array([-1, 0, 1])
y = np.array([-2, 0, 2])
X, Y = np.meshgrid(x, y)
print(X)
			# array([[-1,  0,  1],
            #    	[-1,  0,  1],
            #    	[-1,  0,  1]])
print(Y)
			# array([[-2, -2, -2],
            #	    [ 0,  0,  0],
            #	    [ 2,  2,  2]])
# Alternatively, the functions np.mgrid and np.ogrid can also be used to generate coordinate arrays, 
# using a slightly different syntax based on indexing and slice objects.


# 5.7 Creating Uninitialized Arrays

# To create an array of specific size and data type, but without initializing the elements in
# the array to any particular values, we can use the function np.empty.
np.empty(3, dtype=np.float)

# 5.8 Creating Arrays with Properties of Other Arrays

# create new arrays that share properties, such as shape and data type, with another array. 
# NumPy provides a family of functions for this purpose: np.ones_like, np.zeros_like, np.full_like, and np.empty_like.

# use case
def f(x):
    y = np.ones_like(x)
    # compute with x and y
    return y

# 5.8 Creating Matrix Arrays

# Function np.identity generates a square matrix with ones on the diagonal and zeros elsewhere:
np.identity(4)
		# array([[ 1.,  0.,  0.,  0.],
        #        [ 0.,  1.,  0.,  0.],
        #        [ 0.,  0.,  1.,  0.],
        #        [ 0.,  0.,  0.,  1.]])

# The similar function numpy.eye generates matrices with ones on a diagonal
In [63]: np.eye(3, k=1)
Out[63]: array([[ 0.,  1.,  0.],
                [ 0.,  0.,  1.],
                [ 0.,  0.,  0.]])
In [64]: np.eye(3, k=-1)
Out[64]: array([[ 0.,  0.,  0.],
                [ 1.,  0.,  0.],
                [ 0.,  1.,  0.]])

# we can use the np.diag function (which also takes the optional keyword argument k to
# specify an offset from the diagonal), as demonstrated here:
In [65]: np.diag(np.arange(0, 20, 5))
Out[65]: array([[0,  0,  0,  0],
                [0,  5,  0,  0],
                [0,  0, 10,  0],
                [0,  0,  0, 15]])
'''third argument to the np.arange function, which specifies the step size in the enumeration of elements 
in the array returned by the function. The resulting array therefore contains the values [0, 5, 10, 15], 
which is inserted on the diagonal of a two-dimensional matrix by the np.diag function.'''

'''
 				6. Indexing and Slicing
'''
# Elements and subarrays of NumPy arrays are accessed using the standard square bracket notation 
# that is also used with Python lists.

# 6.1 One-Dimensional Arrays 
Array_Indexing_and_Slicing = '''
a[m] 	-	Select element at index m, where m is an integer (start counting form 0).

a[-m]	-	Select the n th element from the end of the list, where n is an integer. The last element 
			in the list is addressed as –1, the second to last element as –2, and so on.

a[m:n] 	-	Select elements with index starting at m and ending at n − 1 (m and n are integers).

a[:] or a[0:-1] - Select all elements in the given axis.

a[:n] 	-	Select elements starting with index 0 and going up to index n − 1 (integer).

a[m:] or a[m:-1] - Select elements starting with index m (integer) and going up to the last element in
					the array.

a[m:n:p] -	Select elements with index m through n (exclusive), with increment p.

a[::-1]  -	Select all the elements, in reverse order.
'''
a = np.arange(0, 11)
print(a) # array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
a[0]  		# 0
a[-1] 		# 10
a[4] 		# 4
a[1:-1] 	# array([1, 2, 3, 4, 5, 6, 7, 8, 9])
a[1:-1:2] 	# array([1, 3, 5, 7, 9])
a[:5]		# array([0, 1, 2, 3, 4])
a[-5:]      # array([6, 7, 8, 9, 10])
a[::-2]     # array([10,  8,  6,  4,  2,  0])


# 6.2 Multidimensional Arrays


