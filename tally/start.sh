#!/bin/bash

rm -rf /tmp/.X0-lock
rm -rf /tmp/.X11-unix

nohup Xvfb -screen 0 1280x800x24 &
sleep 1

nohup openbox-session &
sleep 1

nohup x11vnc -display :0 -nopw -listen localhost -no6 -noipv6 -xkb -ncache 10 -ncache_cr -forever -rfbport 5900 &
sleep 3

cd /root
nohup python /root/web.py 2>&1 >/tmp/web.log &

exec /root/noVNC/utils/launch.sh --vnc localhost:5900
