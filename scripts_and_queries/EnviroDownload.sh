# Script used to download weather data from climate.weather.gc.ca from specified dates and weather stations

for year in `seq 2019 2020`;do for month in `seq 1 12`;do wget --content-disposition "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=53506&Year=${year}&Month=${month}&Day=14&timeframe=1&submit= Download+Data" ;done;done
