from django.urls import path

from .views import GetBirthdays, GetBegetNews, GetApptimeSales, DelimiterScore

urlpatterns = [
    path('api/v1.0/get_birthdays', GetBirthdays.as_view(), name='api_get_birthdays'),
    path('api/v1.0/get_beget_news', GetBegetNews.as_view(), name='api_get_beget_news'),
    path('api/v1.0/get_ios_sale', GetApptimeSales.as_view(), name='api_get_apptime_sale'),

    path('api/v1.0/delimiter', DelimiterScore.as_view(), name='api_get_apptime_sale'),
]
