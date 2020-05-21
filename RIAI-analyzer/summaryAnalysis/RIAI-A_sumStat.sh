#!/bin/bash
. ./RIAI-A.config

/usr/local/bin/python3 $DIRPATH/SumStat/RIAI-A-S_day.py

/usr/local/bin/python3 $DIRPATH/SumStat/RIAI-A-S_pi.py

/usr/local/bin/python3 $DIRPATH/SumStat/RIAI-A-S_full.py
