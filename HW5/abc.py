# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

words = "Привет мир меня зовут АБВ но на самом деле не совсем по правде говоря абв друзья часто называют меня абвгдэйка а родители абвабв Абв папа"
final_words = []

letter_list = words.split()
print(letter_list)

for word in letter_list:
    if 'абв' in word.lower():
        print(letter_list.index(word))
        letter_list.pop(letter_list.index(word)) # С удалением символов едет индексация

print(letter_list)
