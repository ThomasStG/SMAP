"""Copied from https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/"""
"""It has been edited to return the path of nodes between a start and end node"""




import sys
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import requests
import numpy as np
import math as m
import geocoder
import time
import os
def findClosest(loc, nodes):
    distances = np.sqrt(np.sum(np.power(nodes - loc, 2), axis=1))
    closest_node_index = np.argmin(distances)
    return closest_node_index


def get_user_location():
    g = geocoder.ip('me')
    # print(g.latlng)
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        # print(data)
        lat, lon = map(float, data['loc'].split(','))
        return lat, lon
    except:
        print("Error: Unable to detect your location.")
        return None, None


class Graph():

    def __init__(self, vertices, graph=[]):
        self.V = vertices
        self.graph = [[0 for column in range(
            vertices + 1)] for row in range(vertices)]
        if graph == []:
            current_file_path = os.path.abspath(__file__)
            current_directory = os.path.dirname(current_file_path)
            map_file_path = os.path.join(current_directory, '..', 'static', 'other', 'map.npy')
            print (os.path.exists(map_file_path))
            self.graph = np.load(map_file_path)

    def minDistance(self, dist, sptSet):
        """
        The function `minDistance` returns the index of the minimum distance vertex from a given set of
        distances and a set of vertices.

        :param dist: The `dist` parameter in the `minDistance` function represents an array that
        stores the shortest distance from a source node to all other nodes in a graph. Each element in
        the `dist` array corresponds to a node in the graph, and the value at that index represents the
        distance from the
        :param sptSet: The `sptSet` parameter is typically used in Dijkstra's algorithm to keep track of
        vertices that have been visited and for which the shortest path has been found. It is a boolean
        array where each element corresponds to a vertex in the graph. If `sptSet[u]` is `
        :return: the index of the vertex with the minimum distance value in the 'dist' array, among the
        vertices that are not yet included in the shortest path tree (sptSet).
        """
        min = sys.maxsize
        min_index = -1

        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    def dijkstra(self, src, final):
        dist = [sys.maxsize] * self.V  # set distance to infinity
        parent = [-1] * self.V  # -1 times the number of nodes
        dist[src] = 0  # distance from source node = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            # calculates minimum distance between
            x = self.minDistance(dist, sptSet)
            # sptSet is a bool array where the shortest path is.
            sptSet[x] = True

            for y in range(self.V):
                if self.graph[x, y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x, y]:  # visit a node not yet visited
                    dist[y] = dist[x] + self.graph[x, y]
                    parent[y] = x

        # self.printSolution(dist, parent)
        path = self.getPath(src, final, parent)
        time = 0
        for i in range(len(path) - 1):
            time += self.graph[path[i], path[i + 1]]
        return (path)

    def getPath(self, src, final, parent):
        path = []
        current = final
        while current != -1:
            path.insert(0, current)
            current = parent[current]
        return path


# Driver's code
if __name__ == "__main__":
    g = Graph(171)
    print(g.dijkstra(46, 169))
    print(get_user_location())
