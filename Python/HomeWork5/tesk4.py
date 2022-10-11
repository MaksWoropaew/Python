# Создать программу, считывающую два полинома из двух файлов и записывающая в третий файл их сумму.


def summa_poly ():
    # Считает сумму
    file_1 = open("Python/HomeWork5/file_1.txt")
    file_2 = open("Python/HomeWork5/file_2.txt")
    file_3 = open("Python/HomeWork5/file_3.txt", "w")
    a = file_1.read()
    b = file_2.read()
    # polynom_1 = 
    # polynom_2 = 
    sum_polynum = polynom_1 + polynom_2
    file_3.write(str(sum_polynum))
    file_1.close()
    file_2.close()
    file_3.close()

summa_poly()