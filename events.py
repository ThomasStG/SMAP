from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://25livepub.collegenet.com/events-calendar/nh/manchester/snhu/training/meeting/meetings/tabling/southern-new-hampshire-university/snhu-all-campus-events-calendar"
    

def getEvents(void):
    calendar=[]
    html = urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    events = soup.find_all("div", class_="vevent")
    for event in events:
        event_title = event.find("h2").get_text()
        event_location = event.find("abbr", class_="dtstart").get_text()
        event_time = event.find("span", class_="location").get_text()
        event_description = event.find("span", class_="description").get_text()
        if event_description == "":
            event_description = "No Description"
        calendar.append((event_title,event_location,event_time,event_description))
    
    return calendar