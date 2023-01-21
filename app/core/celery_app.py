from celery import Celery
from celery.schedules import crontab

from app.api.dependencies import get_settings

celery_app = Celery(
    "worker",
    broker=settings.REDIS_DSN,
    result_backend=settings.REDIS_DSN,
    result_expires=30
)

celery_app.conf.task_routes = {
    "worker.test_celery": "main-queue"
}

celery_app.conf.beat_schedule = {
    'celery_beat_testing': {
        'task': 'celery_app.tasks.test_beat',
        'schedule': crontab(minute='*/1')
    }
}

celery_app.conf.timezone = 'UTC'
celery_app.conf.update(task_track_started=True)
