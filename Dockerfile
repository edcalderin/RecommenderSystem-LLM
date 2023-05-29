FROM python:3.9.7-slim

RUN apt update && apt install --no-install-recommends -y build-essential gcc

RUN adduser --disabled-password --gecos '' new_user

WORKDIR /opt/recommender-api

RUN chown -R new_user:new_user ./

USER new_user

ENV PATH /home/new_user/.local/bin:$PATH

ENV PYTHONPATH .

COPY requirements/requirements.txt requirements/requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --user -r requirements/requirements.txt

COPY . .

CMD ["python", "app/main.py"]