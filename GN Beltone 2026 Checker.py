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
print("=         " + Style.BRIGHT + Fore.BLUE + "Beltone" + Style.RESET_ALL + " Software Update Checker        =")
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
    "Beltone does not review the content of The Checker or the source that The Checker check against",
    "Please view the source disclaimer at:"
    "http://www.supportgn.com/beltone/subsites/disclaimer.php",
    "",
    "Beltone is a trademark of GN Hearing A/S and/or its affiliates (\"GN Group\")",
    "GN is a trademark of GN Store Nord A/S",
    "Solus Pro is a trademark of GN Hearing A/S",
    "Solus Max is a trademark of GN Hearing A/S",
    "SelectaFit is a trademark of GN Hearing A/S (oh dear gosh its really unclear if it actually is or not I've got literally no idea-)",
    "GN Hearing A/S is a subsidiary of GN Store Nord A/S",
    "Beltone is a subsidiary of GN Hearing A/S",
    "Solus is created by Beltone",
    "Solus Pro is created by Beltone",
    "Solus Max is created by Beltone",
    "SelectaFit is created by Beltone"
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by",
    "Beltone, GN Hearing A/S, GN Group or GN Store Nord A/S",
    "Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software.",
    "The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

# Get Phonak Roger Upgrader update from the webpage
bsmURI = "https://www.gnhearing.com/en/products/beltone/fitting-software-download"
try:
    test = requests.get(bsmURI)
    dom = lxml.html.fromstring(test.content)
    hrefs = [x for x in dom.xpath('//a/@href') if '//' in x and 'zip' in x]
    link0 = hrefs[0].replace('%20', ' ')
    filename0 = os.path.basename(urlparse(link0).path)
    title0 = "Beltone Solus Max v" + re.sub(r"_releaseversion\.zip", "", re.sub(r"solusmax_", "", filename0))
    try:
        link1 = hrefs[1].replace('%20', ' ')
        filename1 = os.path.basename(urlparse(link1).path)
        title1 = "Beltone Solus Max v" + re.sub(r"_releaseversion\.zip", "", re.sub(r"solusmax_", "", filename1))
    except:
        link1 = ""
        filename1 = "--"
        title1 = "NOT FOUND"
except:
    link0 = ""
    filename0 = "--"
    title0 = "NOT FOUND"

# Define list of valid versions and their download links
validVersions = [
    ("Current Downloads", "--"),
    ("=================", "--"),
    (title1, filename1, link1),
    (title0, filename0, link0),
    (" ", "--"),
    ("Archived Downloads", "--"),
    ("==================", "--"),
    ("Beltone Solus Max 2.2.209.13", "solusmax_2.2.209.13_releaseversion.zip", "https://supportgn.gnonlineservices.com/downloads/beltone/solusmax_2.2.209.13_releaseversion.zip"),
    ("Beltone Solus Max 2.2", "solusmax_2.2.209.5_releaseversion.zip", "https://supportgn.gnonlineservices.com/downloads/beltone/solusmax_2.2.209.5_releaseversion.zip"),
    ("Beltone Solus Max 2.1 Update 2", "solusmax_2.1.305.17_releaseversion", "https://supportgn.gnonlineservices.com/downloads/beltone/solusmax_2.1.305.17_releaseversion"),
    ("Beltone Solus Max 2.0 Update 3", "solusmax_2.0.132.26_releaseversion", "https://supportgn.gnonlineservices.com/downloads/beltone/solusmax_2.0.132.26_releaseversion"),
    ("Beltone Solus Max 1.18", "Beltone_Solus_Max_1.18.324.0-ReleaseVersion.zip", "https://supportgn.gnonlineservices.com/downloads/beltone/Beltone_Solus_Max_1.18.324.0-ReleaseVersion.zip"),
    ("Beltone Solus Pro 1.10", "soluspro1.10.0.78.zip", "http://www.supportgn.com/files/beltone/soluspro1.10.0.78.zip"),
    ("Beltone Solus 2.7", "solus2.70.14.2c.zip", "http://www.supportgn.com/files/beltone/solus2.70.14.2c.zip"),
]
if(link1 == ""):
    if(link0 == ""):
        print("\n\nThe latest available version is " + Fore.GREEN + validVersions[7][0] + Style.RESET_ALL + "\n\n")
    else:
        print("\n\nThe latest available version is " + Fore.GREEN + title0 + Style.RESET_ALL + "\n\n")
else:
    print("\n\nThe latest available version is " + Fore.GREEN + title1 + Style.RESET_ALL + "\n\n")

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
