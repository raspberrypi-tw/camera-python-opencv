#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# low_light.py
# Take photo in low light situation
#
# Author : sosorry
# Date   : 12/03/2016

import picamera
import time
from fractions import Fraction

camera = picamera.PiCamera() 
camera.resolution = (640, 480)
camera.framerate = Fraction(1, 6)
camera.shutter_speed = 6000000
camera.iso = 800 
time.sleep(30)
camera.exposure_mode = 'off'
camera.capture('dark.jpg')
