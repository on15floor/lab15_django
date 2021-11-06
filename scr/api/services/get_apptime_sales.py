import requests
from bs4 import BeautifulSoup
from django.db.models import Q

from api.models import Apptime


def app_time_pars() -> list:
    """ Функция получает список скидок на игры для ios
    :return: Список словарей с информацией по играм
    """
    response = requests.get("https://app-time.ru/skidki-rasprodazhi-izmeneniya-novinki-appstore")
    soup = BeautifulSoup(response.text, 'html.parser')
    app_time_news = soup.find_all("div", {"class": "item-sales"})
    res = []
    for game in app_time_news:
        res.append({
            'game_name': game.contents[1].contents[0].text,
            'price_old': game.contents[1].contents[3].text,
            'price_new': game.contents[1].contents[2].text,
            'sale_percent': game.contents[0].contents[0].text,
            'cover': game.contents[0].contents[1].attrs['src'],
            'app_link': game.contents[2].attrs['href'].split('?at')[0],
        })
    return res


def get_apptime_sales() -> list:
    """Функция формирует список готовых сообщений из новых скидок app-time.ru для отправки в телеграм"""
    games = []
    apptime_sales = app_time_pars()
    if not apptime_sales:
        return games
    for game in reversed(apptime_sales):
        if not Apptime.objects.filter(Q(game_name__icontains=game['game_name'])):
            # Добавляем в БД новый элемент
            Apptime.objects.create(
                game_name=game['game_name'],
                price_old=game['price_old'],
                price_new=game['price_new'],
                sale_percent=game['sale_percent'],
                cover=game['cover'],
                app_link=game['app_link']
            )
            # Если кол-во новостей в БД больше кол-ва новостей на сайте, удалим первую запись из БД
            if Apptime.objects.count() > len(apptime_sales):
                Apptime.objects.last().delete()
            games.append({
                'massage': f'{game["game_name"]}\n'
                           f'{game["sale_percent"]} ({game["price_old"]} ₽ → <b>{game["price_new"]} ₽</b>)\n'
                           f'🔗 <a href="{game["app_link"]}">Скачать в App Store</a>',
                'cover': game['cover']
            })
    return games
