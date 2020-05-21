import os, csv, datetime
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numpy as np
import pandas as pd
import config

#PRESET ROOT DIRECTORY
root_dir = config.FILEPATH
git_dir = config.GITFILEPATH

csv_in = 'Cleaned_Consolidated.csv'

#Move to Backup Director and iterate through each subdirectory
for entry in os.scandir(root_dir + '/!Speedtest_Results'):
	if entry.is_dir():
		os.chdir(entry.path)

		#Get Filename
		filename = entry.path.replace(root_dir + '/!Speedtest_Results/', '')

		#Create DataFrame
		with open(csv_in) as f:
			f.readline()
			df = pd.read_csv(csv_in)

		df["Period"] = df["Date"].map(str) + ' ' + df["Time"]

		if len(df) > 148:
			#plot([go.Scatter(x=[1, 2, 3], y=[3, 1, 6])])
			#Plot with Plotly
			trace1 = go.Scatter(x=df['Period'], y=df['Download (Mbit/s)'], mode='lines', name='Download (Mbit/s)')
			trace2 = go.Scatter(x=df['Period'], y=df['Upload (Mbit/s)'], mode='lines', name='Upload (Mbit/s)' )
			layout = go.Layout(title=filename+'-plot', plot_bgcolor='rgb(230, 230,230)')

			fig = go.Figure(data=[trace1, trace2], layout=layout)

			# Plot data, save as HTML file
			plot(fig, filename='!'+filename+'-plot.html')
			plot(fig, filename=git_dir+filename+'.html')

			# Plot data, save to Plot.ly account
			#plot(fig, filename=filename+'-plot')


os.chdir(root_dir)
open('log.txt', "a").write('Completed Plots - ' + str(datetime.datetime.now()) + '\n')
