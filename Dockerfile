#FROM python:3.12 AS build-python
#
#RUN apt-get -y update \
#  && apt-get install -y gettext \
#  && apt-get clean \
#  && rm -rf /var/lib/apt/lists/*
#
#WORKDIR /usr/local/www/hfs_app
#RUN --mount=type=cache,mode=0755,target=/root/.cache/pip pip install poetry
#RUN poetry config virtualenvs.create false
#COPY poetry.lock pyproject.toml /usr/local/www/hfs_app/
#RUN --mount=type=cache,mode=0755,target=/root/.cache/pypoetry poetry install --no-root

### Final image
FROM python:3.12-slim

RUN groupadd -r hfs && useradd -r -g hfs hfs

WORKDIR /usr/local/www/hfs_app

# Pillow dependencies
RUN apt-get update &&  \
    apt-get install -y \
    gettext \
    redis \
    redis-server \
    curl \
    build-essential \
    libffi8 \
    tzdata \
    postgresql \
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

RUN mkdir -p /usr/local/www/hfs_app/media /usr/local/www/hfs_app/static &&  \
    chown -R hfs:hfs /usr/local/www/hfs_app/

RUN pip install --upgrade pip
RUN pip install poetry

COPY poetry.lock pyproject.toml  /usr/local/www/hfs_app/
RUN  poetry config virtualenvs.create false --local && poetry install --no-interaction --no-ansi --no-root


COPY .  /usr/local/www/hfs_app/

# RUN curl -sSL https://install.python-poetry.org | python3 -


# RUN poetry config virtualenvs.create false \
#    && poetry install --no-root && rm -rf $POETRY_CACHE_DIR

#COPY --from=build-python /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
#COPY --from=build-python /usr/local/bin/ /usr/local/bin/
#COPY .  /usr/local/www/hfs_app/
#WORKDIR  /usr/local/www/hfs_app/

#RUN curl -sSL https://install.python-poetry.org | python3 -
#
#ENV POETRY_NO_INTERACTION=1 \
#    POETRY_VIRTUALENVS_IN_PROJECT=1 \
#    POETRY_VIRTUALENVS_CREATE=1 \
#    POETRY_CACHE_DIR=/tmp/poetry_cache

#COPY pyproject.toml /usr/local/www/hfs_app
#RUN poetry install --no-interaction --no-ansi --no-root && rm -rf $POETRY_CACHE_DIR
#COPY . /usr/local/www/hfs_app

EXPOSE 8000
ENV PYTHONUNBUFFERED=1

#CMD ["python3", "manage.py", "makemessages", "--all"]
#CMD ["python3", "manage.py", "compilemessages"]
#CMD ["python3", "manage.py", "collectstatic"]
#CMD ["python3", "manage.py", "migrate"]
#CMD ["python3", "manage.py", "wait_for_db"]
#CMD ["python3", "manage.py", "runserver"]
RUN #echo `ls -lart /usr/local/www/hfs_app/`
#CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--preload", "--worker-class", "uvicorn.workers.UvicornWorker", "config.wsgi:application"]
