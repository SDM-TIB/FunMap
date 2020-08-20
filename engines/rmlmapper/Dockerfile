FROM ubuntu:18.04

RUN apt-get update && apt-get install -y openjdk-8-jdk vim htop bc wget
RUN mkdir /rmlmapper
RUN mkdir /results
RUN mkdir /data
RUN mkdir /mappings
RUN wget -O /rmlmapper/rmlmapper.jar https://github.com/RMLio/rmlmapper-java/releases/download/v4.7.0/rmlmapper-4.7.0-r150.jar
COPY . /rmlmapper

CMD ["tail", "-f", "/dev/null"]
