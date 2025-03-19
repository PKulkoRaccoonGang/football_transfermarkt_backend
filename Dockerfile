FROM python:3.10-alpine

WORKDIR /app

RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    python3-dev

RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=football_transfermarkt.settings

EXPOSE 9000

WORKDIR /app/football_transfermarkt

CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
