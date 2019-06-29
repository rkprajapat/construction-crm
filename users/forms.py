from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Role
from django.contrib.auth.admin import UserAdmin
from django.db.models.query import QuerySet


class CustomUserCreationForm(UserCreationForm):
    roles = forms.ModelMultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        queryset=Role.objects.all()
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username')


class CustomUserChangeForm(UserChangeForm):
    roles = forms.ModelMultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        queryset=Role.objects.all()
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'username')