import telebot
from django.conf import settings


class TBot:
    """ Обёртка для работы с API Телеграм """
    def __init__(self):
        """ Инициализация бота """
        bot_token = settings.TELEGRAM_BOT_TOKEN
        self._bot = telebot.TeleBot(bot_token)

    def send_message(self, chat_id=-1001254598595, message=''):
        """ Отправка сообщения, chat_id - id группы или пользователя """
        self._bot.send_message(chat_id=chat_id, text=message)

    def send_caption(self, chat_id, photo_link, message, parse_mode=None):
        """ Отправка изображения с сообщением, chat_id - id группы или пользователя """
        self._bot.send_photo(chat_id=chat_id, photo=photo_link, caption=message, parse_mode=parse_mode)
