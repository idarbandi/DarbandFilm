from django.db import models

# accounts/models.py
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class MyUser(AbstractUser):
    username = models.CharField(unique=True, verbose_name='نام کاربری', max_length=32, null=True)
    email = models.EmailField(verbose_name="ایمیل")
    phone = PhoneNumberField(verbose_name="شماره تلفن", region='IR', null=True, blank=True, unique=True)
    has_account = models.BooleanField(default=False)

    # add additional fields in here

    def __str__(self):
        return f"{self.username}, {self.email}"
