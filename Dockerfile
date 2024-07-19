FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app


# Install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]