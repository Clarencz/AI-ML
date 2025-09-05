# After transposition, we can perform the matrix product
# https://nnfs.io/crq

# if we look at this from the perspective of the input and weights we need to perform the dot product of each input and each weight set in all of their combinatinos. The dot product takes the row from the first array and the column from the second one. Transposing the second array shapes the data to be column-aligned. The matrix product of inputs and transposed weights wil result in a matrix containing all atomic dot products that we need to calculate. the resulting matrix consists of outputs of all neurons after operations performed on each input sample:

# Code and visuals depicting the dot product of inputs and transposed weights
# https://nnfs.io/gjw

# We mentioned that the second argument for ​np.dot()​ is going to be our transposed weights, so first will be inputs, but previously weights were the first parameter. We changed that here. Before, we were modeling neuron output using a single sample of data, a vector, but now we are a step forward when we model layer behavior on a batch of data. We could retain the current parameter order, but, as we’ll soon learn, it’s more useful to have a result consisting of a list of layer outputs per each sample than a list of neurons and their outputs sample-wise. We want the resulting array to be sample-related and not neuron-related as we’ll pass those samples further through the network, and the next layer will expect a batch of inputs.

# Code and visuals for inputs multiplied by the weights, plus the bias
# https://nnfs.io/qty

import numpy as np


inputs = [[1.0, 2.0, 3.0, 2.5],
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]

weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2.0, 3.0, 0.5]

layer_outputs = np.dot(inputs,np.array(weights).T) + biases
print(layer_outputs)

# As you can seee our neural network takes in a group of samples (inputs) and outputs a group of predictions. If you've used any of the deep learning libraries, this is why you pass in a list of inputs(even if it's just one feature set) and are returned a list of predictions even if there's is only one prediction