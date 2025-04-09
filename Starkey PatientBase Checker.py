#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import os
import requests
import lxml.html
from urllib.parse import urlparse
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader

just_fix_windows_console()

print("\n\n")
print("==================================================")
print("=       " + Style.BRIGHT + Fore.BLUE + "Starkey" + Style.RESET_ALL + " PatientBase Update Checker       =")
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
    "Inspire OS is created by Starkey Laboratories, Inc.",
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

# Get PatientBase update from the webpage
pbURI = "https://patientbase.starkeyhearingtechnologies.com"
fallbackDownload = "https://softwaredownload.starkey.com/PatientBase/PatientBase Setup 28.0.10003.0.exe"
try:
    test = requests.get(pbURI)
    dom = lxml.html.fromstring(requests.get(pbURI).content)
    hrefs = [x for x in dom.xpath('//a/@href') if '//' in x and 'exe' in x]
    filename0 = os.path.basename(urlparse(hrefs[0]).path).replace('%20', ' ')
    link0 = hrefs[0].replace('%20', ' ')
except:
    filename0 = "NOT FOUND"
    link0 = fallbackDownload

# Define list of valid versions and their download links (direct from CDN)
# sadly az493319.vo.msecnd.net is no longer available...
validVersions = [
    ("Current Downloads", "--"),
    ("=================", "--"),
    ("PatientBase (Latest Version)", filename0, link0),
    (" ", "--"),
    ("Archived Downloads", "--"),
    ("==================", "--"),
    ("PatientBase 28.0.10003.0", "for Pro Fit 1.0+ and Inspire 2023.1+", fallbackDownload),
#     ("PatientBase 26.0.10014.0", "for Inspire 2022.1 - 2023.0", "https://az493319.vo.msecnd.net/install/PatientBase Setup 26.0.10014.0.exe"),
#     ("PatientBase 24.0.10102.0", "for Inspire 2021.0 - 2022.0", "https://az493319.vo.msecnd.net/install/PatientBase Setup 24.0.10102.0.exe"),
#     ("PatientBase 15.0.386.0", "for Inspire 2016 - 2020", "https://az493319.vo.msecnd.net/install/PatientBase Setup 24.0.10102.0.exe"),
]
print("\n\nThe latest available version is " + Fore.GREEN + filename0 + Style.RESET_ALL + "\n\n")

# Select outputDir and targetVersion
outputDir = libhearingdownloader.selectOutputFolder()
targetVersion = libhearingdownloader.selectFromList(validVersions)
print("\n\n")

# Create download folder
outputDir += validVersions[targetVersion][0] + "/"

if(libhearingdownloader.verboseDebug):
    print("V:" + str(targetVersion))
    print("T:" + validVersions[targetVersion])

# Download the file
libhearingdownloader.downloadFile(validVersions[targetVersion][2], outputDir + validVersions[targetVersion][2].split("/")[-1], "Downloading " + validVersions[targetVersion][0])

print("\n\nDownload Complete!")
