import telebot
from telebot import types
import random

f = open('horoscope.txt', encoding='UTF-8')
horos = f.readlines()
f.close()

bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def start(message):
    markup_inline = types.InlineKeyboardMarkup(row_width=2)
    item_1=types.InlineKeyboardButton('Да', callback_data='yes')
    item_2=types.InlineKeyboardButton('Нет', callback_data='no')
    markup_inline.add(item_1, item_2)

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}! Веришь в гороскопы?', reply_markup=markup_inline)

@bot.callback_query_handler (func=lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = (types.KeyboardButton('Козерог'))
        item2 = (types.KeyboardButton('Водолей'))
        item3 = (types.KeyboardButton('Рыбы'))
        item4 = (types.KeyboardButton('Овен'))
        item5 = (types.KeyboardButton('Телец'))
        item6 = (types.KeyboardButton('Близнецы'))
        item7 = (types.KeyboardButton('Рак'))
        item8 = (types.KeyboardButton('Лев'))
        item9 = (types.KeyboardButton('Дева'))
        item10 = (types.KeyboardButton('Весы'))
        item11 = (types.KeyboardButton('Скорпион'))
        item12 = (types.KeyboardButton('Скорпион'))
        markup_reply.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
        bot.send_message(call.message.chat.id, 'Выбери свой знак зодиака и узнай свой гороскоп!', reply_markup=markup_reply)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Я больше ничего не знаю. Пока, друг!')

@bot.message_handler(content_types= ['text'])
def get_text(message):
    if message.text == 'Козерог':
        bot.send_message(message.chat.id, random.choice(horos))
    if message.text == 'Водолей':
        bot.send_message(message.chat.id, random.choice(horos))
    if message.text == 'Рыбы':
        bot.send_message(message.chat.id, random.choice(horos))
    if message.text == 'Овен':
        bot.send_message(message.chat.id, random.choice(horos))
    if message.text == 'Телец':
        bot.send_message(message.chat.id, random.choice(horos))
    if message.text == 'Близнецы':
        bot.send_message(message.chat.id, random.choice(horos))
    if message.text == 'Рак':
        bot.send_message(message.chat.id, random.choice(horos))
    if message.text == 'Лев':
        bot.send_message(message.chat.id, random.choice(horos))
    if message.text == 'Дева':
        bot.send_message(message.chat.id, random.choice(horos))
    if message.text == 'Весы':
        bot.send_message(message.chat.id, random.choice(horos))
    if message.text == 'Скорпион':
        bot.send_message(message.chat.id, random.choice(horos))
    if message.text == 'Скорпион':
        bot.send_message(message.chat.id, random.choice(horos))

bot.polling(none_stop=True)