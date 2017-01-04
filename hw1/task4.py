#!/usr/bin/python3

import math
import random

def comb_sort(lst):
    step = math.floor(len(lst) / 1.247)
    while step > 0:
        i = 0
        while i + step < len(lst):
            if lst[i] > lst[i + step]:
                lst[i], lst[i + step] = lst[i + step], lst[i]
            i += 1
        step = math.floor(step / 1.247)
    return lst

lst = [random.randint(1, 30) for i in range(1, 10)]
print("Source array: " + str(lst))
comb_sort(lst)
print("Result array: " + str(lst))
