#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2017, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# find_contour.py
# Find and draw contours
#
# Author : sosorry
# Date   : 08/31/2016
# Usage  : python draw_contour.py lena256rgb.jpg
# Usage  : python draw_contour.py

import cv2
import sys

try:
    imagePath = sys.argv[1]
    image = cv2.imread(imagePath)
except:
    image = cv2.imread("lena512rgb.png")

# convert RGB to Gray to Binary
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(_, binary) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# find contours
#   @mode: CV_RETR_EXTERNAL / CV_RETR_LIST / CV_RETR_CCOMP / CV_RETR_TREE
#   @method: CV_CHAIN_APPROX_NONE / CV_CHAIN_APPROX_SIMPLE
(contours, _) = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("Binary", binary)
cv2.waitKey(0)

cv2.drawContours(image, contours, -1, (0,255,0), 3)
cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


