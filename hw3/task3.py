#!/usr/bin/python3

import random
import string

def randstring(n):
    a = string.ascii_letters + string.digits
    return ''.join([random.choice(a) for i in range(n)])

text = randstring(30)
print(text)
maxdigitindex, digitlen, max = 0, 1, 0
for i in range(len(text) - 1):
    if text[i].isdigit() == 1 & text[i+1].isdigit() == 1:
        digitlen += 1
        if digitlen > max:
            max = digitlen
            maxdigitindex = i
    else:
        digitlen = 1
if max == 0:
    print("Максимальна длина 1")
else:
    print("Максимальна длина " + str(max))
    print("Начиная с позиции " + str(maxdigitindex))
