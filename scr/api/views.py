from datetime import datetime

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.views import View

from birthdays.models import Birthday
from .services.telegram import TBot


class BaseMixin:
    def __init__(self):
        self.token = ''
        self.res = {}
        self.uri = ''
        self.status = 'success'

    def check_token(self, request):
        if 'token' in request.GET:
            self.token = request.GET['token']
            self.uri = request.path
            if self.token == settings.API_QUERY_TOKEN:
                return
        self.status = 'error'
        self.save_log_to_mongodb({'permission_denied': 'wrong token'})
        raise PermissionDenied

    def save_log_to_mongodb(self, res):
        log = {
            'status': self.status,
            'token': self.token,
            'uri': self.uri
        }
        self.res = {**log, **res}
        print(self.res)
        return self.res


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
