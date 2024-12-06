import numpy as np
import time

# Number of vertices in the graph
V = 171

# Define infinity as a large enough value
INF = 99999

def floydWarshall(graph):
    """Calculate shortest paths and predecessors between all pairs of vertices using Floyd-Warshall algorithm."""
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    pred = [[None if i != j and graph[i][j] < INF else None for j in range(V)] for i in range(V)]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = k

    return dist, pred

def reconstructPath(pred, start, end):
    """Reconstruct the path from start to end using the predecessor matrix."""
    path = []
    def recurse(v):
        if pred[start][v] is not None:
            recurse(pred[start][v])
        path.append(v)
    
    recurse(end)
    return path

def formatMatrix(matrix):
    """Format the matrix as a string with rows separated by newlines and values separated by commas."""
    result = []
    for row in matrix:
        result.append(', '.join('INF' if x == INF else str(x) for x in row))
    return '\n'.join(result)

def saveMatrixToFile(matrix, filename):
    """Save the formatted matrix to a file."""
    with open(filename, 'w') as f:
        f.write(formatMatrix(matrix))

def savePathsToNumpyFile(pred, filename):
    """Save the paths from each node to each other node as a numpy array."""
    all_paths = np.empty((V, V), dtype=object)
    
    for start in range(V):
        for end in range(V):
            if start != end:
                path = reconstructPath(pred, start, end)
                all_paths[start][end] = path
            else:
                all_paths[start][end] = []

    np.save(filename, all_paths)

# Driver's code
if __name__ == "__main__":
    now = time.time()
    
    # Load graph from file
    graph = np.load('./static/other/map.npy')
    
    # Compute shortest paths and predecessors
    shortest, predecessors = floydWarshall(graph)
    
    # Save the shortest path matrix to a file
    saveMatrixToFile(shortest, "./testPaths.txt")
    
    # Save the paths to a numpy file
    savePathsToNumpyFile(predecessors, "./testPathsPaths.npy")
    
    # Print a specific distance for testing
    print(predecessors[112][1])
    
    
   
    new = np.load("./testPathsPaths.npy", allow_pickle=True)
    print(new[112,1])
    then = time.time()
    print(then-now)
