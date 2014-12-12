import urllib.request
from urllib.error import  URLError
import json

def foreCast():
    city = input("Enter the city name: ")
    try:
        page = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+city)
        data = json.loads(page.read().decode("UTF-8"))
        print(data["weather"])
        print(data["main"])
        print(data["wind"])
    except:
        print("No data available for the entered city")

foreCast()
