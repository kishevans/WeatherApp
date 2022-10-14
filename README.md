# WeatherApp
A web app that shows the weather of a city upon searching the city's name.
The app consumes the openweathermap api for weather data as well as the opeweathermap
geocoding api for city coordinates

## Prerequisites
* Python
* pip

## Initial setup
1. Clone this repo
2. pip install -r requirements.txt
3. Register with openweathermap.org to obtain api keys. Save in .env file

## Run
``` 
export FLASK_APP=app.py
flask run --reload
```

## Test
Search for a city and the results will be displayed

## TODO
1. Update time
2. Update temperature change functionality
3. Fix css issues on smaller screens