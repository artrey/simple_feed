from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin

from . import models


@admin.register(models.Post)
class PostAdmin(MPTTModelAdmin):
    mptt_level_indent = 20  # in pixels
    mptt_indent_field = 'author'

    list_display = 'author', 'html_body', 'created_at',
    list_filter = 'author',
    search_fields = 'author__first_name', 'author__last_name', 'body',
    readonly_fields = 'created_at',

    def html_body(self, obj: models.Post) -> str:
        return mark_safe(obj.body.replace('<img', '<img style="max-width: 200px"'))
    html_body.short_description = 'содержимое поста'
