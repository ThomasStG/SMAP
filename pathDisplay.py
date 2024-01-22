import numpy as np

nodes = np.load('coordinates.npy')
nodes = nodes.astype(float)

first_node = nodes[0]
node_coordinates = []

for node in nodes:
    relative_position = node - first_node
    
    node_coordinates.append((relative_position[0],relative_position[1]))

for node in node_coordinates:
    
