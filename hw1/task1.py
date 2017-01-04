#!/usr/bin/python3

import random

numbers = [random.randint(1, 50) for i in range(1, 6)]

random.shuffle(numbers)
print(numbers)

count = 0
print("Length: " + str(len(numbers)))
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            count += 1
print(count)
