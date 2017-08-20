#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2017, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# gaussian_blur.py
# Do the Gaussian Blur effect for loaded image or image from camera
#
# Author : sosorry
# Date   : 08/31/2016
# Usage  : python gaussian_blur.py

import cv2
import sys
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Gaussian_Blur')
cv2.createTrackbar('ksize', 'Gaussian_Blur', 0, 10, nothing)

try:
    imagePath = sys.argv[1]
    image = cv2.imread(imagePath)
except:
    image = cv2.imread("lena512rgb.png")

while True:
    ksize  = cv2.getTrackbarPos('ksize', 'Gaussian_Blur')

    blur = cv2.GaussianBlur(image, (2*ksize+1, 2*ksize+1), 0)
    cv2.imshow('Gaussian_Blur', blur)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
