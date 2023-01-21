celery -A worker worker -l info -Q main-queue -c 1
celery -A worker beat
