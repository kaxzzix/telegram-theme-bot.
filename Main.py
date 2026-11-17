
import os
import telebot

TOKEN = os.getenv("8841141485:AAH9hQbFlWy2upccvh9Kgq2rB2lKRptuCZY")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "ррn"
        "крол!"
    )

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "Скоро здесь появится генератор тем!")

bot.infinity_polling()
