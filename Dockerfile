FROM python:3.9.7-slim

RUN apt update && apt install --no-install-recommends -y build-essential gcc

RUN adduser --disabled-password --gecos '' recom-user

WORKDIR /opt/recommender-api

COPY requirements/requirements.txt requirements/requirements.txt


RUN pip install --upgrade pip
RUN pip install --no-cache-dir --user -r requirements/requirements.txt

COPY . .

RUN chmod +x /opt/recommender-api/run.sh
RUN chown -R recom-user:recom-user ./

USER recom-user

CMD ["python", "app/main.py"]