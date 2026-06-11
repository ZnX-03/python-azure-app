FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=projetoweb.settings

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

# Roda migrations e cria superuser padrão, depois sobe o servidor
CMD python manage.py migrate && \
    echo "from django.contrib.auth import get_user_model; U=get_user_model(); U.objects.filter(username='admin').exists() or U.objects.create_superuser('admin','admin@email.com','admin123')" | python manage.py shell && \
    gunicorn projetoweb.wsgi:application --bind 0.0.0.0:8000 --workers 2
