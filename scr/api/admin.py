from django.contrib import admin

from .models import Beget


@admin.register(Beget)
class PostAdmin(admin.ModelAdmin):
    model = Beget
    list_display = ('id', 'news', 'date')
    search_fields = ('news', )
