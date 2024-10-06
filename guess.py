from random import randint

from telebot import TeleBot, types

from config import TOKEN

bot = TeleBot(TOKEN)
LOW = 1
HIGH = 100
bot_number = None


@bot.message_handler(commands=["start"])
def start(message):

    keyboard_markup = types.InlineKeyboardMarkup()
    button_start = types.InlineKeyboardButton(text="Начать", callback_data="start")
    keyboard_markup.add(button_start)
    
    bot.send_message(message.chat.id, 'Привет, я бот для игры в "угадай число", нажми "Начать" чтобы играть', reply_markup=keyboard_markup)


@bot.message_handler(func=lambda message: True)
def any_other_message(message):
    bot.send_message(message.chat.id, "Выйди из бота")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "start":      
        global bot_number  
        bot_number = randint(LOW, HIGH)
        output_message = f"Я загадал число от {LOW} до {HIGH}, какое?"
        message = call.message

        bot.edit_message_text(chat_id=message.chat.id,
                              message_id=message.id,
                              text=output_message)
        bot.register_next_step_handler(message, process_guess_number_step)

def process_guess_number_step(message):
    str_number = message.text
    if not str_number:
        bot.send_message(message.chat.id, "Вы ввели не число, введите число")
        bot.register_next_step_handler(message, process_guess_number_step)
        return
    
    number = int(str_number)
    if number == bot_number:
        output_message = "Вы угадали!"
    elif number < bot_number:
        output_message = "Я загадал число больше"
    elif number > bot_number:
        output_message = "Я загадал число меньше"
    bot.send_message(message.chat.id, output_message)
    if output_message != "Вы угадали!":
        bot.register_next_step_handler(message, process_guess_number_step)



bot.infinity_polling()
