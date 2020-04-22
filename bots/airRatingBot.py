from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import logging
import re

token_api = '2eda286e5245044e8f0ba577462a7c1a060b0f2f'


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def get_info(city, token):
    contents = requests.get('https://api.waqi.info/feed/{0}/?token={1}'.format(city, token)).json()
    if contents['status'] == 'error':
        if 'data' in contents:
            return contents['data']
        elif 'message' in contents:
            return contents['message']

    else:
        current_aqi = contents['data']['aqi']
        station_name = contents['data']['city']['name']
        try:
            if current_aqi < 50:
                text = 'Качество воздуха считается удовлетворительным, и загрязнение воздуха представляется ' \
                       'незначительным в пределах нормы.'
            elif 50 <= current_aqi < 100:
                text = 'Качество воздуха является приемлемым; однако некоторые загрязнители могут ' \
                           'представлять опасность для людей, являющихся особо чувствительным к загрязнению воздуха.'
            elif 100 <= current_aqi < 150:
                text = 'Может оказывать эффект на особо чувствительную группу лиц. На среднего представителя ' \
                       'не оказывает видимого воздействия.'
            elif 150 <= current_aqi < 200:
                text = 'Каждый может начать испытывать последствия для своего здоровья; особо ч' \
                       'увствительные люди могут испытывать более серьезные последствия.'
            elif 200 <= current_aqi < 300:
                text = 'Опасность для здоровья от чрезвычайных условий. Это отразится, вероятно, на всем населении.'
            elif current_aqi >= 300:
                text = 'Опасность для здоровья: каждый человек может испытывать более серьезные ' \
                       'последствия для здоровья'
            else:
                text = ' '
            return current_aqi, station_name, text
        except TypeError:
            text = 'Данные в данный момент недоступны, попробуйте другой город'
            return current_aqi, station_name, text


def rate(update, context):
    city = ' '.join(context.args)
    contents = get_info(city, token_api)
    if contents == 'unknownCity' or contents == 'Unknown station':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Название города мне не понятно или его нет'
                                                                        ' в базе данных. Попробуйте нап'
                                                                        'исать международное название латиницей')
    elif contents == '404':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Пожалуйста, укажите навзание города через '
                                                                        'пробел после запроса. Например, /rate Odessa')
    elif contents == 'overQuota':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Слишком много запросов. Попробуйте снова через'
                                                                        'пару минут')
    elif contents == 'invalidKey':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Ключ API устарел. '
                                                                        'Обратитесь к @nikolai_franko')
    else:
        aqi, station_name, text = contents
        message = 'Сейчас в {0} рейтинг загрязнения воздуха {1}.\n{2}'.format(station_name, aqi, text)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def start(update, context):
    keyboard = [[InlineKeyboardButton('Как пользоваться ботом?')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привет, я могу сказать тебе рейтинг загрязнения воздуха в почти любом городе мира. '
                              'Автор: @nikolai_franko', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query
    query.edit_message_text(text='Чтобы начать пользоваться ботом, напишите /rate и название города или страны через '
                                 'пробел. Например, /rate Odessa')
    query.answer()


def unknown_command(update, context):
    update.message.reply_text(text='Неизвестная команда, /start для того, чтобы начать')


def main():
    updater = Updater('1168328699:AAG3SoENF2cyxujdyfev9kuMbFwNg1AhIxY', use_context=True)
    dp = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dp.add_handler(start_handler)
    rate_handler = CommandHandler('rate', rate)
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(rate_handler)
    dp.add_handler(MessageHandler(Filters.text, unknown_command))
    dp.add_handler(MessageHandler(Filters.command, unknown_command))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
