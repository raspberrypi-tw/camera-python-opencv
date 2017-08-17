#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Author : sosorry
# Date   : 05/31/2015
# A simple page of flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
   return "Hello Flask"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
