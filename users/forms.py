from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.db.models.query import QuerySet
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible
from allauth.account.forms import LoginForm

from .models import CustomUser, Role


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


class MyCustomLoginForm(LoginForm):
    captcha = ReCaptchaField()

    def login(self, *args, **kwargs):
        return super(MyCustomLoginForm, self).login(*args, **kwargs)