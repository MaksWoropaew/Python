# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). 
# Играют два игрока делая ход друг после друга. Первый ход определяется 
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# Человек против человека

import random

cand = int(input("Введите количество конфет: "))
max_cand = int(input("\nВведите максимальное количество конфет, которые можно забрать за один ход: "))
person_1 = input("\nВведите имя первого игрока: ")
person_2 = input("\nВведите имя второго игрока: ")
draw = random.choice([person_1, person_2])
print(f'\nПервым ходит: {draw}')

def check_num(max_can, name):
    x = int(input(f"\n{name}, можете забрать конфет в диапозоне от {1} - {max_can}: "))
    while x < 1 or x > max_can:
        x = int(input(f"\n{name}, можете забрать конфет в диапозоне от {1} - {max_can}: "))
    return x

def person(candy, max_candy, player_1, player_2):
    while candy != 0:
        if candy < max_candy:
            max_candy = candy
        number = check_num(max_candy, player_1)
        candy -= number
        print(f"\n{player_1} забрал {number} конфет, осталось {candy}")
        if candy < max_candy:
            max_candy = candy
        if candy == 0:
            print(f"\n{player_1} ПРОИГРАЛ")
            break
        else:
            number = check_num(max_candy, player_2)
            candy -= number
            print(f"\n{player_2} забрал {number} конфет, осталось {candy}")
            if candy == 0:
                print(f"\n{player_2} ПРОИГРАЛ")
                break
            else:
                continue

if draw == person_1:
    person(cand, max_cand, person_1, person_2)
else:
    person(cand, max_cand, person_2, person_1)
  