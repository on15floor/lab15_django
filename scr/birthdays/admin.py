from django.contrib import admin

from .models import Birthday


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    model = Birthday
    list_display = ('name', 'male', 'birthdate', 'birthdate_checked', 'comment')
    search_fields = ('name', 'comment')

