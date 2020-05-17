import telebot
from os import system

TOKEN = '1251893542:AAGgw6Z3lXmshV7FXheGB9cFwG-d5A08Aa0'

bot = telebot.TeleBot(TOKEN)

bot.send_message(462508160, 'updated successfully')

@bot.message_handler(commands=['update'])
def update(message):
    if message.chat.id == 462508160:
        system("reboot")

bot.polling()
