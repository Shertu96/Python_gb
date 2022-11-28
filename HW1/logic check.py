# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# A = [
#         [False, False, False],
#         [False, False, True],
#         [False, True, False],
#         [False, True, True],
#         [True, False, False],
#         [True, False, True],
#         [True, True, False],
#         [True, True, True]
# ]
#
# elem = A[0]
# while elem in len(A):
#     print (not False in elem)
#     elem+=1

x = input("Введите x: ") # Не дано, какой тип данных будем проверять, поэтому конвертировать не будем
y = input("Введите y: ")
z = input("Введите z: ")

print(not (x or y or z) == (not x and not y and not z))
