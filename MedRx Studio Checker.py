import configparser
import os
import datetime
import requests
import lxml.html
import json
from urllib.parse import urlparse
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader
import rot_codec

just_fix_windows_console()

print("\n\n")
print("==================================================")
print("=           " + Style.BRIGHT + Fore.RED + "MedRx" + Style.RESET_ALL + " Studio Update Checker          =")
print("="*(47-len(libhearingdownloader.downloaderVersion)) + " " + Fore.GREEN + libhearingdownloader.downloaderVersion + Style.RESET_ALL + " =")

turboFile = Path("turbo.txt")
if not turboFile.is_file():
    libhearingdownloader.printWarranty()

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

# Read configuration file
config = configparser.ConfigParser()
config.read('config.ini')
releaseChannel = config.get('MedRx', 'ReleaseChannel', fallback='Studio')

# Get MedRx Studio update from the webpage with current time to prevent cache
currentTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
jsonURL = rot_codec.rot47_decode("9EEADi^^>65CI") + "-" + rot_codec.rot47_decode("DFAA@CE]4@>^$EF5:@^") + releaseChannel + rot_codec.rot47_decode("]FA52E6];D@?n?@42496l") + currentTime

print("\n\nFetching Data...")

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        rawJsonData = requests.get(jsonURL)
        rawJsonDataText = rawJsonData.text
        if rawJsonDataText.startswith(u'\uFEFF'):
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

print("\n\nThe latest available MedRx Studio version is " + Fore.GREEN + "v" + relVer + Style.RESET_ALL + "\n\n")

mrsURI = rot_codec.rot47_decode("9EEADi^^>65CI") + "-" + rot_codec.rot47_decode("DFAA@CE]4@>^$EF5:@^")
try:
    test = requests.get(mrsURI)
    if (libhearingdownloader.verboseDebug):
        print(test.status_code)
        print(test.headers)
        print(test.content)
    dom = lxml.html.fromstring(test.content)
    exeHrefs = [x for x in dom.xpath('//a/@href') if '//' in x and 'exe' in x]
    zipHrefs = [x for x in dom.xpath('//a/@href') if '//' in x and 'zip' in x]
    if (libhearingdownloader.verboseDebug):
        print(exeHrefs)
        print(zipHrefs)
    exeLink = exeHrefs[0].replace('%20', ' ')
    exeFilename = os.path.basename(urlparse(exeLink).path)
    exeTitle = "MedRx Studio v" + relVer
    zipLink = zipHrefs[0].replace('%20', ' ')
    zipFilename = os.path.basename(urlparse(zipLink).path)
    zipTitle = "MedRx Sutdio v" + relVer + " complete setup packgae"
except:
    exeLink = ""
    exeFilename = "--"
    exeTitle = "NOT FOUND"
    zipLink = ""
    zipFilename = "--"
    zipTitle = "NOT FOUND"

# Define list of valid versions and their download links
validVersions = [
    (exeTitle, exeFilename, exeLink),
    (zipTitle, zipFilename, zipLink),
]

# Select outputDir and targetVersion
outputDir = libhearingdownloader.selectOutputFolder()
targetVersion = libhearingdownloader.selectFromList(validVersions)
print("\n\n")

# Create download folder
outputDir += validVersions[targetVersion][0] + "/"

if(libhearingdownloader.verboseDebug):
    print("V:" + str(targetVersion))
    print("T:" + validVersions[targetVersion][0])

# Download the file
libhearingdownloader.downloadFile(validVersions[targetVersion][2], outputDir + validVersions[targetVersion][2].split("/")[-1], "Downloading " + validVersions[targetVersion][0])

print("\n\nDownload Complete!")
