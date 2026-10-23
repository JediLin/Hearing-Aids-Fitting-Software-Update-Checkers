#!/bin/bash

# Thanks https://stackoverflow.com/a/29710607
cd -- "$(dirname "$0")"

clear
echo "Installing/upgrading requirements..."
python3 -m pip install --no-warn-script-location --upgrade pip
python3 -m pip install --no-warn-script-location --upgrade -r ./requirements.txt
python3 -m pip install --no-warn-script-location --upgrade -r ./requirements_pending.txt
python3 -m pip install --no-warn-script-location --upgrade -r ./requirements_uncertain.txt

clear
python3 "./Checker Menu.py"

read -p 'Press any key to continue...'
