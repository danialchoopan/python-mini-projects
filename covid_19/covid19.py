import requests

print('wlecome to covid 19 status')
country_name=input("enter country name : ")
api_url="http://api.covid19api.com/live/{country_name}/status/confirmed".format(country_name=country_name)
json_from_web=requests.get(api_url,allow_redirects=True).json()
print("weather:")

print("confirmed cases: "+str(json_from_web[0]["Confirmed"]))