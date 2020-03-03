# collate and refactor downloaded JSON to one CSV file with daily data
#
# Kjell Svensson 2020-02-28

import io
import json
import datetime
import numpy as np
import pandas as pd

def daterange(d1, d2):
    return (d1 + datetime.timedelta(days=i) for i in range((d2 - d1).days + 1))

start_date = date = datetime.date(2019, 8, 20)
end_date = datetime.date(2020, 2, 25)

# empty dataframe to store daily values
df = pd.DataFrame(columns=['date', 'temp'])
for a in daterange(start_date, end_date):
    date = a.strftime('%Y%m%d')
    filename = 'WUdata-' + str(date) + '.json'
    with open(filename) as data_file:
        data = json.load(data_file)
    # put the day's hourly values in a dataframe
    df2 = pd.json_normalize(data, ['observations'])
    # calculate the mean for the day and store in a new dataframe
    aggr_data = {'date': [date], 'temp': [df2['metric.tempAvg'].mean()]}
    df3 = pd.DataFrame(aggr_data)
    # add a row to the df dataframe
    df = pd.concat([df, df3], ignore_index=True)

# output to CSV
df.to_csv('Galgeberg2.csv', index=False)


