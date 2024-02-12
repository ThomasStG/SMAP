import requests
from bs4 import BeautifulSoup
import re

def getEvents(url = "https://25livepub.collegenet.com/events-calendar/nh/manchester/snhu/training/meeting/meetings/tabling/southern-new-hampshire-university/snhu-all-campus-events-calendar"):

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        calendar = []
        
        soup = BeautifulSoup(response.content, 'html.parser')
        events = soup.find_all("div", class_="vevent")
        
        for event in events:
            event_title = event.find("h2").get_text()
            event_location = event.find("abbr", class_="dtstart").get_text()
            event_time = event.find("span", class_="location").get_text()
            event_description = event.find("span", class_="description").get_text()
            
            if event_description == "":
                event_description = "No Description"

            # find urls in the description
            url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

            # Replace all matched URLs with HTML anchor tags
            def replace_url(match):
                url = match.group(0)
                loc_match = re.match(r'https?://(?:www\.)?([^\/]+)', url)
                loc = loc_match.group(1) if loc_match else url
                return f'<a style="color:gold" href="{url}">{loc}</a>'

            # Perform the substitution
            event_description_with_links = url_pattern.sub(replace_url, event_description)

            # Append the modified event_description to the calendar
            calendar.append((event_title, event_time, event_location, event_description_with_links))

        return calendar
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    finally:
        if 'response' in locals():
            response.close()


