#!/bin/bash

# Thanks https://stackoverflow.com/a/29710607
cd -- "$(dirname "$0")"

clear
echo "Installing/upgrading requirements..."
python -m pip install --upgrade pip
python -m pip install --upgrade -r ./requirements.txt
python -m pip install --upgrade -r ./requirements_waiting.txt
python -m pip install --upgrade -r ./requirements_uncertain.txt

clear
python "./Checker Menu.py"

read -p 'Press any key to continue...'
