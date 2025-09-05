# neural networks receive data in batches during training. the example instance input data have been only one sample(or observation) of various features called a feature set:
inputs = [1,2,3,2.5]

# here the [1,2,3,2.5] data are somehow meaningful and descriptive to the output we desire. imagine each number as a value from different sensor, from the example in chapter 1, all simultaneously. Each of these values is a feature observation datum, and together they form a feature set instance, also called an observation, or most commonly a sample

# Visualizing a 1D array.
# https://nnfs.io/lqw

# often, neural networks expect to take in many samplees at a time for two reasons. one reason is that batches help with generalization during training. If you fit(perform a step of a training process) on one sample at a time, you're likely to keep fitting to that individual sample rather than slowly producing general tweaks to weights and biases that fit the entire dataset. Fitting or training in batches gives you a higher chancee of making more meaningful changes to weights and biases. 

# Example of a linear equation fitting batches of 32 chosen samples. See animation below for other sizes of samples at a time to see how much of a difference batch size can make.
# https://nnfs.io/vyu

# Example of a batch, its shape, and type. 
# https://nnfs.io/lqw

# In python lists are useful containers for holding a sample as well as multiple samples that make up a batch of observation.m Such an example of a batch of observation, each with its own sample looks like:
inputs = [[1,2,3,2.5],[2,5,-1,2],[-1.5,2.7,3.3,-0.8]]
# this list could be made into an array as it is homologous. Each list in the above list is a sample reepresenting a feature set or a feature set instance or observations

# in the example we need to manage both matrices as lists of vectors and perform dot product on all of them in all combinations, resulting in a list of lists output, or a matrix; this operation is called the matrix product