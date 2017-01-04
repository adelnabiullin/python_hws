#!/usr/bin/python3

import random
import numpy as np

def revert_matrix(target):
    result = []
    for row in target:
        result.insert(0, row)
    return result

matr = [[random.randint(1, 30) for x in range(6)] for y in range(6)]

print(np.matrix(matr))
print("")
print(np.matrix(revert_matrix(matr)))
