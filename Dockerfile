# FROM nexus-dev.tech.moex.com/moex-docker-static-hosted/python:3.10
FROM python:3.11-slim

ENV POETRY_VERSION=1.8.2
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

# Install system-wide dependencies
RUN apt-get update && \
  apt-get install --no-install-recommends -y git curl gcc && \
  python3 -m pip install setuptools && \
  apt-get clean autoclean && \
  apt-get autoremove --yes && \
  rm -rf /var/lib/apt/lists/*

# Create user for app
ENV APP_USER=appuser
RUN useradd --create-home $APP_USER
WORKDIR /home/$APP_USER
USER $APP_USER

# Use venv directly via PATH
ENV VENV_PATH=/home/$APP_USER/.venv/bin
ENV USER_PATH=/home/$APP_USER/.local/bin
ENV PATH="$VENV_PATH:$USER_PATH:$PATH"

RUN  pip install --user --no-cache-dir poetry==$POETRY_VERSION

RUN poetry config virtualenvs.in-project true

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-dev

COPY alembic.ini .
COPY app app

CMD alembic upgrade head && python -m app
