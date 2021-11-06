from django.http import JsonResponse
from django.views import View

from .services.get_beget_news import get_beget_news
from .services.get_birthdays import get_birthdays_today
from .services.get_apptime_sales import get_apptime_sales
from .services.mixins import BaseMixin
from .services.telegram import TBot


class GetBirthdays(BaseMixin, View):
    """ Отправка информации о сегодняшних именниках """
    def get(self, request, *args, **kwargs):
        self.check_token(request)
        telegram_mess = get_birthdays_today()
        if telegram_mess:
            TBot().send_message(message=f'🎂Сегодня свои дни рождения празднуют:\n {telegram_mess}')
        res = self.save_log_to_mongodb({'lucky_ones_today': telegram_mess.count('\n')})
        return JsonResponse(res)


class GetBegetNews(BaseMixin, View):
    """ Проверка новостей beget.ru и отправка новых """
    def get(self, request, *args, **kwargs):
        self.check_token(request)
        telegram_mess = get_beget_news()
        if telegram_mess:
            TBot().send_message(message=f'ℹ️Beget news:\n {telegram_mess}')
        res = self.save_log_to_mongodb({'beget_fresh_news': telegram_mess.count('\n')})
        return JsonResponse(res)


class GetApptimeSales(BaseMixin, View):
    """ Проверка скидок на app-time.ru и отправка новых """
    def get(self, request, *args, **kwargs):
        self.check_token(request)
        games = get_apptime_sales()
        if games:
            for game in games:
                TBot().send_caption(chat_id=-1001560904244,
                                    message=game['massage'],
                                    photo_link=game['cover'],
                                    parse_mode='HTML')
        res = self.save_log_to_mongodb({'apptime_fresh_sales': len(games)})
        return JsonResponse(res)
