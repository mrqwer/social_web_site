FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
        && apt-get install -y --no-install-recommends \
            postgresql-client \
            && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock /usr/src/app/
RUN pip install --upgrade pip \
        && pip install pipenv \
            && pipenv install --system

COPY . /usr/src/app/
COPY ./entrypoint.sh .

# EXPOSE 8000
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
# CMD [ "python3" "manage.py" "runserver" ]
#RUN apt-get update && apt-get install netcat -y
#RUN apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y
#RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry/bin/poetry python && \
#    cd /usr/local/bin && \
#    ln -s /opt/poetry/bin/poetry && \
#    poetry config virtualenvs.create false

# ENV POETRY_VERSION=1.2.0
# ENV POETRY_HOME=/opt/poetry
# ENV POETRY_VENV=/opt/poetry-venv

# Tell Poetry where to place its cache and virtual environment
# ENV POETRY_CACHE_DIR=/opt/.cache

# Create stage for Poetry installation
# FROM python-base as poetry-base

# Creating a virtual environment just for poetry and install it with pip
# RUN python3 -m venv $POETRY_VENV \
#     && $POETRY_VENV/bin/pip install -U pip setuptools \
#     && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Create a new stage from the base python image
#FROM python-base as example-app

# Copy Poetry to app image
# COPY --from=poetry-base ${POETRY_VENV} ${POETRY_VENV}

# Add Poetry to PATH
# ENV PATH="${PATH}:${POETRY_VENV}/bin"

# COPY ./pyproject.toml ./poetry.lock* /usr/src/app/
# RUN poetry install




# COPY ./entrypoint.sh .
# COPY . .

# EXPOSE 8000
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

