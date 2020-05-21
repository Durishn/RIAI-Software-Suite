import os, datetime, operator, csv, codecs
import config

#PRESET ROOT DIRECTORY
root_dir = config.FILEPATH

csv_in = 'Consolidated.csv'
csv_out = 'Cleaned_Consolidated.csv'
csv_header = 'MAC Address,External IP Address,Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)\n'

#Move to Backup Director and iterate through each subdirectory
for entry in os.scandir(root_dir + '/!Speedtest_Results'):
	if entry.is_dir():
		os.chdir(entry.path)

		outputfile = open(csv_out,'w')
		writer = csv.writer(outputfile, delimiter=',')

		with open(csv_in) as f:
			f.readline()

			#replace all NULL values
			reader = csv.reader(x.replace('\0', '') for x in f)

			#replace all Dates
			for row in reader:
				if row[2] != 'Date' and row[2] != 'ERROR':
					row[2] = str(datetime.datetime.strptime(row[2], '%m.%d.%y').date())
				writer.writerow(row)
		outputfile.close()

		#Sort new output file
		newreader = csv.reader(open(csv_out), delimiter=",")
		sortedlist = sorted(newreader, key=operator.itemgetter(2), reverse=False)

		#Write new list to file
		with open(csv_out, "w") as file:
			file.write(csv_header)
			fileWriter = csv.writer(file, delimiter=',')
			for row in sortedlist:
				fileWriter.writerow(row)
		print('Completed Clean of ' + csv_in)




os.chdir(root_dir)
open('log.txt', "a").write('Completed Cleaning of Consolidations - ' + str(datetime.datetime.now()) + '\n')
