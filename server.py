import os
import sys
from flask import Flask, render_template, request, jsonify
from waitress import serve
import numpy as np
from datetime import datetime

from events import getEvents
from pathing import Graph
from pathDisplay import get_path
#from api.Messages.SendMessage import Send, Delete, Get
from seleniumFood import getFood

app = Flask(__name__)
# app.debug = True

campus_map = Graph(171)
current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
map_file_path = os.path.join(
    current_directory, '.', 'static', 'other', 'coordinates.npy')
nodes = np.load(map_file_path).astype(float)


buildings = {
    'Academic Center': 0,
    'Athletic Center': 1,
    'Belknap': 2,
    'Dining Hall': 3,
    'Gustafson Welcome Center': 4,
    'Green Center': 5,
    'Hampton Hall': 6,
    'Hospitality Center': 7,
    'Kingston Hall': 8,
    'Learning Commons': 9,
    'Lincoln Hall': 10,
    'Madison House': 11,
    'Mark A. Ouellette Stadium': 12,
    'Morrissey House': 13,
    'Monadnock Hall': 14,
    'New Castle Hall': 15,
    'Online': 16,
    'Other': 17,
    'Robert A. Freese Student Center': 18,
    'Robert Frost Hall': 19,
    'SETA': 20,
    'Tuckerman Hall': 21,
    'Washington Hall': 22,
    'Webster Hall': 23,
    'William S. and Joan Green Center for Student Success': 24,
    'Windsor Hall': 25,
}
"""
    This Python function retrieves events from a calendar, parses their datetime strings, extracts
    individual components, and filters events based on the current date and month before rendering them
    in a template.
    :return: The `index` function is returning a rendered template called 'index.html' with a filtered
    list of events for the current day and month. The filtered list is stored in the variable `cal1` and
    passed to the template as `calendar`.
    """


def flaskStart():
    app.run(host="0.0.0.0", port=3000, debug=True)


def waitressStart():
    print("http://localhost:3000")
    serve(app, host="0.0.0.0", port=3000)


def startApp():
    # flaskStart()
    waitressStart()


@app.route('/')
@app.route('/index')
def index():
    # print(weather, forecast)
    food = getFood()
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
        event = (event[0], event[1], (day_of_week, month,
                 day_of_month, year, time), event[3])
        if day_of_month == current_date.day and month.lower() == current_date.strftime("%B").lower():
            cal1.append(event)

    return render_template('index.html', calendar=cal1, food=food)


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

    return render_template("events.html",
                           title="SNHU",
                           calendar=calendar,
                           eventCount=eventCount)


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
        parsed_datetime = datetime.strptime(event[1], format_str)

        # Extract individual components
        day_of_week = parsed_datetime.strftime("%A")
        month = parsed_datetime.strftime("%B")
        day_of_month = parsed_datetime.day
        year = parsed_datetime.year
        time = parsed_datetime.strftime("%I:%M %p")
        event = (event[0], event[2], (day_of_week, month,
                 day_of_month, year, time), event[3])
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
    #if from_loc == -1:
    #    from_loc = findClosest(get_user_location(), nodes)
    path = campus_map.dijkstra(from_loc, to_loc)
    images = get_path(path)

    return render_template("path.html", path=path, path_images=images)


@app.route('/get_food_data')
def get_food_data():
    today = datetime.today().date()
    file_path = f"{today}-food.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read()
    else:
        try:
            f = getFood()
        except Exception as e:
            return f"Error getting food data: {e}"

        # Delete old food files
        files = os.listdir(".")
        for file in files:
            if file.endswith("-food.json"):
                os.remove(os.path.join(".", file))

        # Write new food data to file
        with open(file_path, "w") as file:
            file.write(f)
        return f

"""
@app.route('/chat')
def show():
    messages = Get()
    mes = []
    for message in messages:
        data = datetime.fromisoformat(message[1])
        delta = datetime.now() - data
        if delta.days <= 100:
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
    honeypot = request.form['bot_test']
    if honeypot == "":
        Send(content)
    return show()
"""


if __name__ == "__main__":
    startApp()
