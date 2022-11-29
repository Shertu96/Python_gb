# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.

import random

N = int(input("Введите число N: "))
numbers = list(range(-N, N + 1))

f = open('file.txt') # Открыли файл
file_text = f.read() # Прочитали весь файл
text = [int(el) for el in file_text.split('\n')]
text.sort()

new_list = list()
size_of_numbers = len(numbers) - 1
for i in text:
    if i > size_of_numbers:
        break
    new_list.append(numbers[i])

# import random         -------- По условию задачи методом нельзя, так что для памяти
#
# random.shuffle(new_list)
# print(new_list)

print(new_list)

for i in range(1000):
    pos1 = random.randint(0, len(new_list)-1)
    pos2 = random.randint(0, len(new_list)-1)
    new_list[pos1], new_list[pos2] = new_list[pos2], new_list[pos1]

multiply = 1
for el in new_list:
    multiply *= el

print(numbers) # Проверка
print(text) # Проверка
print(new_list)
print(multiply)
