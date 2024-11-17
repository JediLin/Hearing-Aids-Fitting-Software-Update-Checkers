#!/bin/bash

# Thanks https://stackoverflow.com/a/29710607
cd -- "$(dirname "$0")"

clear
echo "Installing requirements..."
python -m pip install --upgrade pip
pip install --upgrade -r ./requirements.txt
pip install --upgrade -r ./requirements_uncertain.txt

clear
python "./Checker Menu.py"

read -p 'Press any key to continue...'
