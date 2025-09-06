# next we will create non-linear data - meaning data that can not be represented wel by a straight line

#pip install nnfs
#nnfs - package that contains functions that we can use to create data


from nnfs.datasets import spiral_data

# we will also use this packag to enssure repeatability for everyone, using nnfs.init() after importing numpy

import numpy as np
import nnfs

# the nnfs.init() - sets the random seed to 0 by default, creates a float3 2 dtype default, and overrides the original dot product from numpy to ensure repeatability for following along.
# the spiral_data function allows you to create a dataset as many classes as we want. the function has parameteres to choose the number of classes and the number of points/observations per class in the resulting non-linear dataset.

import matplotlib.pyplot as plt
X, y = spiral_data(samples = 100, classes = 3)
# x axis = X[:,0]
# y axis = X[:,1]
# y= classes
plt.scatter(X[:,0],X[:,1], c=y, cmap="brg")
plt.show()
