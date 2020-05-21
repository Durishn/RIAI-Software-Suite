#CREATES RIAISumStatDay BASED OFF OF RAITMaster.csv

import csv
import os
from datetime import timedelta, datetime, date, time
import pandas as pd
import math
import numpy as np
from numpy import array
from scipy.stats import skew
import config

def main():

    os.chdir(config.DIRPATH)
    masterdf = pd.read_csv("./!Data/Cleaner/RIAIMaster.csv")
    piindexlist = []
    for i in range(0, int((len(masterdf.columns)-3)/3) ):
        piindexlist.append((i*3)+3)


    #Create csv for Statsum by Pi
    with open('./!Data/SumStat/RIAISumStatDay.csv', 'w') as csvFile:
        writer=csv.writer(csvFile,lineterminator='\n',)
        writer.writerow(['Datetime', 'DLMean', 'DLMedian', 'DLMax', 'DLStdDev', 'DLVar', 'DLSkew', 'ULMean', 'ULMedian', 'ULMax', 'ULStdDev', 'ULVar', 'ULSkew', 'RTTMean', 'RTTMedian', 'RTTMax', 'RTTStdDev', 'RTTVar', 'RTTSkew'])

        for rowindex in range(0, len(masterdf.index)):

            datetimevar = masterdf['Datetime'].loc[rowindex]

            #rtt stats
            rttarray = []
            for i in range(0, len(piindexlist)):
                rttarray.append(masterdf[list(masterdf)[piindexlist[i]]].loc[rowindex])

            rttmean = np.nanmean(rttarray)
            rttmedian = np.nanmedian(rttarray)
            rttmax = np.nanmax(rttarray)
            rttstd = np.nanstd(rttarray)
            rttvar = np.nanvar(rttarray)
            nprttarray = array(rttarray)
            rttarraynan = nprttarray[~np.isnan(nprttarray)]
            rttskew = skew(rttarraynan)

            #dl stats
            dlarray = []
            for i in range(0, len(piindexlist)):
                dlarray.append(masterdf[list(masterdf)[piindexlist[i]+1]].loc[rowindex])

            dlmean = np.nanmean(dlarray)
            dlmedian = np.nanmedian(dlarray)
            dlmax = np.nanmax(dlarray)
            dlstd = np.nanstd(dlarray)
            dlvar = np.nanvar(dlarray)
            npdlarray = array(dlarray)
            dlarraynan = npdlarray[~np.isnan(npdlarray)]
            dlskew = skew(dlarraynan)

            #ul stats
            ularray = []
            for i in range(0, len(piindexlist)):
                ularray.append(masterdf[list(masterdf)[piindexlist[i]+2]].loc[rowindex])

            ulmean = np.nanmean(ularray)
            ulmedian = np.nanmedian(ularray)
            ulmax = np.nanmax(ularray)
            ulstd = np.nanstd(ularray)
            ulvar = np.nanvar(ularray)
            npularray = array(ularray)
            ularraynan = npularray[~np.isnan(npularray)]
            ulskew = skew(ularraynan)

            #write row
            newrow=[datetimevar, dlmean, dlmedian, dlmax, dlstd, dlvar, dlskew, ulmean, ulmedian, ulmax, ulstd, ulvar, ulskew, rttmean, rttmedian, rttmax, rttstd, rttvar, rttskew]
            writer.writerow(newrow)
            print('Completed statsum for - ', datetimevar)

    open('./log.txt', "a").write(str(datetime.now()) + '  -  SumStat/RIAISumStatDay.csv successfully created \n')





if __name__ == '__main__':
    main()
