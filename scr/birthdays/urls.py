from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import BirthdaysView, BirthdayDetailsView, BirthdayDelete

urlpatterns = [
    path('birthdays/add/', login_required(BirthdayDetailsView.as_view()), name='birthday_add'),
    path('birthdays/<condition>/', login_required(BirthdaysView.as_view()), name='birthdays'),
    path('birthdays/<bd_id>/update', login_required(BirthdayDetailsView.as_view()), name='birthday_update'),
    path('birthdays/<bd_id>/del', login_required(BirthdayDelete.as_view()), name='birthday_delete'),
]
