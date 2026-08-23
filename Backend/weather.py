import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """
    Fetch current weather for a given city using the OpenWeather API.
    Returns temperature, humidity, weather description, and wind speed.
    """
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"  # Get temperature in Celsius
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Check if the API returned an error (e.g., city not found)
        if response.status_code != 200:
            return {"error": data.get("message", "Failed to fetch weather data")}

        weather_info = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }

        return weather_info

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}