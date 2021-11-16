from django.db import models
from django.utils.timezone import now


class Song(models.Model):
    """ Модель песни """
    objects = models.Manager()

    instrument = models.TextField('Инструмент', max_length=100)
    song_name = models.TextField('Песня', max_length=100)
    song_text = models.TextField('Текст песни')
    date = models.DateTimeField('Дата создания', default=now)

    class Meta:
        ordering = ['song_name']

    def __str__(self):
        return f'[{self.instrument}] {self.song_name}'
