import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getFood():
    food = []
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_options.add_argument("--no-sandbox")  # Disable sandbox mode (Linux only)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://amerifit.afvusa.com/MenuMain.aspx?a=MTk5NTI4NDMwMg==")
    
    try:
        # Wait for the menu items to load
        driver.find_element(By.CLASS_NAME, "glyphicon-step-backward").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "menuItem")))
        
        container = driver.find_element(By.CLASS_NAME, "menuItemRow")
        items = driver.find_elements(By.CLASS_NAME, "menuItem")
        
        
        print(len(items))
        for item in items:
            print(item.text, end="\n\n")
            try:
                meal_time = ""
                station_name = ""
                try:
                    station_name_element = item.find_element(By.XPATH, ".//span[@ng-if]")
                    station_name = station_name_element.text if station_name_element.get_attribute("ng-if") == "special.StationName !=''" else ""
                except NoSuchElementException:
                    station_name = ""
                try:
                    meal_time_element = item.find_element(By.XPATH, ".//span[@ng-if]")
                    meal_time = station_name_element.text if station_name_element.get_attribute("ng-if") == "special.MealTime !=''" else ""
                except NoSuchElementException:
                    meal_time = ""
                recipe_name = ""
                try:
                    recipe_name = item.find_element(By.XPATH, ".//span[@class='fbaloo head14 fblue nutritionalLink ng-binding ng-scope' and @ng-if=\"special.RecipeID!='0'\"]").text
                except Exception:
                    recipe_name=""
                #recipe_name = item.find_element(By.CSS_SELECTOR, ".fbaloo.head14.fblue.nutritionalLink").text
                description = item.find_element(By.CSS_SELECTOR, ".poppins.text10.fgray.ng-binding").text if item.find_element(By.CSS_SELECTOR, ".poppins.text10.fgray.ng-binding") else ""
                icons = [icon.get_attribute("title") for icon in item.find_elements(By.CLASS_NAME, "aller_icon")]
                img_src = ""
                try:
                    img_src = item.find_element(By.CSS_SELECTOR, "img.ng-scope").get_attribute("src")
                    img_src = img_src[35:]
                    img_src = img_src[:-4]
                except Exception:
                    img_src = ""

                food.append({
                    "StationName": station_name,
                    "MealTime": meal_time[2:],
                    "RecipeName": recipe_name,
                    "Description": description,
                    "Icons": icons,
                    "Color": img_src
                })
            except StaleElementReferenceException:
                meal_time = ""
                station_name = ""
                recipe_name = ""
                img_src = ""
                
                try:
                    station_name_element = item.find_element(By.XPATH, ".//span[@ng-if]")
                    station_name = station_name_element.text if station_name_element.get_attribute("ng-if") == "special.StationName !=''" else ""
                except NoSuchElementException:
                    station_name = "No Station Name"
                
                try:
                    meal_time_element = item.find_element(By.XPATH, ".//span[@ng-if]")
                    meal_time = station_name_element.text if station_name_element.get_attribute("ng-if") == "special.MealTime !=''" else ""
                except NoSuchElementException:
                    meal_time = "No Meal Time"
                
                try:
                    recipe_name = item.find_element(By.XPATH, ".//span[@class='fbaloo head14 fblue nutritionalLink ng-binding ng-scope' and @ng-if=\"special.RecipeID!='0'\"]").text
                except Exception:
                    recipe_name=""
                
                description = item.find_element(By.CSS_SELECTOR, ".poppins.text10.fgray.ng-binding").text if item.find_element(By.CSS_SELECTOR, ".poppins.text10.fgray.ng-binding") else "No Description"
                
                icons = [icon.get_attribute("title") for icon in item.find_elements(By.CLASS_NAME, "aller_icon")]
                
                try:
                    img_src = item.find_element(By.CSS_SELECTOR, "img.ng-scope").get_attribute("src")
                    img_src = img_src[35:]
                    img_src = img_src[:-4]
                except Exception:
                    img_src = "No Rating"

                food.append({
                    "StationName": station_name,
                    "MealTime": meal_time[2:],
                    "RecipeName": recipe_name,
                    "Description": description,
                    "Icons": icons,
                    "Color": img_src
                })
                
            except Exception as e:
                print(f"Error processing item: {e}")
                
    except Exception as e:
        print(f"Error loading menu items: {e}")
    finally:
        driver.quit()
    return json.dumps(food)
