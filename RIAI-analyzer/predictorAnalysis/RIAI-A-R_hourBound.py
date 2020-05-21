#CREATES RIAISumStatDay BASED OFF OF RAITMaster.csv

import csv
import os
from datetime import timedelta, datetime, date, time
import pandas as pd
import math
import numpy as np
from numpy import array
from scipy.stats import skew
from scipy.stats.mstats import gmean
import config

def main():

    os.chdir(config.DIRPATH)
    masterdf = pd.read_csv("./!Data/SumStat/RIAISumStatDay.csv")
    piindexlist = []


    #Create csv for Statsum by Pi
    with open('./!Data/regAnalysis/RIAIHourlyMedian.csv', 'w') as csvFile:
        writer=csv.writer(csvFile,lineterminator='\n',)
        writer.writerow(['Datetime', 'DLMean', 'DLMedian', 'DLMax', 'ULMean', 'ULMedian', 'ULMax', 'RTTMean', 'RTTMedian', 'RTTMax'])

        for rowindex in range(0, len(masterdf.index)-1, 3):

            datetimevar = pd.to_datetime(masterdf['Datetime'].loc[rowindex]) - timedelta(minutes=5)

            dlmean = (masterdf['DLMean'].loc[rowindex]*masterdf['DLMean'].loc[rowindex+1]*masterdf['DLMean'].loc[rowindex+2])**(1/3)
            dlmedian = (masterdf['DLMedian'].loc[rowindex]*masterdf['DLMedian'].loc[rowindex+1]*masterdf['DLMedian'].loc[rowindex+2])**(1/3)
            dlmax = max(masterdf['DLMax'].loc[rowindex], masterdf['DLMax'].loc[rowindex+1], masterdf['DLMax'].loc[rowindex+2])

            ulmean = (masterdf['ULMean'].loc[rowindex]*masterdf['ULMean'].loc[rowindex+1]*masterdf['ULMean'].loc[rowindex+2])**(1/3)
            ulmedian = (masterdf['ULMedian'].loc[rowindex]*masterdf['ULMedian'].loc[rowindex+1]*masterdf['ULMedian'].loc[rowindex+2])**(1/3)
            ulmax = max(masterdf['ULMax'].loc[rowindex], masterdf['ULMax'].loc[rowindex+1], masterdf['ULMax'].loc[rowindex+2])

            rttmean = (masterdf['RTTMean'].loc[rowindex]*masterdf['RTTMean'].loc[rowindex+1]*masterdf['RTTMean'].loc[rowindex+2])**(1/3)
            rttmedian = (masterdf['RTTMedian'].loc[rowindex]*masterdf['RTTMedian'].loc[rowindex+1]*masterdf['RTTMedian'].loc[rowindex+2])**(1/3)
            rttmax = max(masterdf['RTTMax'].loc[rowindex], masterdf['RTTMax'].loc[rowindex+1], masterdf['RTTMax'].loc[rowindex+2])

            #write row
            newrow=[str(datetimevar), dlmean, dlmedian, dlmax, ulmean, ulmedian, ulmax, rttmean, rttmedian, rttmax]
            writer.writerow(newrow)
            print('Completed statsum for - ', str(datetimevar))

    #open('./log.txt', "a").write(str(datetime.now()) + '  -  SumStat/RIAISumStatDay.csv successfully created \n')





if __name__ == '__main__':
    main()
