from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import GitLogView

urlpatterns = [
    path('dashboard/gitlog/', login_required(GitLogView.as_view()), name='dashboard_gitlog'),
]
