FROM python:3.9
MAINTAINER Nikita Golovaniuk
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
COPY app /app

CMD gunicorn --bind 0.0.0.0:5000 app:app