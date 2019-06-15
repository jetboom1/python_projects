import requests


class Bot:
    def __init__(self, token):
        self.token = token
        self.url = "https://api.telegram.org/bot{0}/".format(self.token)

    def get_updates(self, offset=None, timeout=30):
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

    def get_chat_id(self):
        chat_id = self.last_update()['message']['chat']['id']
        return chat_id

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

    def return_last_message(self):
        return self.last_update()['message']['text']

    def return_text_log(self):
        user_name = self.last_update()['message']['from']['username']
        chat_id = self.last_update()['message']['chat']['id']
        result = 'Сообщение от {0} в чате {1} с неизвестным содержимым'.format(user_name, chat_id)
        if self.last_update()['message'].get('text') is not None:
            user_text = self.last_update()['message']['text']
            result = 'Сообщение от {0} в чате {1} с текстом: {2}'.format(user_name, chat_id, user_text)
        return result


my_bot = Bot('809619657:AAGa1UwaqxHyMNxlvYqzzSvAlZBtRQSUJic')


def main():
    new_offset = None
    while True:
        my_bot.get_updates(new_offset)
        print(my_bot.get_updates(new_offset))
        last_update = my_bot.last_update()
        if last_update == {}:
            # print('pass')
            pass
        else:
            last_update_id = last_update['update_id']
            if last_update['message'].get('text') is not None and last_update['message'].get('reply_to_message') is not None:
                last_update_text = last_update['message']['text']
                if last_update_text == '/start' or last_update_text == '/help':
                    my_bot.send_message('Этот бот будет просто передразнивать вас. Отправьте ему какое-либо сообщение. '
                                        'Поддерживаются текст, фото, стикеры и гифки', my_bot.get_chat_id())
                    new_offset = last_update_id + 1
                elif last_update_text == '/author':
                    my_bot.send_message('Автор - Франко Николай @nikolai_franko', my_bot.get_chat_id())
                    new_offset = last_update_id + 1
                else:
                    print(my_bot.return_text_log())
                    my_bot.send_message(last_update_text, my_bot.get_chat_id())
                    new_offset = last_update_id+1
            else:
                new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
