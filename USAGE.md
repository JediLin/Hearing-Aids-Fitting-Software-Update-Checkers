# Hearing Aids Fitting Software Update Checkers
## How to use it

### Standard release
1. [Install Python](#pre-requirement-install-python) (and reboot your computer) if you don't have it yet
2. Download The Checker from here: https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/releases/latest<br/>Click on the link and then click on the `HAFS-Update-Checkers.zip` link to download it
3. Extract the ZIP to a folder
4. Go to the extracted folder, double-click the `start-Windows.bat` file and follow the instructions on-screen; for Linux or macOS users, there is a corresponding `start-Linux-macOS.sh` which should do the job, too

NOTE: If The Checker looks like it has frozen, then try disabling `quickEdit` by running the `fixQuickedit.reg` file before running `start-Windows.bat`

**WARNING**: The Checker always tries to upgrade `pip` and some used Python packages. If you are using Python for other reasons and need to keep particular version, be advised to make your own backup or prepare a separate environment.

### Portable release
1. Download The Checker from here: https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/releases/latest<br/>Click on the link and then click on the `HAFS-Update-Checkers_Win7x86-Portable.zip` or `HAFS-Update-Checkers_Win10x64-Portable.zip` link to download it
2. Extract the ZIP to a folder
3. Go to the extracted folder, double-click the `start-Windows.bat` file and follow the instructions on-screen

NOTE: If The Checker looks like it has frozen, then try disabling `quickEdit` by running the `fixQuickedit.reg` file before running `start-Windows.bat`

**WARNING**: The Checker always tries to upgrade `pip` and some used Python packages. If you have Python installed on the system for other reasons and need to keep particular version, be advised to make your own backup or prepare a separate environment.

### Pro-tip & Configuration
Not all market regions get the same versions for all hearing aids fitting software. In case you see newer versions from some forums or sites yet the checkers report older ones, try changing `target market` on-the-fly to other countries to get alternative results. You can check [Versions](https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/wiki/Versions) information from our Wiki.

To change checking variables such as (target) `Market` or (spoof) `Version`, simply edit `config.ini` with any plain-text editor. This file is sectioned by hearing aid brands.

This project will try to keep up changing default target market for most up-to-date results. Scripts automatically fetch this information from this project (*LiveUpdate*-ish) without needing to re-download the whole release package.

### Pre-requirement: Install Python
For Standard release of The Checker, the following steps need to be done **ONCE** on each system:
1. Go to: https://www.python.org/downloads/
2. Download and install the latest version of Python, according to your operation system environment (such as Windows 64-bit); make sure you select `Add python.exe to PATH` in the start of the installer
3. **Reboot your computer**

NOTE: If you run The Checker (on Windows OS) without Python installed yet, The Checker will refuse to run and bring you to Python download page instead.

NOTE: The portable releases (`HAFS-Update-Checkers_Win7x86-Portable.zip` and `HAFS-Update-Checkers_Win10x64-Portable.zip`) are bundled with Windows x86/x64 version of Python respectively, thus can work on Windows x86/x64 system without needing to install Python first.
