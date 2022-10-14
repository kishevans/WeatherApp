from dotenv import load_dotenv
import os
load_dotenv()
import requests
from flask import Flask, jsonify, render_template, request
import json

import requests
from datetime import datetime
import math



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/Public/index.html') 

@app.route('/update', methods=['POST'])
def weather_update():
    citys = request.get_json()['city']
    urlcity = "http://api.openweathermap.org/geo/1.0/direct?q={}&appid={}".format(citys,os.getenv('APIKEY'))
    city=requests.get(urlcity).json()
    cityd = {
        'city': city[0]['name'],
        'lat':city[0]['lat'],
        'lon':city[0]['lon']
    }
    
    urlweather = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(cityd['lat'],cityd['lon'],os.environ.get("APIKEY"))
    cityweather = requests.get(urlweather).json()
    timestamp = float(cityweather['dt'])
    timezone = cityweather['timezone']
    localtime = datetime.fromtimestamp(timestamp)
    print(localtime)
    weather  = {
        'description': cityweather['weather'][0]['description'],
        'time': localtime,
        'day': localtime.strftime("%A"),
        'icon': cityweather['weather'][0]['icon'],
        'temp': cityweather['main']['temp']
    }
    
    return jsonify({
        'city': cityd['city'],
        'weather': weather['description'],
        'day': weather['day'],
        'icon': weather['icon'],
        'temp': (math.trunc(weather['temp']-273.5)),
        'time':weather['time']
    })

   




if __name__ == "__main__":
    app.run(debug=True)
    
    
