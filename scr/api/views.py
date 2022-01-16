from django.http import JsonResponse
from django.views import View

from .services.delimiter import Delimiter
from .services.get_apptime_sales import get_apptime_sales
from .services.get_beget_news import get_beget_news
from .services.get_birthdays import get_birthdays_today
from .services.mixins import BaseMixin
from .services.telegram import TBot
from django.conf import settings


class GetBirthdays(BaseMixin, View):
    """ Отправка информации о сегодняшних именниках """
    def get(self, request, *args, **kwargs):
        self.check_token(request)
        telegram_mess = get_birthdays_today()
        if telegram_mess:
            TBot().send_message(message=f'🎂Сегодня свои дни рождения празднуют:\n {telegram_mess}')
        telegram_mess_count = telegram_mess.count('\n')
        res = self.save_log_to_mongodb(message=f'Lucky ones today: {telegram_mess_count}')
        return JsonResponse(res)


class GetBegetNews(BaseMixin, View):
    """ Проверка новостей beget.ru и отправка новых """
    def get(self, request, *args, **kwargs):
        self.check_token(request)
        telegram_mess = get_beget_news()
        if telegram_mess:
            TBot().send_message(message=f'ℹ️Beget news:\n {telegram_mess}')
        telegram_mess_count = telegram_mess.count('\n')
        res = self.save_log_to_mongodb(message=f'Beget fresh news: {telegram_mess_count}')
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
        res = self.save_log_to_mongodb(message=f'Apptime fresh sales: {len(games)}')
        return JsonResponse(res)


class DelimiterScore(BaseMixin, View):
    """ Получение и сохранения рекордов игры Delimiter """
    def get(self, request, *args, **kwargs):
        self.check_token(request, token=settings.API_DELIMITER_TOKEN)
        return JsonResponse(Delimiter().get_best_scores(13))

    def post(self, request, *args, **kwargs):
        self.check_token(request, token=settings.API_DELIMITER_TOKEN)
        in_data = {'user_id': request.POST.get('user_id', ''),
                   'user_name': request.POST.get('user_name', ''),
                   'best_score': int(request.POST.get('best_score', ''))}
        Delimiter().save_records(in_data)
        return JsonResponse({'Satus': 'ok'})
