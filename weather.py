import requests
class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_weather_data()

    def get_weather_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=2f9a1fe29aa8d849fa58dea919e7a612")
        except:
            print("Error: Failed to retrieve data.")
        
        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"] 
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def print_weather_data(self):
        unit_symbol = "C"
        if self.units == "imperial":
            unit_symbol = "F"
        print(f"In {self.name} the current temperature is {self.temp}°{unit_symbol}")
        print(f"Today's High {self.temp_min}°{unit_symbol}")
        print(f"Today's Low {self.temp_max}°{unit_symbol}")

city1 = City("Chennai", 13.0843, 80.2705)
city1.print_weather_data()

city2 = City("Philadelphia",39.9526, -75.1652, units="imperial")
city2.print_weather_data()
print(city2.response_json)

