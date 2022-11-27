from django.contrib import admin
from django.contrib.admin import register

from account.models import account


@register(account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'days', 'remaining_days', 'expired']
