from flask import Flask, render_template, request
from waitress import serve
import sqlite3
from events import getEvents
from pathing import findClosest, get_user_location, Graph
from pathDisplay import get_path
from api.CustomEvent.CreateEvent import CreateEvent
from api.CustomEvent.GetEvent import GetEvents
from api.Messages.SendMessage import Send, Delete, Get
import numpy as np
from datetime import datetime

app = Flask(__name__)

campus_map = Graph(171)
nodes = np.load('coordinates.npy')
nodes = nodes.astype(float)


buildings = {
        80: "Academic Center",
        24: "Athletic Center",
        54: "Belknap",
        150: "Conway Hall",
        78: "Dining Hall",
        111: "Gustafson Welcome Center",
        136: "Hampton Hall",
        65: "Hospitality Center",
        20: "Kingston Hall",
        117: "Learning Commons",
        153: "Lincoln Hall",
        115: "Madison House",
        167: "Mark A. Ouellette Stadium",
        127: "Morrissey House",
        116: "Monadnock Hall",
        10: "New Castle Hall",
        113: "Operations Center",
        63: "Robert A. Freese Student Center",
        64: "Robert Frost Hall",
        168: "SETA",
        165: "SETA Annex",
        158: "Tuckerman Hall",
        32: "Washington Hall",
        86: "Webster Hall",
        38: "William S. and Joan Green Center for Student Success",
        136: "Windsor Hall",
        17: "Exeter Hall"}

@app.route('/')
@app.route('/index')
def index():
    calendar = getEvents()
    format_str = "%A, %B %d, %Y, %I:%M %p"
    cal1 = []
    current_date = datetime.now()
    # Parse the datetime string using the defined format
    for event in calendar:
        datetime_str = event[1].replace('\xa0', ' ')
        parsed_datetime = datetime.strptime(datetime_str, format_str)

        # Extract individual components
        day_of_week = parsed_datetime.strftime("%A")
        month = parsed_datetime.strftime("%B")
        day_of_month = parsed_datetime.day
        year = parsed_datetime.year
        time = parsed_datetime.strftime("%I:%M %p")
        event = (event[0],event[1], (day_of_week, month, day_of_month, year, time), event[3])
        if day_of_month == current_date.day and month.lower() == current_date.strftime("%B").lower():
            cal1.append(event)
        
    return render_template('index.html', calendar=cal1)

@app.route('/events')
def events():
    eventCount = [0] * len(buildings)
    calendar = getEvents()

    for event in calendar:
        if len(event) > 2:
            description = event[2]

            if "Aerobic/Exercise Room" in description:
                eventCount[1] += 1
            elif "BELKNAP" in description:
                eventCount[2] += 1
            elif "Dining Center" in description:
                eventCount[3] += 1
            elif "Gustafson Welcome Center" in description:
                eventCount[4] += 1
            elif "Hospitality Center" in description:
                eventCount[7] += 1
            elif "Library" in description or "Learning Commons" in description:
                eventCount[9] += 1
            elif "Student Center" in description:
                eventCount[18] += 1
            elif "Robert Frost" in description:
                eventCount[19] += 1
            elif "Innovation & Design Education" in description:
                eventCount[20] += 1
            elif "Green Center" in description:
                eventCount[24] += 1
            elif "OL" in description:
                eventCount[16] += 1
            else:
                eventCount[17] += 1
        else:
            print("Invalid event format:", event)

    return render_template("events.html", title="SNHU", calendar=calendar, eventCount=eventCount)
    
@app.route("/path")
def paths():
    return render_template("pathing.html")

@app.route("/calendar")
def calendar():
    calendar = getEvents()
    format_str = "%A, %B %d, %Y, %I:%M %p"
    cal1 = []

    # Parse the datetime string using the defined format
    for event in calendar:
        datetime_str = event[1].replace('\xa0', ' ')
        parsed_datetime = datetime.strptime(datetime_str, format_str)

        # Extract individual components
        day_of_week = parsed_datetime.strftime("%A")
        month = parsed_datetime.strftime("%B")
        day_of_month = parsed_datetime.day
        year = parsed_datetime.year
        time = parsed_datetime.strftime("%I:%M %p")
        event = (event[0],event[1], (day_of_week, month, day_of_month, year, time), event[3])
        cal1.append(event)
    
    return render_template("calendar.html", calendar=cal1)

@app.route('/paths/find', methods=["GET", "POST"])
def handle_data():
    from_str = request.form.get('fromBuildingDropdown')
    to_str = request.form.get('toBuildingDropdown')
    if from_str == "None" or to_str == "None" or not from_str or not to_str:
        return render_template("pathing.html")
    from_loc = int(from_str)
    to_loc = int(to_str)
    if from_loc == -1:
        from_loc = findClosest(get_user_location(), nodes)
    path = campus_map.dijkstra(from_loc, to_loc)
    images = get_path(path)
    
    return render_template("path.html", path=path, path_images=images)
"""
@app.route('/createEvent', methods=["GET", "POST"])
def create():
    if request.method != "POST":
        return render_template("customevent.html", success=None)
    timeformat = "%H:%M:%S"
    title = request.form['title']
    description = request.form['description']
    location = eval(request.form['location'])
    location_str = buildings.get(location, None)
    date = request.form['date']
    time = request.form['time']
    time += ":00"
    if title == "" or description == "" or location_str == "" or time == "" or date == "":
        return render_template("customevent.html", success=False)
    success = CreateEvent(title, description, date, time, location_str)
    return render_template("customevent.html", success=success)
    
@app.route('/viewEvents')
def read():
    events = GetEvents()
    cal = []
    for event in events:
        Y,M,D = event[3].split('-')
        H, Min, S = event[4].split(':')
        Min = Min.lstrip('0')
        if Min == '':
            Min = 0
        else:
            Min = int(Min)
        d=datetime(int(Y),int(M.lstrip('0')),int(D.lstrip('0')), int(H.lstrip('0')), Min, 0)
        #return render_template("index.html")
        mon = d.strftime("%B")
        day_of_month = d.day
        year = d.year
        time = d.strftime("%I:%M %p")
        cal.append((event[1], event[2], (d.strftime('%A'), mon, day_of_month, year, time), event[5]))
    return render_template("viewevents.html", events=cal)
"""
@app.route('/chat')
def show():
    messages = Get()
    mes = []
    for message in messages:
        data = datetime.fromisoformat(message[1])
        delta = datetime.now() - data
        if  delta.days <= 100:
            year = data.year
            month = data.month
            day = data.day
            time = f"{data.hour}:{data.minute}:{data.second}:{data.microsecond}"
            mes.append((message[0], message[2], (year, month, day, time)))
    
    return render_template("messages.html", messages=mes)

@app.route('/sendMessage', methods=["POST", "GET"])
def send():
    if request.method != "POST":
        return show()
    content = request.form['messageContent']
    Send(content)
    return show()
    
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=3000)
    