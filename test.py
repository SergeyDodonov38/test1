import sys
import os
import telebot

bot = telebot.TeleBot("8068184643:AAGoazJYLgeIYSDnG7NWaXIEIvMcH_Lv91o")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Reply to all messages with a link to the web application"""
    bot.send_message(message.chat.id, "Hello!")


if __name__ == "__main__":
    bot.polling()