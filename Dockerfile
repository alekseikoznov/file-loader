FROM python:3.11-slim

WORKDIR /app

COPY .env /app

COPY webapp/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

COPY webapp/ /app

CMD [ "python3", "./src/manage.py", "runserver", "0.0.0.0:8000"]