from django.db import models

from package.models import Package
from user.models import MyUser


class account(models.Model):
    package = models.OneToOneField(Package, related_name='account', on_delete=models.DO_NOTHING)
    user = models.OneToOneField(MyUser, related_name='account', on_delete=models.CASCADE)
    expiration = models.PositiveSmallIntegerField(null=True)
    expired = models.BooleanField(default=False)


    creation_date

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.expiration = self.package.days
        except:
            self.expiration = None
