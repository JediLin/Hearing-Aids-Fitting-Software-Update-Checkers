#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import requests
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader
import xml.etree.ElementTree as xml

just_fix_windows_console()

print("\n\n")
print("==================================================")
print("=          " + Style.BRIGHT + Fore.BLACK + "HANSATON" + Style.RESET_ALL + " scout Update Checker         =")
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
    "HANSATON is a trademark of Sonova AG",
    "Sonova is a trademark of Sonova AG",
    "HANSATON is a subsidiary of Sonova AG",
    "HANSATON scout is created by HANSATON",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by",
    "HANSATON or Sonova AG",
    "Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software.",
    "The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

print("\n\nFetching Data...")
# Yh that's right, Phonak namespace...
xmlns = "{http://cocoon.phonak.com}" # Define the xmlns

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        # checker variables, may effect the latest version available from API
        # Request the updater API (spoof older version to get whole installer files rather than "patch" installers)
        targetMarket = "GB"
        baseVer="5.1.0.26954"
        xmlData = requests.get("https://svc.myunitron.com/1/ObjectLocationService.svc/FittingApplicationInstaller/index?appName=HANSATON%20scout&appVer=" + baseVer + "&dist=Balance&country=" + targetMarket + "&subKeys=").text
        data = xml.fromstring(xmlData)
        break
    except:
        pass

    updaterRetries -= 1
if (updaterRetries == 0):
    print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": Update server could not be reached")
    exit(1)

# Get latest version number (Gets full version from xml and removes the fourth version number as that is not used in files)
latestVersion = '.'.join((data[0].find(xmlns + "UpdateVersion").find(xmlns + "Version").text).split(".")[:-1])
print("\n\nThe latest available HANSATON scout version is " + Fore.GREEN + "v" + latestVersion + Style.RESET_ALL + "\n\n")

# List of versions
validVersions = [
    (latestVersion, 'The latest available HANSATON scout verion'),
    ('manual', 'Manually specify a version (' + Fore.RED + 'WARNING' + Style.RESET_ALL + ': ADVANCED USERS ONLY)')
]

# Select outputDir and targetVersion
outputDir = libhearingdownloader.selectOutputFolder()
targetVersion = validVersions[libhearingdownloader.selectFromList(validVersions)][0]
print("\n\n")


# Logic for "special" versions
if (targetVersion == 'latest'):
    targetVersion = latestVersion
elif (targetVersion == 'manual'):
    targetVersion = ''
    while not targetVersion:
        targetVersion = input("\nPlease enter " + Fore.GREEN + "manual scout version" + Style.RESET_ALL + ": ")
        if (len(targetVersion.split('.')) > 3 or not targetVersion.replace('.', '').isdecimal()):
            print("\nThe version you have selected is " + Fore.RED + "invalid" + Style.RESET_ALL + ".\nPlease try again. (" + Fore.YELLOW + "hint" + Style.RESET_ALL + ": it should be in a similar format to " + Fore.GREEN + "a.b.c" + Style.RESET_ALL + " where " + Fore.GREEN + "a" + Style.RESET_ALL + ", " + Fore.GREEN + "b" + Style.RESET_ALL + ", and " + Fore.GREEN + "c" + Style.RESET_ALL + " are integers)")
            targetVersion = ''
        elif (input("\nYou have selected version (" + Fore.YELLOW + targetVersion + Style.RESET_ALL + ") are you sure you want to download it? [" + Style.DIM + "(" + Style.BRIGHT + Fore.GREEN + "Y" + Style.RESET_ALL + Style.DIM + ")" + Style.RESET_ALL + "/n] ") == "n"):
            targetVersion = ''

# Create download folder
outputDir += "HANSATON scout " + targetVersion + "/"

# Get CDN/Download location
hansatonCDNPath = data[0].find(xmlns + "Location").text

# Get list of files to download for a specified version from the XML data
print ("Downloading directory index")
filesToDownload = {}
for child in data[0].find(xmlns + "ContentInfos"):
    # Construct paths
    filesToDownload[(outputDir + child.find(xmlns + "Key").text).replace(latestVersion, targetVersion)] = (libhearingdownloader.normalizePath(hansatonCDNPath, False) + libhearingdownloader.normalizePath(child.find(xmlns + "RemotePath").text, False) + child.find(xmlns + "Key").text).replace(latestVersion, targetVersion)

# Download and save the files
print("Downloading " + str(len(filesToDownload.keys())) + " files\n")
currentFile = 1
for fileToDownload in filesToDownload.keys():
    if (libhearingdownloader.verboseDebug):
        print(filesToDownload[fileToDownload])

    # Download file
    libhearingdownloader.downloadFile(filesToDownload[fileToDownload], fileToDownload, "Downloading " + fileToDownload.split("/")[-1] + " (" + str(currentFile) + "/" + str(len(filesToDownload.keys())) + ")")

    currentFile += 1

print("\n\nDownload Complete!")
