

def get_number(input_string):
    '''
    Проверка ввода на число
    '''
    try:
        num = int(input(input_string))
        return num
    except(ValueError):
        return get_number(input_string)

number = abs(get_number("Введите число: "))

def negafibo(num):
    '''
    Негафибоначчи
    '''
    list_num = []
    if -num == -1:
        list_num.append(1)
        return list_num
    if -num == -2:
        list_num.append(1)
        list_num.append(-1)
        return list_num
    elif -num < -2:
        list_num.append(1)
        list_num.append(-1)
        for i in range(2, num):
            fib = (list_num[i - 1]) - (list_num[i - 2])
            list_num.append(-fib)
    else:
        return
    return list_num[::-1]

def fibo(num):
    '''
    Фибоначчи
    '''
    list_num = []
    if num == 0:
        list_num.append(0)
        return list_num
    if num == 1:
        list_num.append(0)
        list_num.append(1)
        return list_num
    if num == 2:
        list_num.append(0)
        list_num.append(1)
        list_num.append(1)
        return list_num
    else:
        list_num.append(0)
        list_num.append(1)
        list_num.append(1)
        for i in range(3, num + 1):
            fib = (list_num[i - 1]) + (list_num[i - 2])
            list_num.append(fib)
    return list_num



list_number_1 = negafibo(number)
list_number_2 = fibo(number)
if number == 0:
    print(fibo(number))
else:
    list_number_1.extend(list_number_2)
    print(list_number_1)

