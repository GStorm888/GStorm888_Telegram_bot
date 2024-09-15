import datetime
import config
import telebot
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет")

@bot.message_handler(commands=["current_time", "time", "now"])
def current_time(message):
    now = datetime.datetime.now()
    output_message = f"{now.year} год, {now.month} месяц, {now.day} число"
    bot.send_message(message.chat.id, output_message)

    
bot.infinity_polling()