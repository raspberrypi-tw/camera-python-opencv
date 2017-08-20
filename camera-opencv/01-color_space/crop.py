#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2017, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# crop.py
#
# Author : sosorry
# Date   : 2017/07/27
# Usage  : python cropy.py

import cv2
import numpy as np

img = cv2.imread("lena256rgb.jpg")
cv2.imshow("Normal", img)
cv2.waitKey(0)

face = img[95:195, 100:180]
cv2.imshow("Face", face)
cv2.waitKey(0)
 
body = img[20:, 35:210]
cv2.imshow("Body", body)
cv2.waitKey(0)

cv2.destroyAllWindows()
