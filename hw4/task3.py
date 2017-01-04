#!/usr/bin/python3

c = {}
a = {"character":'symbol',\
     "anyone":'samebody',\
     'familiar':"close",\
     'volume':"size",\
     'text':"topic"}
b = {"anyone":'anybody',\
     'familiar':"habitual",\
     'volume':"capacity",\
     'text':"word",\
     'eccentric': "cam"}
print(a)
print(b)
c = a.copy()
for i in a:
    if i not in b:
        c.pop(i)
print(c)
