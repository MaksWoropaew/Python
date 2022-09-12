# Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def get_number(input_string):
    '''
    Проверка ввода на число
    '''
    try:
        num = int(input(input_string))
        return num
    except(ValueError):
        return get_number(input_string)

num = get_number("Введите число: ")
list_num = []

def transformation(number, list_number):
    '''
    Преобразование десятичного числа в двоичное
    '''
    while number > 0:
        remains = number % 2
        number = int(number / 2)
        list_number.append(str(remains))
    return list_number[::-1]

result = ''.join(transformation(num, list_num))
print(f'{num} -> {result}')