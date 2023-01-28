FROM python:3.8

CMD cp /etc/resolv.conf /etc/resolv.conf
RUN apt-get update && apt-get install -y python3-pip && apt-get clean

WORKDIR /gunicorn
WORKDIR /djangoproject
ADD . /djangoproject
RUN  pip3 install -r requirements.txt

ENV PYTHONUNBUFFERED=1

EXPOSE 8002

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
