# syntax=docker/dockerfile:1

FROM ubuntu:20.04
MAINTAINER Benjamin Clark "bclark@sudoblark.com"
WORKDIR /app


# Install Python3 using apt
RUN apt update
RUN apt install software-properties-common -y
# PPA repo that has newer releases then default Ubuntu repos
RUN add-apt-repository ppa:deadsnakes/ppa  -y
# Install Python and pip
RUN apt install python3.8 -y
RUN apt install python3-pip -y

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# args we expect to be passed in at runtime to setup DB connection
ARG db_host
ARG db_name
ARG db_user
ARG db_pwd

# Copy actual contents across
COPY src src

# Setup config file according to env vars
RUN python3 /app/src/configBootstrap.py "${db_host}" "${db_name}" "${db_user}" "${db_pwd}"

WORKDIR /app/src

# Entry point for container to initialise database if required
ENTRYPOINT ["python3", "database/setup.py"]
# Actual API worker
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]