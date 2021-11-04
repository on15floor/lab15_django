from django.db import models
from datetime import datetime


class Birthday(models.Model):
    """ Модель дня рождения """
    objects = models.Manager()

    name = models.CharField('Имя', max_length=100)
    male = models.BooleanField('Пол')
    birthdate = models.DateField('Дата рождения')
    birthdate_checked = models.BooleanField('ДР проверено')
    comment = models.TextField('Комментарий')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def age(self):
        return int((datetime.now().date() - self.birthdate).days / 365.25)
