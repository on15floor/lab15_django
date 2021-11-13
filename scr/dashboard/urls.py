from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import GitLogView, MongoLogView, CronTabView, CronTabTaskDel, CronTabTaskStart, CronTabTaskStop

urlpatterns = [
    path('dashboard/gitlog/', login_required(GitLogView.as_view()), name='dashboard_gitlog'),
    path('dashboard/mongo_log/<state>', login_required(MongoLogView.as_view()), name='dashboard_mongolog'),
    path('dashboard/crontab/', login_required(CronTabView.as_view()), name='dashboard_crontab'),
    path('dashboard/crontab/<task_id>/del', login_required(CronTabTaskDel.as_view()), name='dashboard_crontab_del'),
    path('dashboard/crontab/<task_id>/start', login_required(CronTabTaskStart.as_view()), name='dashboard_crontab_start'),
    path('dashboard/crontab/<task_id>/stop', login_required(CronTabTaskStop.as_view()), name='dashboard_crontab_stop'),
]
