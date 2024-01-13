import telebot

TOKEN = '6624674944:AAHx9L4U2qvW6fvjAc14Gh14eWDVK7TzcTE'
ADMIN_USERNAMES = ['biestoloch']

bot = telebot.TeleBot(TOKEN)

# Словарь, где ключ - это username пользователя, а значение - стикер, присвоенный пользователю
user_stickers = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Я бот-стикерописатель. Чтобы добавить пользователя, используйте команду /add_user')


@bot.message_handler(commands=['add_user'])
def add_user(message):
    if message.from_user.username in ADMIN_USERNAMES:
        # Получаем username пользователя и стикер, который нужно присвоить
        args = message.text.split(' ')
        if len(args) == 3:
            username = args[1]
            sticker_id = args[2]
            user_stickers[username] = sticker_id
            bot.reply_to(message, f'Пользователь {username} добавлен в список с стикером {sticker_id}')
        else:
            bot.reply_to(message, 'Неверный формат команды')


@bot.message_handler(commands=['remove_user'])
def remove_user(message):
    if message.from_user.username in ADMIN_USERNAMES:
        # Получаем username пользователя, которого нужно удалить из списка
        args = message.text.split(' ')
        if len(args) == 2:
            username = args[1]
            if username in user_stickers:
                del user_stickers[username]
                bot.reply_to(message, f'Пользователь {username} удален из списка')
            else:
                bot.reply_to(message, f'Пользователь {username} не найден в списке')
        else:
            bot.reply_to(message, 'Неверный формат команды')


@bot.message_handler(commands=['change_sticker'])
def change_sticker(message):
    if message.from_user.username in ADMIN_USERNAMES:
        # Получаем username пользователя и новый стикер
        args = message.text.split(' ')
        if len(args) == 3:
            username = args[1]
            sticker_id = args[2]
            if username in user_stickers:
                user_stickers[username] = sticker_id
                bot.reply_to(message, f'Стикер пользователя {username} изменен на {sticker_id}')
            else:
                bot.reply_to(message, f'Пользователь {username} не найден в списке')
        else:
            bot.reply_to(message, 'Неверный формат команды')


@bot.message_handler(func=lambda message: True)
def send_sticker(message):
    if message.from_user.username in user_stickers:
        sticker_id = user_stickers[message.from_user.username]
        bot.send_sticker(message.chat.id, sticker_id)


bot.polling()
