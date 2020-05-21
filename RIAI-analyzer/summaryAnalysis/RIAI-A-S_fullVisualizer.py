#CREATES STATSUM FILES BASED OFF OF RAITMaster.csv

import csv
import os
from datetime import timedelta, datetime, date, time
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import math
import numpy as np
#import matplotlib.pyplot as plt
#plt.style.use('seaborn-whitegrid')
import config
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

#Distribution Plots for Pis
os.chdir(config.DIRPATH)
RTTdf = pd.read_csv("./!Data/Cleaner/Daily/RTTDailyMaster.csv")
RTTcols = RTTdf.columns.tolist()
RTTdf['Datetime']= pd.to_datetime(RTTdf['Datetime'])
DLdf = pd.read_csv("./!Data/Cleaner/Daily/DLDailyMaster.csv")
DLcols = DLdf.columns.tolist()
DLdf['Datetime']= pd.to_datetime(DLdf['Datetime'])
ULdf = pd.read_csv("./!Data/Cleaner/Daily/ULDailyMaster.csv")
ULcols = ULdf.columns.tolist()
ULdf['Datetime']= pd.to_datetime(ULdf['Datetime'])

#plt.style.use('seaborn-darkgrid')
plt.rcParams.update({'font.size': 16})

fig, ax = plt.subplots()
for i in range(1, len(DLcols)-1):
    ax.plot(DLdf[DLcols[0]], DLdf[DLcols[i]], label='Pi #' + str(i), alpha=0.5)
ax.plot(DLdf[DLcols[0]], DLdf[DLcols[len(DLcols)-1]], label='G-Mean', color='blue', alpha=1)
ax.grid(True)
fig.autofmt_xdate()
plt.gca().set(ylabel='Download Speed (Mbps)', xlabel='Date');
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.subplots_adjust(left=None, bottom=None, right=0.8, top=None, wspace=None, hspace=None)
plt.show()

fig, ax = plt.subplots()
for i in range(1, len(ULcols)-1):
    ax.plot(ULdf[ULcols[0]], ULdf[ULcols[i]], label='Pi #' + str(i), alpha=0.5)
ax.plot(ULdf[ULcols[0]], ULdf[ULcols[len(ULcols)-1]], label='G-Mean', color='blue', alpha=1)
ax.grid(True)
fig.autofmt_xdate()
plt.gca().set(ylabel='Upload Speed (Mbps)', xlabel='Date');
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.subplots_adjust(left=None, bottom=None, right=0.8, top=None, wspace=None, hspace=None)
plt.show()

fig, ax = plt.subplots()
for i in range(1, len(RTTcols)-1):
    ax.plot(RTTdf[RTTcols[0]], RTTdf[RTTcols[i]], label='Pi #' + str(i), alpha=0.5)
ax.plot(RTTdf[RTTcols[0]], RTTdf[RTTcols[len(RTTcols)-1]], label='G-Mean', color='blue', alpha=1)
ax.grid(True)
fig.autofmt_xdate()
plt.yscale("log")
plt.gca().set(ylabel='Round Trip Time (milliseconds)', xlabel='Date');
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.subplots_adjust(left=None, bottom=None, right=0.8, top=None, wspace=None, hspace=None)
plt.show()


#open('./log.txt', "a").write(str(datetime.now()) + '  -  SumStat - Visualizations successfully created \n')
