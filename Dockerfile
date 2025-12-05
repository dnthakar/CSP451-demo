# CloudMart API - Production Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn azure-cosmos pydantic

# Copy application code
COPY deploy/main_cosmosdb.py /app/main.py

# Expose port
EXPOSE 80

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

### 5.2 Build and Push to Docker Hub

```bash
# Build image
$ docker build -t dcjoker/cloudmart-api:latest .

# Login to Docker Hub
$ docker login -u dcjoker

# Push image
$ docker push dcjoker/cloudmart-api:latest
