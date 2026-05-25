from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'username', 'role', 'is_staff']
    list_filter  = ['role']
    fieldsets    = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('role', 'phone', 'nationality', 'passport_no', 'avatar')}),
    )