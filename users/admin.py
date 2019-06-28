from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Role

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    search_fields = ('email',)
    ordering = ('email',)
    list_display = ['email', 'username', 'primary_phone_number']
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2', 'roles')}
        ),
        ('Personal Info', {'fields': ('full_name', 'address', 'primary_phone_number', 'secondary_phone_number')}),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'roles')}),
        ('Personal Info', {'fields': ('full_name', 'address', 'primary_phone_number', 'secondary_phone_number')}),
        ('Permissions', {'fields': ('is_active',)}),
    )

class RoleAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.unregister(Group)