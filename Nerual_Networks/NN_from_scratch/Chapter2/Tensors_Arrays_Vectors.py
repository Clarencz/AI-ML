# Tensors, Arrays and Vectors

# Tensors: closely related to arrays, you can interchange tensor/array/matrix when it comes to machine learning

# Let's describe things that hold data
# List
# L = [1,5,6,2]
#  A list of lists
# LOL = [[1,3,5,6],
#        [2,4,5,6]]

# A list of lists of lists! 
# lolol ​= ​[[[​1​,​5​,​6​,​2​], 
#           [​3​,​2​,​1​,​3​]], 
#          [[​5​,​2​,​1​,​2​], 
#           [​6​,​4​,​8​,​4​]], 
#          [[​2​,​8​,​5​,​3​], 
#           [​1​,​1​,​9​,​4​]]]

# Everything shown so far could also be an array or an array representation of a tensor. A list is just a list, and it can do anything

# another_list_of_lists ​= ​[[​4​,​2​,​3​], 
#                          [​5​,​1​]]
# a list is dscribed as homologous if each list along a dimesion is identically long and must be true for each dimension. A non-homologous list can not be regarded as an array. 
# While failing to be consistent in one dimension is enough to show that this example is not homologous, we could also read down the “column” dimension (the first dimension); the first two columns are 2 elements long while the third column only contains 1 elementIn the above example,  Note that every dimension does not necessarily need to be the same length; it is perfectly acceptable to have an array with 4 rows and 3 columns (i.e., 4x3
# when reading across the “row” dimension (also called the second dimension), the first list is 3 elements long, and the second list is 2 elements long hence not homologous hence not an array

# A matrix is pretty simple. It’s a rectangular array. It has columns and rows. It is two dimensional. So a matrix can be an array (a 2D array). Can all arrays be matrices? No. An array can be far more than just columns and rows, as it could have four dimensions, twenty dimensions

# list_matrix_array ​= ​[[​4​,​2​], 
#                      [​5​,​1​], 
#                      [​8​,​2​]]

# A matrix is a 2-dimensional array.The first dimension is what’s inside the most outer brackets, and if we look at the above matrix, we can see 3 lists there: ​[​4​,​2​]​, ​[​5​,​1​]​, and ​[​8​,​2​]​; thus,the size in this dimension is 3 and each of those lists has to be the same shape to form an array (and matrix in this case).The next dimension's size is the number of eleements insidee this more inner pair of brackets and we see that is's 2 as all of them contain 2 elements.


# With 3-dimensional arrays, like in ​lolol​ below, we’ll have a 3rd level of brackets: 
# lolol ​= ​[[[​1​,​5​,​6​,​2​], 
#           [​3​,​2​,​1​,​3​]], 
#          [[​5​,​2​,​1​,​2​], 
#           [​6​,​4​,​8​,​4​]], 
#          [[​2​,​8​,​5​,​3​], 
#           [​1​,​1​,​9​,​4​]]] 
 
# The first level of this array contains 3 matrices: 
#         [[​1​,​5​,​6​,​2​], 
#          [​3​,​2​,​1​,​3​]] 
 
#         [[​5​,​2​,​1​,​2​], 
#          [​6​,​4​,​8​,​4​]] 
 
# And 
#         [[​2​,​8​,​5​,​3​], 
#          [​1​,​1​,​9​,​4​]]

# That’s what’s inside the most outer brackets and the size of this dimension is then 3. If we look at the first matrix, we can see that it contains 2 lists ​—​ ​[​1​,​5​,​6​,​2​]​ and ​[​3​,​2​,​1​,​3​]​ so the size of this dimension is 2 ​—​ while each list of this inner matrix includes 4 elements. These 4 elements make up the 3rd and last dimension of this matrix since there are no more inner brackets. Therefore, the shape of this array is ​(3, 2, 4)​ and it’s a 3-dimensional array, since the shape contains 3 dimensions

# Example of a 3-dimensional array.
# https://nnfs.io/jps

"""A tensor object is an object that can be represented as an array meaning we can treat tensors as array in the contet of deep learning
Array - an orderd homologous container for numbers
Linear Array - 1-dimensional array is the simplest form of array
Arrays can also consist of multi-dimensional data known as a matrix in math which will be reprsented as a 2-dimensional array and each element of the array can be accessed using a tuple as a key
Vector in math is what is refered to as a list in pythonor a 1-dimensional array in numpy"""
