import configparser
import os
import datetime
import requests
import json
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader
import rot_codec

just_fix_windows_console()

print("\n\n")
print("==================================================")
print("=           " + Style.BRIGHT + Fore.RED + "MedRx" + Style.RESET_ALL + " Studio Update Checker           =")
print("="*(47-len(libhearingdownloader.downloaderVersion)) + " " + Fore.GREEN + libhearingdownloader.downloaderVersion + Style.RESET_ALL + " =")

turboFile = Path("turbo.txt")
if not turboFile.is_file():
    libhearingdownloader.printWaranty()

disclaimer = [
    "DISCLAIMER",
    "",
    "The contributors of the Hearing Aids Fitting Software Update Checkers (\"The Checker\")",
    "do not take any responsability for what you do with The Checker.",
    "",
    "MedRx is a trademark of MedRx Inc.",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by",
    "MedRx, Inc.",
    "Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software.",
    "The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

# Get MedRx Studio update from the webpage with current time to prevent cache
currentTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
jsonURL = "https://medrx-support.com/Studio/Studio.update.json?nocache=" + currentTime

print("\n\nFetching Data...")

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        rawJsonData = requests.get(jsonURL)
        rawJsonDataText = rawJsonData.text
        if rawJsonDataText.startswith(u'\ufeff'):
            rawJsonDataText = rawJsonDataText.encode('utf8')[3:].decode('utf8')
        data = json.loads(rawJsonDataText)
        relVer = data[0]['Version']
        break
    except:
        pass

    updaterRetries -= 1
if (updaterRetries == 0):
    print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": Update server could not be reached")
    exit(1)

if (libhearingdownloader.verboseDebug):
    print(rawJsonData.text)

print("\n\nThe latest available MedRx Studio version is " + Style.BRIGHT + Fore.GREEN + "v" + relVer + Style.RESET_ALL)

exit(1)

availableFiles = [] # List of available files
availableFilesCount = len(data['assets'])
while availableFilesCount > 0:
    availableFilesCount -= 1
    availableFiles.append( (data['tag_name'], os.path.basename(data['assets'][availableFilesCount]['browser_download_url']), data['assets'][availableFilesCount]['browser_download_url']) )

availableFiles.reverse()

if (libhearingdownloader.verboseDebug):
    print(availableFiles)

# Select outputDir and targetFile
outputDir = libhearingdownloader.selectOutputFolder()
targetFile = availableFiles[libhearingdownloader.selectFromList(availableFiles)]

# Create download folder
downloadVer = 'Update Checker ' + targetFile[0]
outputDir += '.'.join(downloadVer.split('.')) + "/"
print("\n\n")

# Download file
libhearingdownloader.downloadFile(targetFile[2], outputDir + targetFile[1], "Downloading " + targetFile[1])

print("\n\nDownload Complete!")
