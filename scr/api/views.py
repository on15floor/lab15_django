from datetime import datetime

from django.http import JsonResponse
from django.views import View

from birthdays.models import Birthday
from .services.mixins import BaseMixin
from .services.telegram import TBot


class GetBirthdays(BaseMixin, View):
    """ Отправка информации о сегодняшних именниках """
    def get(self, request, *args, **kwargs):
        self.check_token(request)
        telegram_mess = ''
        birthdays_db = Birthday.objects.filter(birthdate__month=datetime.now().month, birthdate__day=datetime.now().day)
        for lucky in birthdays_db:
            male = '🚹' if lucky.male == 1 else '🚺'
            birthdate_checked = '✅' if lucky.birthdate_checked == 1 else '❌'
            telegram_mess += f'{male}{birthdate_checked}{lucky.name} [{lucky.age} лет]\n'
        if telegram_mess:
            TBot().send_message(message=f'Сегодня свои дни рождения празднуют:\n {telegram_mess}')

        res = self.save_log_to_mongodb({'lucky_ones_today': len(birthdays_db)})
        return JsonResponse(res)
