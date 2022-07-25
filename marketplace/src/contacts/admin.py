from django.contrib import admin

# Register your models here.
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email',)
    list_display = ('name', 'email')
    list_filter = ('name', 'email',)
    ordering = ('name',)


admin.site.register(Contact, ContactAdmin)
