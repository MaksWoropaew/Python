from datetime import datetime as dt

def logger(data, result):
    '''
    Записывает время операции, саму операцию и её результат
    '''
    time = dt.now().strftime('%d.%m.%Y - %H:%M')
    with open('HomeWork10/log.csv', 'a', encoding = 'UTF-8') as file:
        file.write(f'{time}: \t{data} \t= {result}\n')