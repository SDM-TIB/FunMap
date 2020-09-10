#! /bin/bash

echo "Installing FunMap..."
cd FunMap/
python3 -m pip install -r requirements.txt

echo "Installing SDM-RDFizer without FnO support..."
cd ../SDM-RDFizer/
python3 -m pip install -r requirements.txt

echo "Installing SDM-RDFizer with FnO support..."
cd ../SDM-RDFizer-Functions/
python3 -m pip install -r requirements.txt