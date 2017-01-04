#!/usr/bin/python3

import random
from math import hypot

def min_dist(coords):
    "Finds minimal distance between coordinates"
    count = len(coords)
    if count < 2:
        print("Need 2 or more coordinates")
        return None
    m_dist = hypot(coords[-1][0] - coords[-2][0], coords[-1][1] - coords[-2][1])
    indicies = (count - 2, count - 1)
    for i in range(count - 2):
        for j in range(i + 1, count):
            dist = hypot(coords[i][0] - coords[j][0], coords[i][1] - coords[j][1])
            if dist < m_dist:
                m_dist = dist
                indicies = (i, j)
    return [m_dist, indicies[0], indicies[1]]


coordinates, tmp = [], []
for x in range(5):
    tmp = [random.randint(-5, 5) for i in range(2)]
    coordinates.append(tuple(tmp))
print(coordinates)

m = min_dist(coordinates)
if m:
    print(m)
