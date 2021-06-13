from django.shortcuts import render, redirect
import requests
from django.conf import settings
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# bierze api key z settings.py > DATABASES
api = getattr(settings, 'DATABASES')

API_KEY = api['default']['API_KEY']


def weather(request):

    city_name = request.POST.get('miasto')

    if city_name:

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

        city_weather = requests.get(url.format(city_name, API_KEY)).json()
        print(city_weather)
        if city_name != None:
            city_name = city_name.capitalize()

        weather = {
            'city': city_name,
            'temperature': int(city_weather['main']['temp'] - 273),
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
            'wind': int(city_weather['wind']['speed'] * 3.6),
            'direction': (city_weather['wind']['deg'] - 225),
            'main': city_weather['weather'][0]['main'],
            'humidity': city_weather['main']['humidity'],

        }

        return render(request, 'blog/weather.html', {'weather': weather})
    else:
        return render(request, 'blog/weather.html')