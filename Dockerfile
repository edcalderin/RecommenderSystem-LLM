FROM python:3.9.7-slim

RUN apt update && apt install --no-install-recommends -y build-essential gcc

RUN adduser --disabled-password --gecos '' recom-user

WORKDIR /opt/recommender-api

RUN chown -R recom-user:recom-user ./

USER recom-user


COPY requirements/requirements.txt requirements/requirements.txt


RUN pip install --upgrade pip
RUN pip install --no-cache-dir --user -r requirements/requirements.txt

COPY . .


CMD ["python", "app/main.py"]