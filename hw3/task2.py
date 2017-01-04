#!/usr/bin/python3

import random
import string

text = ' '.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(20))
print(text)
count = 0
for i in range(len(text)):
    if text[i].isdigit() == 1:
        count += 1
print(count)
