ECHO OFF
set "LorNew=null"
set "parmLaunch=launch"
set "parm2=null"
CLS

:LegacyORNew
ECHO.
ECHO Choose a Number:
ECHO     1 = Run Legacy Starkey Inspire OS fitting software
ECHO     2 = Run New/Current  Starkey Pro Fit fitting software
ECHO.
set /P LorNew="Please enter a number between 1 and 2? "
If %LorNew% == 1 GOTO SELECT
If %LorNew% == 2 GOTO SELECT
GOTO LegacyORNew

:SELECT
ECHO.
ECHO Choose a Number:
ECHO     1 = AGX/AudigyGroup
ECHO     2 = Amplifon
ECHO     3 = Audibel
ECHO     4 = Audika (French/Francaise) before Audika sold to Oticon
ECHO     5 = AudioSync (Brazil = Portuguese) (Pro Akustik = German)
ECHO     6 = Horex (German/Deutsche)
ECHO     7 = KIND
ECHO     8 = Lisound (Chinese/Zhongguo)
ECHO     9 = Medtronic
ECHO    10 = MicroTech
ECHO    11 = Starkey
ECHO    12 = NuEar
ECHO    13 = Visaudio (French/Francaise)
ECHO    14 = MiracleEar
ECHO    15 = [!! Pro Fit ONLY !!] Microsom
ECHO    16 = [!! Pro Fit ONLY !!] SoundGear
ECHO.

set /P MyNum="Please enter a number between 1 and 16? "

If %MyNum% == 1 SET "parm2=AudigyGroupFitting"
If %MyNum% == 2 SET "parm2=AmplifonFitting"
If %MyNum% == 3 SET "parm2=AudibelFitting"
If %MyNum% == 4 SET "parm2=AudikaFitting"
If %MyNum% == 5 SET "parm2=AudioSyncGeneralFitting"
If %MyNum% == 6 SET "parm2=HorexFitting"
If %MyNum% == 7 SET "parm2=KINDFitting"
If %MyNum% == 8 SET "parm2=LisoundFitting"
If %MyNum% == 9 SET "parm2=MedtronicFitting"
If %MyNum% == 10 SET "parm2=MicroTechFitting"
If %MyNum% == 11 SET "parm2=Starkey"
If %MyNum% == 12 SET "parm2=NuEarFitting"
If %MyNum% == 13 SET "parm2=VisaudioFitting"
If %MyNum% == 14 SET "parm2=MiracleEar"
If %MyNum% == 15 SET "parm2=MicrosomFitting"
If %MyNum% == 16 SET "parm2=SoundGearFitting"
If %parm2% == null GOTO ERROR
GOTO STARTSW

:ERROR
ECHO.
ECHO You Selected an Invalid Number: %MyNum%
ECHO Try Again
ECHO.
GOTO SELECT

:STARTSW
If %LorNew% == 1 ECHO Started Your Selection Legacy Starkey Inspire to run %MyNum% = %parm2%
If %LorNew% == 2 ECHO Started Your Selection New/Current  Starkey Pro Fit to run %MyNum% = %parm2%

If %LorNew% == 1 Start "" "C:\Program Files (x86)\Starkey Laboratories\Inspire OS\Starkey.Inspire.Host.PatientBase.exe" %parmLaunch% %parm2%
If %LorNew% == 2 Start "" "C:\Program Files (x86)\Starkey\ProFit\ProFit.Host.PatientBase.exe" %parmLaunch% %parm2%
set "parm2=null"
PAUSE
EXIT /B
::
:: Instructions for Changing this .txt file into an Executable .Bat file
::
:: 1) Download this StarkeyOtherBrands.txt file
:: 2) Right button click the StarkeyOtherBrands.txt file and select Open With > Notepad
:: 3) Use Keystroke combinations Ctrl-a and Ctrl-c to Select and Copy everything to your Windows Scratchpad
:: 4) Exit out of Notepad (your Windows Scratchpad will be saved)
:: 5) Start a new/empty copy of Notepad (Start/Notepad)
:: 6) Use Keystroke combination Ctrl-v to Paste the Scratchpad contents
:: 7) File/Save as/StarkeyOtherBrands.Bat
:: 8) Now you can double-mouse-click your new StarkeyOtherBrands.Bat to run/execute the commands
::