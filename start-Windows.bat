@echo off

cls
echo Installing requirements...
pip install -r ./requirements.txt
pip install -r ./requirements_uncertain.txt
pause

:MENU
cls
python "./Checker Menu.py"

pause
goto MENU