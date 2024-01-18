
"""Copied from https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/"""
"""It has been edited to return the path of nodes between a start and end node"""
# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
 
# Library for INT_MAX
import sys

class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
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
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
                    parent[y] = x
 
        #self.printSolution(dist, parent)
        path = self.getPath(src, final, parent)
        time = 0
        for i in range(len(path)-1):
            time += self.graph[path[i]][path[i+1]]
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
    g = Graph(9)
    #adjacency graph (node 0 is weight 4 away from node 1 and weight 8 away from node 7. It is not connected to any other nodes)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]
 
    print(g.dijkstra(0, 5))