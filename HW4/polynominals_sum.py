# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

with open('polynominal1.txt', 'w') as poly1:
    poly1.write('3ab^5 + 6b^6 + 4a^5')
with open('polynominal2.txt', 'w') as poly2:
    poly2.write('6b^6 - ab^5 + 3a^5')


with open('polynominal1.txt','r') as poly1:
    poly1 = poly1.readline()
    list_of_poly1 = poly1.split()

with open('polynominal2.txt', 'r') as poly2:
    poly2 = poly2.readline()
    list_of_poly2 = poly2.split()

print(f'{list_of_poly1} + {list_of_poly2}')
poly_sum = list_of_poly1 + list_of_poly2

with open('polynominal_sum', 'w') as poly_sum:
    poly_sum.write(f'{list_of_poly1} + {list_of_poly2}')
