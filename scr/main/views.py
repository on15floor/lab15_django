from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View
from .models import NoSmokingStages

from .services.hints_view import get_markdown
from .services.no_smoking_view import build_collection
from .services.ping_view import get_client_ip


class MainView(View):
    """Главная страница сайта"""
    def get(self, request, *args, **kwargs):
        return render(request, 'main/index.html')


class PingView(View):
    """Ping (возвращает IP)"""
    def get(self, request, *args, **kwargs):
        return HttpResponse(f'Requester IP: {get_client_ip(request)}<br>'
                            f'User-agent: {request.headers["User-Agent"]}')


class NoSmokingView(View):
    """Страница No Smoking"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.no_smoking_db = NoSmokingStages.objects.order_by('id')

    def get(self, request, *args, **kwargs):
        return render(request, 'main/no_smoking.html',
                      context={'data_out': build_collection('2008-02-01', '2021-08-30', 50, 150),
                               'no_smoking_db': self.no_smoking_db})

    def post(self, request, *args, **kwargs):
        time_start = request.POST.get('in_start_day', '')
        time_stop = request.POST.get('in_stop_day', '')
        price_start = int(request.POST.get('in_price_start', ''))
        price_stop = int(request.POST.get('in_price_stop', ''))
        return render(request, 'main/no_smoking.html',
                      context={'data_out': build_collection(time_start, time_stop, price_start, price_stop),
                               'no_smoking_db': self.no_smoking_db})


class HintsView(View):
    """Страница Hints"""
    def get(self, request, doc, *args, **kwargs):
        docs = ['git', 'markdown', 'python', 'sql', 'bash', 't', 'vim']
        if doc in docs:
            return render(request, 'main/docs.html', context={'md_to_html_content': get_markdown(doc)})
        else:
            raise Http404()


class UnityView(View):
    """Страница Unity"""
    def get(self, request, game, *args, **kwargs):
        games = ['simple_cube', 'delimiter', 'kot_guide']
        if game in games:
            return render(request, f'main/unity/{game}.html')
        else:
            raise Http404()


class UnityPPView(View):
    """Страница Unity Privacy Policy"""
    def get(self, request, game, *args, **kwargs):
        games = ['simple_cube', 'delimiter', 'kot_guide']
        if game in games:
            game_name = game.replace('_', ' ').title()
            return render(request, f'main/unity/privacy_policy.html', context={'game': game_name})
        else:
            raise Http404()


class Handler404(View):
    """404 Ошибка. TODO: Реализация логирования в MongoDB"""
    def get(self, request, *args, **kwargs):
        return render(request, '404.html', status=404)


class Handler500(View):
    """500 Ошибка. TODO: Реализация логирования в MongoDB"""
    def get(self, request, *args, **kwargs):
        return render(request, '500.html', status=500)
