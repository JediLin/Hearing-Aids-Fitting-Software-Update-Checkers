@echo off
mode 160,30
for /f "tokens=3-7 delims=[.] " %%i in ('ver') do @(if %%i==XP (set os_ver_org=%%k.%%l) else (if %%j geq 10 (set os_ver_org=%%j.%%k.%%l) else (set os_ver_org=%%j.%%k)))
set os_ver=%os_ver_org%
if %os_ver_org:~0,1% gtr 3 set os_ver=0%os_ver_org%
set colorSupport=No
if %os_ver% GEQ 10.0.10586 set colorSupport=Yes
if %colorSupport%==Yes color
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
if %colorSupport%==Yes (
  set /P c=Do you want to check another software? [[1;30m^([0;32mY[1;30m^)[0mes/no]:
) else (
  set /P c=Do you want to check another software? [^(Y^)es/no]:
)
if /I "%c%" EQU "N" exit
if /I "%c%" EQU "NO" exit
goto MENU

:errorNoPython
if %colorSupport%==Yes (
  echo Please install [1;34mPython[0m and [33mreboot[0m your computer first.
  echo Press [32many key[0m to open [1;34mPython[0m download page with default web browser...
) else (
  echo Please install Python and reboot your computer first.
  echo Press any key to open Python download page with default web browser...
)
pause > nul
start "" "https://www.python.org/downloads/"
exit
