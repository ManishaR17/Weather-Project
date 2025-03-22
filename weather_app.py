import streamlit as st
import requests

def get_weather(city):
    api_key = "2f9a1fe29aa8d849fa58dea919e7a612"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Invalid city name or API issue"}

st.title("Today's Weather")

city = st.text_input("Enter city name:")
if st.button("Submit"):
    if city:
        weather_data = get_weather(city)
        st.subheader("Here is the weather data:")
        #st.text(weather_data)
        st.text(f"The current temperature in {city} is {weather_data["main"]["temp"]}°C")
        st.text(f"The minimum temperature is {weather_data["main"]["temp_min"]}°C")
        st.text(f"The minimum temperature is {weather_data["main"]["temp_max"]}°C")
    else:
        st.error("Please enter a city name.")
