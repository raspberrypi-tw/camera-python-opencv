#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2017, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# hsv_binary.py
#
# Author : sosorry
# Date   : 08/30/2016
# Usage  : python hsv_binary.py

import cv2
import numpy as np

image = cv2.imread("lena256rgb.jpg")

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define range of purple color in HSV
lower = np.array([141, 0, 0])
upper = np.array([164, 145, 197])

# Threshold the HSV image to get only purple colors
binary = cv2.inRange(hsv, lower, upper)

bitwise_not = cv2.bitwise_not(binary)
cv2.imshow("Bitwise_not", bitwise_not)
cv2.waitKey(0)

bitwise_not = cv2.bitwise_not(image, mask=binary)
cv2.imshow("Bitwise_not_mask", bitwise_not)
cv2.waitKey(0)

bitwise_and = cv2.bitwise_and(image, image, mask=binary)
cv2.imshow("Bitwise_and", bitwise_and)
cv2.waitKey(0)

cv2.destroyAllWindows()

