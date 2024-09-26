import requests
import json
import pyttsx3

command = pyttsx3.init()
city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=f9689016896f4b5fb6f91443242004&q={city}"

r = requests.get(url)
print(r.text)

wDic = json.loads(r.text)
w = wDic["current"]["temp_c"]
lU = wDic["current"]["last_updated"]

print(wDic["current"]["temp_c"],"degrees")
print("last updated:",wDic["current"]["last_updated"])
command.say(f"The current weather in {city} is {w} degreees")

command.runAndWait()


