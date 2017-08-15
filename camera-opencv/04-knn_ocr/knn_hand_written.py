#!/usr/bin/python
#
# knn_hand_written.py
# Test the hand written classification with KNN
#
# Author : Ashing Tsai
# Date   : 2016/11/17
# Origin : http://arbu00.blogspot.tw/2016/11/1-opencv-knn.html
# Usage  : DO "python knn_ocr_sample.py" BEFORE "python knn_hand_written.py"

import numpy as np
import cv2
from matplotlib import pyplot as plt
 
# Load exist data
with np.load('knn_data.npz') as data:
    train = data['train']
    train_labels = data['train_labels']

# Initiate kNN, train the data
knn = cv2.KNearest()
knn.train(train, train_labels)
 
input_number, image_number, image_result = [None]*10, [None]*10, [None]*10
test_number, result, result_str = [None]*10, [None]*10, [None]*10

for i in range(10):
    input_number[i] = str(i) + ".JPG"

# Predicting
for i in range(10):  
    image_number[i] = cv2.imread( 'data/' + input_number[i], 0)
    test_number[i]  = image_number[i][:,:].reshape(-1, 400).astype(np.float32) # size = (1, 400)
    ret, result[i], neighbours, dist = knn.find_nearest(test_number[i], k=5)
    image_result[i] = np.zeros((64, 64, 3), np.uint8)
    image_result[i][:,:] = [255, 255, 255]
    result_str[i] = str(result[i][0][0].astype(np.int32))

    if result[i][0][0].astype(np.int32) == i:
        cv2.putText(image_result[i], result_str[i], (15,52), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0),3)
    else:
        cv2.putText(image_result[i], result_str[i], (15,52), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0),3)

input_name   = ['Input 0',   '1', '2', '3', '4', '5', '6', '7', '8', '9']
predict_name = ['Predict 0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(10):
    plt.subplot(2, 10, i+1),    plt.imshow(image_number[i], cmap = 'gray')
    plt.title(input_name[i]),   plt.xticks([]), plt.yticks([])
    plt.subplot(2, 10, i+11),   plt.imshow(image_result[i], cmap = 'gray')
    plt.title(predict_name[i]), plt.xticks([]), plt.yticks([])

plt.show()
