# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, 
# которые имеют средний балл более «4».
# Пример:
# Волков Андрей 5
# Наталья Тарасова 5
# Фредди Меркури 3
# Денис Байцуров 4

# Программа выдаст:
# ВОЛКОВ АНДРЕЙ 5
# НАТАЛЬЯ ТАРАСОВА 5
# Фредди Меркури 3
# Денис Байцуров 4

file = open("HomeWork4/file_1.txt", "r+", encoding="utf-8")
def get_number(input_string):
    '''
    Проверка ввода на число
    '''
    try:
        num = int(input(input_string))
        return num
    except(ValueError):
        return get_number(input_string)

list_num = []
lines = file.readlines()
for line in lines:
    list_num.append(line.strip())

def student_mark(list_number):
    '''
    Перевод в верхний регистр всех букв, если бал студента больше 4
    '''
    file.seek(0)
    for i in range(len(list_number)):
        if int(str(list_number[i])[len(list_number[i]) - 1]) > 4:
            list_number[i] = str(list_number[i]).upper()
        # print(list_num[i])
        file.write('\n' + str(list_num[i]))
    file.close()

student_mark(list_num)