# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

sequence = [1, 3, 6, 2, 3, 6, 9] # Задали последовательность, алгоритм для int, float
sequence.sort()
print(sequence) # Проверка

sequence_new = []

for i in range(len(sequence)):
    if sequence[i] not in sequence_new:
        sequence_new.append(sequence[i])
    else:
        continue

print(sequence_new)
