#CREATES SumStat - Distribution Graphics BASED OFF OF RAITMaster.csv

import csv
import os
from datetime import timedelta, datetime, date, time
import pandas as pd
import math
import numpy as np
#import matplotlib.pyplot as plt
#plt.style.use('seaborn-whitegrid')
import config
import matplotlib.pyplot as plt

#Distribution Plots for Pis
os.chdir(config.DIRPATH)
masterdf = pd.read_csv("./!Data/Cleaner/RIAIMaster.csv")
sumstatdaydf = pd.read_csv("./!Data/SumStat/RIAISumStatDay.csv")
piindexlist = []
for i in range(0, int((len(masterdf.columns)-3)/3) ):
    piindexlist.append((i*3)+3)


sampleday = 4890
samplepi = 6
dlarray, piarray, datearray = ([] for i in range(3))

#Fill and clean dlarray
for i in range(0, len(piindexlist)):
    dlarray.append(masterdf[list(masterdf)[piindexlist[i]+1]].loc[sampleday])
for i in reversed(range(len(piindexlist))):
    if math.isnan(dlarray[i]) or np.isnan(dlarray[i]):
        dlarray.pop(i)

for i in range(0, len(masterdf[list(masterdf)[piindexlist[samplepi]+1]])):
    piarray.append(masterdf[list(masterdf)[piindexlist[samplepi]+1]].loc[i])
    datearray.append(str(masterdf[list(masterdf)[0]].loc[i]) + ' ' + str(masterdf[list(masterdf)[1]].loc[i]))

pinanarray = piarray.copy()
print(pinanarray)
for i in reversed(range(len(pinanarray))):
    if math.isnan(pinanarray[i]) or np.isnan(pinanarray[i]):
        pinanarray.pop(i)

for i in reversed(range(len(dlarray))):
    if math.isnan(dlarray[i]) or np.isnan(dlarray[i]):
        dlarray.pop(i)

#Build data from sumstat


plt.hist(dlarray, bins=40, range=[np.nanmin(dlarray)-(np.nanmin(dlarray)*0.1), np.nanmax(dlarray)+(np.nanmax(dlarray)*0.1)])
plt.gca().set(ylabel='Frequency', xlabel='Download Speed (Mbps)');
plt.yticks(np.arange(0, 3, 1))
plt.show()

plt.hist(pinanarray, bins=40, range=[np.nanmin(pinanarray)-(np.nanmin(pinanarray)*0.1), np.nanmax(pinanarray)+(np.nanmax(pinanarray)*0.1)])
plt.gca().set(ylabel='Frequency', xlabel='Download Speed (Mbps)');
plt.show()


open('./log.txt', "a").write(str(datetime.now()) + '  -  SumStat - Distribution Graphics successfully created \n')
