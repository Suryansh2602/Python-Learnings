import requests
latitude = 22.7008
longitude = -75.8774

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
response = requests.get(url)
data = response.json()


# print(data)
data.keys()

data['current_weather']