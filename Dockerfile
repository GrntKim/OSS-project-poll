FROM python:3.11-slim

WORKDIR /app
RUN pip install --no-cache-dir Django==4.2.23
COPY . .

RUN mkdir -p /app && chmod 755 /app

EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate && python manage.py shell -c \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')\" && python manage.py runserver 0.0.0.0:8000"]