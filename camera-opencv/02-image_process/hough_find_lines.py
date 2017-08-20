#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2017, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# hough_find_lines.py
# Do Hough Transform to find the unlimited length of lines from edge
#
# Author : sosorry
# Date   : 08/31/2016
# Usage  : python hough_find_lines.py hough_demo.jpg
	
import cv2
import sys
import numpy as np

try:
    imagePath = sys.argv[1]
    image = cv2.imread(imagePath)
except:
    image = cv2.imread("hough_demo.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
h, w = gray.shape

edges = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(gray, 50, 150, 3)

try:
    lines = cv2.HoughLines(edges, 1, np.pi/180, 250)[0]
    print lines

    for (rho, theta) in lines:
        x0 = np.cos(theta)*rho 
        y0 = np.sin(theta)*rho
        pt1 = ( int(x0 + (h+w)*(-np.sin(theta))), int(y0 + (h+w)*np.cos(theta)) )
        pt2 = ( int(x0 - (h+w)*(-np.sin(theta))), int(y0 - (h+w)*np.cos(theta)) )
        cv2.line(image, pt1, pt2, (0, 0, 255), 3) 

    cv2.imshow("HoughLines", image)
    cv2.waitKey(0)

except TypeError:
    print "The Houghlines function returns None, try decrease the threshold!"

cv2.destroyAllWindows()   

