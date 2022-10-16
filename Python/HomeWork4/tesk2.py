# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список исключит повторы элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

def get_number(input_string):
    '''
    Проверка ввода на число
    '''
    try:
        num = int(input(input_string))
        return num
    except(ValueError):
        return get_number(input_string)

list_number = [get_number("Введите число: ") for i in range(get_number("Введите размер списка: "))]
list_number_2 = []

def fill_list_num_2(list_num, list_num_2):
    for i in list_num:
        if i in list_num_2:
            continue
        else:
            list_num_2.append(i)
    return list_num_2

print(f"Исходная последовательность -> {list_number}")
print(f"Список неповторяющихся элементов исходной последовательности -> {fill_list_num_2(list_number, list_number_2)}")