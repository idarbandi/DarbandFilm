from django.contrib import admin

from purchase.models import Purchase
from django.contrib.admin.decorators import register


@register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    fields = ['user', 'package', 'price', 'status', 'payment']
    list_display = ['status']