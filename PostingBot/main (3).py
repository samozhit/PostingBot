

import telebot

ADMIN_TOKEN = '1224989639:AAGznDiDMjXxtww2_jwTNFDVrGr6tRCsu2o'
admin_bot = telebot.TeleBot(ADMIN_TOKEN)


def post_on_tg(text, audio, document, photo, video):
	admin_bot.send_message()


def post_on_vk(text, audio, document, photo, video):
	pass



@admin_bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'video'])
def handle_docs_audio(message):
    text = message.text
    audio = 123

    post_on_tg(text=text, audio=audio)
    post_on_vk()


