"""
Let’s say we have a single neuron, and there are three inputs to this neuron. As in most cases, when you initialize parameters in neural networks, our network will have weights initialized randomly, and biases set as zero to start
"""

inputs = [1,2,3]

'''
Each input also needs a weight associated with it. Inputs are the data that we pass into the model to get desired outputs, while the weights are the parameters that we’ll tune later on to get these results. Weights are one of the types of values that change inside the model during the training phase, along with biases that also change during training. The values for weights and biases are what get “trained,” and they are what make a model actually work (or not work) Our input and weights lists should now be'''

inputs = [1,2,3]
weights = [0.2,0.8,-0.5]

"""
next we need the bias and as we a currently working with modelling a single neuron with three inputs we only have one bias value per neuron. The bias is an additional tunable but not associated with any input in contrast to the weights
"""
inputs = [1,2,3]
weights =[0.2,0.8,-0.5]
bias = 2

"""the neuron then sums up the input * weight of each input and later adds the bias to output the result
output ​= ​(inputs[​0​]​*​weights[​0​] ​+ 
          ​inputs[​1​]​*​weights[​1​] ​+ 
          ​inputs[​2​]​*​weights[​2​] ​+ ​bias) 
 
print​(output)
"""

output = inputs[0]* weights[0] + inputs[1] * weights[1]+ inputs[2] + weights[2]
print(output)

# Visualizing the code that makes up the math of a basic neuron
#  ​https://nnfs.io/bkr


'''
if we have 4 inputs rather than 3 
'''
inputs = [1.0,2.0,3.0,2.5]
weights = [0.2,0.8,-0.5,1.0]
bias = 2.0

#  Visualizing how the inputs, weights, and biases from the code interact with the neuron
#  ​https://nnfs.io/bkr

output = (inputs[0] * weights[0]+
          inputs[1] * weights[1]+
          inputs[2] * weights[2]+
          inputs[3] * weights[3])
print(output)

# Visualizing the code that makes up a basic neuron, with 4 inputs this time
# https://nnfs.io/djp

