from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'phone', 'email']
    list_display_links = ['username']
    list_editable = ['first_name', 'last_name']
    search_fields = ('username', 'first_name', 'last_name', 'phone', 'email')

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        ('Custom fields', {'fields': ('first_name', 'last_name', 'phone', 'email', )})
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        ('Custom fields', {'fields': ('phone', )})
    )
