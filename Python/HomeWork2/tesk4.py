# Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import datetime

min_num=int(input('Введите минимальное число диапазона: '))
max_num=int(input('Введите максимальное число диапазона: '))

def rnd(minimum, maximum):
    random = int(datetime.datetime.now().strftime('%f'))/1000000
    random = int(random * (maximum - minimum) + minimum)
    return random

print(f"Случайное число в диапозоне от [{min_num}, {max_num}) -> {rnd(min_num, max_num)}")