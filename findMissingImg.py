from pathDisplay import get_path
from pathing import Graph


def find():
    g = Graph(171)
    p = []
    nodes = [80, 24, 54, 150, 78, 111, 136, 65, 20, 117, 153, 115, 167,
             127, 116, 10, 113, 63, 64, 168, 165, 158, 32, 86, 38, 136, 17]
    for x in range(170):
        for y in range(x+1, 170):
            p.append(g.dijkstra(x, y))

    for path in p:
        get_path(path)


# find()
with open('big.txt', 'r') as file:
    warnings = file.readlines()

unique_warnings = set(warnings)
print(unique_warnings)
"""
{
'Warning: Image not found for path between 163 and 161\n', '
'Warning: Image not found for path between 161 and 160\n', 
'Warning: Image not found for path between 13 and 19\n', 
'Warning: Image not found for path between 91 and 78\n', 
'Warning: Image not found for path between 33 and 31\n', 
'Warning: Image not found for path between 85 and 98\n', 
'Warning: Image not found for path between 52 and 41\n', 
'Warning: Image not found for path between 103 and 118\n', 
'Warning: Image not found for path between 41 and 26\n', 
'Warning: Image not found for path between 62 and 69\n', 
'Warning: Image not found for path between 48 and 62\n', 
'Warning: Image not found for path between 66 and 73\n', 
'Warning: Image not found for path between 56 and 48\n', 
'Warning: Image not found for path between 149 and 155\n', 
'Warning: Image not found for path between 41 and 39\n', 
'Warning: Image not found for path between 75 and 85\n', 
'Warning: Image not found for path between 162 and 165\n', 
'Warning: Image not found for path between 32 and 33\n', 
'Warning: Image not found for path between 66 and 72\n', 
'Warning: Image not found for path between 97 and 85\n', 
'Warning: Image not found for path between 130 and 112\n',
'Warning: Image not found for path between 21 and 33\n', 
'Warning: Image not found for path between 22 and 35\n',
'Warning: Image not found for path between 102 and 90\n'}

fix 11-52
fix 105-120
fix 124 and up for extra dot
121-132,
120-131, 
116-121, 
116-120, 
112-129, 
108-126, 
108-125, 
108-124, 
105-121, 
105-120,
99-100, 
68-76
Add ".3 mi to SETA Annex"
"""
