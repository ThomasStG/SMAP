import requests
from bs4 import BeautifulSoup
import re
#to run site, py server.py

green = [("Calories", 600), ("Sodium", 600), ("Saturated Fat", 4), ("Cholesterol", 95)] # less than these values
yellow = [("Calories", 800), ("Sodium", 800), ("Saturated Fat", 7), ("Cholesterol", 150)] # less than these values
red = [("Calories", 800), ("Sodium", 800), ("Saturated Fat", 7), ("Cholesterol", 150)] # greater than these values



def getFood(url = "https://amerifit.afvusa.com/MenuMain.aspx?a=MTk5NTI4NDMwMg=="):

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    try: 

        response = requests.get(url, headers=headers)
        response.raise_for_status() # this calls a funciton to give an error for bad responses

        food = [] 

        soupvar = BeautifulSoup(response.content, 'html.parser')
        allfood = soupvar.find_all("div", class_="col-md-6 menuItem ng-scope")
        # above code gets all the different menu options 
        for event in allfood:
            food_title = event.find("fbaloo head14 fblue nutritionalLink ng-binding ng-scope").get_text()
            food_description = event.find("poppins text10 fgray ng-binding").get_text()
            food_quality = event.find("ng-scope").get_text()
            food_facts = event.find("aller_icon") .get_text()
            food_time = event.find("poppins text14 ng-binding ng-scope").get_text()

        
            #date = event.find("fbaloo currentMenuDate ng-binding")
            #overall_title = event.find("fbaloo head24 fblack")

            if food_description == "":
                food_description = "No Description"

            if food_facts == "":
                food_facts = "Normal"
        

            url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

            def replace_url(match):
                url = match.group(0)
                loc_match = re.match(r'https?://(?:www\.)?([^\/]+)', url)
                loc = loc_match.group(1) if loc_match else url
                return f'<a style="color:gold" href="{url}">{loc}</a>'
        
            event_description_with_links = url_pattern.sub(replace_url, food_description)


            food.append((food_time, food_title, food_description, food_quality, food_facts))
        return food
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    finally:
         if 'response' in locals():
              response.close()




    