ps auxww | grep tally.exe | grep -v grep | awk -F ' ' '{print $2}' | xargs kill
sleep 1
nohup wine ~/.wine/drive_c/Tally.ERP9/tally.exe &
sleep 8

WID=$(xdotool search --name 'Tally.ERP 9')

xdotool windowactivate $WID
sleep 0.5

#xdotool type --window $WID "w"
#sleep 0.5

#xdotool key --window $WID "Return"
#sleep 0.5

xdotool windowsize $(xdotool getactivewindow) 100% 100%
sleep 0.5

# Not needed for 5.4.6
#xdotool key --window $(xdotool search --name 'Tally.ERP 9') "Down"
#xdotool key --window $(xdotool search --name 'Tally.ERP 9') "Down"
#xdotool key --window $(xdotool search --name 'Tally.ERP 9') "Return"

sleep 0.5
xdotool type --window $WID "S"
xdotool key --window $WID "Up"
#sleep 1
#xdotool key --window $(xdotool search --name 'Tally.ERP 9') "BackSpace"
#sleep 3
#xdotool key --window $(xdotool search --name 'Tally.ERP 9') "Escape"
#sleep 3
#xdotool type --window $(xdotool search --name 'Tally.ERP 9') "C:\\Tally.ERP9\\Data"
#xdotool key --window $(xdotool search --name 'Tally.ERP 9') "Return"
#xdotool key --window $(xdotool search --name 'Tally.ERP 9') "Up"
sleep 1
xdotool type --delay 1000 --window $WID "IF Books 16-17"
sleep 20
xdotool key --window $WID "Return"

sleep 0.5
xdotool type --window $WID "moorthy"
sleep 0.5
xdotool key --window $WID "Return"
sleep 0.5
xdotool type --window $WID "ereceipts"
sleep 0.5
xdotool key --window $WID "Return"
sleep 0.5
