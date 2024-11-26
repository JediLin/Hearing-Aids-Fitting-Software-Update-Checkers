import os
import time
import datetime
import urllib.request
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader

just_fix_windows_console()

currentTime = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y%m%d%H%M')
wipName = "Hearing-Aids-Fitting-Software-Update-Checkers-WIP-" + currentTime + ".zip"

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

