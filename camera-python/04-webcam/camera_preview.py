#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# camera_preview.py
# Preview from camera
#
# Author : sosorry
# Date   : 04/18/2015
# Usage  : python camera_preview.py

import cv2

if cv2.__version__.startswith('2'):
    PROP_FRAME_WIDTH = cv2.cv.CV_CAP_PROP_FRAME_WIDTH
    PROP_FRAME_HEIGHT = cv2.cv.CV_CAP_PROP_FRAME_HEIGHT
elif cv2.__version__.startswith('3'):
    PROP_FRAME_WIDTH = cv2.CAP_PROP_FRAME_WIDTH
    PROP_FRAME_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT

#cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture(0)
cap.set(PROP_FRAME_WIDTH, 320)
cap.set(PROP_FRAME_HEIGHT, 240)

while True:
    ret, frame = cap.read()
    cv2.imshow("preview", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

