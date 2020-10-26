#! /usr/bin/python3

import json
import urllib.request
import urllib.error

city = 'Erie,pa,usa'
api_key = 'APIKEY'

try:
    url = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city
            + '&units=imperial&appid=' + api_key)
    json_data = url.read()
    current_weather = json.loads(json_data)

    print(current_weather)

    weather_data = []
    weather_data.append(current_weather['name'])
    weather_data.append(current_weather['main']['temp'])
    weather_data.append(current_weather['main']['feels_like'])
    weather_data.append(current_weather['weather'][0]['main'])
    print(weather_data)

except urllib.error.URLError as url_error:
    print('URL Error code:', url_error.code)
    current_weather = 'Error fetching weather'
