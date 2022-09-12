# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5.17, 10.01] => 0.19 или 19
# - [4.07, 5.1, 8.2444, 6.98] => 0.91 или 91
import os
os.system("cls")

list_num = [1.1, 1.2, 3.1, 5.17, 10.01,8.2444]

def check(number):
    '''
    Получение дробной части    
    '''
    length = int(len(str(number)) - 1)
    while number > 1:
        number = round(number % 1, length)
        return number

def find_max_min(list_number):
    '''
    Нахождение минимального и максимального элемента в списке
    '''
    maximum = check(list_number[0])
    minimum = check(list_number[0])
    for i in range(len(list_number) - 1):
        if maximum < check(list_number[i+1]):
            maximum = check(list_number[i+1])
        elif minimum > check(list_number[i+1]):
            minimum = check(list_number[i+1])
    return minimum, maximum

result = round(find_max_min(list_num)[1] - find_max_min(list_num)[0], 2)
print(f'Разница между максимальным и минимальным элементами -> {result}')