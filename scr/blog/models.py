from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    """ Модель поста """
    objects = models.Manager()

    icon = models.TextField('Icon base64')
    title = models.CharField('Заголовок', max_length=100)
    intro = models.CharField('Интро', max_length=300)
    text = models.TextField('Пост')
    date = models.DateTimeField('Дата создания', default=now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
