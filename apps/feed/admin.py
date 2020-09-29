from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


@admin.register(models.Post)
class PostAdmin(MPTTModelAdmin):
    mptt_level_indent = 16  # in pixels
    mptt_indent_field = 'body'

    list_display = 'author', 'body', 'created_at',
    list_filter = 'author',
    search_fields = 'author__first_name', 'author__last_name', 'body',
    readonly_fields = 'created_at',
