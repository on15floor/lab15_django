from datetime import datetime

from django import template

register = template.Library()


@register.filter(name='percent_left')
def percent_left(date_start: str, total_days):
    """ Фильтр получает время начала события и его продолжительность.
    Рассчитывает на сегодняшний день процент выполнения """
    date_start = datetime.strptime(date_start, '%Y-%m-%d')
    date_now = datetime.now()
    date_delta = date_now-date_start
    res = date_delta.days/float(total_days)*100
    return int(res) if res <= 100 else 100
