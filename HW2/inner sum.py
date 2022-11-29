# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

input_number = input("Введите число: ").replace('.', '').replace(',', '')
number = [int(el) for el in input_number]
print(sum(number))
