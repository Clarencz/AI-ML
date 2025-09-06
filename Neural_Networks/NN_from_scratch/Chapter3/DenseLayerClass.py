# So far, we’ve only used what’s called a ​dense​ or fully-connected​ layer. These layers are commonly referred to as “dense” layers in papers, literature, and code, but you will occasionally see them called fully-connected 
import numpy as np
import nnfs
from nnfs.datasets import spiral_data

class Layer_Dense:
    def __init__(self, n_inputs,n_neurons):
        #initialize weight and biases
        """weights ar often initialized randomly for a model, but not always if you wish to load a pre-trained model, you will initialize the parameters to whatever that prtrined modl finished with"""
        self.weights = 0.01 * np.random.randn( n_inputs, n_neurons)
        self.biases = np.zeros((1,n_neurons))
# Here, we’re setting weights to be random and biases to be 0. Note that we’re initializing weights to be ​(inputs, neurons), ​rather than (​neurons, inputs)​. We’re doing this ahead instead of transposing every time we perform a forward pass, as explained in the previous chapter. Why zero biases? In specific scenarios, like with many samples containing values of 0, a bias can ensure that a neuron fires initially. It sometimes may be appropriate to initialize the biases to some non-zero number, but the most common initialization for biases is 0. However, in these scenarios, you may find success in doing things another way. This will vary depending on your use-case and is just one of many things you can tweak when trying to improve results. One situation where you might want to try something else is with what’s called ​dead neurons   

# the np.random.randn and np.zeros: these methods are convinient ways to initialize arrays np.random.randn produces a Gussian distribution with a mean of 0 and variance of 1, which means that it'll generate random numbers, positive and negative, centered at 0 and with the mean value close to 0. In general, neural networks work best with values between -1 and +1. We're going to multiply this gaussin distribution for the weight by 0.01 to generate numbers that are a couple of magnitude smaller otherwise the model will take more time to fit data during the training procerss as starting values will be disproportionately large compared to the updates being made during training. the idea is to start a model with non zero values small enough that they won't affect training.

# finally the np.random.randn function takes the dimension sizes as parameters and creates the output array with shape. The weight here will be the number of inputs forr the first dimension and the number of neurons for the 2nd dimension

# the np.zeros function takes a desired array shape as an argument and returns an array of that shape filled with zeros

# we initialize the biases with the shape of (1,n_neurons), as a row vector which let us easily add it to the result of the dot product later, without additional operations like transposition)


    def forward(self,inputs):
        #calculate output values from inputs, weights and biases
        """when we pass data through a model from beginning to end, this is called forward pass"""
        self.output = np.dot(inputs,self.weights) + self.biases



#create dataset
X,y = spiral_data(samples = 100, classes= 3)

#create Dense layer with 2 input features and 3 output values
dense1 = Layer_Dense(2,3)

#Perform a forward pass of our training data through this layer
dense1.forward(X)
print(dense1.output[:5])


# in the output we have 5 rows of data that have 3 values each. Each of those 3 values is the value from the neurons in the dense1 layer after passing in each of the samples

