import log
import csv



def imp(list_of_data):
    """
    Импорт данных
    """
    log.logger(f"Пишем данные {list_of_data} в файл txt", "")

    with open('HomeWork8/Telephone_base.txt', 'a', encoding="utf-8") as f:
        f.write('\n\r')
        f.write('\n'.join(list_of_data))


def read_base():
    '''
    Эспорт данных из файла txt в виде списка списков
    '''
    log.logger(f"Читаем данные из файла txt", "")
    with open('HomeWork8/Telephone_base.txt', 'r', encoding='utf-8') as f:
        lst = f.read().splitlines()
    result = []
    for i in range(int(len(lst)/6)+1):
        result.append(lst[i*6:i*6+5])
    return result


def exp(text):
    """
    Поиск и экспорт нужных данных
    """
    # text = input("Введите значение для поиска: ")
    with open('HomeWork8/Telephone_base.txt', 'r', encoding='utf-8') as f:
        lst = f.read().splitlines()
        if text in lst[i]:
            temp = i % 6
            result = (lst[i-temp:i+5-temp])
            return text, result
    return text, "Данные отсутсвуют"




def read_csv():
    '''
    Чтение из файла csv, выводит массив строк
    '''
    log.logger(f"Читаем данные из файла csv", "")

    with open('HomeWork8/data.csv', newline='\n', encoding = 'utf-8') as File:  
        reader = csv.reader(File, delimiter=',', lineterminator='\n')
        file_reader = []        
        for row in reader:
            file_reader.append(row)
    # print(file_reader)        
    return file_reader

def write_csv(array):
    '''
    Запись в csv-файл массива строк
    '''
    log.logger(f"Пишем данные {array} в файл csv", "")

    with open('HomeWork8/data.csv', mode ='a', encoding='utf-8') as file:
     
        file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
        file_writer.writerow(array)

