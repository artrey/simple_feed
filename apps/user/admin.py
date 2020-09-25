from django.contrib import admin
from django.contrib.auth import models as auth_models
from django.contrib.auth import admin as auth_admin

from . import models


@admin.register(models.User)
class UserAdmin(auth_admin.UserAdmin):
    pass


admin.site.unregister(auth_models.Group)
