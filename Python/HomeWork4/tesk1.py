# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

def get_number(input_string):
    '''
    Проверка ввода на число
    '''
    try:
        num = int(input(input_string))
        return num
    except(ValueError):
        return get_number(input_string)

number = abs(get_number("Введите натуральное число: "))

def prime_factors(num): 
    list_num = [1]
    while num % 2 == 0: 
        list_num.append(2) 
        num = num / 2 
    for i in range(3, int(num ** 0.5) + 1, 2): 
        while num % i == 0: 
            list_num.append(i) 
            num = num / i 
    if num > 2: 
        list_num.append(num)
    return list_num

if number == 0:
    print({0})
else:
    print(sorted(set(prime_factors(number))))
