#!/bin/bash
today=`date '+%m.%d.%y'`;

#Use eth0(first line) for pi configuration and en0(second line) for computers :)
macaddr=`cat /sys/class/net/eth0/address`
#macaddr=`ifconfig en0 | grep -Eo ..\(\:..\){5}`
macaddrper=${macaddr//:/.}

#set project filepath, only use PWD when not executed via cronjobs
filepath='/home/pi'

response=$(bash $filepath/Dropbox-Uploader/dropbox_uploader.sh upload $filepath/$macaddrper/$today.csv $macaddrper/$today.csv)

#If connection cannot be made, send filename to caching folder
if [[ $response = *"Error"* ]] || [[ $response = *"error"* ]]; then
  echo "Could not resolve host - logging filename in cache.txt - "`date`
  if [ ! -f "cache.txt" ]; then
  	touch cache.txt
  fi
  echo $today >> cache.txt

#If connection CAN be made, check caching folder
else
  #Else if file does not exist, delete line and continue loop
  if [[ $response = *"No such file"* ]]; then
    echo $today".csv does not exist - "`date`

  #Else if file exists with same hash...
  elif [[ $response = *"same hash"* ]]; then
    echo $today".csv exists with the same hash - "`date`
  
  else
    echo $today".csv successfully uploaded - "`date`
  fi
  
  #If cache.txt is not empty -> upload all files
  if [ -s cache.txt ]; then
  	errflag=0
  	filecounter=0

  	#loop through file attempting to upload each file
  	while [ -s cache.txt ] && [ "$errflag" == 0 ]; do
  	  filename=$(head -n 1 cache.txt)
  	  response=$(bash $filepath/Dropbox-Uploader/dropbox_uploader.sh upload $filepath/$macaddrper/$filename.csv $macaddrper/$filename.csv)
      
  	  #If error connecting to host, break from loop
  	  if [[ $response = *"Error"* ]]; then
  	  	errflag=1

  	  #Else if file does not exist, delete line and continue loop
  	  elif [[ $response = *"No such file"* ]]; then
  	  	echo $filename".csv does not exist"
  	  	tail -n +2 "cache.txt" > "cache.txt.tmp" && mv "cache.txt.tmp" "cache.txt"

      #Else if file exists with same hash, delete line and continue
      elif [[ $response = *"same hash"* ]]; then
        echo $filename".csv exists with the same hash"
        tail -n +2 "cache.txt" > "cache.txt.tmp" && mv "cache.txt.tmp" "cache.txt"

  	  #Else upload is succesful, delete first line of file and continue loop
  	  else
  	  	echo $filename".csv successfully uploaded"
  	  	tail -n +2 "cache.txt" > "cache.txt.tmp" && mv "cache.txt.tmp" "cache.txt"
  	  	((filecounter++))
  	  fi
  	done

  	#Print Output message after loop completiong
  	if [[ "$errflag" == 1 ]]; then
  	  echo "Could not connect to host"
  	else
  	  echo $filecounter "cache files uploaded"
  	fi

  #Else cache.txt is empty
  else
  	echo "cache.txt is currently empty"
  fi
fi

