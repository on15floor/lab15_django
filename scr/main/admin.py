from django.contrib import admin
from .models import NoSmokingStages


@admin.register(NoSmokingStages)
class PostAdmin(admin.ModelAdmin):
    model = NoSmokingStages
    list_display = (
        'name',
        'text',
        'time',
        'time_descr'
    )
