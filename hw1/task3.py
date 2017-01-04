#!/usr/bin/python3

import random

def sets_union(first, second):
    result = first.copy()
    for x in second:
        if x not in first:
            result.add(x)
    return result

def sets_intersection(first, second):
    result = set()
    for x in second:
        if x in first:
            result.add(x)
    return result

def sets_difference(first, second):
    result = first.copy()
    for x in second:
        if x in result:
            result.discard(x)
    return result


numbers_1 = [random.randint(1, 20) for i in range(1, 6)]
numbers_2 = [random.randint(1, 20) for i in range(1, 7)]
set1 = set(numbers_1)
set2 = set(numbers_2)

print("Set #1:")
print(set1)
print("Set #2:")
print(set2)
# print("Union")
# print(set1.union(set2))
# print("Intersection")
# print(set1.intersection(set2))
# print("Difference")
# print(set1.difference(set2))

print("Union")
print(sets_union(set1, set2))
print("Intersection")
print(sets_intersection(set1, set2))
print("Difference")
print(sets_difference(set1, set2))
