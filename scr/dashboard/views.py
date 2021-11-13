from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View

from .services.get_gitlog import get_gitlog
from .services.mongo import MongoDB
from .services.beget_crontab import Crontab


class GitLogView(View):
    """Страница GitLog"""
    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'dashboard/gitlog.html', context={'git_log': get_gitlog()})


class MongoLogView(View):
    """Страница MongoDBLog"""
    template = 'dashboard/mongologs.html'
    mongo = MongoDB()

    def get(self, request, state, *args, **kwargs):
        if state == 'all':
            logs = self.mongo.get_logs_all()
        elif state == 'errors':
            logs = self.mongo.get_logs_errors()
        else:
            raise Http404()
        return render(request, self.template, context={'logs': list(logs)})


class CronTabView(View):
    """Страница CronTab"""
    template = 'dashboard/crontab.html'
    crontab = Crontab()

    def get(self, request, *args, **kwargs):
        return render(request, self.template, context={'crontab_tasks': self.crontab.tasks_get()})


class CronTabTaskDel(View):
    """Удалить задачу CronTab"""
    @staticmethod
    def get(request, task_id, *args, **kwargs):
        Crontab().task_del(task_id)
        return redirect('dashboard_crontab')


class CronTabTaskStart(View):
    """Запустить задачу CronTab"""
    @staticmethod
    def get(request, task_id, *args, **kwargs):
        Crontab().task_change_state(task_id, 0)
        return redirect('dashboard_crontab')


class CronTabTaskStop(View):
    """Остановить задачу CronTab"""
    @staticmethod
    def get(request, task_id, *args, **kwargs):
        Crontab().task_change_state(task_id, 1)
        return redirect('dashboard_crontab')
