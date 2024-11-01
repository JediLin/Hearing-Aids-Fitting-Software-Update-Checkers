@echo off
mode 160,30
cls
echo Installing requirements...
pip install -r ./requirements.txt
pip install -r ./requirements_uncertain.txt
pause

:MENU
cls
python "./Checker Menu.py"

echo:
echo:
echo Operation finished.
echo:
echo:
:CHOICE
set /P c=Do you want to check another software? [(Y)es/no]:
if /I "%c%" EQU "N" exit
if /I "%c%" EQU "NO" exit
goto MENU
