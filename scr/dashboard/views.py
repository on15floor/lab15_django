from django.http import Http404
from django.shortcuts import render
from django.views import View

from .services.get_gitlog import get_gitlog
from .services.mongo import MongoDB


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
