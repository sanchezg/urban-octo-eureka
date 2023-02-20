FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y software-properties-common gcc \
    && add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update \
    && apt-get install -y python3.10 python3-distutils \
        python3-pip python3-apt python3-dev libpq-dev git \
        python3-psycopg2

RUN mkdir -p /src

ADD ./requirements requirements/
RUN pip3 install -r requirements/requirements-dev.txt

COPY . /src
WORKDIR /src

CMD /bin/bash
