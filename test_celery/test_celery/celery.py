import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_celery.settings")

app = Celery("test_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.beat_schedule = {
    "saver_info": {
        "task": "shop.tasks.test_task",
        "schedule": crontab(),
    },
}
app.conf.timezone = "UTC"