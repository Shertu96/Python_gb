# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math # Подключение стандартной библиотеки

input_list = list(range(5)) # Не хочу усложнять вводом от пользователя и проверками/конвертациями
print(input_list)
multiply = []

for i in (range(math.ceil(len(input_list)/2))): # Вызов метода из импортируемой библиотеки
    multiply.append(input_list[i] * input_list[len(input_list) - (i + 1)])
print(multiply)
