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
draw = random.choice(["Бот", "Вы"])
print(f'\nПервым ходит: {draw}')

def check_num(max_can):
    x = int(input(f"\nВы можете забрать конфет в диапозоне от {1} - {max_can}: "))
    while x < 1 or x > max_can:
        x = int(input(f"\nВы можете забрать конфет в диапозоне от {1} - {max_can}: "))
    return x

def bot(candy, max_candy):
    while candy != 0:
        if candy < max_candy:
            max_candy = candy
        bot = random.randint(1, max_candy)
        candy -= bot
        print(f"\nБот забрал {bot} конфет, осталось {candy}")
        if candy < max_candy:
            max_candy = candy
        if candy == 0:
            print("\nВЫ ВЫИГРАЛИ")
            break
        else:
            number = check_num(max_candy)
            candy -= number
            print(f"\nВы забрали {number} конфет, осталось {candy}")
            if candy == 0:
                print("\nВЫ ПРОИГРАЛИ")
                break
            else:
                continue

def person(candy, max_candy):
    while candy != 0:
        if candy < max_candy:
            max_candy = candy
        number = check_num(max_candy)
        candy -= number
        print(f"\nВы забрали {number} конфет, осталось {candy}\n")
        if candy < max_candy:
            max_candy = candy
        if candy == 0:
            print("ВЫ ПРОИГРАЛИ")
            break
        else:
            bot = random.randint(1, max_candy + 1)
            candy -= bot
            print(f"Бот забрал {bot} конфет, осталось {candy}")
            if candy == 0:
                print("\nВЫ ВЫИГРАЛИ")
                break
            else:
                continue

if draw == 'Бот':
    bot(cand, max_cand)
else:
    person(cand, max_cand)