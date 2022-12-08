# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint

max_val=100

k = int(input('Введите натуральную степень k:'))
factor = [randint(0,max_val) for i in range(k)]+[randint(1,max_val)]

if k <= 0:
    print('Натуральные числа начинаются с 1')
else:
    poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(factor) if j][::-1])
    poly=poly.replace('x^1+', 'x+')
    poly=poly.replace('x^0', '')
    poly+=('','1')[poly[-1]=='+']
    poly=(poly, poly[:-2])[poly[-2:]=='^1']

print(poly)