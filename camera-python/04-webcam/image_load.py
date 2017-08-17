#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# image_load.py
# Load image
#
# Author : sosorry
# Date   : 04/18/2015
# Usage  : python image_load.py abba.png 

import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]

# Read the image
image = cv2.imread(imagePath)

cv2.imshow("preview", image)
cv2.waitKey(0)

cv2.destroyAllWindows()


