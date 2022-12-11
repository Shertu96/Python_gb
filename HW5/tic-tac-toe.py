# Создайте программу для игры в "Крестики-нолики"

field = [
          [' ', ' ', ' '], 
          [' ', ' ', ' '],
          [' ', ' ', ' ']
        ]

current_role = 'X'

def is_winner_list(line):
    if line == ['O', 'O', 'O'] or line == ['X', 'X', 'X']: return True

def does_winning_line_exist(field):
    for line in field:
        if is_winner_list(line): return True
    return False

def does_winning_straight_exist(field):
    for number_of_row in range(len(field)):
        if all(row[number_of_row] == 'X' for row in field): return True
        if all(row[number_of_row] == 'O' for row in field): return True
    return False

def does_winning_cross_exist(field):
    checker_list = []
    for line_number in range(len(field)):
        el = field[line_number][line_number]
        checker_list.append(el)
    if is_winner_list(checker_list): return True

    checker_list = []
    for line_number in range(len(field)):
        el = field[line_number][(len(field) - 1) - line_number]
        checker_list.append(el)
    if is_winner_list(checker_list): return True
    return False


def is_not_game_over(field):
    if does_winning_line_exist(field): return False
    if does_winning_straight_exist(field): return False
    if does_winning_cross_exist(field): return False
    return True

def print_field(field):
    for row in field:
        print('|'.join(row))

def does_position_exist(value, max_value = 2):
    if value < 0 or value > max_value: return False
    return True

def field_blank(row, column):
    if field[row][column] != ' ': return False
    return True

def is_not_correct(row, column):
    if not does_position_exist(row): return True
    if not does_position_exist(column): return True
    if not field_blank(row, column): return True
    return False

def change_current_role(current_role):
    if current_role == 'X': return 'O'
    return 'X'

while is_not_game_over(field):
    print(f'Ход игрока: {current_role}')
    print_field(field)
    row  = int(input('Введите номер строки: ')) - 1
    column = int(input('Введите номер столбца: ')) - 1

    if is_not_correct(row, column):
        print('Вы ввели неверные координаты! Попробуйте ещё раз!\n')
        continue

    field[row][column] = current_role
    current_role = change_current_role(current_role)
    print('-------------------------------')

print_field(field)
print(f"\nПобедил пользователь, игравший за {change_current_role(current_role)}")
