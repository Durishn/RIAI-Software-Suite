import csv
import os
from datetime import timedelta, datetime, date, time
import pandas as pd
import config

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def main():

    os.chdir(config.DIRPATH)

    #Iterate through files to find max and min dates
    topmax = "0"
    botmin = "9999999999"
    for filename in os.listdir("./!Data/Cleaner/TimeBounded"):
        if filename.endswith(".csv"):
            df=pd.read_csv("./!Data/Cleaner/TimeBounded/" + filename)
            max=df['Date'].max()
            min=df['Date'].min()
            if max >= topmax and min <= botmin:
                topmax = max
                botmin = min
                maxfile = filename
            #print(filename[:-7] +"  MIN:"+ min +"  MAX:"+ max)


    #Automatic Date Range
    #maxdate=topmax.split("-")
    #findate = date(int(maxdate[0]), int(maxdate[1]), int(maxdate[2]))
    #mindate=botmin.split("-")
    #startdate = date(int(mindate[0]), int(mindate[1]), int(mindate[2])+1)

    #DateRange Presets
    startdate = date(2019, 4, 9)
    findate = date(2019, 11, 30)

    #Create Master CSV with Maximum daterange based on time interval
    with open('./!Data/Cleaner/!TempFiles/MasterTemplate.csv', 'w') as csvFile:
        writer=csv.writer(csvFile,lineterminator='\n',)
        writer.writerow(['Date'] + ['Time'])

        for single_date in daterange(startdate, findate):
            sindate=str(single_date).split("-")
            for h in range(0,24):
                for m in range ( 5, 46, 20):
                    rowdt = datetime(int(sindate[0]), int(sindate[1]), int(sindate[2]), h, m, 0)
                    writer.writerow([single_date] + [rowdt.strftime('%H:%M:%S')])

    masterdf = pd.read_csv("./!Data/Cleaner/!TempFiles/MasterTemplate.csv")
    for filename in os.listdir("./!Data/Cleaner/TimeBounded"):
        if filename.endswith(".csv"):
            df = pd.read_csv("./!Data/Cleaner/TimeBounded/" + filename)
            masterdf = pd.merge(masterdf, df, on=("Date", "Time"), how='left')
            
    masterdf["Datetime"] = masterdf["Date"].map(str) + ' ' + masterdf["Time"].map(str)
    cols = masterdf.columns.tolist()
    cols.insert(0, cols.pop(cols.index("Datetime")))
    masterdf = masterdf[cols]
    export_csv = masterdf.to_csv (r'./!Data/Cleaner/RIAIMaster.csv', index = None, header=True)

    open('./log.txt', "a").write(str(datetime.now()) + '  -  Cleaner/RIAIMaster.csv successfully created \n')

if __name__ == '__main__':
    main()
