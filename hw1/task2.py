#!/usr/bin/python3

def list_inclusion(l1, l2):
    "check if l2 is in l1"
    tmp = l1[:]
    for e in l2:
        if e not in tmp:
            return False
        else:
            tmp.remove(e)
    return True

lst1 = [ 0, 1, 2, 3, 4 ]
lst2 = [ 1, 2, 3 ]
lst3 = [ 2, 1, 4 ]
lst4 = [ 4, 5 ]
lst5 = [ 0, 1, 2, 3, 4, 4 ]
lst6 = [ 1, 2, 1 ]

print(list_inclusion(lst1, lst2))
print(list_inclusion(lst1, lst3))
print(list_inclusion(lst1, lst4))
print(list_inclusion(lst1, lst5))
print(list_inclusion(lst1, lst6))
