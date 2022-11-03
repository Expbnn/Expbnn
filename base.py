from pars import kategory1
import telebot
from telebot import types

bot =  telebot.TeleBot('5632532758:AAF-PBBsRAIRkMhKnZHH-ExT8THMoVJ51YI')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет')

@bot.message_handler(commands=['button'])
def button(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("кнопка")
    markup.add(item1)
    item2=types.KeyboardButton("кнопка2")
    markup.add(item2)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
@bot.message_handler(content_types=["text"])
def message_reply(message):
    if message.text=="кнопка":
        final = ""
        stok=kategory1()
        stok = stok[0:20]
        for i in stok:
            final += i + "\n"
        print(len(stok))
        bot.send_message(message.chat.id, final)
        return
bot.infinity_polling()
