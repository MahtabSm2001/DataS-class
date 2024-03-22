#tamrine api
import requests
start = input("Tehran's weather from? : ")
end = input("weather of Tehran until? : ")
lat = 35
lon = 51
url = f'https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&start={start}&end={end}&appid=7796677dbfe6e352caf8755df8492b14'
response = requests.get(url)
print(response.text)