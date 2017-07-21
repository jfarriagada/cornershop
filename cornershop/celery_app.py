from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cornershop.settings')

app = Celery('celery_app')
# config celery from settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# redis broker
app.conf.update(
    BROKER_URL='redis://localhost:6379/0',  # Nota 4
)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))