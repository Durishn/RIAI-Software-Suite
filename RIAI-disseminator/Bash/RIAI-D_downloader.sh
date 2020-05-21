#!/bin/bash
. ./RIAI-D.config

TIMESTAMP=$( date +%Y-%m-%d_%H-%M-%S )

#Create Results directory if one doesn't exist
if [ ! -d "$FILEPATH/!Speedtest_Results" ]; then
  mkdir $FILEPATH/!Speedtest_Results
fi

#Create Logs file if one doesn't exist
if [ ! -d "$FILEPATH/log.txt" ]; then
  touch $FILEPATH/log.txt
fi

response=$(bash $FILEPATH/Dropbox-Uploader/dropbox_uploader.sh -s download / $FILEPATH/!Speedtest_Results)

if [[ $response = *"Error"* ]]; then
  printf "ERROR: Could not complete download from Dropbox - $TIMESTAMP \n" >> $FILEPATH/log.txt

else
	printf "Completed Download from Dropbox - $TIMESTAMP \n" >> $FILEPATH/log.txt
fi
