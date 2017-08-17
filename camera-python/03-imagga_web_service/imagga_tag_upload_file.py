#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# imagga_tag_upload_file.py
# Upload file to imagga service and get the result of tag
#
# Author : sosorry
# Date   : 18/04/2015

import ConfigParser
import requests
import json

url = "http://api.imagga.com/v1/content"
files = {"file": open("/home/pi/test.jpg", "rb")}

#
# replace "authorization: "Basic ..." with your Authorization in web_service.conf
#
config = ConfigParser.ConfigParser()
config.read('web_service.conf')
authorization = config.get('imagga', 'authorization')

headers = { 
    "accept": "application/json",
    "authorization": authorization
    }   
response = requests.post(url, files=files, headers=headers)
# un-comment to see all tags
#print response.text

data = json.loads(response.text.encode("ascii"))
uid = data["uploaded"][0]["id"]
print "Get uid... "
print "<< " + uid + " >>"


url = "http://api.imagga.com/v1/tagging"
querystring = {"content": data["uploaded"][0]["id"]}
response = requests.request("GET", url, headers=headers, params=querystring)
# un-comment to see all tags
#print response.text

data = json.loads(response.text.encode("ascii"))
tag = data["results"][0]["tags"][0]["tag"].encode("ascii")
print "Get tag... "
print "<< " + tag + " >>"
