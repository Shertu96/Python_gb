# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = 8

def Fibonacci(n):
    if n in {0, 1}:
        return n
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

list1 = []

for e in range(-k, k + 1): # range опускает последний элемент
    if e < 0:
        list1.append((-1)**(-e + 1)*Fibonacci(-e))
        continue
    list1.append(Fibonacci(e))

print(list1)
