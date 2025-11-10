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
print("=         " + Style.BRIGHT + Fore.RED + "ReSound" + Style.RESET_ALL + " Software Update Checker        =")
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
    "ReSound is a trademark of GN Hearing A/S and/or its affiliates (\"GN Group\")",
    "GN is a trademark of GN Store Nord A/S",
    "Aventa is a trademark of GN Hearing A/S",
    "ReSound Smart Fit is a trademark of GN Group",
    "GN Hearing A/S is a subsidiary of GN Store Nord A/S",
    "ReSound is a subsidiary of GN Hearing A/S",
    "ReSound is created by ReSound",
    "Aventa is created by ReSound",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by",
    "ReSound, GN Hearing A/S, GN Group or GN Store Nord A/S",
    "Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software.",
    "The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

# Get ReSound Smart Fit update from the webpage
rssfURI = "https://www.gnhearing.com/en/products/resound/fitting-software-download"
try:
    test = requests.get(rssfURI)
    dom = lxml.html.fromstring(test.content)
    hrefs = [x for x in dom.xpath('//a/@href') if '//' in x and 'zip' in x]
    link0 = hrefs[0].replace('%20', ' ')
    filename0 = os.path.basename(urlparse(link0).path)
    title0 = "ReSound Smart Fit v" + re.sub(r"_releaseversion\.zip", "", re.sub(r"smartfit_", "", filename0))
    try:
        link1 = hrefs[1].replace('%20', ' ')
        filename1 = os.path.basename(urlparse(link1).path)
        title1 = "ReSound Smart Fit v" + re.sub(r"_releaseversion\.zip", "", re.sub(r"smartfit_", "", filename1))
    except:
        link1 = ""
        filename1 = "--"
        title1 = "NOT FOUND"
except:
    link0 = ""
    filename0 = "--"
    title0 = "NOT FOUND"
    link1 = ""
    filename1 = "--"
    title1 = "NOT FOUND"

# Define list of valid versions and their download links
validVersions = [
    ("Current Downloads", "--"),
    ("=================", "--"),
    (title1, filename1, link1),
    (title0, filename0, link0),
    ("manual", "Manually specify a version of ReSound Smart Fit (" + Fore.RED + "WARNING" + Style.RESET_ALL + ": ADVANCED USERS ONLY)", ""),
    (" ", "--"),
    ("Archived Downloads", "--"),
    ("==================", "--"),
    ("ReSound Smart Fit v2.2", "smartfit_2.2.209.13_releaseversion.zip", "https://supportgn.gnonlineservices.com/downloads/resound/smartfit_2.2.209.13_releaseversion.zip"),
    ("ReSound Smart Fit v2.1 Update 2", "smartfit_2.1.305.17_releaseversion.zip", "https://supportgn.gnonlineservices.com/downloads/resound/smartfit_2.1.305.17_releaseversion.zip"),
    ("ReSound Smart Fit v2.0 Update 3", "smartfit_2.0.132.26_releaseversion.zip", "https://supportgn.gnonlineservices.com/downloads/resound/smartfit_2.0.132.26_releaseversion.zip"),
    ("ReSound Smart Fit v1.18", "ReSound_Smart_Fit_1.18.324.0-ReleaseVersion.zip", "https://supportgn.gnonlineservices.com/downloads/resound/ReSound_Smart_Fit_1.18.324.0-ReleaseVersion.zip"),
    ("ReSound Aventa v2.9", "aventa2.95.7.1a.zip", "https://cdnprdsitecoresto03.azureedge.net/fittingsoftware/aventa2.95.7.1a.zip"),
    ("ReSound Pro-Counsel v1.45", "pro_counsel1.45.zip", "http://www.supportgn.com/files/resound/pro_counsel1.45.zip"),
]
if(link1 == ""):
    if(link0 == ""):
        print("\n\nThe latest available version is " + Fore.GREEN + validVersions[8][0] + Style.RESET_ALL + "\n\n")
    else:
        print("\n\nThe latest available version is " + Fore.GREEN + title0 + Style.RESET_ALL + "\n\n")
else:
    print("\n\nThe latest available version is " + Fore.GREEN + title1 + Style.RESET_ALL + "\n\n")

# Select outputDir and targetVersion
outputDir = libhearingdownloader.selectOutputFolder()
targetVersion = libhearingdownloader.selectFromList(validVersions)
if (validVersions[targetVersion][0] == "manual"):
    validVersion = ""
    while not validVersion:
        validVersion = input("\nPlease enter " + Fore.GREEN + "manual Smart Fit version" + Style.RESET_ALL + ": ")
        if (not len(validVersion.split('.')) == 4 or not validVersion.replace('.', '').isdecimal()):
            print("\nThe version you have selected is " + Fore.RED + "invalid" + Style.RESET_ALL + ".\nPlease try again. (" + Fore.YELLOW + "hint" + Style.RESET_ALL + ": it should be in a similar format to " + Fore.GREEN + "a.b.c.d" + Style.RESET_ALL + " where " + Fore.GREEN + "a" + Style.RESET_ALL + ", " + Fore.GREEN + "b" + Style.RESET_ALL + ", " + Fore.GREEN + "c" + Style.RESET_ALL + ", and " + Fore.GREEN + "d" + Style.RESET_ALL + " are integers)")
            validVersion = ""
        elif (input("\nYou have selected version (" + Fore.YELLOW + "ReSound Smart Fit v" + validVersion + Style.RESET_ALL + ") are you sure you want to download it? [" + Style.DIM + "(" + Style.BRIGHT + Fore.GREEN + "Y" + Style.RESET_ALL + Style.DIM + ")" + Style.RESET_ALL + "/n] ") == "n"):
            validVersion = ""
    validVersions[targetVersion] = ('ReSound Smart Fit v' + validVersion, 'Manually specified version', 'https://supportgn.gnonlineservices.com/downloads/resound/smartfit_' + validVersion + '_releaseversion.zip')

print("\n\n")

# Create download folder
outputDir += validVersions[targetVersion][0] + "/"

if(libhearingdownloader.verboseDebug):
    print("V:" + str(targetVersion))
    print("T:" + validVersions[targetVersion][0])

# Download the file
libhearingdownloader.downloadFile(validVersions[targetVersion][2], outputDir + validVersions[targetVersion][2].split("/")[-1], "Downloading " + validVersions[targetVersion][0])

print("\n\nDownload Complete!")
