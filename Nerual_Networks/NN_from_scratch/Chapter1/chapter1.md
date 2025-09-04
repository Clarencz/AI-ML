# Neural Networks from Scratch

What each sensor measures in this example is called a feature. A group of features makes up a feature set (represented as vectors/arrays), and the values of a feature set can be referred to as a sample. Samples are fed into neural network models to train them to fit desired outputs from these inputs or to predict based on them during the inference phase The “normal” and “failure” labels are ​classifications​ or ​labels.​ ​You may also see these referred to as ​targets​ or ​ground-truths​ while we fit a machine learning algorithm. These targets are the classifications that are the ​goal​ or ​target​, known to be ​true and​ ​correct​, for the algorithm to learn. example of supervised learning in the form of classification. In addition to classification, there’s also regression, which is used to predict numerical values, like stock prices. There’s also unsupervised machine learning, where the machine finds structure in data without knowing the labels/classes ahead of time. There are additional concepts (e.g., reinforcement learning and semi-supervised machine learning) that fall under the umbrella of neural networks.

What is a Neural Network?
Artificial” neural networks are inspired by the organic brain, translated to the computer. It’s not a perfect comparison, but there are neurons, activations, and lots of interconnectivity, even if the underlying processes are quite different A single neuron by itself is relatively useless, but, when combined with hundreds or thousands (or many more) of other neurons, the interconnectivity produces relationships and results that frequently outperform any other machine learning methods.

# Visualizing Neural Network Sizes

# https://nnfs.io/ntr/

Dense layers, the most common layers, consist of interconnected neurons. In a dense layer, each neuron of a given layer is connected to every neuron of the next layer, which means that its output value becomes an input for the next neurons. Each connection between neurons has a weight associated with it, which is a trainable factor of how much of this input to use, and this weight gets multiplied by the input value. Once all of the ​inputs·weights​ flow into our neuron, they are summed, and a bias, another trainable parameter, is added. The purpose of the bias is to offset the output positively or negatively, which can further help us map more real-world types of dynamic data. The concept of weights and biases can be thought of as “knobs” that we can tune to fit our model to data Biases and weights are both tunable parameters, and both will impact the neurons’ outputs, but they do so in different ways. Since weights are multiplied, they will only change the magnitude or even completely flip the sign from positive to negative, or vice versa. ​Output = weight·input+bias is not unlike the equation for a line ​y = mx+b​. Adjusting the weight will impact the slope of the function: As we increase the value of the weight, the slope will get steeper. If we decrease the weight, the slope will decrease. If we negate the weight, the slope turns to a negative:

# How weights and biases impact a single neuron

# https://nnfs.io/bru/

weights and biases help to impact the outputs of neurons, but they do so in slightly different ways. This will make even more sense when we cover ​activation functions​
As a very general overview, the step function meant to mimic a neuron in the brain, either “firing” or not — like an on-off switch. In programming, an on-off switch as a function would be called a step function​
For a step function, if the neuron’s output value, which is calculated by ​sum(inputs·weights) + bias​, is greater than 0, the neuron fires (so it would output a 1). Otherwise, it does not fire and would pass along a 0. The formula for a single neuron might look something like:
output ​= ​sum​(inputs ​\* ​weights) ​+ ​bias

We then usually apply an activation function to this output, noted by ​activation()​:
output = activation(output)
Rectified Linear​ (ReLU) activation function,

full function of a neural network can get very large, let’s start with a simple example with 2 hidden layers of 4 neurons each.
Along with these 2 hidden layers, there are also two more layers here — the input and output layers.
While this data can be “raw” in the exact form it was collected, you will typically ​preprocess​ your data through functions like ​normalization​ and ​scaling​, and your input needs to be in numeric form
It is common to preprocess data while retaining its features and having the values in similar ranges between 0 and 1 or -1 and 1. To achieve this, you will use either or both scaling and normalization functions. The output layer is whatever the neural network returns.
With classification, where we aim to predict the class of the input, the output layer often has as many neurons as the training dataset has classes, but can also have a single output neuron for binary (two classes) classification.
Now lets focus on a classifier that uses a separate output neuron per each class. For example, if our goal is to classify a collection of pictures as a “dog” or “cat,” then there are two classes in total. This means our output layer will consist of two neurons; one neuron associated with “dog” and the other with “cat.” You could also have just a single output neuron that is “dog” or “not dog.”

# Visualization of an example Dogs vs Cats neural network classifier

# https://nnfs.io/qtb/

When represented as one giant function, an example of a neural network’s forward pass would be computed with:

$$
f(x) = W^{[L]} \, \sigma \big( W^{[L-1]} \, \sigma \big( \cdots \sigma ( W^{[1]} x + b^{[1]} ) \cdots \big) + b^{[L-1]} \big) + b^{[L]}
$$

This shows the forward pass of a neural network as one nested function:

- \(x\) = input
- \(W^{[i]}, b^{[i]}\) = weights and biases of layer \(i\)
- \(\sigma(\cdot)\) = activation function (e.g., ReLU, sigmoid, tanh)
- \(f(x)\) = final output

# The math behind an example forward pass through a neural network

# https://nnfs.io/vkt/

A typical neural network has thousands or even up to millions of adjustable ​parameters​ (weights and biases). In this way, neural networks act as enormous functions with vast numbers of parameters​. The concept of a long function with millions of variables that could be used to solve a problem isn’t all too difficult. With that many variables related to neurons, arranged as interconnected layers, we can imagine there exist some combinations of values for these variables that will yield desired outputs. Finding that combination of parameter (weight and bias) values is the challenging part.

The end goal for neural networks is to adjust their weights and biases (the parameters), so when applied to a yet-unseen example in the input, they produce the desired output. When supervised machine learning algorithms are trained, we show the algorithm examples of inputs and their associated desired outputs. One major issue with this concept is ​overfitting​ — when the algorithm only learns to fit the training data but doesn’t actually “understand” anything about underlying input-output dependencies. The network basically just “memorizes” the training data.
Thus, we tend to use “in-sample” data to train a model and then use “out-of-sample” data to validate an algorithm
The goal is for the model to not only accurately predict on the training data, but also to be similarly accurate while predicting on the withheld out-of-sample validation data.
This is called ​generalization​, which means learning to fit the data instead of memorizing it. The idea is that we “train” (slowly adjusting weights and biases) a neural network on many examples of data.
To train these neural networks, we calculate how “wrong” they are using algorithms to calculate the error (called ​loss​), and attempt to slowly adjust their parameters (weights and biases) so that, over many iterations, the network gradually becomes less wrong. The goal of all neural networks is to generalize, meaning the network can see many examples of never-before-seen data, and accurately output the values we hope to achieve. Neural networks can be used for more than just classification. They can perform regression (predict a scalar, singular, value), clustering (assign unstructured data into groups), and many other tasks. Classification is just a common task for neural networks.

# Visualization of the forward pass calculation and path for a neural network

# https://nnfs.io/vkr/
