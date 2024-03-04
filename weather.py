import os
from dotenv import load_dotenv
import requests

def GetWeather():
    # Load environment variables
    load_dotenv(override=True)
    
    # Retrieve WeatherAPI key from environment variables
    key = os.getenv("WEATHER_KEY")
    # Check if the API key is available
    if not key:
        print("Weather API key not found.")
        #return None
    # Define the location for which you want to get weather data (example coordinates)
    latitude = 43.038605
    longitude = -71.452469
    
    # Define the base URL for the WeatherAPI
    base_url = "http://api.weatherapi.com/v1"
    
    # Specify the endpoint for the current weather
    endpoint = "/current.json"
    
    # Construct the complete URL
    url = f"{base_url}{endpoint}?key={key}&q=43.038611,-71.452472"
    
    try:
        # Send GET request to the WeatherAPI
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            weather_data = response.json()
            return weather_data
        else:
            print(f"Failed to fetch weather data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def GetForecast():
    endpoint = "/forecast.json"
    # Load environment variables
    load_dotenv(override=True)
    
    # Retrieve WeatherAPI key from environment variables
    key = os.getenv("WEATHER_KEY")
    
    # Check if the API key is available
    if not key:
        print("Weather API key not found.")
        return None
    
    # Define the location for which you want to get weather data (example coordinates)
    latitude = 43.038605
    longitude = -71.452469
    
    # Define the base URL for the WeatherAPI
    base_url = "http://api.weatherapi.com/v1"
    
    # Specify the endpoint for the current weather
    days = 2
    # Construct the complete URL
    url = f"{base_url}{endpoint}?key={key}&q={latitude},{longitude}&days={days}"
    try:
        # Send GET request to the WeatherAPI
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            weather_data = response.json()
            return weather_data
        else:
            print(f"Failed to fetch weather data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None