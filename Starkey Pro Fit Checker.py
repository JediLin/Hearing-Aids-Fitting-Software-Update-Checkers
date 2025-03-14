#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import os
import datetime
import html
import ast
import json
import requests
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader

just_fix_windows_console()

print("\n\n")
print("==================================================")
print("=         " + Style.BRIGHT + Fore.BLUE + "Starkey" + Style.RESET_ALL + " Pro Fit Update Checker         =")
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
    "Starkey is a trademark of Starkey Laboratories, Inc.",
    "Pro Fit is created by Starkey Laboratories, Inc.",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by",
    "Starkey Laboratories, Inc.",
    "Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software.",
    "The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

# Starkey updater API will check system time...
currentTime = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%m/%d/%Y %H:%M:%S')
headers = {
    "Content-Type": "application/json; charset=utf-8"
}

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        postUrl = 'https://inspireupdater.com/api/Update'
        # Please change geoIP country/region to match your IP address. The update server may check it.
        geoIP = 'Taiwan'
        # Download version data, pretending installed ProFit v2.0.10074.0
        baseVer = '2.0.10074.0'
        rawPostData = '{"ClientID":"00000000-0000-0000-0000-000000000000","ClientID2":"00000000-0000-0000-0000-000000000000+0000000000000000000","Application":"ProFit","ApplicationProperties":[{"Name":"Version","TypeName":"System.String","Value":"' + baseVer + '"},{"Name":"manufacturer","TypeName":"System.String","Value":"Starkey"},{"Name":"targetAudience","TypeName":"System.String","Value":"Starkey International English"},{"Name":"locale","TypeName":"System.String","Value":"en"},{"Name":"Country","TypeName":"System.String","Value":"' + geoIP + '"},{"Name":"MachineName","TypeName":"System.String","Value":"0000"},{"Name":"Time","TypeName":"System.DateTime","Value":"' + currentTime + '"}],"TestMode":false}'
        rawJsonData = requests.post(postUrl, headers=headers, data = rawPostData, verify='inspireupdater-com-chain.pem')
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
    print(rawJsonData.text)

if (data['Update'] is None):
    print("\n\nNo update available since v" + baseVer + " (" + geoIP + ").")
    exit(1)

appVer = data['Update']['Title'] + ' (' + data['Update']['Version'] + ')'
print("\n\nThe latest available version is " + Fore.GREEN + appVer + Style.RESET_ALL)
print("\n" + data['Update']['Description'] + "\n\n")
filesList = json.dumps(ast.literal_eval(str(data['Update']['Files'][0])))
fileData = json.loads(filesList)

availableFiles = [] # List of available files
availableFiles.append( (appVer, os.path.basename(fileData['Url']), fileData['Url']) )

if (libhearingdownloader.verboseDebug):
    print(availableFiles)

# Select outputDir and targetFile
outputDir = libhearingdownloader.selectOutputFolder()
targetFile = availableFiles[libhearingdownloader.selectFromList(availableFiles)]

# Create download folder
downloadVer = 'Starkey ' + targetFile[0]
outputDir += '.'.join(downloadVer.split('.')) + "/"
print("\n\n")

# Download file
libhearingdownloader.downloadFile(targetFile[2], outputDir + targetFile[1], "Downloading " + targetFile[1])

print("\n\nDownload Complete!")
