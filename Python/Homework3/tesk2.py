# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
list_numbers = [2, 3, 5, 6, 7, 4]
list_numbers_2 = []

def composition(list_num, list_num_2):
    if len(list_num) % 2 == 0:
        for i in range(int(len(list_num)/2)):
            item = list_num[i] * list_num[len(list_num) - i - 1]
            list_num_2.append(item)
        return list_num_2
    else:
        for i in range(int(len(list_num)/2) + 1):
            item = list_num[i] * list_num[len(list_num) - i - 1]
            list_num_2.append(item)
        return list_num_2

print(f"Произведение пар чисел списка -> {composition(list_numbers, list_numbers_2)}")