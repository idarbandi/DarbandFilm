from darbandFilm.celery import app
from celery.schedules import crontab
from account.models import account

app.conf.beat_schedule = {
    'check subscription': {
        'task': 'check_subs',
        'schedule': crontab(minute='23', hour='*', day_of_week='*'),
    }
}


@app.task(name='check_subs')
def check_subs():
    for accounts in account.objects.all():
        days = accounts.remaining_days
        accounts.remaining_days = days - 1
        if accounts.remaining_days == 0:
            accounts.expired = True
            accounts.user.has_account = False
        accounts.save()