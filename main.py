import datetime
import config
import contact_boook

import telebot
from telebot import types

import user_contact

bot = telebot.TeleBot(config.token)
contact_builder = contact_boook.ContactBuilder()


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
        delete_keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Имя контакта>>>", reply_markup=delete_keyboard)
        # обработка сообщения
        bot.register_next_step_handler(message, process_name_step)

    elif message.text == "Показать все контакты":
        
        contacts = contact_builder.get_contacts(message.chat.id)
        if len(contacts) > 0:
            bot.send_message(message.chat.id, "Все контакты:")
            for contact in contacts:
                bot.send_message(message.chat.id, str(contact))
        else:
            bot.send_message(message.chat.id, "Список пуст<<<")
            # вывод контактов
        bot.register_next_step_handler(message, handler_main_commands)

    else:
        bot.send_message(message.chat.id, "Не понял")
        # рекурсия
        bot.register_next_step_handler(message, handler_main_commands)



# начало обработка имени
def process_name_step(message):
    name = message.text

    if not name:
        bot.send_message(message.chat.id, "Имя не может быть пустым")
    # рекурсия
        bot.register_next_step_handler(message, process_name_step)
        return
    
    contact_builder.add_name(message.chat.id, name)

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
    
    contact_builder.add_phone_number(message.chat.id, phone_number)


    bot.send_message(message.chat.id, "Описание>>>")
    bot.register_next_step_handler(message, process_description_step)

# начало обработка описания
def process_description_step(message):
    description = message.text
    
    contact_builder.add_description(message.chat.id, description)
    contact_builder.build(message.chat.id)

    bot.send_message(message.chat.id, "Контакт создан!", reply_markup=create_main_keyboard())
    bot.register_next_step_handler(message, handler_main_commands)

bot.infinity_polling()