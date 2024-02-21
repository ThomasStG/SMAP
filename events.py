from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen


def getEvents(url="https://25livepub.collegenet.com/events-calendar/nh/manchester/snhu/training/meeting/meetings/tabling/southern-new-hampshire-university/snhu-all-campus-events-calendar"):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        calendar = []
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            events = soup.find_all("div", class_="vevent")
            for event in events:
                event_title = event.find("h2").get_text()
                event_location = event.find(
                    "abbr", class_="dtstart").get_text()
                event_time = event.find("span", class_="location").get_text()
                event_description = event.find(
                    "span", class_="description").get_text()
                if event_description == "":
                    event_description = "No Description"
                calendar.append((event_title, event_location,
                                event_time, event_description))
            return calendar
        else:
            print('Invalid website URL')
        response.close()
    except:
        print('Invalid website URL')
        return []


print(getEvents())
