FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y

WORKDIR /usr/app/src

COPY ./ ./

RUN pip install pandas
