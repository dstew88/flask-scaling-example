import os

from celery import Celery


# Initialize Celery
celery_instance = Celery(
    'worker',
    broker=f'redis://{os.environ["REDIS_HOST"]}:{os.environ["REDIS_PORT"]}'
)
