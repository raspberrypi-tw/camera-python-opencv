#!/usr/bin/python
#
# knn_ocr_sample.py
# Test the sample data from digits.png and save the result
#
# Author : Ashing Tsai
# Date   : 2016/11/17
# Origin : http://arbu00.blogspot.tw/2016/11/1-opencv-knn.html
# Usage  : python knn_ocr_sample.py

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('data/digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Now we split the image to 5000 cells, each 20x20 size
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]

# Make it into a Numpy array. It size will be (50, 100, 20, 20)
x = np.array(cells)

# Now we prepare train_data and test_data.
train = x[:, :50].reshape(-1, 400).astype(np.float32)    # Size = (2500, 400)
test  = x[:, 50:100].reshape(-1, 400).astype(np.float32) # Size = (2500, 400)

# Create labels for train and test data
k = np.arange(10)
train_labels = np.repeat(k,250)[:, np.newaxis]
test_labels = train_labels.copy()

# Initiate kNN, train the data, then test it with test data for k=5
knn = cv2.KNearest()
knn.train(train, train_labels)
ret, result, neighbours, dist = knn.find_nearest(test, k=5)

# Now we check the accuracy of classification
# For that, compare the result with test_labels and check which are wrong
matches = result==test_labels
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size
print accuracy

# Save the data
np.savez('knn_data.npz', train=train, train_labels=train_labels)

