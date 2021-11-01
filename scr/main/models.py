from django.db import models


class NoSmokingStages(models.Model):
    """ Модель стадий бросания курения """
    objects = models.Manager()

    name = models.CharField('Имя стадии', max_length=100)
    time = models.FloatField('Время (д)')
    time_descr = models.CharField('Описание времени', max_length=100)
    text = models.TextField('Описание стадии')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
