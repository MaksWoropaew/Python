import logging, random
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

TOKEN = "5730572347:AAF7Uu4tnGp9xRy0bDWk0Iic7USNgTUFZ3g"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

candy = 0
max_candy = 0
first_move = 0
pl_0 = 0
pl_1 = 0
sweet = 1
game_move = 0    
game_list = [candy, max_candy, first_move, game_move, sweet, pl_0, pl_1]

logger = logging.getLogger(__name__)

INPUT_CANDY, INPUT_MAX_CANDY, MAX_CANDY, GAME = range(4)

def start(update, _):
    """
    Начало разговора
    """
    update.message.reply_text(
        'Привет! Давай поиграем в игру с конфетами. Есть кучка конфет.'
        ' Из неё за один раз можно брать несколько конфет.'
        ' Проиграет тот, кто забирает последнюю конфету.'
        ' Команда /cancel, чтобы прекратить игру.\n\n'
        'Введи общее количество конфет: ')
    return INPUT_CANDY

def input_candy(update, _):
    """
    Количество конфет за один ход
    """
    global game_list
    word = update.message.text
    if word.isdigit():
        game_list[0]=int(word)
    else:
        update.message.reply_text('Введите число!')
        return INPUT_CANDY
    logger.info("Количество конфет: %s", game_list[0])
    update.message.reply_text('Теперь введи количество конфет, которое можно брать за один раз (не больше 1/3): ')
    return INPUT_MAX_CANDY

def input_max_candy(update, _):
    global game_list
    word = update.message.text
    if not word.isdigit():
        update.message.reply_text('Введите число!')
        return INPUT_MAX_CANDY
    elif int(word) > game_list[0] // 3:
        update.message.reply_text('Введите число, которое не больше 1/3 количества конфет!')
        return INPUT_MAX_CANDY
    else:
        update.message.reply_text('Повторите предыдущее число для подтверждения: ')
        return MAX_CANDY

def check(game_list, mv, update) -> int:
    '''
    Функция проверяет ход игры и выявляет победителя.
    '''
    if game_list[4] < game_list[0]:
        game_list[0] = game_list[0] - game_list[4]
        mv+=1
        return mv, game_list[0]
    elif game_list[4] >= game_list[0]:
        game_list[0]=0
        if game_list[3] == 0:
            update.message.reply_text("Вы проиграли!")
            return -1, -1
        elif game_list[3] == 1:
            update.message.reply_text("Я проиграл!")
            return -1, -1
   
def candy_max(update, _):
    global game_list
    word = update.message.text
    if word.isdigit() and int(word) <= int(game_list[0]/3):
        game_list[1]=int(word)
    else:
        game_list[1]=int(game_list[0]/3)
        update.message.reply_text(f'Количество конфет, которое можно брать за один раз будет = {game_list[1]}')
    logger.info('Количество конфет, которое можно брать за один раз: %s', game_list[1]) 
    first_move = random.randint(0,1)
    game_list[2] = first_move
    print(first_move, game_list)
    if first_move == 0:
        logger.info("Первый ход человека")
        update.message.reply_text('Первым ходишь ты. Ходи: ') 
    else:
        logger.info("Первый ход бота")
        update.message.reply_text('Первым хожу я: ') 
        if bot(update, _) == -1:
            return ConversationHandler.END
    return GAME    

def bot(update, _):
        global game_list
        if game_list[0] < game_list[1]:
                game_list[4] = random.randint(1,game_list[0])
        else:
                game_list[4] = random.randint(1,game_list[1])
        update.message.reply_text(f"Мой ход: {game_list[4]}")
        game_list[3] = 1
        game_list[6], game_list[0] = check(game_list, game_list[6], update)
        if game_list[6] == -1:
            game_list = [0, 0, 0, 0, 0, 0, 0]
            return -1 
        update.message.reply_text(f'Ваших ходов: {game_list[5]}, моих ходов: {game_list[6]}, осталось конфет {game_list[0]}') 
        update.message.reply_text(f'Ваш ход:')
        return GAME 
       
def person(update, _):
        global game_list
        word = update.message.text
        if word.isdigit() and int(word) <= game_list[1]:
            game_list[4]=int(word)
        else:
            game_list[4]=game_list[1]
            update.message.reply_text(f'Количество конфет, которое можно брать за один раз будет = {game_list[4]}')
        logger.info("Количество конфет введенных человеком: %s", game_list[4])            
        game_list[3] = 0
        game_list[5], game_list[0] = check(game_list, game_list[5], update)
        if game_list[5] == -1:
            game_list = [0, 0, 0, 0, 0, 0, 0]
            return -1 
        update.message.reply_text(f'Ваших ходов: {game_list[5]}, моих ходов: {game_list[6]}, осталось конфет {game_list[0]}') 
        return GAME 

def game(update, _):
    global game_list
    game_list[4]=1
    while game_list[0] > 0:
        if person(update, _) == -1:
            return ConversationHandler.END
        if bot(update, _) == -1:
            return ConversationHandler.END
        return GAME
        
def cancel(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    update.message.reply_text(
        'Игра окончена'
        'Если захотите поиграть вновь, то пишите \start', 
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states={
            INPUT_CANDY: [MessageHandler(Filters.text, input_candy)],
            INPUT_MAX_CANDY: [MessageHandler(Filters.text, input_max_candy)],
            MAX_CANDY: [MessageHandler(Filters.text, candy_max)], 
            GAME: [MessageHandler(Filters.text, game)],
        },
        fallbacks = [CommandHandler('cancel', cancel)]
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()
