from random import choice

from telebot import TeleBot, types

from config import TOKEN

bot = TeleBot(TOKEN)

"""
функция для обработки кто победил
# если победил пользователь, то бот проиграл,
но если ничья, то никто 
"""

def who_won(user_input: str, bot_input:str):
    user_input = user_input.lower()
    bot_input = bot_input.lower()

    if user_input == bot_input:
        return "nobody"
    elif user_input == "камень" and bot_input == "ножницы"\
        or user_input == "бумага" and bot_input == "камень"\
        or user_input == "ножницы" and bot_input == "бумага":
        return "user"
    
    return "bot"

def generate_bot_answer():
    choices = ["Камень", "Ножницы", "Бумага"]
    return choice(choices)

"""
функция старт в которой добавили кнопки для выбора предмета
"""
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    rock_btn = types.KeyboardButton("Камень")
    scissors_btn = types.KeyboardButton("Ножницы")
    paper_btn = types.KeyboardButton("Бумага")
    markup.add(rock_btn, scissors_btn, paper_btn)
    bot.send_message(message.chat.id,
                    "Привет! предлагаю сыграть в камень-ножницы-бумага, выбирай:",
                     reply_markup=markup)
    
    bot.register_next_step_handler(message, game)

"""
основная функция для игры
"""
def game(message):
    user_input = message.text
    bot_input = generate_bot_answer()

    winner = who_won(user_input, bot_input)
    if winner == "user":
        bot_response = f"Поздравляю с победой, я загадал: {bot_input}"
    elif winner == "bot":
        bot_response = f"ты проиграл, я загадал: {bot_input}"   
    elif winner == "nobody":
        bot_response = f"Ничья, я тоже загадал: {bot_input}"



    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    play_again = types.KeyboardButton("/start")
    markup.add(play_again)

    bot.send_message(message.chat.id, bot_response, reply_markup=markup)

"""
посмотреть все нюансы bot.polling()
"""
bot.infinity_polling()
