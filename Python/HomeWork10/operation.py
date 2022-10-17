from telegram import ReplyKeyboardMarkup
import csv

def for_start_menu(update, _): 
    '''
    Вывод кнопок СТАРТового меню пользователю в телеграмм
    '''
    reply_keyboard = [['НАЧАТЬ', 'ВЫЙТИ']] 
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text("ToDoList (список дел)"
                            "\nвыберите: НАЧАТЬ или ВЫЙТИ", reply_markup=markup_key)


def for_main_menu(update, _):
    '''
    Вывод кнопок ГЛАВного меню пользователю в телеграмм
    '''
    reply_keyboard = [['СПИСОК', 'НАЙТИ', 'ДОБАВИТЬ', 'УДАЛИТЬ', 'ВЫЙТИ']] 
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text("выберите действие"
                            "\nСПИСОК, НАЙТИ, ДОБАВИТЬ, УДАЛИТЬ или ВЫЙТИ", reply_markup=markup_key)


def output_list(update, _):  
    '''
    Вывод списка из файла пользователю в телеграмм
    '''
    with open('S10_P_ToDo.csv', 'r', encoding='utf-8') as csvfile:
        update.message.reply_text(csvfile.read())  



#   НЕ СДЕЛАНО!!! 
def contact_search(update, context):
    '''
    Поиск записи в файле списка дел
    '''
    line = []
    count = 0
    try:
        open('S10_P_ToDo.csv')
        with open('S10_P_ToDo.csv', encoding='utf-8') as csvfile:
            file_reader = list(csv.reader(csvfile, delimiter=','))
            for row in file_reader:
                if context.capitalize() in row:
                    count += 1
                    line.append(row)  # добавление строки в список 
                    index = file_reader.index(row)  # индекс строки с искомым контактом
                    #print(row)
            if count == 0:
                update.message.reply_text("задача не найдена в списке дел")
                return None
    except FileNotFoundError:
        update.message.reply_text("список дел пуст: добавьте запись")
    return index