FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry && poetry config virtualenvs.create false

RUN poetry install --only main --no-root

COPY . /app/

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "lms.wsgi:application", "--bind", "0.0.0.0:8000"]
