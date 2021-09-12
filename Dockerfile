FROM python:3.8.0-alpine

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN set -e; \
        apk add --no-cache --virtual .build-deps \
                gcc \
                g++ \
                libc-dev \
                libffi-dev \
                musl-dev\
                make\
                linux-headers \
                mariadb-dev \
                python3-dev \
                postgresql-dev \
        ;
RUN python3 -m pip install --no-cache-dir -r ./requirements.txt

COPY . /usr/src/app/

ENV PYTHONPATH /usr/src/app/


# RUN ls -la src/

EXPOSE 5000

RUN chmod u+x ./docker-entrypoint.sh
ENTRYPOINT ["sh", "./docker-entrypoint.sh"]