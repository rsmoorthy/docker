#!/bin/bash

rm -rf /tmp/.X0-lock
rm -rf /tmp/.X11-unix

nohup Xvfb -screen 0 1280x800x24 &
sleep 1

nohup openbox-session &
sleep 1

nohup x11vnc -display :0 -nopw -listen localhost -no6 -noipv6 -xkb -ncache 10 -ncache_cr -forever -rfbport 5900 &
sleep 3

exec /root/noVNC/utils/launch.sh --vnc localhost:5900
