from django.http import JsonResponse
import requests
import ipinfo
import os
from dotenv import load_dotenv

load_dotenv()

IPINFO_TOKEN = os.getenv("IPINFO_TOKEN")
OPENAPI_TOKEN = os.getenv("OPENAPI_TOKEN")

handler = ipinfo.getHandler(IPINFO_TOKEN)
details = handler.getDetails().details

ip = details["ip"]
lat = details["latitude"]
lon = details["longitude"]

def getUrlData():
    data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENAPI_TOKEN}&units=metric').json()
    return data

def hello(request):
    data = getUrlData()
    # my_ip = request.META["REMOTE_ADDR"]
    visitor_name = request.GET.get("visitor_name")
    temperature = data["main"]["temp"]
    location = data["name"]

    response = {
        "client_ip": ip,
        "location": location,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celcius in {location}",
    }

    return JsonResponse(response)
