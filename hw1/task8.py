#!/usr/bin/python3

import numpy as np

def dijkstra(vert_count, current, matr):
    "Finds the shortest path from current to all verticies"
    weights = [max([max(x) for x in matr]) + 1] * vert_count
    weights[current] = 0
    vizited = []
    remained = set()
    while len(vizited) < vert_count:
        neighbors = [i for i, v in enumerate(matr[current]) if i not in vizited and v > 0]
        if neighbors:
            tmp_cur = neighbors[0]
            for i in neighbors:
                tmp_weight = matr[current][i] + weights[current]
                if tmp_weight < weights[i]:
                    weights[i] = tmp_weight
                if weights[i] < weights[tmp_cur]:
                    tmp_cur = i
        elif vert_count > len(vizited) + 1:
            tmp_cur = remained.pop()
        remained.update(neighbors)
        vizited.append(current)
        current = tmp_cur
    return weights

def search_min(matr, vizited):
    "Searches for the closest unvisited vertex"
    _min = max([max(x) for x in matr])
    for ind in vizited:
        for index, elem in enumerate(matr[ind]):
            if elem > 0 and elem < _min and index not in vizited:
                _min = elem # веса путей
                index2 = index # индекс вершины
    return [_min, index2]

def prim(matr):
    "Finds minimum spanning tree"
    vizited = [0]
    result = [0] # начнем с нулевой
    for index in range(1, len(matr)):
        weight, index = search_min(matr, vizited)
        result.append(weight) # в результат будут заноситься веса
        vizited.append(index) # содержит карту пути
    return result

a = [
    [0, 40, 10000, 10000, 18],
    [40, 0, 22, 6, 15],
    [10000, 22, 0, 14, 10000],
    [10000, 6, 14, 0, 20],
    [18, 15, 10000, 20, 0]
    ]
print(np.matrix(a))
print("")
print(dijkstra(5, 1, a))
print("")
print(prim(a))
