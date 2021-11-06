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


class Apptime(models.Model):
    """ Модель скидок app-time.ru """
    objects = models.Manager()

    game_name = models.TextField('Название игры')
    price_old = models.CharField('Старая цена', max_length=10)
    price_new = models.CharField('Новая цена', max_length=10)
    sale_percent = models.CharField('Скидка', max_length=10)
    cover = models.TextField('Cover')
    app_link = models.TextField('AppStore')
    date = models.DateTimeField('Дата создания', default=now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.game_name
