""" 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
    *Пример:*
    
    - Для N = 5: 1, -3, 9, -27, 81

2.Найти сумму элементов массива, лежащих между максимальным и минимальным по значению элементами

3.Найдите количество элементов массива, которые отличны от наибольшего элемента не более чем на 10%

 """

import math
 

def get_min_max (list):
    index_min = list.index(min(list))
    index_max = list.index(max(list))
    print(index_min)
    print(index_max)
    if index_min<index_max:
        list_res = list[index_min:index_max + 1]
    else:
        list_res = list[index_max:index_min + 1]
    print(list_res)
   
list = [99,4,6,1,23,67,2,]
get_min_max(list)

