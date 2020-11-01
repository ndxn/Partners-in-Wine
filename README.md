![](image/Vineyard-chalk-soil.jpg)

# *Partners In Wine*

## First Segment of four 10.18.2020 
* Group #5 , Sonia , Val, Shawn, Neal, Viral and Meredith. 

## Second Segement of four 11.01.2020
* Group #5, Sonia , Val, Shawn, Neal, Viral and Meredith 


## Selected topic:
* Weather and soil conditions affecting wine quality

## Reason we selected the topic:
* We like wine , diverse dataset, enough information to pull across three API's. One for red and white wine , one for weather and one for soil. 

## Description of the source of data:
* Wine API - https://www.globalwinescore.com/api/ 
* Weather API - https://www.ncei.noaa.gov/access/search/data-search/global-summary-of-the-year
* Weather Analysis - https://www.evineyardapp.com/blog/2019/01/17/climate-weather-and-vineyard-management/
* 

## Resources
Data Source:  Python 3.7.6, Anaconda 4.8.4, Jupyter Notebook 6.0.3, Google Colaboratory, spark 3.0.1, java-11, PostgreSQL11.8 (pgAdmin 4.23)
 
## Technologies Used
### * Data Cleaning and Analysis
Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Python.

### * Database Storage
PostgreSQL will be the database we intend to use to store data.

### * Machine Learning
SciKitLearn is the ML library we'll be using to create a classifier.  Deep neural network was used to train our model. For the red and white wine's accuracy, we got 84% and 87% respectively.

### * Dashboard
Tableau will be used to connect the database and create visualizations.

***Link to our  notebook from google colab where we have our mock up database and machine learning model: [Red & White Wine_Database & Machine Learning](https://colab.research.google.com/drive/1HHpNHs4IPrtHj3WlnRHKqREtJmzaJNHD?usp=sharing)***

## Communication Protocols
* Communicate through Slack.  Everyone uploads data to their Github branch and create a pull request.  Sonia merges the data after everyone discuss the final plans. 

## Outline of project 

* Presentation - 
  *Google Slides - 
  ***Link to our storyboard for blue print for Tableau: [Tableau Wine Dahsboard](https://docs.google.com/presentation/d/1EcvvVfTKL4tIiHU0a4hKMTTqq7IEtSOj4YtlxHUAT4Q/edit?usp=sharing) 

* Github - 
  * Each member of team has there own branch and makes at least 4 commits per week 
  * README.MD 

* Data exploration - 
  *

* Database - 
  * ERD - to be included
  * Tables and joins 

* Machine Learning Module - 
  *  Description of preliminary data preprocessing 
  *  Description of preliminary feature engineering and preliminary feature selection, including their decision making process. 
  *  Description of how data was split into training and testing sets
  *  Explanation of model choice, including limitations and benefits 
  
* Analysis - 
  * Look at results from wine data alone, wine data with weather data, wine data with soil data and wine data with weather and soil data. 

* Dashboard - 
  * Tableau - Build various tables and interactive map in tablea for dashboard utlizing CSV files and Tableau. Rough draft storyboard built in google slides. 
  ***Link to google presentations:[Wine Quality Machine Learning](https://docs.google.com/presentation/d/1EcvvVfTKL4tIiHU0a4hKMTTqq7IEtSOj4YtlxHUAT4Q/edit?usp=sharing)
  

## Description of data exploration phase 

## Description of the analysis phase of the project 

## Questions the team hopes to answer with the data:

* How does weather impact wine quality?
    * How do wine scores correlate with rain, temperature, humidity, and sunlight? Averages ? How can we use this to predict wine quality ? 
    * How does score vary by region in USA , by type ( red, white) ?
    
* How does soil quality affect wine quality ?

* Wine by wine ID yearly prediction , by region
