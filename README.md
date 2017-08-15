# Two days workshop for Raspberry Pi Camera + Python + OpenCV

## Intro
In this workshop, we will introudce the Raspberry Pi Camera and Python in day 1, including:
1. Camera application, assembly and usage.
2. Control the camera through command line or python with picamera module.
3. Connect with image tag web service, such as [imagga](https://imagga.com/)
4. The basic of V4L2, pro and cons
5. Build a MJPEG streaming server from scratch

In day 2, we will introduce:
1. Color space, such as RGB and HSV, and the conversion 
2. Basic image process, including blur, erode, dilate method. How to use Canny edge detection and Hough Transform to recognize the angle of meter pointer.
3. Face detection with Haar Feature Cascade, is a machine learning part of OpenCV
4. K-NN classification, is a machine learning part of OpenCV

The slide is available on [Raspberry Pi Camera and OpenCV (Day2)](https://www.slideshare.net/raspberrypi-tw/raspberry-pi-camera-and-opencv-day2)

Our environment is Pi 3 + 2017-09-23-raspbian-jessie.img.

## Required
### Install required package and Python module
```shell  
$ sudo apt-get update
$ sudo apt-get install -y festival python-dev python-opencv python-pip x11vnc liblivemedia-dev libv4l-dev cmake python-matplotlib vlc
$ sudo pip install request flask numpy
```

## Buy Camera and accessories
See [Camera](https://www.raspberrypi.com.tw/shop/camera/)

