from django.urls import path

from .views import MainView, PingView, Handler404, Handler500, HintsView, UnityView, UnityPPView, NoSmokingView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('ping/', PingView.as_view(), name='ping'),
    path('no_smoking/', NoSmokingView.as_view(), name='no_smoking'),
    path('hints/<doc>/', HintsView.as_view(), name='get_docs'),
    path('unity/<game>/', UnityView.as_view(), name='unity'),
    path('unity/privacy_policy/<game>/', UnityPPView.as_view(), name='unity_pp'),
    # Обработка ошибок
    path('404/', Handler404.as_view(), name='404'),
    path('500/', Handler500.as_view(), name='500')
]
