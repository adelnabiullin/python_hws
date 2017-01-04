#!/usr/bin/python3

import random
import numpy as np

def mat_mult(a,b):
    zip_b = list(zip(*b))
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b] for row_a in a]

matr1 = [[random.randint(1, 30) for x in range(3)] for y in range(3)]
matr2 = [[random.randint(1, 30) for x in range(3)] for y in range(3)]

print(np.matrix(matr1))
print("")
print(np.matrix(matr2))
print("")

# with numpy
matr3 = np.dot(matr1, matr2)
print(np.matrix(matr3))
print("")

# without numpy
matr4 = mat_mult(matr1, matr2)
print(np.matrix(matr4))
print("")
