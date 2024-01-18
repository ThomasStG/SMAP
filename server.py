from flask import Flask, render_template, request
from waitress import serve
import sqlite3
from events import getEvents

app = Flask(__name__)

buildings = {
    'Academic Center': 0,
    'Athletic Center': 1,
    'Belknap': 2,
    'Dining Hall': 3,
    'Gustafson Welcome Center': 4,
    'Green Center': 5,
    'Hampton Hall': 6, ##
    'Hospitality Center': 7,
    'Kingston Hall': 8,
    'Learning Commons': 9,
    'Lincoln Hall': 10, ##
    'Madison House': 11, ##
    'Mark A. Ouellette Stadium': 12, ##
    'Morrissey House': 13,
    'Monadnock Hall': 14, ##
    'New Castle Hall': 15, ##
    'Online': 16,
    'Other': 17,
    'Robert A. Freese Student Center': 18,
    'Robert Frost Hall': 19,
    'SETA': 20,
    'Tuckerman Hall': 21, ##
    'Washington Hall': 22,
    'Webster Hall': 23,
    'William S. and Joan Green Center for Student Success': 24,
    'Windsor Hall': 25, ##
}

@app.route('/')
@app.route('/index')
def index():
    eventCount = [0] * len(buildings)
    calendar = getEvents()
    for event in calendar:
        if "Aerobic/Exercise Room" in event[2]:
            eventCount[1] += 1
        elif "BELKNAP" in event[2]:
            eventCount[2] += 1
        elif "Dining Center" in event[2]:
            eventCount[3] += 1
        elif "Gustafson Welcome Center" in event[2]:
            eventCount[4] += 1
        elif "Hospitality Center" in event[2]:
            eventCount[7] += 1
        elif "Library" in event[2] or "Learning Commons" in event[2]:
            eventCount[9] += 1
        elif "Student Center" in event[2]:
            eventCount[18] += 1
        elif "Robert Frost" in event[2]:
            eventCount[19] += 1
        elif "Innovation & Design Education" in event[2]:
            eventCount[20] += 1
        elif "Green Center" in event[2]:
            eventCount[24] += 1
        elif "OL" in event[2]:
            eventCount[16] += 1
        else:
            eventCount[17] += 1
    return render_template("index.html", title="SNHU", calendar=calendar, eventCount=eventCount)
    

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=3000)