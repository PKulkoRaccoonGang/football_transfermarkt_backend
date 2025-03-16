FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV DJANGO_SETTINGS_MODULE=football_transfermarkt.settings

EXPOSE 9000

WORKDIR /app/football_transfermarkt

CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
