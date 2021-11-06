from django.contrib import admin

from .models import Beget, Apptime


@admin.register(Beget)
class BegetAdmin(admin.ModelAdmin):
    model = Beget
    list_display = ('id', 'news', 'date')
    search_fields = ('news', )


@admin.register(Apptime)
class ApptimeAdmin(admin.ModelAdmin):
    model = Apptime
    list_display = ('id', 'game_name', 'price_old', 'price_new', 'sale_percent', 'date')
    search_fields = ('game_name', )
