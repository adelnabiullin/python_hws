#!/usr/bin/python3

import random
import numpy as np

def saddle_points_of(matr):
    "returns dictionary where keys/values = indexes/values of saddle points"
    col_matr = list(zip(*matr))
    s_points = {}
    for index, item in enumerate(matr):
        min_val = min(item)
        min_indexes = [ind for ind, value in enumerate(item) if value == min_val]
        for elem in min_indexes:
            if max(col_matr[elem]) == min_val:
                s_points[(index, elem)] = min_val
    return s_points

matr1 = [[random.randint(1, 100) for x in range(3)] for y in range(3)]
# matr1 = [ [ 1, 2, 3], [ 5, 4, 4 ], [ 7, 2, 0 ] ]

print(np.matrix(matr1))
print("")

sp = saddle_points_of(matr1)
print(sp)
