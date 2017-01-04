#!/usr/bin/python3

def validate(string):
    return string == string[::-1]

palindrome = []
count = 0
words = input('Введите слова(анг), разделённые пробелом: ').split()
print(words)
for i in range(len(words)):
    if validate(words[i]) == 1:
        count += 1
        palindrome.append(words[i])
print("Колличество палиндромов " + str(count))
print("Список палиндромов " + str(palindrome))
