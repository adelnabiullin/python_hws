#!/usr/bin/python3

words = input('Введите слова(анг), разделённые пробелом(-ами): ').split()
result = []
print(words)
maxdigitindex, digitlen, max = 0, 1, 0
for i in range(len(words) - 1):
    if words[i+1].startswith(words[i][len(words[i])-1:len(words[i])]) == 1:
        digitlen += 1
        if digitlen > max:
            max = digitlen
            maxdigitindex = i
    else:
        digitlen = 1
if max == 0:
    print("None")
else:
    print("Максимальна длина " + str(max))
    print("Начиная с позиции " + str(maxdigitindex))

# example
'''It is winter now and it is often cold. I really can't stand the cold. So sometime ago I suddenly fell ill. I had a high temperature, a running nose and a sore throat. I also had a splitting headache and a cough. My whole body was aching. Mymother fixed me a hot lemonade but that trouble each me much. Shewanted to give me some aspirin too, but there wasn't any at home. My mother told me to stay in bed and calleda doctor. The doctor came, took off his coat and put on hiswhite gown. The doctor asked me to strip to the waist. Heexamined my lungs and throat, took my pulse and temperature, measured my blood pressure. Finally he said that it was a light case of flu andtold me to stay in bed and have complete rest. He wrote aprescription for some gargle and cough medicine. He also gave mesome sulfa pills, a slip for X-Ray and blood examination. Herecommended to apply glass-cups and mustard plasters. I followed all thedoctor's instructions and very soon I felt much better. I fully recovered in ten days and resumed my studies.'''
# but that trouble each - в конце второй строки
