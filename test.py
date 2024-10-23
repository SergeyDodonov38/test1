import sys
import os
import telebot

bot = telebot.TeleBot("7516145788:AAEX4-XJcSfjJuYmBo7CJcy3XFAlrFOa4tg")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Reply to all messages with a link to the web application"""
    bot.send_message(message.chat.id, "Hello!")


if __name__ == "__main__":
    bot.polling()