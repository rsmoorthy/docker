#!/bin/sh

export LANG=en_IN
export LANGUAGE=en_IN:en

winetricks win7
winetricks corefonts
wine /mnt/tally9_install.exe
cp /root/Narration.txt /root/.wine/drive_c/Tally.ERP9/
cp /root/Journal.txt /root/.wine/drive_c/Tally.ERP9/
