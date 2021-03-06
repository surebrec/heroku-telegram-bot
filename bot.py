# -*- coding: utf-8 -*-
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
#             ...

#       Your bot code below
bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message.text)
    bot.reply_to(message, "F*CK OFF")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message.text)
    bot.reply_to(message, message.text)

  
bot.polling()
