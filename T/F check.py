# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = input("Введите x: ") # Не дано, какой тип данных будем проверять, поэтому конвертировать не будем
y = input("Введите y: ")
z = input("Введите z: ")

print(not (x or y or z) == (not x and not y and not z))  # Смешанные типы для Python работают
