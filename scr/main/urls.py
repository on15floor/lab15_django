from django.urls import path
from .views import MainView, PingView, Handler404, Handler500, HintsView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('ping/', PingView.as_view(), name='ping'),
    path('docs/<doc>/', HintsView.as_view(), name='get_docs'),
    # Обработка ошибок
    path('404/', Handler404.as_view(), name='404'),
    path('500/', Handler500.as_view(), name='500')
]
