from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import GitLogView, MongoLogView

urlpatterns = [
    path('dashboard/gitlog/', login_required(GitLogView.as_view()), name='dashboard_gitlog'),
    path('dashboard/mongo_log/<state>', login_required(MongoLogView.as_view()), name='dashboard_mongolog'),
]
