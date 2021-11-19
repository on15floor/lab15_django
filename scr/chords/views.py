from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from .forms import SongForm
from .models import Song


class ChordsInstrumentView(View):
    """Главная песенника для инструмента"""
    template = 'chords/chords.html'

    def get(self, request, instrument, *args, **kwargs):
        # Поиск
        query = self.request.GET.get('q')
        if query:
            songs = Song.objects.filter(Q(song_name__icontains=query) | Q(song_name__icontains=query))
        # Вывод всех песен
        else:
            songs = Song.objects.filter(instrument=instrument)
        instrument = 'Гитара' if instrument == 'guitar' else 'Укулеле'
        return render(request, self.template, context={'songs': songs, 'instrument': instrument})


class SongView(View):
    """Страница песни"""
    template = 'chords/song.html'

    def get(self, request, song_id, *args, **kwargs):
        return render(request, self.template, context={'song': Song.objects.get(pk=song_id)})


class SongDetailsView(View):
    """Страница создания (редактирования) песни"""
    template = 'chords/song_details.html'

    def get(self, request, *args, **kwargs):
        form = SongForm(instance=Song.objects.get(pk=kwargs['song_id'])) if 'song_id' in kwargs else SongForm()
        return render(request, self.template, context={'form': form})

    def post(self, request, *args, **kwargs):
        if 'song_id' in kwargs:
            form = SongForm(request.POST, instance=Song.objects.get(pk=kwargs['song_id']))
        else:
            form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            return redirect('chords', song.instrument)
        return render(request, self.template, context={'form': form})


class SongDelete(View):
    """Удаление песни"""
    @staticmethod
    def get(request, song_id, *args, **kwargs):
        song = Song.objects.get(pk=song_id)
        instrument = song.instrument
        song.delete()
        return redirect('chords', instrument)
