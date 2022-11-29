# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

n = int(input("Введите число n: "))

sum_seq = list()
for i in range(n):
    sum_seq.append((i+1) * ((1 + 1/n)**n))

print(sum_seq)
print(sum(sum_seq))
