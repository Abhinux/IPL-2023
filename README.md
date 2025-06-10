# IPL-2023
In this project, we did a descriptive analysis of team spendings per team in the last five years.
Run <ins>**index.py**</ins> to run data collection and <ins>**index.html**</ins> to run the html.

## Data Collection
We gathered selective data from the official site of IPL T20 i.e. https://iplt20.com/auction/ about the spendings of various teams over last five years using web scraping methods like beautifulsoup.

## Data Cleaning
As we gathered only selective data from sites, we don't need to clean it afterwards.

### Handling Missing values
As we used webscraping methods, we had in mind to select the regions to minimize the risk of missing values

## Data Integrity & Consistency
As there was no case of redundancy or disintegrity of data in the official website we did not have any difficulty in the field of data integrity.

## Data Transformation
We handled data transformation in "Data_collection.py" file while writing data into csv files as we were getting all string values and wanted some integer values from them and the amount section had comma separated values e.g. 10,00,00,000 so we had to handle that also.

## Visual Representation
You can find it in "Data Visualisation.py" file in which we used line graphs to plot yearly spendings of each team.
As well as 'index.html' which displays data in form of pie charts and bar graphs.
