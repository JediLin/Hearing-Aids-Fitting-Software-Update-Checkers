@echo off
mode 160,30
cls
python --version 2 > NUL
if errorlevel 1 goto errorNoPython
echo Installing requirements...
echo:
python -m pip install --upgrade pip
pip install --upgrade -r ./requirements.txt
pip install --upgrade -r ./requirements_uncertain.txt

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

:errorNoPython
echo Please install Python first. Press any key to open Python download page with default web browser...
pause > nul
start "" "https://www.python.org/downloads/"
exit
