#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# hough_find_linesp.py
# Do Hough Transform to find the limited length of lines from edge
#
# Author : sosorry
# Date   : 08/31/2016
# Usage  : python hough_find_linesp.py hough_demo.jpg

import cv2
import sys
import numpy as np

try:
    imagePath = sys.argv[1]
    image = cv2.imread(imagePath)
except:
    image = cv2.imread("hough_demo.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

edges = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(gray, 50, 150, 3)

try:
    plines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, None, 100, 5)[0]
    print plines

    for pl in plines:
        cv2.line(image, (pl[0], pl[1]), (pl[2], pl[3]), (255, 0, 0), 3)

    cv2.imshow("HoughLinesP", image)
    cv2.waitKey(0)

except TypeError:
    print "The HoughlinesP function returns None, try decrease the threshold!"

cv2.destroyAllWindows()   

