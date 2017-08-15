#!/usr/bin/python
#
# knn_static.py
# Visualize the KNN classification result with static data
#
# Author : sosorry
# Date   : 2017/01/12
# Origin : http://docs.opencv.org/2.4/modules/ml/doc/k_nearest_neighbors.html
# Usage  : python knn_static.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Feature set containing (x,y) values of 25 known/training data
train = np.array([[ 1.1, 1.1],
    [ 1.2,  2.2],
    [ 1.4,  4.8],
    [ 3.1,  2.3],
    [ 4.7,  1.0],
    [ 4.9,  6.1],
    [ 6.3,  0.7],
    [ 6.1,  6.5],
    [ 6.8,  1.8],
    [ 7.4,  6.8],
    [ 9.7,  5.8]], dtype='float32')

# Labels each one either Red or Blue with numbers 0 and 1
train_labels = np.array([[ 1.],
    [ 1.],
    [ 1.],
    [ 1.],
    [ 1.],
    [ 0.],
    [ 0.],
    [ 1.],
    [ 0.],
    [ 0.],
    [ 0.]], dtype='float32')

# Take Red families and plot them
red = train[train_labels.ravel() == 0]
plt.scatter(red[:,0], red[:,1], 120, 'r', '^')

# Take Blue families and plot them
blue = train[train_labels.ravel() == 1]
plt.scatter(blue[:,0], blue[:,1], 120, 'b', 's')

# Add into new comer(test data)
newcomer = np.array([[6,  1]], dtype='float32')
print "newcomer: ", newcomer, "\n"
plt.scatter(newcomer[:,0], newcomer[:,1], 300, 'g', 'o')

# Train & find nearest k-Nearest Neighbors
knn = cv2.KNearest()
knn.train(train, train_labels)
ret, results, neighbors, dist = knn.find_nearest(newcomer, 3)

print "result: ", results, "\n"
print "neighbors: ", neighbors, "\n"
print "distance: ", dist

plt.show()


