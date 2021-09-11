from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "famPay.settings")
app = Celery("famPay")


app.config_from_object("django.conf:settings")
app.autodiscover_tasks()  # searching for tasks

app.conf.beat_schedule = {
    "send-report-every-single-minute": {
        "task": "youtube.tasks.upload",
        "schedule": crontab(),  # scheduling running tasks
    },
}


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
