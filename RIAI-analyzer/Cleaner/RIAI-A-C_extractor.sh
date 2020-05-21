#!/bin/bash
. ./RIAI-A.config
TIMESTAMP=$( date +%Y-%m-%d_%H-%M-%S )

#Create Logs file if one doesn't exist
if [ ! -d "$DIRPATH/log.txt" ]; then
  touch $DIRPATH/log.txt
fi

cd $DIRPATH/!Data/!InputData/SpeedData

#Iterate through each subdirectory
counter=0
for f in *; do
  if [ -d ${f} ]; then
		cd $f

    	#Iterate through each file
    	for d in *; do
    		#If file is named Cleaned_Consolidated.csv
    		if [[ $d == *"Cleaned_Consolidated.csv"* ]]; then
  				DESTFILE="$f-CC.csv"


          #If filesize is larger than setsize
          if [[ $(find ./$d -type f -size +$SIZETHRESH 2>/dev/null) ]]; then
              cp ./$d $DIRPATH/!Data/Cleaner/RawPiData/$DESTFILE
              ((counter++))
          fi

			  fi
		done
    	cd ..
  fi
done
printf "$TIMESTAMP  -  $counter files successfully copied from /InputData to /Cleaner/RawPiData \n" >> $DIRPATH/log.txt
