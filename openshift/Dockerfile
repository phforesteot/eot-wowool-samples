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


ENV PIP_EXTRA_INDEX_URL https://partners:y7uTy%2B%5D.fYytqq@repo.eyeontext.com/repository/eyeontext-pypi/simple
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "install-pip3-ubuntu.py" && python3 install-pip3-ubuntu.py

pip3 install eot-wowool-common==2.0.4
pip3 install eot-wowool-sdk
pip3 install eot-wowool-english_entity
pip3 install eot-wowool-topic_identifier
