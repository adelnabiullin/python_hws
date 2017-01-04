#!/usr/bin/python3

def invert_dictionary(d):
    newdict = {}
    for i, j in d.items():
        for l in range(0, len(j)):
            newdict.setdefault(j[l], []).append(i)
    return newdict

dct = {'hand': ['ryka', 'kist'],
    'arm': ['ryka'],
    'lift': ['podnimat'],
    'raise': ['podnimat', 'vosxod']}
print(dct)
print(invert_dictionary(dct))
