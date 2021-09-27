import requests
import json

from pprint import pprint

paramss = {"format": "geojson", 
           "starttime": "2010-01-01", 
           "endtime": "2020-12-31"}
url = r"https://earthquake.usgs.gov/fdsnws/event/1/query?"

alert_levels=['green','yellow','orange','red']
data_list = []

def earthquake(level):
    paramss['alertlevel'] = level
    print(paramss)
    try:
        response = requests.get(url, params = paramss)
        print(response.status_code)
        if response.status_code == 200:
            data = json.loads(response.text)
            #pprint(data)

    except requests.exceptions.RequestException as e:
        print(e)
    finally:
        return data

# get data from    
for level in alert_levels:
    data = earthquake(level)
    if data:
        data_list.append(data)

    
with open('data.json', 'w') as outfile:
    json.dump(data_list, outfile)    
    
