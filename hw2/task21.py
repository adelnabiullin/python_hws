#!/usr/bin/python3

import math

def solve(a, b, c):
    "Solves quadratic equation"
    a = float(a)
    b = float(b)
    c = float(c)
    tmp = []
    if a == 0 and b != 0:
        x = (-c) / b
        tmp.append(x)
    elif a == 0 and b == 0 and c == 0:
        tmp.append("infinity")
    elif a != 0:
        D = (b * b) - 4 * a * c
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            tmp.extend([x1, x2])
        elif D == 0:
            x = (-b) / (2 * a)
            tmp.append(x)
    return tmp

print("Type coefficients of quadratic equation (ax^2 + bx + c = 0):")
_a = input('a = ')
_b = input('b = ')
_c = input('c = ')

print("Answer: ", solve(_a, _b, _c))
