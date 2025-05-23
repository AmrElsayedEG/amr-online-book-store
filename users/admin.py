from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'phone', 'user_type', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        ('Personal info', {'fields': ('phone',)}),
        ('Permissions', {'fields': ('is_active', 'user_type', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
    )

admin.site.register(User, CustomUserAdmin)