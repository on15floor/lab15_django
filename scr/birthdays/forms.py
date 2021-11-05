from django.forms import ModelForm, TextInput, CheckboxInput, DateInput

from .models import Birthday


class BirthdayForm(ModelForm):

    class Meta:
        model = Birthday
        fields = ['name', 'male', 'birthdate', 'birthdate_checked', 'comment']
        widgets = {
            'name': TextInput(
                attrs={
                    'id': 'name',
                    'class': 'form-control',
                    'placeholder': 'ФИО',
                    'rows': 1,
                }),
            'male': CheckboxInput(
                attrs={
                    'id': 'male',
                    'value': 'male',
                }),
            'birthdate': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Дата рожденья',
                    'id': 'birthdate',
                    'type': 'date',
                    'class': 'form-control datetimepicker-input',
                }),
            'birthdate_checked': CheckboxInput(
                attrs={
                    'id': 'birthdate_checked',
                    'value': 'birthdate_checked',
                }),
            'comment': TextInput(
                attrs={
                    'id': 'comment',
                    'class': 'form-control',
                    'placeholder': 'Примечание',
                    'rows': 1,
                }),
        }
