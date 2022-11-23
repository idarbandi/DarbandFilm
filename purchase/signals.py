from django.db.models.signals import post_save, post_init
from django.dispatch import receiver

from financial.models import Payment


@receiver(post_save, sender=Payment)
def callback(sender, instance, **kwargs):
    if instance.is_paid and not instance.b_is_paid:
        purchase = instance.purchase.first()
        purchase.status = purchase.PAID
        purchase.save()


@receiver(post_init, sender=Payment)
def store_is_paid_status(sender, instance, **kwargs):
    instance.b_is_paid = instance.is_paid
