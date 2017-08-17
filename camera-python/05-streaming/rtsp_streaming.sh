#!/bin/bash

raspivid -o - -t 0 -hf -w 320 -h 240 -fps 15 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554}' :demux=h264
