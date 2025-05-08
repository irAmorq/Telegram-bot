import telebot
import threading
import time
from flask import Flask

TOKEN = "7965663112:AAEwtPTPLE-sz-XC8RRXUBQs5AP1UYoifus"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton(text="open", url="https://t.me/Sixp_robot/SIXP")
    markup.add(btn)
    bot.send_message(message.chat.id, "لینک مورد نظر:", reply_markup=markup)

def keep_alive():
    @app.route('/')
    def home():
        return "Bot is running!"
    app.run(host='0.0.0.0', port=8080)

threading.Thread(target=keep_alive).start()
bot.infinity_polling()
