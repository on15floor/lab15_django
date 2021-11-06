import requests
from bs4 import BeautifulSoup
from django.db.models import Q

from api.models import Beget


def beget_news_pars() -> list:
    """ Функция получает список новостей с beget.com
    :return: Список новостей
    """
    response = requests.get("https://beget.com/ru/news/2021/beget-12-years")
    soup = BeautifulSoup(response.text, 'html.parser')
    beget_news = soup.find_all("ul", {"class": "nav nav-category-tree flex-nowrap my-0"})
    res = []
    for n in beget_news[0].contents:
        res.append(n.text.strip())
    return res


def get_beget_news() -> str:
    """Функция формирует готовое сообщение из новых новостей beget.ru для отправки в телеграм"""
    telegram_mess = ''
    beget_news = beget_news_pars()
    if not beget_news:
        return telegram_mess
    for n in reversed(beget_news):
        if not Beget.objects.filter(Q(news__icontains=n)):
            # Добавляем в БД новый элемент
            Beget.objects.create(news=n)
            # Если кол-во новостей в БД больше кол-ва новостей на сайте, удалим первую запись из БД
            if Beget.objects.count() > len(beget_news):
                Beget.objects.last().delete()
            telegram_mess = f'{n}\n'
    return telegram_mess
