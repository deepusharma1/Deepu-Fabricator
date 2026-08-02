# backend/Dockerfile

FROM python:3.11-slim


WORKDIR /workspace


# Python optimization
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1



# Required system package
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*



# Install Python dependencies
COPY requirements.txt .


RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt



# Copy backend application
COPY . .



# Create non-root user for security
RUN useradd -m appuser && \
    chown -R appuser:appuser /workspace



USER appuser



# Application port
EXPOSE 8000



# Container health check
HEALTHCHECK --interval=30s \
    --timeout=5s \
    --start-period=10s \
    --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1



# Production server
CMD ["gunicorn", "app.main:app", "-k", "uvicorn.workers.UvicornWorker", "--workers", "4", "--bind", "0.0.0.0:8000"]