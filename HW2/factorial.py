# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

N = int(input("Введите число, факториал которого будем искать: "))

def Factorial(N):
    if N == 1:
        return N
    else:
        return N * Factorial(N-1)

print(Factorial(N))
