
Raspberry Pi Loadout Handout
----------------------------
The purpose of this txt file is to run through the detailed process of loading up new Raspberry Pi's for the Northern Broadband Monitoring Project. 

Before beginning you will need the 'pi' project directory as well as Etcher

# Step 1: Setting up Raspbian Disk Image with Etcher & Copy Project Files
- Download and open Etcher
- Select the Raspbian Lite Disk Image - found in the pi project directory
- Select the appropriate SD card
- Flash image to SD!

# Step 2: Setting up SSH & Change Password

- Run RPi with new SD 

login: `pi`

password: `raspberry`

`sudo raspi-config`

- Navigate to 'Interfacing Options' and selec ssh, hit Enter and select Enable ssh server.
- Navigate to 'Change User Password' & enter new pass (ask now if you don't know!)
- Navigate to 'Finish'

`touch cache.txt`

`nano cache.txt`

`CTRL-X`

`reboot`

- Enter username and new pass

`ifconfig`
- Note the inet addr (IP address) to allow SSHing in future steps


# Step 3: Connect via SSH and SFTP & Copy Files
- From a computer on the same network, open 'Terminal' and enter ssh pi@*inet address from last step* and pass

- Open FileZilla and connect to Pi over SFTP

- Copy /CronJobs, /Dropbox-Uploader & speedtest.py over to 'pi' directory


# Step 4: Install speedtest cli

`sudo apt-get update`

`sudo apt-get upgrade`

`sudo apt-get install python-pip`

`sudo pip install speedtest-cli`

OR SIMPLY

`sudo apt-get update && sudo apt-get upgrade && sudo apt-get install python-pip && sudo pip install speedtest-cli`


# Step 4: Setup Dropbox Uploader??

- Run the following command

`touch DropboxSyncFile && /home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/DropboxSyncFile DropBoxSyncFile && rm DropboxSyncFile`

- Then input the following access token

# Step 5: Test Scripts

`bash CronJobs/speedtest_to_csv.sh`
- Did it work??

`bash Cronjobs/speedtest_uploader.sh`
- Did it work??

- If yes to both, give yourself a pat on the back, you're good to go.


# Step 4: Setup Cron Job
- Give write permission to scripts

`chmod +x /home/pi/CronJobs/speedtest_to_csv.sh && chmod +x /home/pi/CronJobs/speedtest_uploader.sh && crontab -e`

- Then copy in the following lines

`#Upload the file to dropbox at midnight
55 23 * * * /home/pi/CronJobs/speedtest_uploader.sh >> /home/pi/CronOutput.log

#Run speedtest-cli and store in csv every 30 minutes
5-59/20 * * * * /home/pi/CronJobs/speedtest_to_csv.sh >> /home/pi/CronOutput.log`

- Finally run
`sudo /etc/init.d/cron restart`

- ALL DONE! :D




