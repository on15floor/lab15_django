from django.contrib.auth import login, authenticate
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import SignInForm
from .models import NoSmokingStages
from .services.hints_view import get_markdown
from .services.no_smoking_view import build_collection
from .services.ping_view import get_client_ip


class MainView(View):
    """Главная страница сайта"""
    template = 'main/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template)


class PingView(View):
    """Ping (возвращает IP)"""
    @staticmethod
    def get(request, *args, **kwargs):
        return HttpResponse(f'Requester IP: {get_client_ip(request)}<br>'
                            f'User-agent: {request.headers["User-Agent"]}')


class SignInView(View):
    template = 'main/signin.html'

    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, self.template, context={'form': form})

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, self.template, context={'form': form})


class NoSmokingView(View):
    """Страница No Smoking"""
    template = 'main/no_smoking.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.no_smoking_db = NoSmokingStages.objects.order_by('id')

    def get(self, request, *args, **kwargs):
        return render(request, self.template, context={
            'data_out': build_collection('2008-02-01', '2021-08-30', 50, 150),
            'no_smoking_db': self.no_smoking_db})

    def post(self, request, *args, **kwargs):
        time_start = request.POST.get('in_start_day', '')
        time_stop = request.POST.get('in_stop_day', '')
        price_start = int(request.POST.get('in_price_start', ''))
        price_stop = int(request.POST.get('in_price_stop', ''))
        return render(request, self.template, context={
            'data_out': build_collection(time_start, time_stop, price_start, price_stop),
            'no_smoking_db': self.no_smoking_db})


class ConvertorView(View):
    """Страница конвертора валют"""
    def get(self, request, *args, **kwargs):
        return render(request, 'main/converter.html')


class HintsView(View):
    """Страница Hints"""
    template = 'main/docs.html'

    def get(self, request, doc, *args, **kwargs):
        docs = ['git', 'markdown', 'python', 'sql', 'bash', 't', 'vim']
        if doc in docs:
            return render(request, self.template, context={'md_to_html_content': get_markdown(doc)})
        else:
            raise Http404()


class UnityView(View):
    """Страница Unity"""
    @staticmethod
    def get(request, game, *args, **kwargs):
        games = ['simple_cube', 'delimiter', 'kot_guide']
        if game in games:
            return render(request, f'main/unity/{game}.html')
        else:
            raise Http404()


class UnityPPView(View):
    """Страница Unity Privacy Policy"""
    template = 'main/unity/privacy_policy.html'

    def get(self, request, game, *args, **kwargs):
        games = ['simple_cube', 'delimiter', 'kot_guide']
        if game in games:
            game_name = game.replace('_', ' ').title()
            return render(request, self.template, context={'game': game_name})
        else:
            raise Http404()


class Handler404(View):
    """404 Ошибка"""
    def get(self, request, *args, **kwargs):
        return render(request, '404.html', status=404)


class Handler500(View):
    """500 Ошибка"""
    def get(self, request, *args, **kwargs):
        return render(request, '500.html', status=500)
