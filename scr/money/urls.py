from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import StocksView, CryptoView

urlpatterns = [
    path('stocks/', login_required(StocksView.as_view()), name='stocks'),
    path('crypto/', login_required(CryptoView.as_view()), name='crypto'),
]
