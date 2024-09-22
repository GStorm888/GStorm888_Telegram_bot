import datetime
import config
import telebot
import user_contact
bot = telebot.TeleBot(config.token)

contacts = []
phone_number = None
name = None

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для записи контактов")

""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
начало обработки запроса пользователя
"""
@bot.message_handler(commands=["add", "new_contact"])
def new_contact(message):
    user_message = bot.reply_to(message, "Как зовут контакта?")
    bot.register_next_step_handler(user_message, process_name_step)

def process_name_step(user_message):
    global name
    name = user_message.text
    user_message = bot.reply_to(user_message, "Как какой номер телефона у контакта?")
    bot.register_next_step_handler(user_message, process_phone_number_step)

def process_phone_number_step(user_message):
    global phone_number
    phone_number = user_message.text

    user = user_contact.UserContact(name, phone_number)
    contacts.append(user)
    bot.send_message(user_message.chat.id, f"Вы ввели новый контакт")
"""
конец обработки запроса пользователя
"""
@bot.message_handler(commands=["contacts"])
def list_contacts(message):
    if len(contacts) == 0:
        output_message = "Вы не ввели ни  одного контакта"
        bot.send_message(message.chat.id, output_message)
    else:
        for contact in contacts:
            bot.send_message(message.chat.id, str(contact))


""""""""""""""""""""""""""""""""""""""""""""""""""""""


@bot.message_handler(commands=["current_time", "time", "now"])
def current_time(message):
    now = datetime.datetime.now()
    output_message = f"{now.year} год, {now.month} месяц, {now.day} число"
    bot.send_message(message.chat.id, output_message)

    
bot.infinity_polling()