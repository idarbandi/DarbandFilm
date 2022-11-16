from django.dispatch import receiver
from django.db.models.signals import post_save
from account.models import account
from user.models import MyUser


@receiver(post_save, sender=account)
def callback(sender, instance, **kwargs):
    user = MyUser.objects.get(username=instance.user.username)
    user.has_account = True
    user.save()