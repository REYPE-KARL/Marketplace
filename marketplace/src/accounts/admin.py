from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name', 'first_name', 'last_name',)
    list_filter = ('email', 'user_name', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser',)
    ordering = ('user_name',)

    list_display = ('email', 'user_name', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'slug', 'first_name', 'last_name', 'password',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'password1', 'password2',
                       'is_active', 'is_staff', 'is_superuser',)}
         ),
    )


admin.site.register(CustomUser, UserAdminConfig)
