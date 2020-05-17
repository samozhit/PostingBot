import telebot
from os import system

print (123456)
ADMIN_TOKEN ='1251893542:AAGgw6Z3lXmshV7FXheGB9cFwG-d5A08Aa0'
admin_bot = telebot.TeleBot(ADMIN_TOKEN)
TELEGRAM_CHANNEL_ID = '@channelForTestOne'

def post_on_tg( video=None,text=None ,audio=None, document=None, photo=None):
    pass




# @admin_bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'video'])
# def send_video(message):
#     pass


admin_bot.send_message(462508160, 'updated successfully')
admin_bot.send_message(462508160, 'second update')





@admin_bot.message_handler(commands=['update'])
def update_b(message):
    if message.chat.id == 462508160:
         system("reboot")



admin_bot.polling()


