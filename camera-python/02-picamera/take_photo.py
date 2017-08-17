#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# take_photo.py
# Capture an image to a file
#
# Author : sosorry
# Date   : 11/14/2014

import picamera
import time

camera = picamera.PiCamera()
time.sleep(2)    # Camera warm-up time
camera.capture('test.jpg')
