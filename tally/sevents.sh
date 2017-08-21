#!/bin/bash

# Arguments: 1) Company Name 2) Username 3) Password

if [[ -z "$1" || -z "$2" || -z "$3" ]]; then
    echo "Usage: $0: <CompanyName> <Username> <Password> [<Folder Path>]"
    exit;
fi

ps auxww | grep tally.exe | grep -v grep | awk -F ' ' '{print $2}' | xargs kill
sleep 1
nohup wine ~/.wine/drive_c/Tally.ERP9/tally.exe >/dev/nul 2>&1 &
sleep 8

WID=$(xdotool search --name 'Tally.ERP 9')
export WID

xdotool windowactivate $WID
sleep 0.5

# python typekeys.py "w" --ender "Return" --sleep 0.5
xdotool windowsize $(xdotool getactivewindow) 100% 100%
sleep 0.5

# Not needed for 5.4.6
#xdotool key --window $(xdotool search --name 'Tally.ERP 9') "Down"
#xdotool key --window $(xdotool search --name 'Tally.ERP 9') "Down"
#xdotool key --window $(xdotool search --name 'Tally.ERP 9') "Return"
sleep 0.5
python typekeys.py "S" --ender "Up" --sleep 1

python typekeys.py "BackSpace" --ender "Escape" --sleep 1
FolderPath="$4"
if [[ -z "$FolderPath" ]]; then
  FolderPath="C:\Tally.ERP9\Data"
fi
python typekeys.py "$FolderPath" --ender "Return" --sleep 5

python typekeys.py "$1" --ender "Return" --sleep 1

python typekeys.py "$2" --ender "Return" --sleep 1
python typekeys.py "$3" --ender "Return" --sleep 1
