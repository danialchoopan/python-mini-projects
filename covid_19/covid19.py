import requests

print('wlecome to covid 19 status')

country_name=input("enter country name : ")

//api url
api_url="https://api.covid19api.com/live/country/{country_name}/status/confirmed".format(country_name=country_name)

//send request to the api
json_from_web=requests.get(api_url,allow_redirects=True).json()

print("confirmed cases : "+str(json_from_web[0]["Confirmed"]))
