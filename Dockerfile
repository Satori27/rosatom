FROM python:3.10

WORKDIR /src

ENV PYTHONDONTWRITEBITECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app app
COPY alembic.ini alembic.ini
COPY tests tests
