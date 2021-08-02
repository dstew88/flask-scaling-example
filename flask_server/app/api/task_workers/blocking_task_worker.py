from datetime import datetime
import os

from celery import Celery


# Initialize Celery
celery_instance = Celery(
    'worker',
    broker=f'redis://{os.environ["REDIS_HOST"]}:{os.environ["REDIS_PORT"]}'
)


@celery_instance.task()
def blocking():

    start = datetime.now().timestamp()
    while datetime.now().timestamp() < start + 10:
        # mimic a CPU intensive task
        continue

    print("Background worker completed blocking job")
