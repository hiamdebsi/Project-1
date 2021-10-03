# Project-1
Data visualization  project 1
# Earthquake Analysis
Coding in Python, in Jupyter Notebooks, utilizing USGS.gov earthquake api. google maps geomap api, and reverse_geocoder to retrieve country code information.

* Project Contributors: Sherry and Hiam Debsi

## Setup
*Created a github repository
*Created a FOLDER 'starter_code' which has ***Earthquakes_Project_1.ipynb*** and ***Earthquakes_Proj_1_Analysis.ipynb*** execution files.
    *Created a file which has the configuration for the api keys used. This file has not been pushed to github.
    *Earthquakes_Proj_1 (runs first) creates a file called 'data.json' which is saved to the start_code folder.
*Created a FOLDER 'output_data_files' which has the output files and images.:
    Earthquakes_Project_1  saves **EarthqakeData.csv** 
    Earthquakes_Prject_1_Analysis saves various *.png files of interest for project analysis. Screenshot of a heatmap is included.
*Created a FOLDER 'presentation' which holds a Power Point presentation file for final analysis.

API's used: [USGS Earthquake API](https://earthquake.usgs.gov/fdsnws/event/1/?ref=springboard), 
                   [USGS Earthquake Documentation](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)
                   [Google Maps Documenation](https://developers.google.com/maps/documentation/places/web-service/overview)
                    * **Note:** Remember that any API usage beyond the $200 credit will be charged to your personal account. You can set quotas and limits to your daily requests to be sure you can't be charged. Check out [Google Maps Platform Billing](https://developers.google.com/maps/billing/gmp-billing#monitor-and-restrict-consumption) and [Manage your cost of use](https://developers.google.com/maps/documentation/javascript/usage-and-billing#set-caps) for more information.
                    * **Note:** USGS Earthquake API is free.


* Project Scope:
    * An investigation of earthquakes globally,  during a 10 year time frame (2010-2020). 
    * Looking at various factors with earthquakes (when, where, and a possible trend).

* Project Breakdown:
    *Where do earthquakes happen by Country? / top 10
    *What is the density of Magnitudes for Earthquakes
    *What month do earthquakes mostly occur?
    *What is the alert level density of earthquakes
    *Is there a Relationship between Magnitude and % chance of Large Oceanic Event
    

### Part I - ***Earthquakes_Project_1.ipynb***




# Gathering Earthquake Information






Created a series of scatter plots to showcase the following relationships:

* Temperature (F) vs. Latitude
* Humidity (%) vs. Latitude
* Cloudiness (%) vs. Latitude
* Wind Speed (mph) vs. Latitude
