from celery import shared_task
from khayyam.jalali_date import JalaliDate


@shared_task
def calculate_Subscription_Credit(date):
    re_date = str(date)[-1] + str(date)[-2]
    today = str(JalaliDate.today())[-1] + str(JalaliDate.today())[-1]
    return int(today) - int(re_date)