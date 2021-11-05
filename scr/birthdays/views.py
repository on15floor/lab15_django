from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.http import Http404

from .forms import BirthdayForm
from datetime import datetime
from .models import Birthday


class BirthdaysView(View):
    """Главная - дни рожденья"""
    template = 'birthdays/index.html'

    def get(self, request, condition, *args, **kwargs):
        # Поиск
        query = self.request.GET.get('q')
        if query:
            birthdays = Birthday.objects.filter(Q(name__icontains=query) | Q(comment__icontains=query))
        # Фильтры
        else:
            if condition == 'all':
                birthdays = Birthday.objects.all()
            elif condition == 'month':
                birthdays = Birthday.objects.filter(birthdate__month=datetime.now().month)
            elif condition == 'w':
                birthdays = Birthday.objects.filter(male=False)
            elif condition == 'm':
                birthdays = Birthday.objects.filter(male=True)
            else:
                raise Http404()

        return render(request, self.template, context={'birthdays': birthdays})


class BirthdayDetailsView(View):
    """Страница создания (редактирования) поста"""
    template = 'birthdays/bd_details.html'

    def get(self, request, *args, **kwargs):
        form = BirthdayForm(instance=Birthday.objects.get(pk=kwargs['bd_id'])) if 'bd_id' in kwargs else BirthdayForm()
        return render(request, self.template, context={'form': form})

    def post(self, request, *args, **kwargs):
        if 'bd_id' in kwargs:
            form = BirthdayForm(request.POST, instance=Birthday.objects.get(pk=kwargs['bd_id']))
        else:
            form = BirthdayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('birthdays', condition='month')
        return render(request, self.template, context={'form': form})


class BirthdayDelete(View):
    """Удаление дня рожденья"""
    @staticmethod
    def get(request, bd_id, *args, **kwargs):
        birthday = Birthday.objects.get(pk=bd_id)
        birthday.delete()
        return redirect('birthdays', condition='month')
