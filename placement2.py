# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Введите номер четверти: "))
list = [1, 2, 3, 4]

if quarter in list:
    if quarter == 1:
        print("x > 0; y > 0" )
    elif quarter == 2:
        print("x < 0; y > 0")
    elif quarter == 3:
        print("x < 0; y < 0")
    else:
        print("x > 0; y < 0")
else:
    print("Есть всего 4 четверти")
