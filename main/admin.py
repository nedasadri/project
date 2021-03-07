from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class MyUserAdmin(UserAdmin):
    list_display = ('username', 'teacher')
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('username', 'password', 'teacher', 'code')}),)

    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(models.MyUser, MyUserAdmin)
