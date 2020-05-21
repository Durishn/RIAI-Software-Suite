import csv
import os
from datetime import timedelta, datetime, date, time
import pandas as pd
import numpy as np
from scipy import stats
import math
import config

def main():

    os.chdir(config.DIRPATH)
    df = pd.read_csv("./!Data/Cleaner/RIAIMaster.csv")
    cols = df.columns.tolist()

    df['Datetime'] =  pd.to_datetime(df['Datetime'], format='%Y-%m-%d %H:%M:%S')
    df.set_index('Datetime', inplace=True)
    df.pop('Date')
    df.pop('Time')
    piindexlist = []
    for i in range(0, int((len(df.columns))/3) ):
        piindexlist.append((i*3))

    newdf = df.resample('D').mean()



    RTTdf = pd.DataFrame(index=newdf.index)
    DLdf = pd.DataFrame(index=newdf.index)
    ULdf = pd.DataFrame(index=newdf.index)
    for i in range(0, len(piindexlist)):
        RTTdf[list(newdf)[piindexlist[i]]] = newdf[list(newdf)[piindexlist[i]]]
        DLdf[list(newdf)[piindexlist[i]+1]] = newdf[list(newdf)[piindexlist[i]+1]]
        ULdf[list(newdf)[piindexlist[i]+2]] = newdf[list(newdf)[piindexlist[i]+2]]



    RTTmean = []
    DLmean = []
    ULmean = []
    for i in newdf.index:
        RTTarray = []
        for j in range(0, len(RTTdf.columns)):
            RTTarray.append(RTTdf[list(RTTdf)[j]].loc[i]+1)
        for j in reversed(range(len(RTTarray))):
            if math.isnan(RTTarray[j]) or np.isnan(RTTarray[j]):
                RTTarray.pop(j)
        RTTmean.append(stats.gmean(RTTarray)-1)

        DLarray = []
        for j in range(0, len(DLdf.columns)):
            DLarray.append(DLdf[list(DLdf)[j]].loc[i]+1)
        for j in reversed(range(len(DLarray))):
            if math.isnan(DLarray[j]) or np.isnan(DLarray[j]):
                DLarray.pop(j)
        DLmean.append(stats.gmean(DLarray)-1)

        ULarray = []
        for j in range(0, len(ULdf.columns)):
            ULarray.append(ULdf[list(ULdf)[j]].loc[i]+1)
        for j in reversed(range(len(ULarray))):
            if math.isnan(ULarray[j]) or np.isnan(ULarray[j]):
                ULarray.pop(j)
        ULmean.append(stats.gmean(ULarray)-1)

    RTTdf['G-Mean'] = RTTmean
    DLdf['G-Mean'] = DLmean
    ULdf['G-Mean'] = ULmean

    #RTTdf['A-Mean'] = RTTdf.mean(axis=1)
    #RTTdf['Median'] = RTTdf.median(axis=1)
    #DLdf['A-Mean'] = DLdf.mean(axis=1)
    #DLdf['Median'] = DLdf.median(axis=1)
    #ULdf['A-Mean'] = ULdf.mean(axis=1)
    #ULdf['Median'] = ULdf.median(axis=1)

    #print(RTTdf)

    export_csv = RTTdf.to_csv (r'./!Data/Cleaner/Daily/RTTDailyMaster.csv', index = True, header=True)
    export_csv = DLdf.to_csv (r'./!Data/Cleaner/Daily/DLDailyMaster.csv', index = True, header=True)
    export_csv = ULdf.to_csv (r'./!Data/Cleaner/Daily/ULDailyMaster.csv', index = True, header=True)


if __name__ == '__main__':
    main()
