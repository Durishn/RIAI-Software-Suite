#!/bin/bash
today=`date '+%m.%d.%y'`;

#Use eth0(first line) for pi configuration (or linux) and en0(second line) for computers :)
macaddr=`cat /sys/class/net/eth0/address`
#macaddr=`ifconfig en0 | grep -Eo ..\(\:..\){5}`
macaddrper=${macaddr//:/.}

#set project filepath
filepath='/home/pi'

#Create directory if one doesn't exist
if [ ! -d "$filepath/$macaddrper" ]; then
  mkdir $filepath/$macaddrper
fi

#Run Speedtest
echo "Running speedtest.py - " `date`
python $filepath/speedtest.py >> $filepath/$macaddrper/$today.csv