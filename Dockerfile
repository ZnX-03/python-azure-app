FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=projetoweb.settings

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN ls -la && ls -la projetoweb/

RUN python -c "import sys; sys.path.insert(0, '/app'); import projetoweb.settings; print('settings OK')"

RUN python manage.py collectstatic --noinput

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Use the entrypoint script to run migrations & start Gunicorn safely
ENTRYPOINT ["/entrypoint.sh"]
