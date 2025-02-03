FROM python:3.9-slim

WORKDIR /app

COPY server.py /app/

RUN pip install flask prometheus_client werkzeug

CMD ["python", "server.py"]