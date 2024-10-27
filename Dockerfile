### Build and install packages
FROM python:3.12 AS build-python

RUN apt-get update && apt-get upgrade -y \
  && apt-get install -y gettext \
  && apt-get autoremove \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*

ARG LOCAL_PATH=${LOCAL_PATH:-/usr/local/www/hfs_app}

WORKDIR ${LOCAL_PATH}

# Install Python dependencies
RUN --mount=type=cache,mode=0755,target=/root/.cache/pip pip install poetry
RUN poetry config virtualenvs.create false
COPY poetry.lock pyproject.toml ${LOCAL_PATH}
RUN --mount=type=cache,mode=0755,target=/root/.cache/pypoetry poetry install --no-root

### Final image
FROM python:3.12-slim

SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

ARG APP_USER=${APP_USER:-hfs}
ARG LOCAL_PATH=${LOCAL_PATH:-/usr/local/www/hfs_app}

# Create a group and user to run our app
RUN groupadd -r ${APP_USER} && useradd -r -g ${APP_USER} ${APP_USER}

# dependencies
RUN apt-get update &&  \
    apt-get upgrade -y && \
    apt-get install --no-install-recommends -y \
    ca-certificates \
    gettext \
    curl \
    git \
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
  # Cleaning cache:
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
    apt-get clean -y && rm -rf /var/lib/apt/lists/*


# make sure directories exist
RUN mkdir -p ${LOCAL_PATH}/media ${LOCAL_PATH}/static && \
    chown -R ${APP_USER}:${APP_USER} ${LOCAL_PATH}/

# copy project files from build
COPY --from=build-python /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/
COPY .  ${LOCAL_PATH}/
WORKDIR ${LOCAL_PATH}

# This here as we don't want to rebuild everything when we only change the code
ENV PYTHONUNBUFFERED=1

# Change to a non-root user
USER ${APP_USER}:${APP_USER}
