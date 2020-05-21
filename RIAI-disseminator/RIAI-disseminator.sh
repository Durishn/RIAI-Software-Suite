#!/bin/bash
. RIAI-D.config

bash $FILEPATH/Bash/RIAI-D_downloader.sh

/usr/local/bin/python3 $FILEPATH/Python/RIAI-D_mergeCSV.py

/usr/local/bin/python3 $FILEPATH/Python/RIAI-D_cleanCSV.py

/usr/local/bin/python3 $FILEPATH/Python/RIAI-D_plotGen.py

bash $FILEPATH/Bash/RIAI-D_uploader.sh

cd $GITFILEPATH
git add .
git commit -am "SCRIPT - Adding Bi-weekly graphs"
git push
