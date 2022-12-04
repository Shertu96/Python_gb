# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# factor - множитель; divisor - делитель

def primefactors(N):    
    factors = []
    divisor = 2 # Первый натуральный
    m = N # Сохранить исходное число для красивого вывода
    while divisor * divisor <= N:
        if N % divisor == 0:
            factors.append(divisor)
            N = N / divisor
        else:
            divisor += 1 # Прверяем следующий

    factors.append(N) # Последнее простое число
    print('{} = {}' .format(m, factors)) # Последний множитель выводит в формате n.0


N = int(input('Введите натуральное число n: '))
if N <= 0:
    print('Натуральные числа начинаются с 1')
else:
    primefactors(N) # Ф-я нужна для проверки натуральности, если делать без неё (через цикл), проблемы n.0 нет
