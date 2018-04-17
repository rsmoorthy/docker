cd /root

ip=$(/sbin/ifconfig eth0 | grep 'inet addr' | cut -d: -f2 | awk '{print $1}')
hostname=$(hostname)
short_hostname=${hostname:0:15}
echo "${ip} ${short_hostname}" >> /etc/hosts

/usr/bin/wine .wine/drive_c/Program\ Files/Microsoft\ SQL\ Server/80/Tools/Binn/sqlmangr.exe
