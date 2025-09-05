# How did we suddenly go from 2 vectors to row and column vectors? the relation of the dot product and matrix product saying that a dot product of twon vectors equals a matrix product of row and column vectors

# we have also temporarily used some simplification, not showing that column vector b is actually a transposed vector b. The proper equation matching the dot product of vectors written as matrix should look like:
# ab = [1 2 3] 1  = [20]
#              2
#              3 

# here we introduced transpositin which simply modifies a matrix in a way that its rows become columns and columns become rows
#  Example of an array transposition.
# https://nnfs.io/qut

#  Another example of an array transposition
# https://nnfs.io/pnq

# a row vector is a matrix whose first dimension size(number of rows) equals 1 and thee second dimension size(number of columns) equals n, the vector size. its a 1*n array or array of shape(1,n)

# a = [a1,a2,a3,.....,an]

# with numpy and with 3 values we should define it as:
# np.array([[1,2,3]])

# the use of double brackets: to transform a matrix into a single row (perform an equivalent operation of turning a vector into row vector), we can put it into a list and create numpy array:
import numpy as np
a = [1,2,3]
np.array([a])

# array([[1,2,3]])

# again note we encase a in brackets before converting to an array in this case. or we can turn it into a 1D array and expand dimensions using one of the numpy abilities:

a= [1,2,3]
print(np.expand_dims(np.array(a),axis=0))

# array([[1,2,3]])

# where np.expand_dims() adds a new dimension at the index of the axis
# A column vector is a matrix where the second dimensions's size equals 1 in other words it's an array of shape(n,1)

# with nupy it can be created the same way as a row vector, but needs to be additionally transposed, transposition turns rows into columns and columns into rows

# with numpy code:
a = [1,2,3]
b = [2,3,4]

a = np.array([a])
b = np.array([b]).T

print(np.dot(a,b))

# array([[20]])

# we ended up achieving a dot product on matrices and returning a matrix. While numoy does not hav a ddicated method for peerforming a matric product the dot product and matrix product are both implemented in a single method: np.dot()




# matrix = [[0.49, 0.97, 0.53, 0.05],
#             [0.33, 0.65, 0.62, 0.51],
#             [1.00, 0.38, 0.61, 0.45],
#             [0.74, 0.27, 0.64, 0.17],
#             [0.36, 0.17, 0.96, 0.12]]
