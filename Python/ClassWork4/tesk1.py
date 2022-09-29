# file = open('text.txt', encoding='utf-8')
# print(file.read())
# file.close()

# with open('text.txt', encoding='utf-8') as file:#менеджер контекста
#     print(file.read())

# 3. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. 
# Число N вводится пользователем. Позиции хранятся в файле file.txt в одной строке одно число
# Позиции в файл вам нужно программно положить в файл в зависимости от выбранного N: если пользователь введет двойку,
# то в файле вряд ли будут индексы 5 или 16. 
# В решении должны быть и запись в файл, и чтение из файла.

import os
os.system("cls")


def finding_noc_number(x, y): 
    if x > y: 
        greater = x 
    else: 
        greater = y 
    while(True): 
            if((greater % x == 0) and(greater % y == 0)): 
                number = greater 
                break 
            greater += 1 
    return number
                # taking input from users 
                 
num1 = int(input("Введите первое число: ")) 
num2 = int(input("Введите второе число: ")) 
print("Наименьшее общее кратное ", num1,"и", num2,"это", finding_noc_number(num1, num2))

# def max_common_divisor(a, b):
#     temp = 0
#     while b != 0:
#         temp = b
#         b = a % b
#         a = temp
#     print(a, b)
#     return a

# def min_common_divisor(a, b):
#     print(a,b)
#     return (a * b) / max_common_divisor(a, b)

# a = 2
# b = 6
# nok = min_common_divisor(a,b)
# print(f"Наименьшее общее кратное {a} и {b} равно {nok}.")

