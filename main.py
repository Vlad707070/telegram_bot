import telebot

bot = telebot.TeleBot('6978271093:AAGr2ZGO5x7M8_EF2wdQeMet3s762738OFo')


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Привет! Я бот!')


@bot.message_handler(func=lambda message: message.from_user.username in ['syddss', 'diankfr'])
def handle_message(message):
    print(message)
    if message.from_user.username == 'syddss':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAELBeZlhuX__zEIQAqjm1KHm0Idh7Y4NAACRxcAAuUm2Us4slEOn4ofBTME')
    elif message.from_user.username == 'diankfr':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAELBzJlh9i037o-g1tNlsit85pG7TYJAgACGhUAAru3aUjlYr57-57PNDME')


bot.polling()
