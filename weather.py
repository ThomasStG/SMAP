import os
from dotenv import load_dotenv
import requests

def GetWeather():
    load_dotenv(override=True)
    
    # Retrieve WeatherAPI key from environment variables
    key = os.getenv("WEATHER_KEY")
    # Check if the API key is available
    if not key:
        print("Weather API key not found.")
        return None