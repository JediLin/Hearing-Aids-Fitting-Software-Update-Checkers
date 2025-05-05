#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import os
import feedparser
from urllib.parse import urlparse
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader

just_fix_windows_console()

print("\n\n")
print("==================================================")
print("=     " + Style.BRIGHT + Fore.CYAN + "HIMSA" + Style.RESET_ALL + " Noahlink Wireless Update Checker     =")
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
    "HIMSA is a trademark of Hearing Instrument Manufacturers' Software Association.",
    "Noahlink Wireless is a trademark of Hearing Instrument Manufacturers' Software Association.",
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

# Get HIMSA Noahlink Wireless Download update using 3rd party web service (PolitePol)
newsfeed = feedparser.parse('https://politepol.com/fd/smVib0t95riP')
if(newsfeed.feed == {}):
    title0 = "NOT FOUND"
    link0 = ""
    filename0 = "--"
    title1 = title0
    link1 = link0
    filename1 = filename0
else:
    title0 = newsfeed.entries[0].title
    link0 = newsfeed.entries[0].link
    filename0 = os.path.basename(urlparse(link0).path)
    title1 = newsfeed.entries[1].title
    link1 = newsfeed.entries[1].link
    filename1 = os.path.basename(urlparse(link1).path)

# Define list of valid versions and their download links
validVersions = [
    ("Current Downloads", "--"),
    ("=================", "--"),
    (title0, filename0, link0),
    (title1, filename1, link1),
    (" ", "--"),
    ("Archived Downloads", "--"),
    ("==================", "--"),
    ("Noahlink Wireless Driver v1.1.0.0", "for Windows 10 and 11 (March 2017)", "https://himsafiles.com/NoahlinkWireless/Driver_NLW_V.1.1.0.0.exe"),
    ("Noahlink Wireless Firmware v3.3.0.0", "v2.25 (NW1) / v3.23 (NW2) (April 2025)", "https://himsafiles.com/NoahlinkWireless/NLWUpgrader_3.3.0.0.exe"),
    ("Noahlink Wireless Firmware v3.1.0.92", "v2.25 (NW1) / v3.17 (NW2) (May 2024)", "https://himsafiles.com/NoahlinkWireless/NLWUpgrader_3.1.0.92.exe"),
    ("Noahlink Wireless Firmware v2.24", "v2.24 (NW1 only)", "https://himsafiles.com/NoahlinkWireless/NLWUpgrader2.24.exe"),
]
if(newsfeed.feed == {}):
    print("\n\nThe latest available version is " + Fore.GREEN + "Firmware v3.3.0.0" + Style.RESET_ALL + " / " + Fore.GREEN + "Driver v1.1.0.0" + Style.RESET_ALL + "\n\n")
else:
    print("\n\nThe latest available version is " + Fore.GREEN + title0 + Style.RESET_ALL + " / " + Fore.GREEN + title1 + Style.RESET_ALL + "\n\n")

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
