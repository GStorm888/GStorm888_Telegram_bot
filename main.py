import datetime
import config
import telebot
from telebot import types

import user_contact
bot = telebot.TeleBot(config.token)

contacts = []
phone_number = None
name = None

def create_main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    add_contact_btn = types.KeyboardButton("Добавить контакт") 
    show_contact_btn = types.KeyboardButton("Показать все контакты") 
    keyboard.add(add_contact_btn, show_contact_btn)
    return keyboard
"""
команда старт для начала работы бота:
"""
@bot.message_handler(commands=["start"])
def start(message):
    

    bot.send_message(message.chat.id, "Привет! Я бот для записи контактов", reply_markup=create_main_keyboard())
    bot.register_next_step_handler(message, handler_main_commands)

def handler_main_commands(message):
    if message.text == "Добавить контакт":
        print("add contact>>>")
        delete_keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Имя контакта>>>", reply_markup=delete_keyboard)
        # обработка сообщения
        bot.register_next_step_handler(message, process_name_step)

    elif message.text == "Показать все контакты":
        print("chek contacts>>>") 
        bot.send_message(message.chat.id, "Все контакты")
        # вывод контактов
        bot.register_next_step_handler(message)

    else:
        print("i don`t know>>>")
        bot.send_message(message.chat.id, "Не понял")
        # рекурсия
        bot.register_next_step_handler(message, process_name_step)



# начало обработка имени
def process_name_step(message):
    name = message.text

    if not name:
        bot.send_message(message.chat.id, "Имя не может быть пустым")
    # рекурсия
        bot.register_next_step_handler(message, process_name_step)
        return
    
    # contact_builder.add_name(name)

    bot.send_message(message.chat.id, "Номер телефона>>>")
    bot.register_next_step_handler(message, process_phone_number_step)

# начало обработка номера телефона
def process_phone_number_step(message):
    phone_number = message.text

    if not phone_number:
        bot.send_message(message.chat.id, "Номер телефона не может быть пустым")
    # рекурсия
        bot.register_next_step_handler(message, process_phone_number_step)
        return
    
    # contact_builder.add_name(name)

    keyboard = types.InlineKeyboardMarkup()

    skip_btn = types.InlineKeyboardButton(text="Пропустить", callback_data="skip_description")
    keyboard.add(skip_btn)

    bot.send_message(message.chat.id, "Описание>>>", reply_markup=keyboard)
    bot.register_next_step_handler(message, process_description_step)

# начало обработка описания
def process_description_step(message):
    description = message.text
    
    # contact_builder.add_name(name)

    bot.send_message(message.chat.id, "Контакт создан!", reply_markup=create_main_keyboard())
    bot.register_next_step_handler(message, process_phone_number_step)

bot.infinity_polling()