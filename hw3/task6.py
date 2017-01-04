#!/usr/bin/python3

words = input('Введите слова(анг), разделённые пробелом(-ами): ').split()
for i, v in enumerate(words):
    print(words[-i - 1])
