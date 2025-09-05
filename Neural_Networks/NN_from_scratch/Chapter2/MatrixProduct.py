# the matrix product is an operation in which we have 2 matrices, and we are performing dot product of all combinations of rows from the first matrix and the columns of the 2nd matrix, resulting in a matrix of those atomic dot products

# Visualizing how a single element in the resulting matrix from matrix product is calculated. See animation for the full calculation of each element
# https://nnfs.io/jei

# to perform a matrix product, the size of the second dimension of the left matrix must match the sizee of the first dimension of the right matrix. for example if the left matrix has a shape of (5,4) then right matrix must have its shape value(4,7). the shape of the resulting array is always the first dimension of the left array and the ssecond dimension of the right array(5,7)

# a = [1 2 3]
# b= 1
#    2
#    3


# a​ is a row vector. It looks very similar to a vector ​a​ (with an arrow above it) described earlier along with the vector product. The difference in notation between a row vector and vector are commas between values and the arrow above symbol ​a​ is missing on a row vector. It’s called a row vector as it’s a vector of a row of a matrix. ​b​, on the other hand, is called a column vector because it’s a column of a matrix. As row and column vectors are technically matrices, we do not denote them with vector arrows anymore. When we perform the matrix product on them, the result becomes a matrix as well, like in the previous example, but containing just a single value, the same value as in the dot product example we have discussed previously:

# ab = [1 2 3] 1  = [20]
#              2
#              3 
# when we perform  a matrix product on then, the result becomes a matrix as well but containing just a single value, the same value as in the dot product example

# i n other words, row and column vectors are matrices with one of their dimensions being of a size of 1: and we perform the matrix product on them instead of the dot product, which resuts in a matrix containing a single value. In this case, we performed a matrix multiplication of matrices with shapes(1,3) and (3,1) then resulting array has a shape(1,1)


