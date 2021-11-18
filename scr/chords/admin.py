from django.contrib import admin

from .models import Song


@admin.register(Song)
class PostAdmin(admin.ModelAdmin):
    model = Song
    list_display = ('instrument', 'song_name', 'date', 'id')
    search_fields = ('instrument', 'song_name', 'song_text')
