FROM python:3.9

WORKDIR /opt/recommender-api

COPY requirements/requirements.txt requirements/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --user -r requirements/requirements.txt

COPY . .

CMD ["python", "app/main.py"]