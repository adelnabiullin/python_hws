#!/usr/bin/python3

import random
import string

text = ' '.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(20))
print(text)
a = input('Какой символ? = ')
b = input('На какой? = ')
print(text.replace(a, b))
