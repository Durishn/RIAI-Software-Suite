#CREATES SumStatPi BASED OFF OF RAITMaster.csv

import csv
import os
from datetime import timedelta, datetime, date, time
import pandas as pd
import math
import config
from scipy import stats
from numpy import array

def main():

    os.chdir(config.DIRPATH)
    masterdf = pd.read_csv("./!Data/Cleaner/RIAIMaster.csv")
    pi = []
    alpha = 1e-3

    for i in range(0, int((len(masterdf.columns)-3)/3) ):
        pi.append(list(masterdf)[(i*3)+3][:-12])

    #Create csv for Statsum by Pi
    with open('./!Data/SumStat/RIAISumStatPi.csv', 'w') as csvFile:
        writer=csv.writer(csvFile,lineterminator='\n',)
        writer.writerow(['Pi', 'StartDate', 'EndDate', 'Valid', 'Invalid', 'Zero', 'DLMean', 'DLMedian', 'DLMax', 'DLStdDev', 'DLVar', 'DLSkew', 'DLNormal', 'ULMean', 'ULMedian', 'ULMax', 'ULStdDev', 'ULVar', 'ULSkew', 'ULNormal', 'RTTMean', 'RTTMedian', 'RTTMax', 'RTTStdDev', 'RTTVar', 'RTTSkew', 'RTTNormal'])

        for piindex in range(0, len(pi)):
            #Calculate the startdate
            startdateindex=0
            while math.isnan(masterdf[list(masterdf)[(piindex*3)+3]].loc[startdateindex]):
                startdateindex += 1
            startdate = masterdf['Date'].loc[startdateindex]

            #Calculate the enddate
            enddateindex = len(masterdf.index)-1
            while math.isnan(masterdf[list(masterdf)[(piindex*3)+3]].loc[enddateindex]):
                enddateindex -= 1
            enddate = masterdf['Date'].loc[enddateindex]

            #Count valid rows
            validrowcount = 0
            for i in range(0, len(masterdf.index)):
                if math.isnan(masterdf[list(masterdf)[(piindex*3)+3]].loc[i]) == 0:
                    validrowcount += 1

            #Count invalid rows
            invalidrowcount = 0
            for i in range(startdateindex, enddateindex):
                if math.isnan(masterdf[list(masterdf)[(piindex*3)+3]].loc[i]):
                    invalidrowcount += 1

            #Count 0 rows
            zerorowcount = 0
            for i in range(startdateindex, enddateindex):
                if masterdf[list(masterdf)[(piindex*3)+3]].loc[i] == 0:
                    zerorowcount += 1

            #rtt stats
            rttmean = round(masterdf[list(masterdf)[(piindex*3)+3]].mean(axis=0, skipna = True), 5)
            rttmedian = round(masterdf[list(masterdf)[(piindex*3)+3]].median(axis=0, skipna = True), 5)
            rttmax = masterdf[list(masterdf)[(piindex*3)+3]].max()
            rttstd = round(masterdf[list(masterdf)[(piindex*3)+3]].std(), 5)
            rttvar = round(masterdf[list(masterdf)[(piindex*3)+3]].var(), 5)
            rttskew = round(masterdf[list(masterdf)[(piindex*3)+3]].skew(), 5)
            rttarray = array(masterdf[list(masterdf)[(piindex*3)+3]])
            if len(rttarray) < 8:
                rttnorm = 'NA'
            else:
                stat, p = stats.normaltest(rttarray, nan_policy='omit')
                if p < alpha:
                    rttnorm = 'Rejected'
                else:
                    rttnorm = 'Accepted'

            #dl stats
            dlmean = round(masterdf[list(masterdf)[(piindex*3)+4]].mean(axis=0, skipna = True), 5)
            dlmedian = round(masterdf[list(masterdf)[(piindex*3)+4]].median(axis=0, skipna = True), 5)
            dlmax = masterdf[list(masterdf)[(piindex*3)+4]].max()
            dlstd = round(masterdf[list(masterdf)[(piindex*3)+4]].std(), 5)
            dlvar = round(masterdf[list(masterdf)[(piindex*3)+4]].var(), 5)
            dlskew = round(masterdf[list(masterdf)[(piindex*3)+4]].skew(), 5)
            dlarray = array(masterdf[list(masterdf)[(piindex*3)+4]])
            if len(dlarray) < 8:
                rttnorm = 'NA'
            else:
                stat, p = stats.normaltest(dlarray, nan_policy='omit')
                if p < alpha:
                    dlnorm = 'Rejected'
                else:
                    dlnorm = 'Accepted'

            #ul stats
            ulmean = round(masterdf[list(masterdf)[(piindex*3)+5]].mean(axis=0, skipna = True), 5)
            ulmedian = round(masterdf[list(masterdf)[(piindex*3)+5]].median(axis=0, skipna = True), 5)
            ulmax = masterdf[list(masterdf)[(piindex*3)+5]].max()
            ulstd = round(masterdf[list(masterdf)[(piindex*3)+5]].std(), 5)
            ulvar = round(masterdf[list(masterdf)[(piindex*3)+5]].var(), 5)
            ulskew = round(masterdf[list(masterdf)[(piindex*3)+5]].skew(), 5)
            ularray = array(masterdf[list(masterdf)[(piindex*3)+5]])
            if len(ularray) < 8:
                rttnorm = 'NA'
            else:
                stat, p = stats.normaltest(ularray, nan_policy='omit')
                if p < alpha:
                    ulnorm = 'Rejected'
                else:
                    ulnorm = 'Accepted'

            #write row
            newrow=[pi[piindex], startdate, enddate, validrowcount, invalidrowcount, zerorowcount, dlmean, dlmedian, dlmax, dlstd, dlvar, dlskew, dlnorm, ulmean, ulmedian, ulmax, ulstd, ulvar, ulskew, ulnorm, rttmean, rttmedian, rttmax, rttstd, rttvar, rttskew, rttnorm]
            writer.writerow(newrow)
            print('Completed sumstat for - ', pi[piindex])

    open('./log.txt', "a").write(str(datetime.now()) + '  -  SumStat/RIAISumStatPi.csv successfully created \n')



if __name__ == '__main__':
    main()
