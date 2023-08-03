#Importing python image to be used
FROM python:3.9-alpine3.13
LABEL maintainer = "OmarYahya"

ENV PYTHONUNBUFFERED 1

#Copying files from local machine to docker image
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
#Setting working directory in docker image
WORKDIR /app
EXPOSE 8000

#Runs commands in image when building
#Creating new python virtual env
#Updating pip in new virtual env
#Installing dependencies from requirements.txt file to virtual env
#Running shell command to install dependencies from requirements.dev.txt only if DEV argument is true
#Removing tmp directory after installing requirements
#Add new user inside docker image
ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

#Adding to system path
ENV PATH="/py/bin:$PATH"
#Switching to created user
USER django-user
