### Build and install packages
FROM python:3.12 AS build-python

RUN apt-get -y update \
  && apt-get install -y gettext \
  && apt-get autoremove \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/www/hfs_app

# Install Python dependencies
RUN --mount=type=cache,mode=0755,target=/root/.cache/pip pip install poetry
RUN poetry config virtualenvs.create false
COPY poetry.lock pyproject.toml /usr/local/www/hfs_app/
RUN --mount=type=cache,mode=0755,target=/root/.cache/pypoetry poetry install --no-root

### Final image
FROM python:3.12-slim

ARG APP_USER=${APP_USER:-hfs}
# Create a group and user to run our app
RUN groupadd -r ${APP_USER} && useradd -r -g ${APP_USER} ${APP_USER}

# dependencies
RUN apt-get update &&  \
    apt-get install -y \
    ca-certificates \
    gettext \
    redis \
    redis-server \
    curl \
    build-essential \
    libffi8 \
    tzdata \
    libgdk-pixbuf2.0-0 \
    liblcms2-2 \
    libopenjp2-7 \
    libssl3 \
    libtiff6 \
    libwebp7 \
    libpq5 \
    shared-mime-info \
    mime-support && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean  &&  \
    rm -rf /var/lib/apt/lists/*


# make sure directories exist
RUN mkdir -p /usr/local/www/hfs_app/media /usr/local/www/hfs_app/static && \
    chown -R ${APP_USER}:${APP_USER} /usr/local/www/hfs_app/

# copy project files from build
COPY --from=build-python /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/
COPY .  /usr/local/www/hfs_app/
WORKDIR /usr/local/www/hfs_app

# This here as we don't want to rebuild everything when we only change the code
ENV PYTHONUNBUFFERED=1

CMD ["python3", "manage.py", "makemigrations"]
CMD ["python3", "manage.py", "migrate"]
CMD ["python3", "manage.py", "makemessages", "--all"]
CMD ["python3", "manage.py", "compilemessages"]
CMD ["python3", "manage.py", "collectstatic"]

# Change to a non-root user
USER ${APP_USER}:${APP_USER}
