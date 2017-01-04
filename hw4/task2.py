#!/usr/bin/python3

dictionary = {"Anton": [5,4,3,5,4,3,5,4,5,2],'Sveta': [5,3,4,5,2,4,5,3,4,3],'Vladimir': [4,5,4,5,5,5,5,4,4,5],'Nasty': [5,4,3,3,3,5,5,4,5,5]}
loser = []
winner, new = 0, 0
print(dictionary)
for i in dictionary:
    temp = float(float(sum(dictionary[i]))/float(len(dictionary[i])))
    dictionary[i].insert(0, temp)
    if min(dictionary[i]) < 3:
        loser.append(i)
    if temp > new:
        new = temp
        winner = i
    print(str(dictionary[i]) + " " + str(i))
print("Лучший " + str(winner))
print("Задолжники " + str(loser))
