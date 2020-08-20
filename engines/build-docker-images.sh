#!/bin/bash


cd rmlmapper
docker build -t rmlmapper .
cd ../sdmrdfizer
docker build -t sdmrdfizer .
cd ../rocketrml
docker build -t rocketrml .
cd ../FunMap
docker build -t funmap .
docker-compose up -d
