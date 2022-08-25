# A normal typical ubuntu container
# FROM ubuntu:22.04
# In case you you want to use CUDA
# FROM nvidia/cuda:11.6.0-devel-ubuntu20.04
# FROM nvidia/cuda:11.7.1-devel-ubuntu20.04
FROM nvidia/cuda:11.7.0-cudnn8-devel-ubuntu22.04

# https://vsupalov.com/docker-arg-env-variable-guide/
# https://bobcares.com/blog/debian_frontendnoninteractive-docker/
ARG DEBIAN_FRONTEND=noninteractive
# Timezone
ENV TZ="Asia/Bangkok"

# like CD command in terminal. it will create directory if path is not existed
WORKDIR /root/projects
RUN apt update && apt upgrade -y
# Set timezone
RUN apt install -y tzdata
RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone

# Usual terminal commands for installing environment
RUN apt install python3 python3-pip -y
RUN apt install git -y

# I will use `pipenv` to dynamically controll my environment
# If you want to use `pip install`, just remove `pipenv` and continue with `pip install`
# RUN pip install pipenv

# Install library
RUN pip3 install ipykernel
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install matplotlib
RUN pip3 install sklearn
RUN pip3 install torch

CMD tail -f /dev/null