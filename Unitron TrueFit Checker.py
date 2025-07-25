#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import configparser
import requests
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
from iso3166 import countries
import libhearingdownloader
import xml.etree.ElementTree as xml

just_fix_windows_console()

print("\n\n")
print("==================================================")
print("=         " + Style.BRIGHT + Fore.CYAN + "Unitron" + Style.RESET_ALL + " TrueFit Update Checker         =")
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
    "Unitron is a trademark of Sonova AG",
    "Sonova is a trademark of Sonova AG",
    "Unitron is a subsidiary of Sonova AG",
    "Unitron TrueFit is created by Unitron",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by",
    "Unitron or Sonova AG",
    "Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software.",
    "The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

# Read configuration file for toggles with default True
config = configparser.ConfigParser()
config.read('config.ini')
fallbackMarket = config.get('Unitron', 'Market', fallback='FR')

# Read target market from GitHub or local configuration
localMarketPath = Path("Unitron.market")
onlineMarketPath = "https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/raw/refs/heads/main/Unitron.market"
defaultMarketSrc = ""
try:
    onlineMarketFile = requests.get(onlineMarketPath)
    onlineMarket = onlineMarketFile.text.split("\n", 1)[0]
    if (onlineMarket.isalpha()):
        defaultMarket = onlineMarket
        defaultMarketSrc = "online-"
    else:
        if localMarketPath.is_file():
            with localMarketPath.open("r") as localMarketFile:
                localMarket = localMarketFile.read().split("\n", 1)[0]
                if (localMarket.isalpha()):
                    defaultMarket = localMarket
                    defaultMarketSrc = "local-"
                else:
                    defaultMarket = fallbackMarket
        else:
            defaultMarket = fallbackMarket
except:
    if localMarketPath.is_file():
        with localMarketPath.open("r") as localMarketFile:
            localMarket = localMarketFile.read().split("\n", 1)[0]
            if (localMarket.isalpha()):
                defaultMarket = localMarket
                defaultMarketSrc = "local-"
            else:
                defaultMarket = fallbackMarket
    else:
        defaultMarket = fallbackMarket

# Target market input
inputMarket = input("\nPlease enter " + Fore.GREEN + "target market country code" + Style.RESET_ALL + " [" + defaultMarketSrc + "default: " + Fore.YELLOW + defaultMarket + Style.RESET_ALL + "]: ")
if (inputMarket == "" or inputMarket.lower() == defaultMarket.lower()):
    targetMarket = defaultMarket
    print("\nChecking for " + Fore.GREEN + targetMarket + Style.RESET_ALL + " market...")
else:
    try:
        targetMarket = countries.get(inputMarket).alpha2
        print("\nChecking for " + Fore.GREEN + targetMarket + Style.RESET_ALL + " market...")
    except:
        targetMarket = defaultMarket
        print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": Market code is invalid. Using " + Fore.GREEN + defaultMarket + Style.RESET_ALL + " instead...")

print("\n\nFetching Data...")
# Yh that's right, Phonak namespace...
xmlns = "{http://cocoon.phonak.com}" # Define the xmlns

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        # checker variables, may effect the latest version available from API
        # Request the updater API (spoof older version to get whole installer files rather than "patch" installers)
        baseVer = config.get('Unitron', 'Version', fallback='5.1.0.25391')
        xmlData = requests.get("https://svc.myunitron.com/1/ObjectLocationService.svc/FittingApplicationInstaller/index?appName=Unitron%20TrueFit&appVer=" + baseVer + "&dist=Unitron&country=" + targetMarket + "&subKeys=").text
        data = xml.fromstring(xmlData)
        break
    except:
        pass

    updaterRetries -= 1
if (updaterRetries == 0):
    print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": Update server could not be reached")
    exit(1)

# Get latest version number (Gets full version from xml and removes the fourth version number as that is not used in files)
if (xmlData == '<ArrayOfContentIndex xmlns="http://cocoon.phonak.com" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"/>'):
    print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": The latest available Unitron TrueFit version for " + Fore.GREEN + targetMarket + Style.RESET_ALL + " market is not found!\n\n")
    exit(1)
else:
    latestVersion = '.'.join((data[0].find(xmlns + "UpdateVersion").find(xmlns + "Version").text).split(".")[:-1])

print("\n\nThe latest available Unitron TrueFit version for " + Fore.GREEN + targetMarket + Style.RESET_ALL + " market is " + Fore.GREEN + "v" + latestVersion + Style.RESET_ALL + "\n\n")

# List of versions
validVersions = [
    (latestVersion, 'The latest available Unitron TrueFit verion'),
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
        targetVersion = input("\nPlease enter " + Fore.GREEN + "manual TrueFit version" + Style.RESET_ALL + ": ")
        if (len(targetVersion.split('.')) > 3 or not targetVersion.replace('.', '').isdecimal()):
            print("\nThe version you have selected is " + Fore.RED + "invalid" + Style.RESET_ALL + ".\nPlease try again. (" + Fore.YELLOW + "hint" + Style.RESET_ALL + ": it should be in a similar format to " + Fore.GREEN + "a.b.c" + Style.RESET_ALL + " where " + Fore.GREEN + "a" + Style.RESET_ALL + ", " + Fore.GREEN + "b" + Style.RESET_ALL + ", and " + Fore.GREEN + "c" + Style.RESET_ALL + " are integers)")
            targetVersion = ''
        elif (input("\nYou have selected version (" + Fore.YELLOW + targetVersion + Style.RESET_ALL + ") are you sure you want to download it? [" + Style.DIM + "(" + Style.BRIGHT + Fore.GREEN + "Y" + Style.RESET_ALL + Style.DIM + ")" + Style.RESET_ALL + "/n] ") == "n"):
            targetVersion = ''

# Create download folder
outputDir += "Unitron TrueFit " + targetVersion + "/"

# Get CDN/Download location
unitronCDNPath = data[0].find(xmlns + "Location").text

# Get list of files to download for a specified version from the XML data
print ("Downloading directory index")
filesToDownload = {}
for child in data[0].find(xmlns + "ContentInfos"):
    # Construct paths
    filesToDownload[(outputDir + child.find(xmlns + "Key").text).replace(latestVersion, targetVersion)] = (libhearingdownloader.normalizePath(unitronCDNPath, False) + libhearingdownloader.normalizePath(child.find(xmlns + "RemotePath").text, False) + child.find(xmlns + "Key").text).replace(latestVersion, targetVersion)

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
