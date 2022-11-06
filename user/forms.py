# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from user.models import MyUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("username", "email", "phone", "has_account")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ("username", "email", "phone", "has_account")
