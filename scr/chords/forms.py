from django.forms import ModelForm, TextInput, Textarea, RadioSelect, Select
from .models import Song


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['instrument', 'song_name', 'song_text']
        widgets = {
            'instrument': Select(
                choices=[
                    ('guitar', 'Гитара'),
                    ('ukulele', 'Укулеле')],
                attrs={
                    'id': 'instrument',
                    'class': 'form-control',
                }
            ),
            'song_name': TextInput(attrs={
                'id': 'song_name',
                'class': 'form-control',
                'placeholder': 'Введите название песни',
                'rows': 1,
            }),
            'song_text': Textarea(attrs={
                'id': 'song_text',
                'class': 'form-control, text-monospace',
                'placeholder': 'Введите текст песни',
                'rows': 10,
                'style': "width:100%;"
            })
        }
