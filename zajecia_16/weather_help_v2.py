from geopy.geocoders import Nominatim
import requests

city= input("Podaj swoje miasto: ")
date = input("Podaj datę w formacie YYYY-MM-DD: ")

geolocator = Nominatim(user_agent="michal_zietkowski_app")
location = geolocator.geocode(city)
latitude = location.latitude
longitude = location.longitude


url = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&"
       f"hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={date}&end_date={date}")

print(url)
response = requests.get(url=url)

print(response.json())

data = response.json()

rain_sum = data.get("daily", {}).get("rain_sum", [])[0]

print(rain_sum)

#################################

# https://api.open-meteo.com/v1/forecast?latitude=53.4301818&longitude=14.5509623&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date=16.06.2025&end_date=16.06.2025