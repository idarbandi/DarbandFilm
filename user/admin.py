from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from user.models import MyUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = MyUser
    list_display = ["email", "username", "phone", "has_account"]


admin.site.register(MyUser, CustomUserAdmin)
