import os
import requests
import json
import re
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingchecker

just_fix_windows_console()

print("\n\n")
ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
titleText = Style.BRIGHT + Fore.YELLOW + "Hearing Aids Fitting Software Update Checkers" + Style.RESET_ALL
titleTextFooter = Back.BLUE + " Self Update Checker " + Style.RESET_ALL
titleWidth = libhearingchecker.checkerTitleWidth
titleLenth = len(ansi_escape.sub('', titleText))
if (titleLenth > (titleWidth - 4)):
    titleWidth = round(titleLenth/2)*2+4

print("="*titleWidth)
print("=" + " "*(round((titleWidth-2-titleLenth)/2)-(round((titleWidth-2-titleLenth)/2)*2)+(titleWidth-2-titleLenth)) + titleText + " "*round((titleWidth-2-titleLenth)/2) + "=")
print("="*(titleWidth-1-len(ansi_escape.sub('', titleTextFooter))) + titleTextFooter + "=")
print("\n")
print("Checking update from " + Fore.CYAN + "https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/" + Style.RESET_ALL + " ...")

updaterRetries = libhearingchecker.updaterRetries
while updaterRetries > 0:
    try:
        rawJsonData = requests.get("https://api.github.com/repos/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/releases/latest")
        data = json.loads(rawJsonData.text)
        break
    except:
        pass

    updaterRetries -= 1
if (updaterRetries == 0):
    print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": Update server could not be reached")
    exit(1)

if (libhearingchecker.verboseDebug):
    print(rawJsonData.text)

print("\n\nThe latest available version is " + Style.BRIGHT + Fore.GREEN + data['tag_name'] + Style.RESET_ALL)
if (libhearingchecker.isPreRelease):
    if (data['tag_name'] == libhearingchecker.lastCheckerVersion):
        print("\nYou are using " + Fore.GREEN + libhearingchecker.checkerVersion + Style.RESET_ALL + "\n")
    else:
        print("\nYou are using " + Style.BRIGHT + Fore.RED + "OUTDATED " + Style.RESET_ALL + Fore.RED + libhearingchecker.checkerVersion + Style.RESET_ALL + "\n")
elif (data['tag_name'] == libhearingchecker.checkerVersion):
    print("\nYou are using " + Fore.GREEN + libhearingchecker.checkerVersion + Style.RESET_ALL + "\n")
    print("No update is available.\n")
    print("You can still download this version again.\n")
    # exit(1)
else:
    print("\nYou are using " + Fore.RED + libhearingchecker.checkerVersion + Style.RESET_ALL + "\n")

availableFiles = [] # List of available files
availableFilesCount = len(data['assets'])
while availableFilesCount > 0:
    availableFilesCount -= 1
    releaseFileName = os.path.basename(data['assets'][availableFilesCount]['browser_download_url'])
    if ("Portable" in releaseFileName):
        if ("Win10" in releaseFileName):
            releaseFileDescription = data['tag_name'] + " (Portable for 64-bit Windows 10+)"
        elif ("Win7" in releaseFileName):
            releaseFileDescription = data['tag_name'] + " (Portable for 32-bit Windows 7+)"
        else:
            releaseFileDescription = data['tag_name'] + " (Portable)"
    else:
        releaseFileDescription = data['tag_name'] + " (Standard)"
    availableFiles.append( (releaseFileDescription, releaseFileName, data['assets'][availableFilesCount]['browser_download_url']) )

availableFiles.reverse()

if (libhearingchecker.verboseDebug):
    print(availableFiles)

# Select outputDir and targetFile
outputDir = libhearingchecker.selectOutputFolder()
targetFile = availableFiles[libhearingchecker.selectFromList(availableFiles)]

# Create download folder
downloadVer = 'Update Checker ' + targetFile[0]
outputDir += '.'.join(downloadVer.split('.')) + "/"
print("\n\n")

# Download file
libhearingchecker.downloadFile(targetFile[2], outputDir + targetFile[1], "Downloading " + targetFile[1])

print("\n\nDownload Complete!")
