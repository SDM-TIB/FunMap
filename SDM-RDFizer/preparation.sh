#! /bin/bash

echo "Installing FunMap..."
cd FunMap/
pip install -r requirements.txt

echo "Installing SDM-RDFizer without FnO support..."
cd ../SDM-RDFizer/
pip install -r requirements.txt

echo "Installing SDM-RDFizer with FnO support..."
cd ../SDM-RDFizer-Functions/
pip install -r requirements.txt