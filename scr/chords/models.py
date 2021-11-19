from django.db import models
from django.utils.timezone import now

chords = {'A', 'A7', 'Am', 'Am7', 'Adim', 'Aaug', 'A6', 'Amaj7', 'A9',
          'Ab', 'Ab7', 'Abm', 'Abm7', 'Abdim', 'Abaug', 'Ab6', 'Abmaj7', 'Ab9',
          'B', 'B7', 'Bm', 'Bm7', 'Bdim', 'Baug', 'B6', 'Bmaj7', 'B9',
          'Bb', 'Bb7', 'Bbm', 'Bbm7', 'Bbdim', 'Bbaug', 'Bb6', 'Bbmaj7', 'Bb9',
          'C', 'C7', 'Cm', 'Cm7', 'Cdim', 'Caug', 'C6', 'Cmaj7', 'A9',
          'D', 'D7', 'Dm', 'Dm7', 'Ddim', 'Daug', 'D6', 'Dmaj7', 'D9',
          'Db', 'Db7', 'Dbm', 'Dbm7', 'Dbdim', 'Dbaug', 'Db6', 'Dbmaj7', 'Db9',
          'E', 'E7', 'Em', 'Em7', 'Edim', 'Eaug', 'E6', 'Emaj7', 'E9',
          'Eb', 'Eb7', 'Ebm', 'Ebm7', 'Ebdim', 'Ebaug', 'Eb6', 'Ebmaj7', 'Eb9',
          'F', 'F7', 'Fm', 'Fm7', 'Fdim', 'Faug', 'F6', 'Fmaj7', 'F9',
          'G', 'G7', 'Gm', 'Gm7', 'Gdim', 'Gaug', 'G6', 'Gmaj7', 'G9',
          'Gb', 'Gb7', 'Gbm', 'Gbm7', 'Gbdim', 'Gbaug', 'Gb6', 'Gbmaj7', 'Gb9'}


class Song(models.Model):
    """ Модель песни """
    objects = models.Manager()

    instrument = models.CharField('Инструмент', max_length=100)
    song_name = models.CharField('Песня', max_length=100)
    song_text = models.TextField('Текст песни')
    date = models.DateTimeField('Дата создания', default=now)

    class Meta:
        ordering = ['song_name']

    def __str__(self):
        return f'[{self.instrument}] {self.song_name}'

    @property
    def get_song_chords_set(self) -> set:
        return set(self.song_text.split()) & chords

    @property
    def get_song_chords_str(self):
        return ", ".join(map(str, self.get_song_chords_set))
