from django.http import JsonResponse
import requests
import geocoder
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")

ip = geocoder.ip("me").json

my_ip = ip["ip"]

def getUrlData():
    
    data = requests.get(f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={ip}').json()
    return data

def hello(request):
    data = getUrlData()
    visitor_name = request.GET.get("visitor_name")
    temperature = data["current"]["temp_c"]
    location = data["location"]["name"]

    response = {
        "client_ip": my_ip,
        "location": location,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celcius in {location}",
    }

    return JsonResponse(response)
