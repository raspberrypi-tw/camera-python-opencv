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
# Add route & template to flask

from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('link.html')

@app.route("/foo")
def foo():
    extns = ['Flask', 'Jinja2', 'Awesome']
    return render_template('bar.html', extns=extns)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
