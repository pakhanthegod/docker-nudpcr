import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

CELERY_TIMEZONE = 'Europe/Moscow'

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()