#Dependencies
import json
import requests as req
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from citipy import citipy
import random

#Set up lists to collect data
cities = []
temps = []
humid = []
wind = []
clouds = []
frames = []

#Randomly generate lat/lng and collect nearest city
for i in range(5):
    lat = numpy.random.uniform(low=-90.00000, high=90.000000, size = 60)
    lng = numpy.random.uniform(low=-120.00000, high=120.000000, size = 60)
    for j in range(60):
        query = citipy.nearest_city(lat[j], lng[j])
        #API request
        url = "api.openweathermap.org/data/2.5/weather?q=" + query + "&APPID=d77529b69cd743d50d241b93b6553ec5"
        response = req.get(url)
        print("Retrieving weather data for " + query)
        print(url)
        response_json = response.json()
        #Collect data from JSON 
        temperature.append(response_json["main"]["temp"])
        humidity.append(response_json["main"]["humidity"])
        wind.append(response_json["wind"]["speed"])
        clouds.append(response_json["clouds"]["all"])
        cities.append(query)
        df = pd.DataFrame(data = {"Cities": cities, "Latitude": lat[j], "Temperature": temps, "Humidity": humid, "Wind Speed": wind, "Cloud Cover": clouds)
        frames.append(df)

#Combine data and export to csv
latitude_climate = pd.concat(frames)
latitude_climate.to_csv("climate.csv")