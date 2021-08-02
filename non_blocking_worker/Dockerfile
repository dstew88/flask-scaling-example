FROM python:3.6.12-alpine

RUN mkdir -p /opt/app/

WORKDIR /opt/app/

RUN adduser -S app

COPY worker.py .
COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN chown -R app /opt/app/

USER app

CMD ["celery", "worker", "--app=worker.app", "--pool=gevent", "--concurrency=20", "--queues=minio", "--loglevel=INFO"]
