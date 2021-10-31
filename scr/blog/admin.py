from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = (
        'id',
        'date',
        'title',
        'intro'
    )
    search_fields = (
        'title',
        'intro',
        'text',
    )
