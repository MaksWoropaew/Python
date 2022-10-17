import operation as op
import config as c
import logging as l
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,  ConversationHandler

# Включим ведение журнала
l.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=l.INFO
)
logger = l.getLogger(__name__)


MAIN_MENU, WORKING_IN_MENU = range(2)


def start(update, _):
    op.for_start_menu(update, _)
    return MAIN_MENU

def main_menu(update, _):
    user_choice = update.message.text
    if user_choice == 'НАЧАТЬ':
        op.for_main_menu(update, _)
    elif user_choice == 'ВЫЙТИ':
        return cancel(update, _)
    return WORKING_IN_MENU

def working_in_menu(update, _):
    user_choice = update.message.text
    if user_choice == 'СПИСОК':
        op.output_list(update, _) 
    # elif user_choice == "НАЙТИ":  
    # elif user_choice == "ДОБАВИТЬ": 
    # elif user_choice == "УДАЛИТЬ":     
    elif user_choice == "ВЫЙТИ":
        return cancel(update, _)
    return op.for_main_menu(update, _)






def cancel(update, _):
    update.message.reply_text(
        'Вы вышли', 
        reply_markup=ReplyKeyboardRemove()  # убрать клавиатуру
    )
    return ConversationHandler.END


if __name__ == '__main__':
   
    updater = Updater(c.TOKEN)
    dispatcher = updater.dispatcher 

    conv_handler = ConversationHandler(

        entry_points=[CommandHandler('start', start), ('cancel', cancel)],
        states={
            MAIN_MENU: [MessageHandler(Filters.regex('^(НАЧАТЬ|ВЫЙТИ)$'), main_menu)],
            WORKING_IN_MENU: [MessageHandler(Filters.regex('^(СПИСОК|НАЙТИ|ДОБАВИТЬ|УДАЛИТЬ|ВЫЙТИ)$'), working_in_menu)],

        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )


dispatcher.add_handler(conv_handler)

print('server started')
updater.start_polling()
updater.idle()