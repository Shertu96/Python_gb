# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

words = "Привет мир меня зовут АБВ но на самом деле не совсем по правде говоря абв друзья часто называют меня абвгдэйка а родители абвабв Абв папа"
final_words = []

letter_list = words.split()

for word in letter_list:
    if not('абв' in word.lower()): final_words.append(word)

print(' '.join(final_words))
