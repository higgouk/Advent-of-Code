import numpy as np

with open('day8data') as file:
    data = file.read().splitlines()

pairs = []

for index, line1 in enumerate(data):
    x, y, z = map(int, line1.split(','))
    point_1 = np.array([x, y, z])
    for line2 in data[index + 1:]:
        x2, y2, z2 = map(int, line2.split(','))
        point_2 = np.array([x2, y2, z2])
        if point_2[0] != point_1[0]:
            dist = float(np.sqrt(np.sum((point_1 - point_2) ** 2)))
            tuple = (line1, line2, dist)
            pairs.append(tuple)

sorted_pairs = sorted(pairs, key=lambda t: t[2])
junction_boxes = data

parent = {j: j for j in junction_boxes}

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    parent[rb] = ra
    return True

components = len(junction_boxes)

for p1, p2, d in sorted_pairs:
    if union(p1, p2):
        components -= 1
        if components == 1:
            x1 = int(p1.split(',')[0])
            x2 = int(p2.split(',')[0])
            print(x1 * x2)
            print(x1)
            print(x2)
            break
