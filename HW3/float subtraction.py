# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

input_list = [1.1, 1.2, 3.1, 5, 10.01]
sub = 0

list_new = []
for i in input_list:
    list_new.append(round(i % 1, 10))

print(list_new)
print(max(list_new) - min(list_new)) # 0.2 - 0.0
