# 🐳 STACK INFRASTRUCTURE (V2.0) - WEB
FROM python:3.13-slim-bookworm

# 🛠️ SYSTEM DEPENDENCIES
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 📦 POETRY INSTALLATION
ENV POETRY_VERSION=2.0.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -

# 🏗️ ENVIRONMENT SETUP
WORKDIR /src
COPY pyproject.toml* poetry.lock* ./
RUN poetry install --no-root

# 🌀 DJANGO SERVICE
EXPOSE 8000
CMD ["python", "web/manage.py", "runserver", "0.0.0.0:8000"]
