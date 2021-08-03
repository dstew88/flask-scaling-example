from datetime import datetime

from ..celery import celery_instance


@celery_instance.task()
def blocking(time: int):

    start = datetime.now().timestamp()
    while datetime.now().timestamp() < start + time:
        # mimic a CPU intensive task
        continue

    print("Background worker completed blocking job")
