# Hearing Aids Fitting Software Update Checkers
## Making portable by yourself
If you want to make portable version of The Checker by yourself, you can:
1. It's highly recommended that making portable version on a clean, no-Python-installed system, so that you can easily make all necessary modules portable too. ([Windows Sandbox](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/) works perfectly.)
2. Download the standard release of The Checker from https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/releases/latest
3. Extract the ZIP to a folder
4. Go to: https://www.python.org/downloads/windows/
5. Download latest (recommended) or *3.8.x* (for Windows 7 compatability) version of `Windows embeddable package` (ZIP archive file) according to your and your target's system architecture (64-bit, 32-bit, or ARM64)
6. Extract the ZIP to the folder in step 3, you should get `python.exe`, `requirements.txt`, and `start-Windows.bat` (among other files) in the same folder
7. Download (right click and Save link as...) [get-pip.py](https://bootstrap.pypa.io/get-pip.py) (or [get-pip.py for Python 3.8.x](https://bootstrap.pypa.io/pip/3.8/get-pip.py) if working with Python 3.8.x) and put it into the folder in step 3, so you get `python.exe` and `get-pip.py` in the same folder
8. Run [Windows Command Prompt (cmd)](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd)
9. Use [cd](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cd) command to change working path to the folder in step 3; for example:
> cd c:\Users\WDAGUtilityAccount\Downloads\Hearing-Aids-Fitting-Software-Update-Checkers
10. Install `pip` by this command:
> python.exe get-pip.py
11. Edit `python314._pth` (`314` means Python v*3.14*; this filename will be different for each Python version you downloaded from step 5. So you should edit `python38._pth` if dealing with Python v3.8) with any plain-text editor, uncomment (delete the leading `#`) the last line so the last line of this file should be like this:
> import site
12. Install necessary modules by these commands:
> python.exe -m pip install --upgrade -r ./requirements.txt<br>
> python.exe -m pip install --upgrade -r ./requirements_pending.txt<br>
> python.exe -m pip install --upgrade -r ./requirements_uncertain.txt
13. That's all, you made it! Now you can bring the whole folder (or make a ZIP/RAR/7z/whatever archive file of it) with you.

NOTE: In case you want to make a portable version for Windows 7, you have to use Windows embeddable package for Python *3.8*.x instead in step 5, [get-pip.py for Python 3.8.x](https://bootstrap.pypa.io/pip/3.8/get-pip.py) in step 7, and edit `python38._pth` instead in step 11.
