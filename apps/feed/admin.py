from django.contrib import admin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'author', 'text', 'created_at',
    list_filter = 'author',
    search_fields = 'author', 'text',
    readonly_fields = 'created_at',
