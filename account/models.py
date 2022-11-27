from django.db import models

from package.models import Package
from user.models import MyUser
from khayyam.jalali_date import JalaliDate


class account(models.Model):
    package = models.OneToOneField(Package, related_name='account', on_delete=models.DO_NOTHING)
    user = models.OneToOneField(MyUser, related_name='account', on_delete=models.CASCADE)
    days = models.PositiveSmallIntegerField(null=True)
    remaining_days = models.PositiveSmallIntegerField(null=True)
    expired = models.BooleanField(default=False)

    created_time = models.DateField(default=str(JalaliDate.today()))
    modified_time = models.DateField(default=str(JalaliDate.today()))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.days = self.package.days
            self.remaining_days = self.days
        except:
            self.expiration = None
