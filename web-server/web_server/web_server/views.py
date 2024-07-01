from django.http import JsonResponse
import requests
import geocoder
import environ

env = environ.Env()
environ.Env.read_env()


API_KEY = env("API_KEY")

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