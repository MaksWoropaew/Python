from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
from operation import *
from telegram import *
from datetime import datetime as dt
import logging
from config import TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

TIME_NOW = dt.now().strftime('%D_%H:%M')

SHOW_MENU, MENU, EDIT, ADD, DELETE, VIEW, SEARCH, SEARCH_MENU, GET_TASK, GET_DATE, DATA, TIME, RETASK = range(13)

def show_menu(update, _):
    reply_keyboard = [
        ['Показать', 'Добавить', 'Поиск', 'Удалить', 'Редактировать', 'Выход']]
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text('Это ваш список дел. Что бы вы хотели сделать?', reply_markup=markup_key)
    return MENU

def menu(update, _):
    user = update.message.from_user
    logger.info("Выбор операции: %s: %s", user.first_name, update.message.text)
    choice = update.message.text
    if choice == 'Показать':
        return VIEW
    if choice == 'Добавить':
        update.message.reply_text('Введите задачу: ')
        return ADD
    if choice == 'Поиск':
        update.message.reply_text("Текст дял поиска: ")
        return SEARCH
    if choice == 'Удалить':
        update.message.reply_text("Найти задачу для удаления: ")
        return DELETE
    if choice == 'Редактировать':
        update.message.reply_text("Найти задачу для редактирования: ")
        return EDIT
    if choice == 'Выход':
        return cancel(update, _)

def view(update, _):
    user = update.message.from_user
    logger.info("Контакт %s: %s", user.first_name, update.message.text)
    tasks = read_csv()
    tasks_string = view_tasks(tasks)
    update.message.reply_text(tasks_string)
    return show_menu(update, _)

def add(update, context):
    user = update.message.from_user
    logger.info("Task %s: %s", user.first_name, update.message.text)
    name = update.message.text
    if len(name) >= 3:
        context.user_data['name'] = name
        update.message.reply_text("Введите дату в формате ДД/ММ/ГГ: ")
        return DATA
    else:
        update.message.reply_text('Не менее 3 символов')
        return

def data(update, context):
    user = update.message.from_user
    logger.info("Task %s: %s", user.first_name, update.message.text)
    data = update.message.text

    if len(data) == 8 and data[2] == '/' and data[5] == '/':
        temp = data.replace('/', '')
        if temp.isdigit():
            data += '_'
            context.user_data['data'] = data
            update.message.reply_text("Введите время в формате ЧЧ:ММ ")
            return TIME
        else:
            update.message.reply_text("Введите дату в формате ДД/ММ/ГГ: ")
    data += '_'
    context.user_data['data'] = data
    update.message.reply_text("Введите время в формате ЧЧ:ММ ")
    return TIME

def time(update, context):
    task = {}
    user = update.message.from_user
    logger.info("Task %s: %s", user.first_name, update.message.text)
    time = update.message.text
    if len(time) == 5 and time[2] == ':':
        temp = time.replace(':', '')
        if temp.isdigit():
            data = context.user_data.get('data') + time
            name = context.user_data.get('name')
            task['Имя'] = user.first_name
            task['Фамилия'] = user.last_name
            task['Текущая дата'] = TIME_NOW
            task['Дата выполнения'] = data
            task['Задача'] = name
            tasks.append(task)
            write_csv(tasks)
            update.message.reply_text('Задача добавлена')
            return show_menu(update, context)
        else:
            update.message.reply_text("Введите время в формате ЧЧ:ММ ")
    else:
        update.message.reply_text("Введите время в формате ЧЧ:ММ ")

def search(update, _):
    user = update.message.from_user
    logger.info("Выбор поиска: %s: %s", user.first_name, update.message.text)
    searchstring = update.message.text
    tasks = read_csv()

    if check_have_task(searchstring, tasks):
        find = find_tasks(tasks, searchstring)
        result = view_tasks(find)
        update.message.reply_text(
            f'По запросу <{searchstring}> найдено: ')
        update.message.reply_text(result)
    else:
        update.message.reply_text(f'Ничего не найдено')
    return show_menu(update, _)

def delete(update, _):
    tasks = read_csv()
    user = update.message.from_user
    logger.info("Выбор удаления: %s: %s", user.first_name, update.message.text)
    searchstring = update.message.text
    if len(searchstring) >= 3:
        if delete_task(searchstring, tasks):
            update.message.reply_text('Задача удалена')
            write_csv(tasks)
        else:
            update.message.reply_text('Такой задачи нет')
    else:
        update.message.reply_text('Введите от трех букв')
    return show_menu(update, _)

def edit(update, context):
    tasks = read_csv()
    user = update.message.from_user
    logger.info("Выбор редактирования: %s: %s",
                user.first_name, update.message.text)
    searchstring = update.message.text
    if check_have_task(searchstring, tasks):
        if len(searchstring) >= 3:
            context.user_data['searchstring'] = searchstring
            update.message.reply_text('Введите задачу: ')
            return RETASK
        else:
            update.message.reply_text('Введите не менее трех букв для поиска')
            return
    else:
        update.message.reply_text('Такой задачи нет')
        return

def retask(update, context):
    tasks = read_csv()
    retask = update.message.text
    searchstring = context.user_data.get('searchstring')
    if len(retask) >= 3:
        edit_task(searchstring, tasks, retask)
        write_csv(tasks)
        update.message.reply_text('Задача отредактирована')
    else:
        update.message.reply_text(
            'Введите не менее трех букв для новой задачи')
        return
    return show_menu(update, context)


def cancel(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    update.message.reply_text(
        'Вы знаете где меня найти.',)
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    game_conversation_handler = ConversationHandler(  # здесь строится логика разговора
        entry_points=[CommandHandler('start', show_menu)],
        states={
            VIEW: [MessageHandler(Filters.text, view)],
            SHOW_MENU: [MessageHandler(Filters.text, show_menu)],
            ADD: [MessageHandler(Filters.text, add)],
            DELETE: [MessageHandler(Filters.text, delete)],
            SEARCH: [MessageHandler(Filters.text, search)],
            MENU: [MessageHandler(Filters.text, menu)],
            EDIT: [MessageHandler(Filters.text, edit)],
            DATA: [MessageHandler(Filters.text, data)],
            TIME: [MessageHandler(Filters.text, time)],
            RETASK: [MessageHandler(Filters.text, retask)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(game_conversation_handler)
    updater.start_polling()
    updater.idle()