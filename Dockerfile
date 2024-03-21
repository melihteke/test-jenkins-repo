FROM python:3.9.5-slim-buster

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app/

USER mely

RUN apt-get update && apt-get install -y openssh-client gcc python3-dev

RUN pip install --upgrade pip
RUN pip install -U -r requirements.txt

COPY . /opt/app/

CMD ["python", "-u", "/opt/app/main.py"]
