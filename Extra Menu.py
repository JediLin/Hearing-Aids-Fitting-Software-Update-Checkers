import os
import requests
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader

just_fix_windows_console()

# clean screen
print("\033c\033[3J", end='')

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        checkerCommits = requests.get("https://api.github.com/repos/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/commits")
        lastCommitDate = checkerCommits.json()[0]['commit']['committer']['date'][:10]
        lastCommitId = checkerCommits.json()[0]['sha'][:7]
        break
    except:
        lastCommitDate = "???"
        lastCommitId = "???"
        pass

    updaterRetries -= 1

turboFile = Path("turbo.txt")

downloaders = [
    (Style.RESET_ALL + Style.DIM + "...Back to Main Menu" + Style.RESET_ALL, "", "Checker Menu.py"),
    (Style.RESET_ALL + "Show version changes", "", "README.py"),
    (Style.RESET_ALL + "Get " + Back.RED + " Pre-release " + Style.RESET_ALL + " work-in-progress version" + Style.RESET_ALL + "\n    (Last update: " + lastCommitDate + ", commit #" + lastCommitId + ")\n    " + Style.DIM + "-------------------------------------------" + Style.RESET_ALL, "", "PreRelease.py") if not turboFile.is_file() else (Style.RESET_ALL + "Get " + Back.RED + " Pre-release " + Style.RESET_ALL + " work-in-progress version" + Style.RESET_ALL + "\n    (Last update: " + lastCommitDate + ", commit #" + lastCommitId + ")", "", "PreRelease.py"),
    (Style.RESET_ALL + "Quick Scan\n    " + Style.DIM + "-------------------------------------------" + Style.RESET_ALL, "", "Quick Scan.py") if turboFile.is_file() else ("", "--"),
    (Style.RESET_ALL + "Sonova " + Style.BRIGHT + Fore.GREEN + "Phonak" + Style.RESET_ALL + " Target MEDIA" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Phonak Target Media Checker.py"),
    (Style.RESET_ALL + "Sonova " + Style.BRIGHT + Fore.GREEN + "Phonak" + Style.RESET_ALL + " Target SOUNDS" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Phonak Target Sounds Checker.py"),
    (Style.RESET_ALL + "Sonova " + Style.BRIGHT + Fore.GREEN + "Phonak Roger" + Style.RESET_ALL + " Upgrader" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Phonak Roger Upgrader Checker.py"),
    (Style.RESET_ALL + "Demant " + Style.BRIGHT + Fore.MAGENTA + "Oticon" + Style.RESET_ALL + " Genie 2 (2024)" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Oticon Genie 2 2024 Checker.py"),
    (Style.RESET_ALL + "Demant " + Style.BRIGHT + Fore.MAGENTA + "Oticon" + Style.RESET_ALL + " Genie 2 (Legacy)" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Oticon Genie 2 Checker.py"),
    (Style.RESET_ALL + "Demant " + Style.BRIGHT + Fore.MAGENTA + "Oticon" + Style.RESET_ALL + " Genie (Legacy)" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Oticon Genie Checker.py"),
    (Style.RESET_ALL + "Demant " + Style.BRIGHT + Fore.RED + "Bernafon" + Style.RESET_ALL + " OasisNXT Custom" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Bernafon OasisNXT Custom 2024 Checker.py"),
    (Style.RESET_ALL + "Demant " + Style.BRIGHT + Fore.RED + "Bernafon" + Style.RESET_ALL + " OasisNXT (Legacy)" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Bernafon OasisNXT Checker.py"),
    (Style.RESET_ALL + "Demant " + Style.BRIGHT + Fore.CYAN + "Sonic" + Style.RESET_ALL + " ExpressFit Pro (Legacy)" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Sonici ExpressFit Checker.py"),
    (Style.RESET_ALL + "Demant " + Style.BRIGHT + Fore.BLUE + "Philips" + Style.RESET_ALL + " HearSuite (Legacy)" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Philips HearSuite Checker.py"),
    (Style.RESET_ALL + Style.BRIGHT + Fore.BLUE + "Starkey" + Style.RESET_ALL + " Inspire OS" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Starkey Inspire Checker.py"),
    (Style.RESET_ALL + Style.BRIGHT + Fore.BLUE + "Starkey" + Style.RESET_ALL + " PatientBase" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Starkey PatientBase Checker.py"),
    (Style.RESET_ALL + Style.BRIGHT + Fore.CYAN + "HIMSA" + Style.RESET_ALL + " Noahlink Wireless" + Style.DIM + " Update Checker" + Style.RESET_ALL + "\n    " + Style.DIM + "-------------------------------------------" + Style.RESET_ALL, "", "HIMSA Noahlink Wireless Checker.py"),
    (Style.RESET_ALL + "ReBrand Code Viewer", "", "ReBrand Code.py"),
    (Style.RESET_ALL + Style.DIM + "...Visit project page with default web browser" + Style.RESET_ALL, "", "GitHub Page.py"),
]

print("")
print("===============================================")
print("=  " + Style.BRIGHT + Fore.YELLOW + "Extra and Legacy Software Update Checkers" + Style.RESET_ALL + "  =")
print("================================= " + Fore.GREEN + libhearingdownloader.downloaderVersion + Style.RESET_ALL + " =")
if (os.name != "nt"):
    print("NOTE: You are running The Checker on an Unix (*NIX) or mac Operating System. Hearing aids software requires Windows OS to run, but can still be checked on Unix (*NIX) or mac OS")

selectedDownloader = libhearingdownloader.selectFromList(downloaders, "checker", numberSeperator=')', confirmationCheck=False)

os.system('python ./"' + downloaders[selectedDownloader][2] + '"')
