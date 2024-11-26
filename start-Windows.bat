@echo off
mode 160,30
color
cls
python --version 2 > NUL
if errorlevel 1 goto errorNoPython
echo Installing/upgrading requirements...
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
set /P c=Do you want to check another software? [[1;30m([0;32mY[1;30m)[0mes/no]:
if /I "%c%" EQU "N" exit
if /I "%c%" EQU "NO" exit
goto MENU

:errorNoPython
echo Please install Python first. Press [32many key[0m to open Python download page with default web browser...
pause > nul
start "" "https://www.python.org/downloads/"
exit
