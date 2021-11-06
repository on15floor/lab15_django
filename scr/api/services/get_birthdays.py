from datetime import datetime
from birthdays.models import Birthday


def get_birthdays_today() -> str:
    """Функция формирует готовое сообщение из именинников для отправки в телеграм"""
    telegram_mess = ''
    birthdays_db = Birthday.objects.filter(birthdate__month=datetime.now().month, birthdate__day=datetime.now().day)
    for lucky in birthdays_db:
        male = '🚹' if lucky.male == 1 else '🚺'
        birthdate_checked = '✅' if lucky.birthdate_checked == 1 else '❌'
        telegram_mess += f'{male}{birthdate_checked}{lucky.name} [{lucky.age} лет]\n'
    return telegram_mess
