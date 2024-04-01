from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

def getLocation():
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--headless")  # Run Chrome in headless mode
    driver_path = './chromedriver.exe'  # Edit path of chromedriver accordingly
    driver = webdriver.Chrome( options=options)
    timeout = 20
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)  # Consider using WebDriverWait instead of sleep
    longitude = driver.find_elements(By.XPATH, '//*[@id="longitude"]')  # Replace with any XPath    
    longitude = [x.text for x in longitude]    
    longitude = str(longitude[0])    
    latitude = driver.find_elements(By.XPATH, '//*[@id="latitude"]')    
    latitude = [x.text for x in latitude]    
    latitude = str(latitude[0])    
    driver.quit()    
    return (latitude, longitude)

print(getLocation())
