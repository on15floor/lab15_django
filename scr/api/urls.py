from django.urls import path

from .views import GetBirthdays, GetBegetNews

urlpatterns = [
    path('api/v1.0/get_birthdays', GetBirthdays.as_view(), name='api_get_birthdays'),
    path('api/v1.0/get_beget_news', GetBegetNews.as_view(), name='api_get_begetnews'),
    # path('api/v1.0/get_ios_sale/', PostView.as_view(), name='post'),
]
