from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['email','username', 'rut', 'first_name', 'last_name', 'cellphone','is_admin','date_of_birth']
    fieldsets = (
        (None, {'fields': ('email','rut','first_name', 'last_name','cellphone')}),
    )
    