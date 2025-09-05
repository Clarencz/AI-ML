"""
Neural networks typically have layers that consist of more than one neuron. Layers are nothing more than groups of neurons. Each neuron in a layer takes exactly the same input, input can mean mean training data or output from the previous layer but it contains its own set off weights and its own bias producing its own unique output. The layers output is a set of each of these outputs that is one per each neuron   

"""
# Visualizing a layer of neurons with common input.
# https://nnfs.io/mxo

"""we continue with the previous 4inputs and set of weights for the first neuron and add 2 additional made up sets of weights and 2 additional biases to form 2 new neurons for a total of 3 in the layer"""

inputs=[1,2,3,2.5]

weights1 = [0.2,0.8,-0.5,1]
weights2 = [0.5,-0.91,0.26,-0.5]
weights3 = [-0.26,-0.27,0.17,0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

outputs = [
    #Neuron1
    inputs[0] * weights1[0]+
    inputs[1] * weights1[1]+
    inputs[2] * weights1[2]+
    inputs[3] * weights1[3]+ bias1,
    
    #Neuron2
    inputs[0] * weights1[0]+
    inputs[1] * weights1[1]+
    inputs[2] * weights1[2]+
    inputs[3] * weights1[3]+ bias2,
    
    #Neuron3
    inputs[0] * weights1[0]+
    inputs[1] * weights1[1]+
    inputs[2] * weights1[2]+
    inputs[3] * weights1[3]+ bias3,
    
]
print(outputs)

# Code, math and visuals behind a layer of neurons
# https://nnfs.io/mxo

# the above code there are thre sets of weights and three biases, which define three neurons. Each neuron is connected to the same inputs. The differnce is in the seperate weights and bias that each neuron applies to the input 

'''fully connected neural neetwork - every neuron in the current layer has connections to every neuron from the previous layer '''

"""
we could use a loop to scale and handle dynamically-sized inputs and layers to code more layers and more neurons. We’ve turned the separate weight variables into a list of weights so we can iterate over them, and we changed the code to use loops instead of the hardcoded operations"""

inputs = [1,2,3,2.5]
weights = [[0.2,0.8,-0.5,1],
           [0.5,-0.91,0.26,-0.5],
           [0.5,-0.91,0.26,-0.5],
           [-0.26,-0.27,0.17,0.87]]
biases = [2,3,0.5]

#Output of current layer
layer_outputs = []
#For each neuron
for neuron_weight,neuron_bias in zip(weights,biases):
    #Zeroed output of given neuron
    neuron_output = 0
    #For each input and weight to the neuron
    for n_input, weight in zip(inputs, neuron_weight):
        #mulitply this input by associated weight
        #and add to the neurons's output variable
        neuron_output += n_input * weight
    #Add bias
    neuron_output +=neuron_bias
    #Put neurons's result to the layer's output list
    layer_outputs.append(neuron_output)
    
print(layer_outputs)

# If you find yourself confused at one of the steps, ​print​()​ out the objects to see what they are and what’s happening.

# How do we know we have three neurons? Why do we have three? We can tell we have three neurons because there are 3 sets of weights and 3 biases. When you make a neural network of your own, you also get to decide how many neurons you want for each of the layers

