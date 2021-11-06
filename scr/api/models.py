from django.db import models
from django.utils.timezone import now


class Beget(models.Model):
    """ Модель новостей beget.ru """
    objects = models.Manager()

    news = models.TextField('Новость')
    date = models.DateTimeField('Дата создания', default=now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.news
