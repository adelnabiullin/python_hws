#!/usr/bin/python3

string = 'anyone who reads Old and Middle English literary text will be familiar with the mid-brown volume of the EETS'
dictionary = {"anyone":'samebody','familiar':"close",'volume':"size",'text':"topic"}
result = []
s_list = string.split()
print(string)
print(dictionary)
for i in s_list:
    if i in dictionary: result.append(dictionary[i])
    else: result.append(i)
print(" ".join(result))
