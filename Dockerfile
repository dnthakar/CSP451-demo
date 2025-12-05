FROM python:3.11-slim AS base

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# install dependencies
COPY applications/backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy backend code
COPY applications/backend /app

EXPOSE 80

# run uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
