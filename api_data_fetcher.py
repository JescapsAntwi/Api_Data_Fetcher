import requests

api_url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q": "New York", "appid": "your_api_key", "units": "metric"}

response = requests.get(api_url, params=params)
data = response.json()

if response.status_code == 200:
    print(f"Temperature in New York: {data['main']['temp']}°C")
else:
    print("Failed to fetch data.")