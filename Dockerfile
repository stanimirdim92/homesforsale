FROM python:3.12 AS build-python

RUN apt-get -y update \
  && apt-get install -y gettext \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/www/hfs_app
RUN --mount=type=cache,mode=0755,target=/root/.cache/pip pip install poetry
RUN poetry config virtualenvs.create false
COPY poetry.lock pyproject.toml /usr/local/www/hfs_app/
RUN --mount=type=cache,mode=0755,target=/root/.cache/pypoetry poetry install --no-root

### Final image
FROM python:3.12-slim

RUN groupadd -r hfs && useradd -r -g hfs hfs

# dependencies
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

# install poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 -

# copy project files
RUN mkdir -p /usr/local/www/hfs_app/media /usr/local/www/hfs_app/static &&  \
    chown -R hfs:hfs /usr/local/www/hfs_app/

# copy project files from build
COPY --from=build-python /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/
COPY .  /usr/local/www/hfs_app/
WORKDIR /usr/local/www/hfs_app


#ENV PATH=/opt/poetry/bin:$PATH
#RUN  poetry config virtualenvs.in-project true && poetry install --no-interaction --no-ansi --no-root

#ENV POETRY_NO_INTERACTION=1 \
#    POETRY_VIRTUALENVS_IN_PROJECT=1 \
#    POETRY_VIRTUALENVS_CREATE=1 \
#    POETRY_CACHE_DIR=/tmp/poetry_cache


EXPOSE 8000
ENV PYTHONUNBUFFERED=1

#CMD ["python3", "manage.py", "makemessages", "--all"]
#CMD ["python3", "manage.py", "compilemessages"]
#CMD ["python3", "manage.py", "collectstatic"]
#CMD ["python3", "manage.py", "migrate"]
#CMD ["python3", "manage.py", "wait_for_db"]
CMD ["python3", "manage.py", "runserver"]
#RUN echo `ls -lart /usr/local/www/hfs_app`
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--preload", "--worker-class", "uvicorn.workers.UvicornWorker", "config.wsgi:application"]
