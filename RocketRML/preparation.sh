#! /bin/bash

echo "Installing RocketRML..."
npm i rocketrml@1.1.0
npm i fs

echo "Installing FunMap..."
cd FunMap/
python3 -m pip install -r requirements.txt
