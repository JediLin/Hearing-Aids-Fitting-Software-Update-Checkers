#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import configparser
import os
import json
import shutil
import zipfile
import requests
import rot_codec
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader

just_fix_windows_console()

print("\n\n")
print("==================================================")
print("=        " + Style.BRIGHT + Fore.WHITE + "Widex" + Style.RESET_ALL + " Compass GPS Update Checker        =")
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
    "Widex is a trademark of WS Audiology A/S",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by",
    "WS Audiology A/S",
    "Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software.",
    "The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

# Read configuration file for toggles with default True
config = configparser.ConfigParser()
config.read('config.ini')
fallbackMarket = config.get('Widex', 'Market', fallback='Main_Test_Distributor')

# Read target market from GitHub or local configuration
fallbackMarket = "Main_Test_Distributor"
localMarketPath = Path("Widex.market")
onlineMarketPath = "https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/raw/refs/heads/main/Widex.market"
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
possibleMarkets = ("Acuitis", "Albania", "Algeria", "Alternate_Test_Distributor", "Argentina", "Audigy", "Australia", "Austria", "Belarus", "Belgium", "Bolivia", "Bosnia Herzegovina", "Brazil", "Bulgaria", "Canada", "Chile", "China", "Colombia", "ConHearing", "Costa Rica", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Estonia", "F.Y.R.O.M.", "Finland", "France", "Germany", "Ghana", "Grand Audition", "Greece", "Guyana", "Hong Kong", "Huier", "Hungary", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Korea", "Kosovo", "Kuwait", "Kyrgyzstan", "Latvia", "Lebanon", "Libya", "Lithuania", "Main_Test_Distributor", "Malaysia", "Malta", "Mexico", "Mongolia", "Morocco", "Namibia", "Netherlands", "New Zealand", "Nigeria", "Norway", "Oman", "Pakistan", "Panama", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Romania", "Russia", "Saudi Arabia", "SayWhat", "Serbia", "Singapore", "Slovakia", "Slovenia", "South Africa", "Spain", "Specsavers", "Sri Lanka", "Sudan", "Sweden", "Switzerland", "Syria", "Taiwan", "Thailand", "Tunisia", "Turkey", "Ukraine", "United Arab Emirates", "United Kingdom", "Uruguay", "USA", "Venezuela", "Veteran Affairs US", "Vietnam", "Widex Monitoring System", "Yemen")
possibleMarketsSet = set(possibleMarkets)
inputMarket = input("\nPlease enter " + Fore.GREEN + "target Distributor ID (Case-Sensitive!)" + Style.RESET_ALL + " [" + defaultMarketSrc + "default: " + Fore.YELLOW + defaultMarket + Style.RESET_ALL + "]: ")
if (inputMarket == "" or inputMarket.lower() == defaultMarket.lower()):
    targetMarket = defaultMarket
    print("\nChecking for " + Fore.GREEN + targetMarket + Style.RESET_ALL + " market...")
elif (inputMarket in possibleMarketsSet):
    targetMarket = inputMarket
    print("\nChecking for " + Fore.GREEN + targetMarket + Style.RESET_ALL + " market...")
else:
    targetMarket = defaultMarket
    print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": Distributor ID is invalid. Using " + Fore.GREEN + defaultMarket + Style.RESET_ALL + " instead...")

# Base information
baseId = config.get('Widex', 'ID', fallback='CompassGPS')
baseVer = config.get('Widex', 'Version', fallback='4.8.6193.0')

# API key
apiKey = config.get('Widex', 'Key', fallback='24fbe5gacg`hcdf535dd34ed6_237347')

# Special headers for the Widex updater API
headers = {
    "Ocp-Apim-Subscription-Key": rot_codec.rot47_decode(apiKey),
    "x-ApiEnvironment": "prod",
    "x-ClientProgram": baseId+"/"+baseVer,
    "Content-Type": "application/json; charset=utf-8",
    "Host": "apimgmt.widex.com"
}

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        # Download update file list from updater API
        postUrl = rot_codec.rot47_decode("9EEADi^^2A:>8>E]H:56I]4@>^75D^G`^2A:^&A52E6n2==lECF6U3C6G:EJlE6CD6")
        rawPostData = '{"Id":"'+baseId+'","Version":"'+baseVer+'","Environment":[{"Name":"distributors","Value":"' + targetMarket + '"}]}'
        rawJsonData = requests.post(postUrl, headers=headers, data = rawPostData)
        # Expect something like {"Packages": [],"CustomProperties": {}}
        data = json.loads(rawJsonData.text)
        break
    except:
        pass

    updaterRetries -= 1
if (updaterRetries == 0):
    print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": Update server could not be reached")
    exit(1)
    
if (libhearingdownloader.verboseDebug):
    print(rawPostData)
    print("\n\nUpdate server responded:\n")
    print(rawJsonData.text)

if "statusCode" in data:
    print("\n\n" + data['message'])

