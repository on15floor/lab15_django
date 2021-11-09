from django.shortcuts import render
from django.views import View
import subprocess
from django.conf import settings


class GitLogView(View):
    """Страница GitLog"""
    template = 'dashboard/index.html'

    def get(self, request, *args, **kwargs):
        format = '--format=format:<span class="git-version">%h</span>-' \
                 '<span class="git-time">(%ar)</span> %s - <span class="git-author"><b>%an</b></span>' \
                 '<span class="badge bg-warning text-dark">%d</span>'
        command = [
            'git',
            'log',
            '--graph',
            '--all',  # Все ветки
            format,
            '--abbrev-commit',  # Сокращенный номер коммита
            '--date=relative',
            '--since=6 month ago',  # Коммиты за последние 6 месяцев
        ]
        result = subprocess.run(command, cwd=settings.BASE_DIR, stdout=subprocess.PIPE)
        git_log = result.stdout.decode("utf-8")
        git_log = git_log.replace('\n', '<br />')
        return render(request, self.template, context={'git_log': git_log})
