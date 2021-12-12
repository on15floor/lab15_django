from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (MainView, PingView, Handler404, Handler500, HintsView, UnityView, UnityPPView, NoSmokingView,
                    SignInView, ConvertorView)

urlpatterns = [
    # Основные
    path('', MainView.as_view(), name='index'),
    path('ping/', PingView.as_view(), name='ping'),
    path('signin/', SignInView.as_view(), name='sign_in'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='sign_out'),
    # Статические страницы
    path('no_smoking/', NoSmokingView.as_view(), name='no_smoking'),
    path('converter/', ConvertorView.as_view(), name='converter'),
    path('hints/<doc>/', HintsView.as_view(), name='hints'),
    path('unity/<game>/', UnityView.as_view(), name='unity'),
    path('unity/privacy_policy/<game>/', UnityPPView.as_view(), name='unity_pp'),
    # Обработка ошибок
    path('404/', Handler404.as_view(), name='404'),
    path('500/', Handler500.as_view(), name='500')
]
