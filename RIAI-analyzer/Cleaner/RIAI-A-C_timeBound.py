import csv
import os
from datetime import timedelta, datetime, date, time
import pandas as pd
import config

def main():

    os.chdir(config.DIRPATH)

    #Iterate through files
    counter = 0
    for filename in os.listdir("./!Data/Cleaner/RawPiData"):
        if filename.endswith(".csv") :
            df=pd.read_csv("./!Data/Cleaner/RawPiData/" + filename)

            #Create New CSV in ADTimeSort
            with open('./!Data/Cleaner/TimeBounded/' + filename[:-4] + 'TB.csv', 'w') as csvFile:
                writer=csv.writer(csvFile,lineterminator='\n',)
                writer.writerow([list(df)[2], list(df)[3], filename[:-7] + ' - ' + list(df)[4], filename[:-7] + ' - ' + list(df)[5], filename[:-7] + ' - ' + list(df)[6]])


                for rowindex in range(0, len(df.index)):

                    #Round time into 1 of 3 thresholds and store in newtime
                    filedate=str(df['Date'].loc[rowindex]).split("-")
                    filetime=str(df['Time'].loc[rowindex]).split(":")
                    filedt=datetime(int(filedate[0]), int(filedate[1]), int(filedate[2]), int(filetime[0]), int(filetime[1]), int(filetime[2]))
                    thresh5 = datetime(int(filedate[0]), int(filedate[1]), int(filedate[2]), int(filetime[0]), 5, 0)
                    thresh25 = datetime(int(filedate[0]), int(filedate[1]), int(filedate[2]), int(filetime[0]), 25, 0)
                    thresh45 = datetime(int(filedate[0]), int(filedate[1]), int(filedate[2]), int(filetime[0]), 45, 0)
                    if filedt <= (thresh5 + timedelta(minutes=15)) and filedt >= (thresh5 - timedelta(minutes=5)):
                        newtime = time(int(filetime[0]), 5, 0)
                    elif filedt <= (thresh25 + timedelta(minutes=15)) and filedt >= (thresh25 - timedelta(minutes=5)):
                        newtime = time(int(filetime[0]), 25, 0)
                    elif filedt <= (thresh45 + timedelta(minutes=15)) and filedt >= (thresh45 - timedelta(minutes=5)):
                        newtime = time(int(filetime[0]), 45, 0)
                    else:
                        newtime = time(int(filetime[0]), int(filetime[1]), int(filetime[2]))
                    #print(filename, " --> ", df['Time'].loc[rowindex], " --> ", newtime)

                    newrow = [df[list(df)[2]].loc[rowindex], str(newtime), df[list(df)[4]].loc[rowindex], df[list(df)[5]].loc[rowindex], df[list(df)[6]].loc[rowindex]]
                    writer.writerow(newrow)

                counter+=1
                print(filename[:-4] + 'TB.csv - Completed')

    open('./log.txt', "a").write(str(datetime.now()) + '  -  ' + str(counter) + ' files successfully copied from /Cleaner/RawPiData to /Cleaner/TimeBounded \n')





if __name__ == '__main__':
    main()
