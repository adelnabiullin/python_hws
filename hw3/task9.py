#!/usr/bin/python3

def validate(string):
    return "YES" if " ".join(string.split()) == " ".join(string.split()[::-1]) else "NO"

print(validate("so patient a    doctor to doctor a patient   so"))
#print validate(raw_input('Введите слова, разделённые пробелом: '))  # Ручной ввод
