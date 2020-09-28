from django.contrib import admin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'author', 'body', 'created_at', 'parent',
    list_filter = 'author', 'parent',
    search_fields = 'author__first_name', 'author__last_name', 'body',
    readonly_fields = 'created_at',
