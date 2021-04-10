import requests
import json
city_name=input("enter city name : ")
api_key=""
api_url="https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+api_key
json_from_web=requests.get(api_url).json()
print("weather:")
print(json_from_web["weather"][0]["main"])
print(json_from_web["weather"][0]["description"])
temp_c=float(json_from_web["main"]["temp"])-273.15
print(temp_c)
print("___________________________")
