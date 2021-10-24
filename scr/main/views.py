from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View
from .services.ping_view import get_client_ip
from .services.hints_view import get_markdown


class MainView(View):
    """Главная страница сайта"""
    def get(self, request, *args, **kwargs):
        return render(request, 'main/index.html')


class PingView(View):
    """Ping (возвращает IP)"""
    def get(self, request, *args, **kwargs):
        return HttpResponse(f'Requester IP: {get_client_ip(request)}<br>'
                            f'User-agent: {request.headers["User-Agent"]}')


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
