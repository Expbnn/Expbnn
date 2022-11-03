import telebot
from telebot import types
from telebot.types import  ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from button import kb,ktgbtn

bot =  telebot.TeleBot('5632532758:AAF-PBBsRAIRkMhKnZHH-ExT8THMoVJ51YI')
@bot.message_handler(content_types=["text"])

img = open('1.jpg', 'rb')
bot.send_photo(message.chat.id, img, reply_markup = kb)
img = open('2.jpg', 'rb')
bot.send_photo(message.chat.id, img, reply_markup = kb)
img = open('3.jpg', 'rb')
bot.send_photo(message.chat.id, img, reply_markup = kb)
img = open('4.jpg', 'rb')
bot.send_photo(message.chat.id, img, reply_markup = kb)
img = open('5.jpg', 'rb')
bot.send_photo(message.chat.id, img, reply_markup = kb)
img = open('6.jpg', 'rb')
bot.send_photo(message.chat.id, img, reply_markup = kb)
img = open('7.jpg', 'rb')
bot.send_photo(message.chat.id, img, reply_markup = kb)
img = open('8.jpg', 'rb')
bot.send_photo(message.chat.id, img, reply_markup = kb)
img = open('9.jpg', 'rb')
