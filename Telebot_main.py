import telebot
from config import *
from extentions import Converter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = f"Приветствую! \n" \
           f"Хотите увидеть список доступных валют? \n" \
           f"Для этого введите команду /values! \n" \
           f"Я умею конвертировать валюту \n" \
           f"по команде /convert! \n" \
           f"Формат ввода валют: CNY RUB 10"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for currency in exchanges.keys():
        text = '\n'.join((text, currency))
    bot.reply_to(message, text)


@bot.message_handler(commands=['convert'])
def values(message: telebot.types.Message):
    text = 'Выберите валюту из которой будете конвертировать в формате ⮞ CNY ⮜'
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, base_curr_handler)


def base_curr_handler(message: telebot.types.Message):
    base_curr = message.text.strip()
    text = 'Выберите валюту в которую будете конвертировать в формате ⮞ RUB ⮜'
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, exchange_curr_handler, base_curr)


def exchange_curr_handler(message: telebot.types.Message, base_curr):
    exchange_curr = message.text.strip()
    text = 'Выберите количество конвертируемой валюты:'
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, amount_handler, base_curr, exchange_curr)


def amount_handler(message: telebot.types.Message, base_curr, exchange_curr):
    amount = message.text.strip()
    exchange_amount = Converter.get_exchange_amount(base_curr, exchange_curr, amount)
    text = f"Цена {amount}  {base_curr} в {exchange_curr} : {exchange_amount}"
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    commands = message.text.split()
    base_curr, exchange_curr, amount = commands
    if len(commands) != 3:
        bot.reply_to(message, "Неверное количество параметров!")

    if base_curr == exchange_curr:
        bot.reply_to(message, "Вы ввели одинаковые валюты!")


bot.polling(none_stop=True)
