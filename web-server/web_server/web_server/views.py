from django.http import JsonResponse
import socket
import requests
import geocoder
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")

def hello(request):
    ip = geocoder.ip("me").json
    data = requests.get(f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={ip}').json()
    visitor_name = request.GET.get("visitor_name")
    temperature = data["current"]["temp_c"]
    location = data["location"]["name"]

    response = {
        "client_ip": ip["ip"],
        "location": location,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celcius in {location}",
    }

    return JsonResponse(response)
