#CREATES RIAISumStatFull FILES BASED OFF OF SumStatPi & SumStatDay

import csv
import os
from datetime import timedelta, datetime, date, time
import pandas as pd
import math
import numpy as np
import config

def main():

    os.chdir(config.DIRPATH)
    masterpidf = pd.read_csv("./!Data/SumStat/RIAISumStatPi.csv")
    masterdaydf = pd.read_csv("./!Data/SumStat/RIAISumStatDay.csv")

    #Create csv for Statsum by Pi
    with open('./!Data/SumStat/RIAISumStatFull.csv', 'w') as csvFile:
        writer=csv.writer(csvFile,lineterminator='\n',)
        writer.writerow(['Dataframe', 'StartDate', 'EndDate', 'TotalCount', 'Invalid', 'Zero', 'Mean', 'Median', 'Max', 'StdDev', 'Var', 'Skew'])

        dfclistday = [1,2,3,4,6,7,8,9,10,12,13,14,15,16,18]
        dfclistpi = [6,7,8,9,11,13,14,15,16,18,20,21,22,23,25]

        #Count valid rows
        validrowcount = 0
        for i in range(0, len(masterdaydf.index)):
            if math.isnan(masterdaydf[list(masterdaydf)[2]].loc[i]) == 0:
                validrowcount += 1

        #Count invalid rows
        invalidrowcount = 0
        for i in range(0, len(masterdaydf.index)):
            if math.isnan(masterdaydf[list(masterdaydf)[2]].loc[i]):
                invalidrowcount += 1

        #Count 0 rows
        zerorowcount = 0
        for i in range(0, len(masterdaydf.index)):
            if masterdaydf[list(masterdaydf)[2]].loc[i] == 0:
                zerorowcount += 1

        for ri in range(0, len(dfclistday)):
            mean = round(masterdaydf[list(masterdaydf)[dfclistday[ri]]].mean(axis=0, skipna = True), 5)
            median = round(masterdaydf[list(masterdaydf)[dfclistday[ri]]].median(axis=0, skipna = True), 5)
            max = masterpidf[list(masterdaydf)[dfclistday[ri]]].max()
            std = round(masterdaydf[list(masterdaydf)[dfclistday[ri]]].std(), 5)
            var = round(masterdaydf[list(masterdaydf)[dfclistday[ri]]].var(), 5)
            skew = round(masterdaydf[list(masterdaydf)[dfclistday[ri]]].skew(), 5)

            newrow=[list(masterdaydf)[dfclistday[ri]]+'-Day', masterpidf['StartDate'].min(), masterpidf['EndDate'].max(), validrowcount+invalidrowcount+zerorowcount, invalidrowcount, zerorowcount, mean, median, max, std, var, skew]
            writer.writerow(newrow)
            print('Completed sumstat for - ', list(masterdaydf)[dfclistday[ri]]+'-Day')

        for ri in range(0, len(dfclistpi)):
            mean = round(masterpidf[list(masterpidf)[dfclistpi[ri]]].mean(axis=0, skipna = True), 5)
            median = round(masterpidf[list(masterpidf)[dfclistpi[ri]]].median(axis=0, skipna = True), 5)
            max = masterpidf[list(masterpidf)[dfclistpi[ri]]].max()
            std = round(masterpidf[list(masterpidf)[dfclistpi[ri]]].std(), 5)
            var = round(masterpidf[list(masterpidf)[dfclistpi[ri]]].var(), 5)
            skew = round(masterpidf[list(masterpidf)[dfclistpi[ri]]].skew(), 5)

            newrow=[list(masterpidf)[dfclistpi[ri]]+'-Pi', masterpidf['StartDate'].min(), masterpidf['EndDate'].max(), validrowcount+invalidrowcount+zerorowcount, invalidrowcount, zerorowcount, mean, median, max, std, var, skew]
            writer.writerow(newrow)
            print('Completed sumstat for - ', list(masterpidf)[dfclistpi[ri]]+'-Pi')

    open('./log.txt', "a").write(str(datetime.now()) + '  -  SumStat/RIAISumStatFull.csv successfully created \n')


if __name__ == '__main__':
    main()
