import os
import datetime
import csv
import config

#PRESET ROOT DIRECTORY
root_dir = config.FILEPATH

csv_header = 'MAC Address,External IP Address,Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)'
csv_header2 = 'MAC Address,IP Address,Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)'
csv_out = 'Consolidated.csv'

#Move to Backup Director and iterate through each subdirectory
for entry in os.scandir(root_dir+'/!Speedtest_Results'):
	if entry.is_dir():
		os.chdir(entry.path)

		#Iterate through each file within each subdirectory
		for dirpath, dirnames, filenames in os.walk(entry.path):
			pass

		#Build list of CSV files
		csv_list = []
		for file in filenames:
			if file.endswith('.csv'):
				csv_list.append(file)

		#Writer Header
		csv_merge = open(csv_out, 'w')
		csv_merge.write(csv_header)
		csv_merge.write('\n')

		#Merge each line of csv files into Consolidated.csv
		for file in csv_list:
			if file != csv_out and file != 'Cleaned_Consolidated.csv':
				csv_in = open(entry.path+'/'+file, 'r')
				for line in csv_in:
					if line.startswith(csv_header) or line.startswith(csv_header2):
						continue
					csv_merge.write(line)
				csv_in.close()
				print('Completed Consolidation of ' + file)

		csv_merge.close()
#with open("logs.txt", "a") as myfile:
#    myfile.write('Completed Consolidation of CSVs - ')

os.chdir(root_dir)
open('log.txt', "a").write('Completed Consolidation of CSVs - ' + str(datetime.datetime.now()) + '\n')
