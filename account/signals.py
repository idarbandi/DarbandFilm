from django.dispatch import receiver
from django.db.models.signals import post_save
from purchase.models import Purchase
from account.models import account


@receiver(post_save, sender=Purchase)
def callback(sender, instance, **kwargs):
    if instance.status == Purchase.PAID:
        user_account = account.objects.create(package=instance.package,
                                              user=instance.user)
        user_account.save()
