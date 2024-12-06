import numpy as np
import time
from pathDisplay import get_path
from pathing import Graph 

# Define infinity as a large enough value
INF = 99999
N = 171

nodes_of_interest = [130, 97, 56, 61, 23, 15, 7, 6, 29, 2, 0, 14, 58, 59, 68, 106, 83,82,107,143,124,146,139,158,157,151,113,167,10,23,24,20,63,17,26,38,64,55,54,65,45,111,127,117,78,73,83,116,144,80,65,46,35,168,32,68,86,101,175,158,137,147,153,150,160,163,167,165,113]

"""
Path pieces to add:
['160-161', '66-73', '85-98', '41-52', '48-62', '62-69', '13-19', '161-163', '26-41'] (72, 73?)
"""
campus_map = Graph(171)

P = np.load("./paths.npy", allow_pickle=True)
D = np.load("./distance.npy", allow_pickle=True)
# things to add (back and side doors kingston)

def gen_paths():
    graph = np.load("./static/other/map.npy")

    pred = [[None if i != j and graph[i][j] < INF else None for j in range(N)] for i in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i,j] is not INF and graph[i,k] is not INF and graph[k,j] is not INF and graph[i,k] + graph[k,j] < graph[i,j] and i != j:
                    graph[i,j] = graph[i,k] + graph[k,j]
                    pred[i][j] = k

    
    np.save("paths.npy", np.array(pred, dtype=object))
    np.save("distance.npy", graph)


def check_path(path, start = 0):
    for i in range(start, len(path) - 1):
        if P[path[i], path[i+1]] != None: 
            path.insert(i+1, P[path[i], path[i+1]])
            check_path(path, i)
    return path

def find_path(node1, node2, path):
    if P[node1,node2] is not None:
        path.insert(1,P[node1,node2])
        find_path(node1, P[node1,node2], path)
    
    return check_path(path)
    #return path

for i in range(len(nodes_of_interest)):
    for j in range(i, len(nodes_of_interest)):
        get_path(find_path(nodes_of_interest[i],nodes_of_interest[j], [nodes_of_interest[i], nodes_of_interest[j]]))
#print(P[98,169])
n1 = 1
n2 = 112
#for i in range(12):
    #if n2 is not None and n1 is not None:
#print(P[98])
#print(P[P[n1,n2]], P[P[n1,n2]])
#print(P[P[n1,n2],P[P[n1,n2], n2]])
print(find_path(1,112, [1,112]))
        
"""
for i in range(171):
    for j in range(171):
        if i != j:
            get_path(find_path(i,j, [i,j]))"""

#gen_paths()
"""
l = []
iterations = 0
while True:
    iterations += 1
    if P[n2,n1]!= None and iterations < 30: # they are connected
        l.append(n2)
        n3 = P[n2,n1]
    elif iterations >= 30:
        break
    else:
        print(l)
n3 = P[n2,n1] #169
P[n2,n3]
P[n3,n1]"""

"""[None None 0 None 2 3 4 4 5 6
 6 7 7 7 8 9 11 20 12 29
 13 32 14 15 16 20 40 18 18 8
 33 33 8 32 32 22 22 24 25 41 
 33 40 27 27 28 28 57 36 37 42 
 41 40 51 43 43 43 45 34 57 47 
 47 62 48 49 49 51 52 50 60 169 
 67 65 71 66 66 169 68 70 70 58 
 72 72 81 74 169 169 76 76 76 78 
 77 78 78 79 79 169 169 169 169 87 
 88 88 169 90 128 91 93 94 94 169 
 169 169 169 169 99 100 121 92 128 128 
 105 105 106 107 108 108 108 169 103 132 
 169 120 121 122 123 124 125 125 126 126 
 126 132 131 131 132 140 136 146 142 139 
 140 141 142 145 148 154 149 151 154 156 
 156 160 160 161 163 162 163 164 34 56 136]"""
 
def gen_paths2():
    graph = np.array([
        [INF, 2, 4], 
        [2, INF, 3],
        [123, 2, INF]
    ])
    N = 3

    pred = [[None if i != j and graph[i][j] < INF else None for j in range(N)] for i in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i,j] and graph[i,k] + graph[k,j] < graph[i,j] and i != j:
                    graph[i,j] = graph[i,k] + graph[k,j]
                    pred[i][j] = k
                    print(graph)
                    print(pred)
#gen_paths()


