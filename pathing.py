
"""Copied from https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/"""
"""It has been edited to return the path of nodes between a start and end node"""
# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
 
# Library for INT_MAX
import sys
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import requests
import numpy as np
import math as m
import geocoder

import time

def findClosest(loc, nodes):
    distances = np.sqrt(np.sum(np.power(nodes - loc, 2), axis=1))
    closest_node_index = np.argmin(distances)
    return closest_node_index

def get_user_location():
    g = geocoder.ip('me')
    print(g.latlng)
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        print(data)
        lat, lon = map(float, data['loc'].split(','))
        return lat, lon
    except:
        print("Error: Unable to detect your location.")
        return None, None

class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
            for row in range(vertices)]
        self.graph = np.load('map.npy')

 
    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        min_index = -1
 
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
 
        return min_index
 
    def dijkstra(self, src, final):
        dist = [sys.maxsize] * self.V
        parent = [-1] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for _ in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
 
            for y in range(self.V):
                if self.graph[x, y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x, y]:
                    dist[y] = dist[x] + self.graph[x, y]
                    parent[y] = x
 
        #self.printSolution(dist, parent)
        path = self.getPath(src, final, parent)
        time = 0
        for i in range(len(path)-1):
            time += self.graph[path[i], path[i+1]]
        return (path, time)
 
    def getPath(self, src, final, parent):
        path = []
        current = final
        while current != -1:
            path.insert(0, current)
            current = parent[current]
        return path
 
# Driver's code
if __name__ == "__main__":
    """g = Graph(170)
    loc = (-71.450127, 43.038479)
    #loc = get_user_location()
    #loc.reverse()
    #loc = [eval(i) for i in loc]
    #loc = tuple(loc)
    #print(loc)
    nodes = np.load('coordinates.npy')
    closest = findClosest(loc, nodes)
    print(closest[0], "is the distance from loc to node ", closest[1])
    print(g.dijkstra(closest[1], 169))"""
    print(get_user_location())
# display path pieces https://chat.openai.com/share/2150ff02-b9d8-44e6-bde8-209e7dc7ad98