# sqlalchemy-challenge

Congratulations! You have decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you have decided to do a climate analysis about the area. 

Part 1: Analyze and Explore the Climate Data

In this section, we’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, we’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib.
![Screen Shot 2023-07-18 at 8 42 22 PM](https://github.com/kshirazi5/sqlalchemy-challenge/assets/116853144/2824752f-ea8d-49fd-ad59-5343dc552732)

![Screen Shot 2023-07-18 at 8 42 50 PM](https://github.com/kshirazi5/sqlalchemy-challenge/assets/116853144/6d7baeb3-5dc5-4064-9fcd-8369b8b02514)


Part 2: Design Your Climate App

Now that we’ve completed our initial analysis, we’ll design a Flask API based on the queries that we just developed.To do so, use Flask to create your routes as follows:


/
Start at the homepage.
List all the available routes.
/api/v1.0/precipitation
Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
Return the JSON representation of your dictionary.
/api/v1.0/stations
Return a JSON list of stations from the dataset.
/api/v1.0/tobs
Query the dates and temperature observations of the most-active station for the previous year of data.
Return a JSON list of temperature observations for the previous year.
/api/v1.0/<start> and /api/v1.0/<start>/<end>
Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
