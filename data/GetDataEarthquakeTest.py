#TESTING FILES ONLY COLLECTING JSON GETTING DATA

import requests
import json
import pandas as pd
#import reverse_geocoder as rg  pip install reverse_geocoder
from datetime import datetime as dt
import os
import csv

from pprint import pprint

paramss = {"format": "geojson", 
           "starttime": "2010-01-01", 
           "endtime": "2020-12-31"}
url = r"https://earthquake.usgs.gov/fdsnws/event/1/query?"

alert_levels=['green','yellow','orange','red']
data_list = []

def earthquake(level):
    # function to get the json data from earthquake.usgs.gov
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
def getJsonData():
    for level in alert_levels:
        data = earthquake(level)
        if data:
            data_list.append(data)
    #save to .json file
    with open('data.json', 'w') as outfile:
     json.dump(data_list, outfile) 

#getJsonData()    
   
    
#get the json file to loop through
# Opening JSON file
f = open('data.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)
earthquake_subdata= []
# Iterating through the json
# list
for feature in data[0]['features']:
    #pprint(feature)
    dEarthquake = {}
    #print(feature['id'])
    dEarthquake['id']= feature['id']
    dEarthquake['lat']= feature['geometry']['coordinates'][0]
    dEarthquake['lng']= feature['geometry']['coordinates'][1]
    dEarthquake['latlngdepth']=feature['geometry']['coordinates']
    dEarthquake['alert']= feature['properties']['alert']
    dEarthquake['place']= feature['properties']['place']
    dEarthquake['date']= dt.fromtimestamp(feature['properties']['time']/1000)
    dEarthquake['magnitude']= feature['properties']['mag']
    dEarthquake['tsunami']= feature['properties']['tsunami']
    dEarthquake['type']= feature['properties']['type']
    
    earthquake_subdata.append(dEarthquake)



    #pprint(i)
 
# Closing file
f.close()
# get the json information that we need

earthquake_data= pd.DataFrame(earthquake_subdata)


output_folder = "../outputs/"
earthquake_data.to_csv(output_folder + "EarthquakeData.csv", encoding="utf-8", index = True)





# def reverseGeocode(coordinates):
#     result = rg.search(coordinates)
#     # result is a list containing ordered dictionary.
#     pprint.pprint(result)
# #Driver function
# if __name__==“__main__“:
#     # Coordinates tuple.Can contain more than one pair.
#     coordinates =(-21.1005,-0.7603)
#     reverseGeocode(coordinates)






