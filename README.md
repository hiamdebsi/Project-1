# Project-1
Data visualization  project 1
# Earthquake Analysis
Coding in Python, in Jupyter Notebooks, utilizing USGS.gov earthquake api. google maps geomap api, and reverse_geocoder to retrieve country code information.

* Project Contributors: Sherry and Hiam Debsi
* Team Project using github to push and pull updates. 

## Setup
*Created a github repository
*Created a FOLDER 'starter_code' which has ***Earthquakes_Project_1.ipynb*** and ***Earthquakes_Proj_1_Analysis.ipynb*** execution files.
    *Created a file which has the configuration for the api keys used. This file has not been pushed to github.
    *Earthquakes_Proj_1 (runs first) creates a file called 'data.json' which is saved to the start_code folder.
*Created a FOLDER 'output_data' which has the output files and images.:
    Earthquakes_Project_1  saves **EarthqakeData.csv** 
    Earthquakes_Prject_1_Analysis saves various *.png files of interest for project analysis. Screenshot of a heatmap is included.
*Created a FOLDER 'presentation' which holds a Power Point presentation saved as a .pdf file for a final analysis review once downloaded.

API's used: [USGS Earthquake API](https://earthquake.usgs.gov/fdsnws/event/1/?ref=springboard), 
                   [USGS Earthquake Documentation](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)
                   [Google Maps Documenation](https://developers.google.com/maps/documentation/places/web-service/overview)
                    * **Note:** Remember that any API usage beyond the $200 credit will be charged to your personal account. You can set quotas and limits to your daily requests to be sure you can't be charged. Check out [Google Maps Platform Billing](https://developers.google.com/maps/billing/gmp-billing#monitor-and-restrict-consumption) and [Manage your cost of use](https://developers.google.com/maps/documentation/javascript/usage-and-billing#set-caps) for more information.
                    * **Note:** USGS Earthquake API is free.


* Project Scope:
    * An investigation of earthquakes globally,  during a 10 year time frame (2010-2020). 
    * Looking at various factors with earthquakes (when, where, and a possible trend).



### Part I - ***Earthquakes_Project_1.ipynb***
# Gathering Earthquake Information

### Data exporation and cleanup

1. pip install reverse_geocoder 
    * this allows one to convert latitude and longitude values to gather Country and Country Code information. 
2.  Requested geojson infomation from the USGS site 
    * Parameters: **Alert Levels**: Green, Yellow, Orange and Red , **Dates to and from** Jan 1st 2010 to Dec 31st 2020
3.  Saved the json information as data.json in the start_code folder.
4.  Used reverse_geocoder to get more Country information from lat/long
5.  Ensured the cleaning of the data after it was retrieved.  Used Pandas to clean and format
6.  Merged the files
7. Saved the clean data as EarthquakeData.csv to output_data folder


### Part II- ***Earthquakes_Proj_1_Analysis.ipynb***
# Final Data Analysis

1. Loaded the clean csv file and formatted the date column as datetime
2. Created Project question to answer through data analysis
* Project Breakdown:
    * Where do earthquakes happen by Country? / top 10
    * What is the density of Magnitudes for Earthquakes
    * What month do earthquakes mostly occur?
    * What is the alert level density of earthquakes
    * Is there a Relationship between Magnitude and % chance of Large Oceanic Event

3. Used matplotlib to create a series of charts to support our findings and analysis.
4. Showed scatter plots and regression analysis to display any relationship between Magnitude and % Chance of Large Oceanic Event.
5. Used heatmaps and tags to display earthquake zones. 
6. Saved the plots as *.png files in the output_data folder.
6. Did a write up ***summarizing major findings*** at the top Earthquakes_Proj_1_Analysis.ipynb file.
7. Created a power point presentation, saved as Project_1_Earthquake_Analysis_Presentation.pdf in the presentation folder,  which shows a summary of the findings as well. This file needs to be downloaded to show vertically.
8. The summary shows each question asked with an analysis of what was found. 



