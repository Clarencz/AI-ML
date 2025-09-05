# When mulitplying vectors you either perform a dot product or a cross product. A cross product results in a vector while a dot product results in a scalar(singlr value/number)

"""A dot product of two vectors is a sum of products of consecutive vector elements.Both vectors must be of the same size(have an eequal number of elements)"""

a = [1,2,3]
b= [ 2,3,4]
# to obtain the dot product
dot_product = a[0] * b[0] + a[1]*b[1] + a[2]*b[2]
print(dot_product)

# Math behind the dot product example
# https://nnfs.io/xpo

# let's call a as inputs and b weights thus enabling us to use the dot product to perform calculations in neural network code 
# The addition of the two vectors is an operation performed element-wise, which means that both vectors have to be of the same size, and the result will become a vector of this size as well. The result is a vector calculated as a sum of the consecutive vector elements:  
