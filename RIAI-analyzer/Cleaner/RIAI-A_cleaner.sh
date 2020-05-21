#!/bin/bash
. ./RIAI-A.config

bash $DIRPATH/Cleaner/RIAI-A-C_extractor.sh

/usr/local/bin/python3 $DIRPATH/Cleaner/RIAI-A-C_timeBound.py

/usr/local/bin/python3 $DIRPATH/Cleaner/RIAI-A-C_merger.py
