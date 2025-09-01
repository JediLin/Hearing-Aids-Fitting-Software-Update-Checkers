#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import os
import requests
import lxml.html
import re
from urllib.parse import urlparse
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader

just_fix_windows_console()

print("\n\n")
print("==================================================")
print("=      " + Style.BRIGHT + Fore.GREEN + "Phonak Roger" + Style.RESET_ALL + " Upgrader Update Checker      =")
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
    "Roger is a trademark of Sonova AG",
    "Phonak is a trademark of Sonova AG",
    "Sonova is a trademark of Sonova AG",
    "Phonak is a subsidiary of Sonova AG",
    "Phonak Roger Upgrader is created by Phonak",
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

# Get Phonak Roger Upgrader update from the webpage
ruURI = "https://www.phonak.com/en-int/hearing-devices/microphones/roger-upgrader"
try:
    test = requests.get(ruURI)
    dom = lxml.html.fromstring(test.content)
    hrefs = [x for x in dom.xpath('//a/@href') if '//' in x and 'zip' in x]
    link0 = hrefs[0].replace('%20', ' ')
    filename0 = re.sub(r"\....\.coredownload", "", os.path.basename(urlparse(link0).path))
    title0 = "Roger Upgrader Software v1." + re.sub(r"\.zip", "", re.sub(r"[Rr]oger.*[Uu]pgrader1\.*", "", filename0))
except:
    link0 = ""
    filename0 = "--"
    title0 = "NOT FOUND"

# Define list of valid versions and their download links
validVersions = [
    ("Current Downloads", "--"),
    ("=================", "--"),
    (title0, filename0, link0),
    (" ", "--"),
    ("Archived Downloads", "--"),
    ("==================", "--"),
    ("Roger Upgrader Software v1.31", "rogerupgrader131.zip", "https://www.phonak.com/content/dam/phonak/en/documents/packages/rogerupgrader131.zip.coredownload.zip"),
    ("Roger Upgrader Software v1.30", "Roger_Upgrader1.30.zip", "https://www.phonak.com/content/dam/phonak/en/documents/packages/Roger_Upgrader1.30.zip.coredownload.zip"),
    ("Roger Upgrader Software v1.29", "Roger_Upgrader1.29.zip", "https://www.phonak.com/content/dam/phonak/en/documents/packages/Roger_Upgrader1.29.zip.coredownload.zip"),
    ("Roger Upgrader Software v1.28", "Roger Upgrader1.28.zip", "https://www.phonak.com/content/dam/phonak/en/documents/packages/Roger Upgrader1.28.zip.coredownload.zip"),
    ("Roger Upgrader Software v1.27", "Roger Upgrader1.27.zip", "https://www.phonak.com/content/dam/phonak/en/documents/packages/Roger Upgrader1.27.zip.coredownload.zip"),
]
if(link0 == ""):
    print("\n\nThe latest available version is " + Fore.GREEN + validVersions[6][0] + Style.RESET_ALL + "\n\n")
else:
    print("\n\nThe latest available version is " + Fore.GREEN + title0 + Style.RESET_ALL + "\n\n")

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
libhearingdownloader.downloadFile(validVersions[targetVersion][2], outputDir + re.sub(r"\....\.coredownload", "", validVersions[targetVersion][2].split("/")[-1]), "Downloading " + validVersions[targetVersion][0])

print("\n\nDownload Complete!")
