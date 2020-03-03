# historical hourly data from Weather Underground
#
# Kjell Svensson 2020-02-28

import io
import json
import datetime
import requests
import os.path
import numpy as np
import pandas as pd


def daterange(d1, d2):
    return (d1 + datetime.timedelta(days=i) for i in range((d2 - d1).days + 1))


# my weather station at Galgeberg, Oslo
STATION = 'IOSLO1862'
API_KEY = '4041e9e02d404a5981e9e02d407a59e9'

# date range: 2019-08-20 to 2020-02-25
start_date = date = datetime.date(2019, 8, 20)
end_date = datetime.date(2020, 2, 25)

# loop through dates in range, saving a JSON file for each day
for a in daterange(start_date, end_date):
    date = a.strftime('%Y%m%d')
    filename = 'WUdata-' + str(date) + '.json'

    # skip days that are already downloaded, otherwise: get data and write to file
    if not (os.path.exists(filename)):
        # print(date)
        url = 'https://api.weather.com/v2/pws/history/hourly?stationId=' + STATION
        url += '&format=json&units=m&date=' + str(date) + '&apiKey=' + API_KEY
        url += '&numericPrecision=decimal'
        # print (url)
        res = requests.get(url)

        with io.open(filename, 'w', encoding='utf8') as outfile:
            data = json.dumps(res.json(),
                              indent=4, sort_keys=False,
                              separators=(',', ': '), ensure_ascii=False)
            outfile.write(data)
