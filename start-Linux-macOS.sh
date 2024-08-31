#!/bin/bash

# Thanks https://stackoverflow.com/a/29710607
cd -- "$(dirname "$0")"

clear
echo "Installing requirements..."
pip install -r ./requirements.txt
pip install -r ./requirements_uncertain.txt

clear
python "./Checker Menu.py"

read -p 'Press any key to continue...'