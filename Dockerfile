FROM python:3.11-slim

WORKDIR /app
RUN pip install --no-cache-dir Django==4.2.23
COPY . .
RUN touch ./data/db.sqlite3
RUN python manage.py migrate
RUN python manage.py shell -c "\
from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='admin').exists() or \
User.objects.create_superuser('admin', 'admin@example.com', 'admin123')"
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]