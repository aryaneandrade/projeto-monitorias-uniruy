# Start from official Python slim image
FROM python:3.12-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       gcc \
       libpq-dev \
       libjpeg-dev \
       zlib1g-dev \
       netcat-openbsd \
       curl \
    && rm -rf /var/lib/apt/lists/*

# Create app user
RUN useradd --create-home --shell /bin/bash appuser
WORKDIR /home/appuser

# Copy only requirements first for cached installs
COPY requirements.txt /home/appuser/requirements.txt

# Install pip dependencies including gunicorn
RUN pip install --no-cache-dir -r /home/appuser/requirements.txt \
    && pip install --no-cache-dir gunicorn

# Copy project
COPY . /home/appuser/projeto
WORKDIR /home/appuser/projeto

# Ensure non-root owns the project files
RUN chown -R appuser:appuser /home/appuser/projeto
RUN mkdir -p /home/appuser/projeto/staticfiles && chown -R appuser:appuser /home/appuser/projeto/staticfiles

# Entrypoint
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER appuser

ENV PATH="/home/appuser/.local/bin:$PATH"

EXPOSE 8000

CMD ["/entrypoint.sh"]
