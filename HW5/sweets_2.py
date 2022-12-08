# Игра с конфетами:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте, как наделить бота "интеллектом"

from random import * # Все библиотеки random

# Для 2-ого человека
def human_play(sweets, max_sweet_per_turn):
    turn = randint(0, 1)
    print(f"Первый ход за игроком под номером {turn + 1}")
    while sweets > 0:
        print(f"Сейчас в стопке {sweets}")
        wish_sweets = int(input(f"Дорогой игрок под №{turn + 1}, cколько конфет Вы хотите взять?\n"))
        if wish_sweets > max_sweet_per_turn:
          print(f"Увы, но больше {max_sweet_per_turn} взять нельзя!")
          continue
        sweets -= wish_sweets
        turn = turn_map[turn]
    print(f"Игрок №{turn + 1} проиграл!")

def wish_sweets_track(turn):
    if turn:
        return int(input(f"Дорогой игрок, cколько конфет Вы хотите взять?\n"))

    comp_score = randint(1, max_sweet_per_turn)
    print(f"Компьютер взял {comp_score} конфет.")
    return comp_score

# Для компьютера
def computer_play(sweets, max_sweet_per_turn):
    turn = randint(0, 1)
    print(f"Первый ход за {name_map[turn]}")
    while sweets > 0:
        print(f"\nСейчас в стопке {sweets}")
        wish_sweets = wish_sweets_track(turn)
        if wish_sweets > max_sweet_per_turn:
          print(f"Увы, но больше {max_sweet_per_turn} взять нельзя!")
          continue
        sweets -= wish_sweets
        turn = turn_map[turn]
    print(f"{name_map[turn].capitalize()} проиграл!")

sweets = 2021
max_sweet_per_turn = 500
first_player = 0
second_player = 0
turn_map = {0: 1, 1: 0}
name_map = {0: "компьютером", 1: "человеком"}

human_play(sweets, max_sweet_per_turn)
computer_play(sweets, max_sweet_per_turn)
