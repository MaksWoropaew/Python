from datetime import datetime as dt

def logger(data: str, result: str)-> str:
    '''
    Записывает время операции, саму операцию и её результат
    '''
    time = dt.now().strftime('%d.%m.%Y - %H:%M')
    with open('Seminar_8/Programmer/log.csv', 'a', encoding = 'UTF-8') as file:
        file.write(f'{time}: \t{data} \t= {result}\n')