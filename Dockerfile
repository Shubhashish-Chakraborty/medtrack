FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# collectstatic loads settings, so give it throwaway values just for the build
RUN SECRET_KEY=build-only DEBUG=False DATABASE_URL=sqlite:////tmp/build.db \
    python manage.py collectstatic --noinput

RUN useradd --create-home appuser && chown -R appuser /app
USER appuser

EXPOSE 8008
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8008", "--workers", "3"]