from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.http import Http404

# from .forms import PostForm
from datetime import datetime
from .models import Birthday


class BirthdaysView(View):
    """Главная - дни рожденья"""
    template = 'birthdays/index.html'

    def get(self, request, filter, *args, **kwargs):
        # Поиск
        query = self.request.GET.get('q')
        if query:
            birthdays = Birthday.objects.filter(Q(name__icontains=query) | Q(comment__icontains=query))
        # Фильтры
        else:
            if filter == 'all':
                birthdays = Birthday.objects.all()
            elif filter == 'month':
                birthdays = Birthday.objects.filter(birthdate__month=datetime.now().month)
            elif filter == 'w':
                birthdays = Birthday.objects.filter(male=False)
            elif filter == 'm':
                birthdays = Birthday.objects.filter(male=True)
            else:
                raise Http404()

        return render(request, self.template, context={'birthdays': birthdays})
