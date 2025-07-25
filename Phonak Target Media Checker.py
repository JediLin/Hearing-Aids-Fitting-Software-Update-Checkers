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
print("=       " + Style.BRIGHT + Fore.GREEN + "Phonak" + Style.RESET_ALL + " Target Media Update Checker       =")
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
    "Phonak is a trademark of Sonova AG",
    "Sonova is a trademark of Sonova AG",
    "Phonak is a subsidiary of Sonova AG",
    "Phonak Target is created by Phonak",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by",
    "Phonak or Sonova AG",
    "Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software.",
    "The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

# Read configuration file for toggles with default True
config = configparser.ConfigParser()
config.read('config.ini')
fallbackMarket = config.get('Phonak', 'Market', fallback='GB')

# Read target market from GitHub or local configuration
localMarketPath = Path("Phonak.market")
onlineMarketPath = "https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/raw/refs/heads/main/Phonak.market"
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
xmlns = "{http://cocoon.phonak.com}" # Define the xmlns

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        # checker variables, may effect the latest version available from API
        # Request the updater API (spoof older version to get whole installer files rather than "patch" installers)
        targetMarketFallback = config.get('Phonak', 'MarketFallback', fallback='US')
        hostBaseVer = config.get('Phonak', 'Version', fallback='6.0.1.695')
        baseVer = "0.0.0.0"
        hostXmlData = requests.get("https://p-svc1.phonakpro.com/1/ObjectLocationService.svc/FittingApplicationInstaller/index?appName=Phonak%20Target&appVer=" + hostBaseVer + "&dist=Phonak&country=" + targetMarket + "&subKeys=").text
        hostData = xml.fromstring(hostXmlData)
        hostAppVer = hostData[0].find(xmlns + "UpdateVersion").find(xmlns + "Version").text
        # Request the updater API with the latest version number of Phonak Target
        xmlData = requests.get("https://p-svc1.phonakpro.com/1/ObjectLocationService.svc/MediaInstaller/index?appName=Target%20Media&appVer=" + baseVer + ";" + hostAppVer + "&dist=Phonak&country=" + targetMarket + "&subKeys=").text
        if (xmlData == '<ArrayOfContentIndex xmlns="http://cocoon.phonak.com" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"/>'):
            print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": The latest available Phonak Target Media version for " + Fore.GREEN + targetMarket + Style.RESET_ALL + " market is not found!\n\nNow checking again for " + Fore.GREEN + targetMarketFallback + Style.RESET_ALL + " market...\n\n")
            targetMarket = targetMarketFallback
            hostXmlData = requests.get("https://p-svc1.phonakpro.com/1/ObjectLocationService.svc/FittingApplicationInstaller/index?appName=Phonak%20Target&appVer=" + hostBaseVer + "&dist=Phonak&country=" + targetMarket + "&subKeys=").text
            hostData = xml.fromstring(hostXmlData)
            hostAppVer = hostData[0].find(xmlns + "UpdateVersion").find(xmlns + "Version").text
            xmlData = requests.get("https://p-svc1.phonakpro.com/1/ObjectLocationService.svc/MediaInstaller/index?appName=Target%20Media&appVer=" + baseVer + ";" + hostAppVer + "&dist=Phonak&country=" + targetMarket + "&subKeys=").text
            if (xmlData == '<ArrayOfContentIndex xmlns="http://cocoon.phonak.com" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"/>'):
                print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": The latest available Phonak Target Media version for " + Fore.GREEN + targetMarket + Style.RESET_ALL + " market is not found!\n\n")
                exit(1)
        data = xml.fromstring(xmlData)
        break
    except:
        pass

    updaterRetries -= 1
if (updaterRetries == 0):
    print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": Update server could not be reached")
    exit(1)

# Previous: Get latest version number (Gets full version from xml and removes the fourth version number as that is not used in files)
# latestVersion = '.'.join((data[0].find(xmlns + "UpdateVersion").find(xmlns + "Version").text).split(".")[:-1])
# Start from v10.0.0, version number from XML doesn't include fourth number anymore.
latestVersion = data[0].find(xmlns + "UpdateVersion").find(xmlns + "Version").text
print("\n\nThe latest available Phonak Target Media version for " + Fore.GREEN + targetMarket + Style.RESET_ALL + " market is " + Fore.GREEN + "v" + latestVersion + Style.RESET_ALL + "\n\n")

# List of versions
validVersions = [
    (latestVersion, 'The latest available Phonak Target Media verion'),
#    ('6.2.8', 'The last version of Phonak Target compatible with the iCube (obsolete proprietary hearing aid programmer)'),
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
        targetVersion = input("\nPlease enter " + Fore.GREEN + "manual Target Media version" + Style.RESET_ALL + ": ")
        if (len(targetVersion.split('.')) > 3 or not targetVersion.replace('.', '').isdecimal()):
            print("\nThe version you have selected is " + Fore.RED + "invalid" + Style.RESET_ALL + ".\nPlease try again. (" + Fore.YELLOW + "hint" + Style.RESET_ALL + ": it should be in a similar format to " + Fore.GREEN + "a.b.c" + Style.RESET_ALL + " where " + Fore.GREEN + "a" + Style.RESET_ALL + ", " + Fore.GREEN + "b" + Style.RESET_ALL + ", and " + Fore.GREEN + "c" + Style.RESET_ALL + " are integers)")
            targetVersion = ''
        elif (input("\nYou have selected version (" + Fore.YELLOW + targetVersion + Style.RESET_ALL + ") are you sure you want to download it? [" + Style.DIM + "(" + Style.BRIGHT + Fore.GREEN + "Y" + Style.RESET_ALL + Style.DIM + ")" + Style.RESET_ALL + "/n] ") == "n"):
            targetVersion = ''

# Create download folder
outputDir += "Phonak Target Media " + targetVersion + "/"

# Get CDN/Download location
phonakCDNPath = data[0].find(xmlns + "Location").text

# Get list of files to download for a specified version from the XML data
print ("Downloading directory index")
filesToDownload = {}
for child in data[0].find(xmlns + "ContentInfos"):
    # Construct paths
    filesToDownload[(outputDir + child.find(xmlns + "Key").text).replace(latestVersion, targetVersion)] = (libhearingdownloader.normalizePath(phonakCDNPath, False) + libhearingdownloader.normalizePath(child.find(xmlns + "RemotePath").text, False) + child.find(xmlns + "Key").text).replace(latestVersion, targetVersion)

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