if "Packages" in data:
    if (data['Packages']==[]):
        print("\n\nThe latest available " + baseId + " version is " + Fore.GREEN + "v" + baseVer + Style.RESET_ALL + "\n\n")
        print("No further update available.")
        exit(1)
    else:
        latestBaseVersion = data['Packages'][0]['Version']
        latestRevision = str(data['Packages'][0]['Revision'])
        latestVersion = latestBaseVersion + " (Revision " + latestRevision + ")"


print("\n\nThe latest available " + baseId + " version for " + Fore.GREEN + targetMarket + Style.RESET_ALL + " distributor is " + Fore.GREEN + "v" + latestVersion + Style.RESET_ALL + "\n\n")

# List of versions
validVersions = [
    (latestVersion, 'The latest available ' + baseId + ' verion'),
    ('manual', 'Manually specify a version (' + Fore.RED + 'WARNING' + Style.RESET_ALL + ': ADVANCED USERS ONLY)'),
]

# Select outputDir and targetVersion
outputDir = libhearingdownloader.selectOutputFolder()
targetVersion = validVersions[libhearingdownloader.selectFromList(validVersions)][0]
print("\n\n")

# Logic for "manual" versions
if (targetVersion == 'manual'):
    manualVersion = True
    targetVersion = ''
    while not targetVersion:
        targetBaseVersion = ''
        while not targetBaseVersion:
            targetBaseVersion = input("\nPlease enter " + Fore.GREEN + "manual Compass GPS version" + Style.RESET_ALL + ": ")
            if (not len(targetBaseVersion.split('.')) == 3 or not targetBaseVersion.replace('.', '').isdecimal()):
                print("\nThe version you have selected is " + Fore.RED + "invalid" + Style.RESET_ALL + ".\nPlease try again. (" + Fore.YELLOW + "hint" + Style.RESET_ALL + ": it should be in a similar format to " + Fore.GREEN + "a.b.c" + Style.RESET_ALL + " where " + Fore.GREEN + "a" + Style.RESET_ALL + ", " + Fore.GREEN + "b" + Style.RESET_ALL + ", and " + Fore.GREEN + "c" + Style.RESET_ALL + " are integers)")
                targetBaseVersion = ''
        targetRevision = ''
        while not targetRevision:
            targetRevision = input("\nPlease enter " + Fore.GREEN + "revision" + Style.RESET_ALL + ": ")
            if (not targetRevision.isdecimal()):
                print("\nThe revision you have selected is " + Fore.RED + "invalid" + Style.RESET_ALL + ".\nPlease try again. (" + Fore.YELLOW + "hint" + Style.RESET_ALL + ": it should be in a single integer)")
                targetRevision = ''
        targetVersion = targetBaseVersion + " (Revision " + targetRevision + ")"
        if (input("\nYou have selected version (" + Fore.YELLOW + targetVersion + Style.RESET_ALL + ") are you sure you want to download it? [" + Style.DIM + "(" + Style.BRIGHT + Fore.GREEN + "Y" + Style.RESET_ALL + Style.DIM + ")" + Style.RESET_ALL + "/n] ") == "n"):
            targetVersion = ''
else:
    manualVersion = False

# Create download folder
outputDir += "Widex Compass GPS " + targetVersion + "/"
if (libhearingdownloader.verboseDebug):
    print(outputDir)

print ("Downloading directory index")

packageResources = data['Packages'][0]['Resources']

filesToDownload = {}
if (manualVersion):
    slash = "/"
    for resourceFile in packageResources:
        filesToDownload[resourceFile['Value'].split("/")[-1]] = slash.join(resourceFile['Value'].split("/")[:-3]) + "/" + targetBaseVersion + "/" + targetRevision + "/" + resourceFile['Value'].split("/")[-1]
else:
    for resourceFile in packageResources:
        filesToDownload[resourceFile['Value'].split("/")[-1]] = resourceFile['Value']

if (libhearingdownloader.verboseDebug):
    print(filesToDownload)

# Download and save the files
print("Downloading " + str(len(filesToDownload.keys())) + " files\n")
currentFile = 1
for fileToDownload in filesToDownload.keys():
    if (libhearingdownloader.verboseDebug):
        print(filesToDownload[fileToDownload])
        print(outputDir + fileToDownload)
        print("Downloading " + fileToDownload + " (" + str(currentFile) + "/" + str(len(filesToDownload.keys())) + ")")
    # Download file
    libhearingdownloader.downloadFile(filesToDownload[fileToDownload], outputDir + fileToDownload, "Downloading " + fileToDownload + " (" + str(currentFile) + "/" + str(len(filesToDownload.keys())) + ")")

    currentFile += 1


print("\n\n")
print("Creating installer from zip")
with zipfile.ZipFile(outputDir + "Setup.exe.zip", 'r') as zipFile:
    zipFile.extractall(outputDir)

os.makedirs(outputDir + "installations/")

for fileDownloaded in filesToDownload.keys():
    if fileDownloaded != "Setup.exe.zip":
        shutil.move(outputDir + fileDownloaded, outputDir + "installations/" + fileDownloaded)
    else:
        setupFile = Path(outputDir + "Setup.exe")
        if setupFile.is_file():
            os.remove(outputDir + fileDownloaded)

print("\n\nDownload Complete!")
