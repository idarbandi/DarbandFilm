from django.db.models.signals import post_save
from django.dispatch import receiver

from financial.models import Payment


@receiver(post_save, sender=Payment)
def callback(sender, instance, **kwargs):
    if instance.is_paid:
        purchase = instance.purchase.first()
        purchase.status = purchase.PAID
        purchase.save()
