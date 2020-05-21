#!/bin/bash
. ./RIAI-D.config

TIMESTAMP=$( date +%Y-%m-%d_%H-%M-%S )
ERRFLAG=false

#Create Logs file if one doesn't exist
if [ ! -d "$FILEPATH/log.txt" ]; then
  touch $FILEPATH/log.txt
fi

cd $FILEPATH/!Speedtest_Results

#Iterate through each subdirectory
for f in *; do
	if [ -d ${f} ]; then
		cd $f

    	#Iterate through each file
    	for d in *; do
    		#If file is .html file
    		if [[ $d == *".html"* ]]; then
  				SOURCEPATH="$(pwd -P)/$d"
  				TARGETPATH="$f/$d"
  				#printf "$SOURCEPATH\n$TARGETPATH\n\n"

  				#Upload File to Dropbox
  				response=$(bash $FILEPATH/Dropbox-Uploader/dropbox_uploader.sh upload $SOURCEPATH $TARGETPATH)

				if [[ $response = *"Error"* ]]; then
					printf "Error occured in uploading\n"
					ERRFLAG=true
				else
					printf "Upload Successful\n"
				fi
			fi
		done
    	cd ..
    fi
done

#Print results to log file
if [ $ERRFLAG = true ]; then
  printf "ERROR: Could not complete upload to Dropbox - $TIMESTAMP \n" >> $FILEPATH/log.txt

else
	printf "Completed Upload to Dropbox - $TIMESTAMP \n" >> $FILEPATH/log.txt
fi
