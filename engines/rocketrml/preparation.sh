#!/bin/bash

curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt install -y nodejs

npm i rocketrml@1.1.0
npm i fs