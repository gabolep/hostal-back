from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'rut', 'first_name', 'last_name', 'cellphone','is_admin']
    fieldsets = (
        (None, {'fields': ('email','rut','first_name', 'last_name','cellphone')}),
    )
    