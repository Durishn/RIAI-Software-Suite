import os
import re
import subprocess
import time
import socket
import fcntl
import struct
import uuid
from urllib2 import urlopen

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

response = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read()

#If response is retrieved from speedtest-cli
if len(response) != 0: 
	ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
	download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
	upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

	ping[0] = ping[0].replace(',', '.')
	download[0] = download[0].replace(',', '.')
	upload[0] = upload[0].replace(',', '.')
	ip = urlopen('http://ip.42.pl/raw').read()

#If no response from network, plug zero into datapoints
else:
	ping = ['0']
	download = ['0']
	upload = ['0']
	ip = 'ERROR'

filepath = "/home/pi"
with open('/sys/class/net/eth0/address') as f:
    mac = f.readline()
mac = mac[:-1]
mac = mac.replace(":", ".")

try:
    if os.stat(filepath + '/' + mac + '/' + time.strftime('%m.%d.%y') + '.csv').st_size == 0:
        print 'MAC Address,External IP Address,Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)'
except:
    pass


print '{},{},{},{},{},{},{}'.format(mac,ip, time.strftime('%m.%d.%y'), time.strftime('%H:%M:%S'), ping[0], download[0], upload[0])