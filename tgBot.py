import telebot
from mainSettings import *

def telegramBot(name, prise, m2, link, linkSalesman):
    bot = telebot.TeleBot(APIToken)

    @bot.message_handler(commands=['start'])
    def sendMessage(message):
        bot.send_message(message.chat.id, 'Hi user! This application was created\nto quickly receive data from the cyan site.')

    @bot.message_handler(commands=['call'])
    def sendMessage(message):
        bot.send_message(message.chat.id, f'Advertisement name: {name}\nPrise: {prise}\nPrice per square meter: {m2}\nLink to real estate: {link}\nSeller link: {linkSalesman}'.format(message.from_user, bot.get_me()),parse_mode='html')

    @bot.message_handler(commands=['help'])
    def sendMessage(message):
        bot.send_message(message.chat.id, f"Commands:\n/start\n/call\n/help\nFeedBack:\n{Telegram}\n{Discord}\nVersion: 2.5\nName project: sendMessageInTelegram".format(message.from_user, bot.get_me()),parse_mode='html')

    bot.polling(
