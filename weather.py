import os
#from dotenv import load_dotenv
import requests

def GetWeather():
    #load_dotenv(override=True)
    
    # Retrieve WeatherAPI key from environment variables
    key = "1a11a7238e6541f2b9b191338241002"#os.getenv("WEATHER_KEY")
    # Check if the API key is available
    if not key:
        print("Weather API key not found.")
        return None
    
    baseUrl = "http://api.weatherapi.com/v1"
    endpoint = "/current.json"

    url = f"{baseUrl}{endpoint}?key={key}&q=43.040871,-71.457512"
    try:
        # Send GET request to the WeatherAPI
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            weatherdata = response.json()
            return weatherdata
        else:
            print(f"An error has occured {response.status_code}")
            return None
    except Exception as e:
        print(f"an error has occored {e}")
        return None

def GetForecast():

    #load_dotenv(override=True)
    
    # Retrieve WeatherAPI key from environment variables






    key = "1a11a7238e6541f2b9b191338241002"#os.getenv("WEATHER_KEY")









    
    # Check if the API key is available
    if not key:
        print("Weather API key not found.")
        return None
    
    baseUrl = "http://api.weatherapi.com/v1"
    endopoint = "/forecast.json"

#The docs are at https://www.weatherapi.com
    
    url = f"{baseUrl}{endopoint}?key={key}&q=43.040871,-71.457512&days=2"
    try:
        # Send GET request to the WeatherAPI
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            weatherdata = response.json()
            return weatherdata
        else:
            print(f"An error has occured {response.status_code}")
            return None
    except Exception as e:
        print(f"an error has occored {e}")
        return None

print ("weather\n")
print(GetWeather())
print("\n") 
print("forcast\n")
print(GetForecast())
