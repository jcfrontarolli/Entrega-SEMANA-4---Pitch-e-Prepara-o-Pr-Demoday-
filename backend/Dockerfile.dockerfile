FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY compostech_backend /app/compostech_backend

ENV HOST=0.0.0.0
ENV PORT=5000
EXPOSE 5000

CMD ["python", "-m", "compostech_backend.app"]