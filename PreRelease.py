import os
import time
import datetime
import requests
import urllib.request
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader

just_fix_windows_console()

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        checkerCommits = requests.get("https://api.github.com/repos/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/commits")
        lastCommitDate = checkerCommits.json()[0]['commit']['committer']['date'][:10]
        lastCommitId = checkerCommits.json()[0]['sha'][:7]
        break
    except:
        lastCommitDate = ""
        lastCommitId = ""
        pass

    updaterRetries -= 1

currentTime = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y%m%d%H%M')
wipName = "Hearing-Aids-Fitting-Software-Update-Checkers-WIP(" + lastCommitDate + "_" + lastCommitId + ")-" + currentTime + ".zip"

print("\nYou are about to download the pre-release work-in-progress version.\nPlease use it AT YOUR OWN RISK!\n")

# Select outputDir and targetFile
outputDir = libhearingdownloader.selectOutputFolder()

# Create download folder
downloadVer = 'Update Checker Pre-release WIP'
outputDir += '.'.join(downloadVer.split('.')) + "/"

# Download file
print("\nDownloading " + Fore.GREEN + os.path.basename(wipName) + Style.RESET_ALL + " ...")
os.makedirs('/'.join(outputDir.split("/")[:-1]), exist_ok=True) # Create path if it doesn't exist

urllib.request.urlretrieve("https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/archive/refs/heads/main.zip", outputDir + os.path.basename(wipName))

print("\n\nDownload Complete!")

# Unlock TURBO mode
turboFile = Path("turbo.txt")
if not turboFile.is_file():
    with turboFile.open('w') as file:
        file.write("Delete (or rename) this file to disable TURBO mode.")
    print(Fore.YELLOW + "==============================================" + Style.RESET_ALL)
    print(Fore.YELLOW + "=           " + Style.BRIGHT + "Achievement Unlocked!!" + Style.NORMAL + "           =" + Style.RESET_ALL)
    print(Fore.YELLOW + "=  " + Style.DIM + Fore.WHITE + "----------------------------------------" + Style.NORMAL + Fore.YELLOW + "  =" + Style.RESET_ALL)
    print(Fore.YELLOW + "=  " + Fore.WHITE + "You are brave and dare to try something" + Fore.YELLOW + "   =" + Style.RESET_ALL)
    print(Fore.YELLOW + "=  " + Fore.WHITE + "new and unknown." + Fore.YELLOW + "                          =" + Style.RESET_ALL)
    print(Fore.YELLOW + "=  " + Style.DIM + Fore.WHITE + "----------------------------------------" + Style.NORMAL + Fore.YELLOW + "  =" + Style.RESET_ALL)
    print(Fore.YELLOW + "=  " + Fore.WHITE + "To reward your courage to take risk," + Fore.YELLOW + "      =" + Style.RESET_ALL)
    print(Fore.YELLOW + "=  " + Fore.WHITE + "from now on, you can use The Checker in" + Fore.YELLOW + "   =" + Style.RESET_ALL)
    print(Fore.YELLOW + "=  " + Style.BRIGHT + Fore.RED + "T" + Fore.YELLOW + "U" + Fore.CYAN + "R" + Fore.GREEN + "B" + Fore.BLUE + "O" + Style.NORMAL + Fore.WHITE + " mode. Enjoy!" + Fore.YELLOW + "                        =" + Style.RESET_ALL)
    print(Fore.YELLOW + "==============================================" + Style.RESET_ALL)
else:
    print("\nNote: if you want to disable " + Style.BRIGHT + Fore.RED + "T" + Fore.YELLOW + "U" + Fore.CYAN + "R" + Fore.GREEN + "B" + Fore.BLUE + "O" + Style.RESET_ALL + " mode, simply delete or rename the " + Fore.GREEN + "turbo.txt" + Style.RESET_ALL + " file.")
