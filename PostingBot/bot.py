import telebot

ADMIN_TOKEN ='838760869:AAF4GjkiYdwZxLmWFlzEeHk0MqDfyD5w0_k'
admin_bot = telebot.TeleBot(ADMIN_TOKEN)
TELEGRAM_CHANNEL_ID = '@channelForTestOne'

def post_on_tg( video,text=None ,audio=None, document=None, photo=None):
        admin_bot.send_video(TELEGRAM_CHANNEL_ID, video)




@admin_bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'video'])
def send_video(message):


    post_on_tg(message.video,)

admin_bot.polling()