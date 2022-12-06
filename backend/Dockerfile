FROM python:3.9-slim


ENV APP_HOME /app
WORKDIR $APP_HOME

COPY requirements.txt 

RUN pip install -U pip && pip install -r requirements.txt

COPY . .

ENV Port 8080

ENV PYTONBUFFERED TRUE

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 ticketingsystem.wsigi:application
