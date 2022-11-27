from celery import Celery
from django.conf import settings
from celery.schedules import crontab

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'darbandFilm.settings')


app = Celery('darbandFilm')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


