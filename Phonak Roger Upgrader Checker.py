#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import os
import re
import feedparser
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

# Get Phonak Roger Upgrader Download update using 3rd party web service (PolitePol)
newsfeed = feedparser.parse('https://politepol.com/fd/uGyRlUyOYsXs.xml')
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
    ("Roger Upgrader Software v1.30", "Roger_Upgrader1.30.zip", "https://www.phonak.com/content/dam/phonak/en/documents/packages/Roger_Upgrader1.30.zip.coredownload.zip"),
    ("Roger Upgrader Software v1.29", "Roger_Upgrader1.29.zip", "https://www.phonak.com/content/dam/phonak/en/documents/packages/Roger_Upgrader1.29.zip.coredownload.zip"),
    ("Roger Upgrader Software v1.28", "Roger Upgrader1.28.zip", "https://www.phonak.com/content/dam/phonak/en/documents/packages/Roger Upgrader1.28.zip.coredownload.zip"),
    ("Roger Upgrader Software v1.27", "Roger Upgrader1.27.zip", "https://www.phonak.com/content/dam/phonak/en/documents/packages/Roger Upgrader1.27.zip.coredownload.zip"),
    ("Roger On™ firmware update quick guide", "PH_QuickGuide_RogerOnUpgrader_210x297_EN.pdf", "https://www.phonak.com/content/dam/celum/phonak/master-assets/en/documents/accessories/roger/PH_QuickGuide_RogerOnUpgrader_210x297_EN.pdf.coredownload.pdf"),
]
if(newsfeed.feed == {}):
    print("\n\nThe latest available version is " + Fore.GREEN + "Roger Upgrader Software v1.30" + Style.RESET_ALL + "\n\n")
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
libhearingdownloader.downloadFile(validVersions[targetVersion][2], outputDir + re.sub(r"\....\.coredownload", "", validVersions[targetVersion][2].split("/")[-1]), "Downloading " + validVersions[targetVersion][0])

print("\n\nDownload Complete!")
