# import time
import datetime

import requests


class Bot:
    database: list = []
    months: dict = {
        '01': 'января',
        '02': 'февраля',
        '03': 'марта',
        '04': 'апреля',
        '05': 'мая',
        '06': 'июня',
        '07': 'июля',
        '08': 'августа',
        '09': 'сентября',
        '10': 'октября',
        '11': 'ноября',
        '12': 'декабря',
        1: 'января',
        2: 'февраля',
        3: 'марта',
        4: 'апреля',
        5: 'мая',
        6: 'июня',
        7: 'июля',
        8: 'августа',
        9: 'сентября',
        10: 'октября',
        11: 'ноября',
        12: 'декабря',
    }
    notification_id: int = 0

    def __init__(self, token):
        self.token = token
        self.url = f"https://api.telegram.org/bot{self.token}/"

    def get_updates(self, offset=None, timeout=10):
        params = {'timeout': timeout, 'offset': offset}
        response = requests.get(self.url + 'getUpdates', params)
        return response.json()['result']

    def last_update(self):
        result = self.get_updates()
        if len(result) > 0:
            last_update = result[-1]
        else:
            last_update = {}
        return last_update

    '''def last_chat_update(self, chat_id):
        update = self.get_updates()
        if len(update) > 0:
            for i in range(1, len(update)):
                k = -i
                if update[k]['message']['chat']['id'] == chat_id:
                    last_chat_update = update[k]
                else:
                    last_chat_update = {}
            print(last_chat_update)
        return last_chat_update'''

    def send_message(self, text, chat_id):
        params = {'chat_id': chat_id, 'text': text}
        response = requests.post(self.url + 'sendMessage', data=params)
        return response

    def send_sticker(self, file_id, chat_id):
        params = {'chat_id': chat_id, 'sticker': file_id}
        response = requests.post(self.url + 'sendSticker', data=params)
        return response

    def send_photo(self, file_id, chat_id):
        params = {'chat_id': chat_id, 'photo': file_id}
        response = requests.post(self.url + 'sendPhoto', data=params)
        return response

    def send_gif(self, file_id, chat_id):
        params = {'chat_id': chat_id, 'animation': file_id}
        response = requests.post(self.url + 'sendAnimation', data=params)
        return response

    def return_text_log(self):
        user_name = self.last_update()['message']['from']['username']
        chat_id = self.last_update()['message']['chat']['id']
        result = 'Сообщение от {0} в чате {1} с неизвестным содержимым'.format(user_name, chat_id)
        if self.last_update()['message'].get('text') is not None:
            user_text = self.last_update()['message']['text']
            result = 'Сообщение от {0} в чате {1} с текстом: {2}'.format(user_name, chat_id, user_text)
        return result


my_bot = Bot('896845867:AAFojelBunLM7dZctkouwEkt75mqzOJOiaU')


def return_date_matches(date):
    need_to_remind = []
    for value in my_bot.database:
        if date == value[2]:
            need_to_remind.append(value)
    return need_to_remind


def remind_notifications():
    now = datetime.datetime.now().strftime("%Y%m%d%H%M")
    remind_list = return_date_matches(now)
    for notification in remind_list:
        my_bot.send_message(f'Напоминаю {notification[1]}', notification[0])
        my_bot.database.remove(notification)


def send_user_notifications(chat_id):
    user_notifications = []
    big_string = ''
    for value in my_bot.database:
        if value[0] == chat_id:
            string = value[1] + f' | {value[2][6:8]} {my_bot.months[value[2][4:6]]} в ' \
                                f'{value[2][8:10]}:{value[2][10:12]}'
            user_notifications.append(string)
    for string in user_notifications:
        big_string += (string + '\n')
    my_bot.send_message('У вас активны следующие напоминания:\n' + big_string, chat_id)


def create_notification():
    my_bot.notification_id += 1
    new_offset = None
    for stage in range(3):
        if stage == 0:
            my_bot.get_updates(new_offset)
            last_update = my_bot.last_update()
            if last_update == {}:
                # print('pass')
                pass
            else:
                my_bot.send_message('Отлично, что вам нужно напомнить?', last_update['message']['chat']['id'])
                new_offset = last_update['update_id'] + 1
        if stage == 1:
            my_bot.get_updates(new_offset)
            last_update = my_bot.last_update()
            if last_update == {}:
                # print('pass')
                pass
            else:
                notification_text = last_update['message']['text']
                my_bot.send_message('Хорошо, когда вам это нужно напомнить'
                                    '(введите в формате год месяц день час минута)?',
                                    last_update['message']['chat']['id'])
                new_offset = last_update['update_id'] + 1
        if stage == 2:
            my_bot.get_updates(new_offset)
            last_update = my_bot.last_update()
            if last_update == {}:
                # print('pass')
                pass
            else:
                notification_time = last_update['message']['text']
                date_list = list(map(int, notification_time.split()))
                print(date_list)
                date_and_time = datetime.datetime(date_list[0], date_list[1], date_list[2], date_list[3], date_list[4])
                result_time = date_and_time.strftime("%Y%m%d%H%M")
                my_bot.database.append([
                    last_update['message']['chat']['id'],  # chat_id
                    notification_text,  # text
                    result_time  # 'time':
                ])
                my_bot.send_message(
                    f'Отлично, мы напомним вам {notification_text} {date_list[2]} {my_bot.months[date_list[1]]}'
                    f' в {date_list[3]}:{date_list[4]}',
                    last_update['message']['chat']['id'])
                print(my_bot.database)
                new_offset = last_update['update_id'] + 1


def main():
    new_offset = None
    while True:
        my_bot.get_updates(new_offset)
        print(my_bot.get_updates(new_offset))
        last_update = my_bot.last_update()
        remind_notifications()
        if last_update == {}:
            # print('pass')
            pass
        else:
            last_update_id = last_update['update_id']
            last_update_text = last_update['message']['text']
            if last_update_text == '/start':
                my_bot.send_message('Вас приветствует бот-напоминалка! Если вы хотите поставить напоминание, то'
                                    'отправьте мне "/newnotification"', last_update['message']['chat']['id'])
            if last_update_text == '/author':
                my_bot.send_message('Автор - Николай Франко @nikolai_franko', last_update['message']['chat']['id'])
            if last_update_text == '/newnotification':
                create_notification()
            if last_update_text == '/viewmynotifications':
                send_user_notifications(last_update['message']['chat']['id'])
            new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
