# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Расстояние считаем через нахождение длины вектора по 2-м точкам


def dist(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

x1 = int(input('Введите координату x точки A: '))
y1 = int(input('Введите координату y точки A: '))
x2 = int(input('Введите координату x точки B: '))
y2 = int(input('Введите координату y точки B: '))

print(dist(x1,y1,x2,y2))
