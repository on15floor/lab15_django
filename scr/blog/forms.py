from django.forms import ModelForm, TextInput, Textarea
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['icon', 'title', 'intro', 'text']
        widgets = {
            'title': TextInput(attrs={
                'id': 'title',
                'class': 'form-control',
                'placeholder': 'Введите название',
                'rows': 1,
            }),
            'intro': Textarea(attrs={
                'id': 'intro',
                'class': 'form-control',
                'placeholder': 'Введите анонс',
                'rows': 2,
            }),
            'text': Textarea(attrs={
                'id': 'text',
                'class': 'form-control',
                'placeholder': 'Введите основной текст',
                'rows': 10,
            }),
            'icon': Textarea(attrs={
                'id': 'icon',
                'class': 'form-control',
                'placeholder': 'Ссылка на иконку',
                'rows': 2,
            })
        }
