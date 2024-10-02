### Build and install packages
FROM python:3.12 AS build-python

RUN apt-get -y update \
  && apt-get install -y gettext \
  # Cleanup apt cache
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
WORKDIR /app
#RUN --mount=type=cache,mode=0755,target=/root/.cache/pip pip install poetry
#RUN poetry config virtualenvs.create false
#COPY poetry.lock pyproject.toml /app/
#RUN --mount=type=cache,mode=0755,target=/root/.cache/pypoetry poetry install --no-root

### Final image
FROM python:3.12-slim

RUN groupadd -r hfs && useradd -r -g hfs hfs

# Pillow dependencies
RUN apt-get update \
  && apt-get install -y \
  libffi8 \
  libgdk-pixbuf2.0-0 \
  liblcms2-2 \
  libopenjp2-7 \
  libssl3 \
  libtiff6 \
  libwebp7 \
  libpq5 \
  shared-mime-info \
  mime-support \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app/media /app/static \
  && chown -R hfs:hfs /app/


RUN curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock pyproject.toml /app/
RUN poetry install  --no-interaction --no-ansi --no-root
COPY . /app/

ARG STATIC_URL
ENV STATIC_URL=${STATIC_URL:-/static/}
RUN SECRET_KEY=dummy STATIC_URL=${STATIC_URL} python3 manage.py collectstatic --no-input

EXPOSE 8000
#ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "config.wsgi.application"]
