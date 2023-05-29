import requests

#The api key that has the weather data
api_key = '30d4741c779ba94c470ca1f63045390a'

#The city that the user is trying to see the forecast for
user_input = input("Enter city: ")

#The url has the weather data for the given city
weather_data = requests.get(
f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

#json prints the data in weather_data in json format
weather = weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])

#when print(weather_data.json()) is printed, it shows all the data
#related to weather for that city, so the "main", the "weather", and 
#the "temp" make sense

print(f"The weather in {user_input} is: {weather}")
print(f"The temperature in {user_input} is: {temp}ºF")
    
   