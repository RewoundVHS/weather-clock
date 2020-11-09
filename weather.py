#! /usr/bin/python3
import json
import urllib.request
import urllib.error
from PIL import Image, ImageDraw, ImageFont
import sys
from datetime import date, datetime

city = 'Erie'
lat = 42.13
lon = -80.09
api_key = 'APIKEY'

# TODO generalize printing data to canvas with Y axis offsets
# TODO add icons for different weather conditions
# TODO find larger font
# TODO add dates for forecast days

try:
    url = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/onecall?lat='
    + str(lat) + '&lon=' + str(lon) + '&units=imperial&exclude=minutely,hourly&appid=' + api_key)
    json_data = url.read()
    current_weather = json.loads(json_data)

    cur_weather_data = []
    cur_weather_data.append(city)
    cur_weather_data.append(str(round(current_weather['current']['temp'])) + '°')
    cur_weather_data.append(str(round(current_weather['current']['feels_like'])) + '°')
    cur_weather_data.append(current_weather['current']['weather'][0]['main'])
    print('current: ', cur_weather_data)

    # TODO loop to create entries for next 5 or 7 days
    tom_weather_data = []
    tom_weather_data.append(str(round(current_weather['daily'][0]['temp']['min'])) + '°')
    tom_weather_data.append(str(round(current_weather['daily'][0]['temp']['max'])) + '°')
    tom_weather_data.append(current_weather['daily'][0]['weather'][0]['main'])
    print('tomorrow: ', tom_weather_data)

except urllib.error.URLError as url_error:
    print('URL Error code:', url_error.code)
    current_weather = 'Error fetching weather'

im = Image.open('canvas.bmp')

draw = ImageDraw.Draw(im)
font = ImageFont.load("./fonts/curieBold-12.pil")
draw.text((10,30), ' '.join(cur_weather_data), font=font, fill=128)

today = date.today()
curDate = today.strftime("%B %d, %Y")
draw.text((10,15), curDate, font=font, fill=128)

now = datetime.now()
curTime = now.strftime("%I:%M %p")
draw.text((10,45), curTime, font=font, fill=128)

draw.text((10,60), ' '.join(tom_weather_data), font=font, fill=128)

# write to stdout
im.show()

im.save('draw.png')
