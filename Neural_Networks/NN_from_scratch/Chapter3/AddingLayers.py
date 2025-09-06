# layers between the input and output layer have values that we fon necessarily deal with hence the name hidden often used to improve the neural network or diagnose issues.
# Samples(feature set data) get fed through the input, which does not change it in any way, to oue first hidden layer, which we can see has 3 sets of weights with 4 values each

# Each of those 3 unique weight sets is associated with its distinct neuron. Thus, since we have 3 weight sets, we have 3 neurons in this first hidden layer. Each neuron has a unique set of weights, of which we have 4 (as there are 4 inputs to this layer), which is why our initial weights have a shape of ​(3,4)​. Now, we wish to add another layer. To do that, we must make sure that the expected input to that layer matches the previous layer’s output. We have set the number of neurons in a layer by setting how many weight sets and biases we have. The previous layer’s influence on weight sets 
# for the current layer is that each weight set needs to have a separate weight per input. This means a distinct weight per neuron from the previous layer (or feature if we’re talking the input). The previous layer has 3 weight sets and 3 biases, so we know it has 3 neurons. This then means, for the next layer, we can have as many weight sets as we want (because this is how many neurons this new layer will have), but each of those weight sets must have 3 discrete weights. To create this new layer, we are going to copy and paste our ​weights​ ​and ​biases​ to ​weights2 and ​biases2​, and change their values to new made up sets. Here’s an example:

import numpy as np

"""
Input Layer   ---   Hidden Layer 1   ---   Hidden Layer 2

 4 Neurons    ->     3 Neurons        ->     3 Neurons
"""

inputs = [[1.0, 2.0, 3.0, 2.5], # Neuron 1 in Hidden Layer 1 will be receiving input data from 4 neurons
          [2.0, 5.0, -1.0, 2.0], # Neuron 2 in Hidden Layer 1 will be receiving input data from 4 neurons
          [-1.5, 2.7, 3.3, -0.8]] # Neuron 3 in Hidden Layer 1 will be receiving input data from 4 neurons

weights = [[0.2, 0.8, -0.5, 1.0], # Neuron 1 in Hidden Layer 1 weights 
           [0.5, -0.91, 0.26, -0.5], # Neuron 2 in Hidden Layer 1 weights
           [-0.26, -0.27, 0.17, 0.87]] # Neuron 3 in Hidden Layer 1 weights

biases = [2, 3, 0.5] # Neurons 1 -> 3 in Hidden Layer 1 biases

layer1_outputs = np.dot(inputs, np.array(weights).T) + biases
print(layer1_outputs) 

"""
Hidden Layer 1 Outputs:

[[ 4.8    1.21   2.385] # Neuron 1 in Hidden Layer 2 will be receiving output data from 3 neurons in Hidden Layer 1
[ 8.9   -1.81   0.2  ] # Neuron 2 in Hidden Layer 2 will be receiving output data from 3 neurons in Hidden Layer 1
[ 1.41   1.051  0.026]] # Neuron 3 in Hidden Layer 2 will be receiving output data from 3 neurons in Hidden Layer 1
"""


weights2 = [[0.1, -0.14, 0.5], # Neuron 1 in Hidden Layer 2 weights 
            [-0.5, 0.12, -0.33], # Neuron 2 in Hidden Layer 2 weights
            [-0.44, 0.73, -0.13]] # Neuron 3 in Hidden Layer 2 weights

biases2 = [-1, 2, -0.5] # Neurons 1 -> 3 in Hidden Layer 2 biases

layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2
print(layer2_outputs)

""" 
Hidden Layer 2 Outputs:

[[ 0.5031  -1.04185 -2.03875]
[ 0.2434  -2.7332  -5.7633 ]
[-0.99314  1.41254 -0.35655]]
"""