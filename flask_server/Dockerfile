FROM python:3.6.12-alpine

RUN mkdir -p /opt/app/

WORKDIR /opt/app/

RUN adduser -S app

COPY app app/
COPY flask_server.py .
COPY .flaskenv .
COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN chown -R app /opt/app/

USER app
