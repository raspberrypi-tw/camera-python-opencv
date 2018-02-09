#!/usr/bin/python
'''
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# camera_face_detect.py
# Face detect from camera
#
# Author : Fletcher Heisler, Michael Herman, Jeremy Johnson
# Date   : 06/22/2014
# Origin : https://realpython.com/blog/python/face-detection-in-python-using-a-webcam/
# Usage  : python camera_face_detect.py haarcascade_frontalface_default.xml
'''
import sys
import cv2

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

if cv2.__version__.startswith('2'):
    PROP_FRAME_WIDTH = cv2.cv.CV_CAP_PROP_FRAME_WIDTH
    PROP_FRAME_HEIGHT = cv2.cv.CV_CAP_PROP_FRAME_HEIGHT
    HAAR_FLAGS = cv2.cv.CV_HAAR_SCALE_IMAGE

elif cv2.__version__.startswith('3'):
    PROP_FRAME_WIDTH = cv2.CAP_PROP_FRAME_WIDTH
    PROP_FRAME_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT
    HAAR_FLAGS = cv2.CV_FEATURE_PARAMS_HAAR

cap = cv2.VideoCapture(0)
cap.set(PROP_FRAME_WIDTH, 320)
cap.set(PROP_FRAME_HEIGHT, 240)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=HAAR_FLAGS
    )

    print "Found {0} faces!".format(len(faces))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("preview", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
