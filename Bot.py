import telebot
from Extensions import ConvertionException, Misstakes
from Settings import token, values

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду в формате: \n"имя валюты"\
    "в какую валюту перевести"\
    "количество" \nВажно! Валюты нужно писать с заглавной буквы. \nCписок всех доступных валют:  /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def value(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in values.keys():
        text = '\n'.join((text, i, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convertation(message: telebot.types.Message):
    try:
        value = message.text.split(' ')
        if len(value) > 3:
            raise ConvertionException('Слишком много параметров :)')
        elif len(value) < 3:
            raise ConvertionException('Маловато параметров :)')
        value1, value2, count = value
        result = Misstakes.misstake(value1, value2, count)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {count} {value1} в {value2} - {result}'
        bot.send_message(message.chat.id, text)
bot.polling(none_stop=True)