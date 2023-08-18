# This is a example Dockerfile for running a FastAPI app in a Docker container. Change it to suit your needs.
# Use the official lightweight Python image (https://hub.docker.com/_/python)
FROM python:{{cookiecutter.__python_version}}-slim

# Update pip and install Poetry
RUN pip install --upgrade pip \
    && pip install poetry

# Set the working directory
WORKDIR /app

# Copy the dependencies file to the working directory
COPY pyproject.toml poetry.lock ./

# Install 3rd party dependencies.
RUN poetry config virtualenvs.options.no-pip true \
    && poetry config virtualenvs.options.no-setuptools true \
    && poetry install \
    --no-ansi --no-interaction --no-plugins --no-cache \
    --no-root \
    --compile --without dev --sync

# Copy over the source code
COPY README.md ./
COPY src/{{cookiecutter.__package_name}} ./src/{{cookiecutter.__package_name}}

# Install just the source code
RUN poetry install \
    --no-ansi --no-interaction --no-plugins --no-cache \
    --compile --only-root

# Set environment variables
ENV HOME=/root

# Expose the port that the app will run on
EXPOSE 8080

# An ENTRYPOINT allows you to configure a container that will run as an executable
ENTRYPOINT ["poetry", "run", "uvicorn", "{{cookiecutter.__package_name}}.app.main:app", "--host", "0.0.0.0", "--port", "8080"]
