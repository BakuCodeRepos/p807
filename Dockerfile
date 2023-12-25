# FROM python:3.10-slim

# ENV PYTHONUNBUFFERED 1
# ENV DEBUG False
# ENV APP_ROOT /code

# WORKDIR ${APP_ROOT}

# COPY ./requirements.txt requirements.txt

# RUN apt-get update && \
#   apt-get install -y \
#   locales \
#   locales-all \
#   build-essential \
#   libpcre3 \
#   libpcre3-dev \
#   curl \
#   libzbar-dev \
#   && pip install --upgrade pip \
#   && pip install --no-cache-dir -r requirements.txt \
#   && apt-get clean --dry-run

# COPY ./mime.types /etc/mime.types
# COPY ./uwsgi.ini /conf/uwsgi.ini
# COPY . /code

# # Start uWSGI
# CMD [ "uwsgi", "--ini", "/conf/uwsgi.ini"]

# Use Python 3.10 slim as the base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DEBUG=False
ENV APP_ROOT=/code

# Set the working directory
WORKDIR ${APP_ROOT}

# Copy the requirements file
COPY ./requirements.txt requirements.txt

# Update package lists, clear APT cache, and install necessary packages
RUN apt-get clean && \
    apt-get update && \
    apt-get install -y \
    build-essential \
    libpcre3 \
    libpcre3-dev \
    curl \
    libzbar-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Install locales separately to avoid potential issues
RUN apt-get install -y locales && \
    dpkg-reconfigure locales && \
    apt-get install -y locales-all

# Clean up APT when done
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy additional necessary files
COPY ./mime.types /etc/mime.types
COPY ./uwsgi.ini /conf/uwsgi.ini
COPY . /code

# Command to run uWSGI
CMD ["uwsgi", "--ini", "/conf/uwsgi.ini"]
