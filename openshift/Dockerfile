FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Brussels

RUN apt-get update \
    && apt-get install -y --no-install-recommends software-properties-common curl \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get install -y --no-install-recommends python3.9 python3.9-venv python3.9-dev \
    && rm -rf /var/lib/apt/lists/*

# install python
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1
