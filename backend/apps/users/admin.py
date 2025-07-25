from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_active', 'is_premium_subscribed')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'is_premium_subscribed')
    fieldsets = UserAdmin.fieldsets + (
        ('Subscription', {'fields': ('is_premium_subscribed',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Subscription', {'fields': ('is_premium_subscribed',)}),
    )
