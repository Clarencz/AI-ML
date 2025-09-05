# Now we would like to calc the output of a layer of 3 neurons, which means that the weight will be a matrix or list of weight vectors. which will be a 2-dimensional array which we'll call matrix.
# we also desribed the dot product of two vectors but the weights are now a matrix and we need to perform a dot product of them and the input vector, treating this matrix as a list of vectors and performing the dot product one by one with the veector of inputs hence returning a list of dot products
# the dot products result is a vector(or a list) of sums of the weight and input products for each of the neurons. then we add corresponding biases to them as they are a vector of the same size.

import numpy as np 
inputs = [1,2,3,2.5]
weights = [[0.2,0.8,-0.5,1],
           [0.5,-0.91,0.26,-0.5],
           [0.5,-0.91,0.26,-0.5],
           [-0.26,-0.27,0.17,0.87]]
biases = [2,3,0.5]

layer_outputs = np.dot(weights,inputs) + biases
print(layer_outputs) 

# Code and visuals for the sum of the dot product and bias with a layer of neurons
# https://nnfs.io/cyx


# This syntax involving the dot product of weights and inputs followed by the vector addition of bias is the most commonly used way to represent this calculation of ​inputs·weights+bias​. To explain the order of parameters we are passing into ​np.dot()​, we should think of it as whatever comes first will decide the output shape. In our case, we are passing a list of neuron weights first and then the inputs, as our goal is to get a list of neuron outputs. As we mentioned, a dot product of a matrix and a vector results in a list of dot products. The ​np.dot()​ method treats the matrix as a list of vectors and performs a dot product of each of those vectors with the other vector. In this example, we used that property to pass a matrix, which was a list of neuron weight vectors and a vector of inputs and get a list of dot products ​—​ neuron outputs.   
