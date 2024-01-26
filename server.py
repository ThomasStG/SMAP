from flask import Flask, render_template, request
from waitress import serve
import sqlite3
from events import getEvents
from pathing import findClosest, get_user_location, Graph
import numpy as np
import geojson
import socket

app = Flask(__name__)

campus_map = Graph(170)
nodes = np.load('coordinates.npy')
nodes = nodes.astype(float)


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
    return render_template('index.html')

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
    
@app.route("/paths")
def paths():
    return render_template("pathing.html")

@app.route('/paths/find', methods=['POST'])
def handle_data():
    from_str = request.form.get('fromDropdown')
    to_str = request.form.get('toDropdown')
    if from_str == "None" or to_str == "None" or not from_str or not to_str:
        return render_template("pathing.html")
    from_loc = int(from_str)
    to_loc = int(to_str)
    if from_loc == -1:
        from_loc = findClosest(get_user_location(), nodes)
    path = campus_map.dijkstra(from_loc, to_loc)
    with open('drawRoutes.js', 'a') as js_file:
        js_file.write('const optimalRoute = {};'.format(path))
        js_file.write('const nodes = {};'.format(nodes))
    
    return render_template("path.html", path=path)

def FindPath(start, finish):
    return render_template("", path=campus_map.dijkstra(start, finish))

if __name__ == "__main__":
    print(get_user_location())
    serve(app, host="0.0.0.0", port=3000)