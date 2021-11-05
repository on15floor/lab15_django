from django.urls import path

from .views import GetBirthdays

urlpatterns = [
    path('api/v1.0/get_birthdays', GetBirthdays.as_view(), name='api_get_birthdays'),
    # path('api/v1.0/get_beget_news/', login_required(PostDetailsView.as_view()), name='post_create'),
    # path('api/v1.0/get_ios_sale/', PostView.as_view(), name='post'),
]
