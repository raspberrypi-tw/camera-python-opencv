#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# puttext.py
# Add an text overlay on image and save the result
#
# Author : sosorry
# Date   : 04/18/2015
# Usage  : python puttext.py abba.png 

import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]

# Read the image
image = cv2.imread(imagePath)
cv2.putText(image, "HELLO", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
cv2.imshow("preview", image)
cv2.waitKey(0)
cv2.imwrite("puttext.png", image)

cv2.destroyAllWindows()


