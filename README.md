![](image/Vineyard-chalk-soil.jpg)

# Wine , weather and soil. 

## First Segment of four 10.18.2020 
* Group #5 , Sonia , Val, Shawn, Neal, Viral and Meredith. 

## Selected topic:
* Weather and soil conditions affecting wine quality

## Reason we selected the topic:
* We like wine , diverse dataset, enough information to pull across three API's. One for red and white wine , one for weather and one for soil. 

## Description of the source of data:
* Wine API - https://www.globalwinescore.com/api/ 
* Weather API - https://www.ncei.noaa.gov/access/search/data-search/global-summary-of-the-year
* Weather Analysis - https://www.evineyardapp.com/blog/2019/01/17/climate-weather-and-vineyard-management/

## Resources
Data Source:  Python 3.7.6, Anaconda 4.8.4, Jupyter Notebook 6.0.3, Google Colaboratory, spark 3.0.1, java-11, PostgreSQL11.8 (pgAdmin 4.23)
 
## Technologies Used
### * Data Cleaning and Analysis
Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Python.

### * Database Storage
PostgreSQL will be the database we intend to use to store data.
This is the link to our database notebook from google colab: [Red & White Wine_Database](https://colab.research.google.com/drive/1HHpNHs4IPrtHj3WlnRHKqREtJmzaJNHD?usp=sharing)

### * Machine Learning
SciKitLearn is the ML library we'll be using to create a classifier. Our training and testing setup is ___. Extra ML verbiage here.

### * Dashboard
Tableau will be used to connect the database and create visualizations.

## Communication Protocols
* Communicate through Slack.  Everyone uploads data to their Github branch and create a pull request.  Sonia merges the data after everyone discuss the final plans. 

## Questions the team hopes to answer with the data:

* How does weather impact wine quality?
    * How do wine scores correlate with rain, temperature, humidity, and sunlight? Averages ? How can we use this to predict wine quality ? 
    * How does score vary by region in USA , by type ( red, white) ?
    
* How does soil quality affect wine quality ?

 * Wine by wine ID yearly prediction , by region
