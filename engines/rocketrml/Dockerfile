FROM node:8


RUN apt-get update && apt-get install -y vim htop bc wget

RUN npm init -y && npm i rocketrml@1.6.0


RUN mkdir /rocketrml
COPY . /rocketrml/

CMD ["tail", "-f", "/dev/null"]
