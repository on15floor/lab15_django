from django.forms import ModelForm, TextInput, Textarea
from .models import Song


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['instrument', 'song_name', 'song_text']
        widgets = {
            'instrument': TextInput(attrs={
                'id': 'instrument',
                'class': 'form-control',
                'placeholder': 'Введите название инструмента',
                'rows': 1,
            }),
            'song_name': TextInput(attrs={
                'id': 'song_name',
                'class': 'form-control',
                'placeholder': 'Введите название песни',
                'rows': 1,
            }),
            'text': Textarea(attrs={
                'id': 'text',
                'class': 'form-control',
                'placeholder': 'Введите текст песни',
                'rows': 20,
            })
        }
