import requests

try:
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=13.0843&lon=80.2705&appid=2f9a1fe29aa8d849fa58dea919e7a612")
    print(response.json())

except:
    print("Error: Failed to retrieve data.")
