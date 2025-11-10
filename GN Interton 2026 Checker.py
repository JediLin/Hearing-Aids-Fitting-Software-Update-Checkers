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
print("=        " + Style.BRIGHT + Fore.YELLOW + "Interton" + Style.RESET_ALL + " Software Update Checker        =")
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
    "Interton does not review the content of The Checker or the source that The Checker check against",
    "Please view the source disclaimer at:"
    "http://www.supportgn.com/interton/subsites/disclaimer.php",
    "",
    "Interton is a trademark of GN Hearing A/S and/or its affiliates (\"GN Group\")",
    "GN is a trademark of GN Hearing A/S",
    "Interton Fitting is a trademark of GN Hearing A/S",
    "GN Hearing A/S is a subsidiary of GN Hearing A/S",
    "Interton is a subsidiary of GN Hearing A/S",
    "Interton Fitting is created by Interton",
    "Appraise is created by Interton",
    "CompuFit is created by Interton"
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by",
    "Interton, GN Hearing A/S, GN Group or GN Hearing A/S",
    "Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software.",
    "The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

# Get Interton Fitting update from the webpage
ifURI = "https://www.gnhearing.com/en/products/interton/fitting-software-download"
try:
    test = requests.get(ifURI)
    dom = lxml.html.fromstring(test.content)
    hrefs = [x for x in dom.xpath('//a/@href') if '//' in x and 'zip' in x]
    link0 = hrefs[0].replace('%20', ' ')
    filename0 = os.path.basename(urlparse(link0).path)
    title0 = "Interton Fitting v" + re.sub(r"_releaseversion\.zip", "", re.sub(r"fitting_", "", filename0))
    try:
        link1 = hrefs[1].replace('%20', ' ')
        filename1 = os.path.basename(urlparse(link1).path)
        title1 = "Interton Fitting v" + re.sub(r"_releaseversion\.zip", "", re.sub(r"fitting_", "", filename1))
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
    ("manual", "Manually specify a version of Interton Fitting (" + Fore.RED + "WARNING" + Style.RESET_ALL + ": ADVANCED USERS ONLY)", ""),
    (" ", "--"),
    ("Archived Downloads", "--"),
    ("==================", "--"),
    ("Interton Fitting v2.2", "fitting_2.2.209.13_releaseversion.zip", "https://supportgn.gnonlineservices.com/downloads/interton/fitting_2.2.209.13_releaseversion.zip"),
    ("Interton Fitting v2.1 Update 2", "fitting_2.1.305.17_releaseversion.zip", "https://supportgn.gnonlineservices.com/downloads/interton/fitting_2.1.305.17_releaseversion.zip"),
    ("Interton Fitting v2.0 Update 3", "fitting_2.0.132.26_releaseversion.zip", "https://supportgn.gnonlineservices.com/downloads/interton/fitting_2.0.132.26_releaseversion.zip"),
    ("Interton Fitting v1.18", "Interton_Fitting_1.18.324.0-ReleaseVersion.zip", "https://supportgn.gnonlineservices.com/downloads/interton/Interton_Fitting_1.18.324.0-ReleaseVersion.zip"),
    ("Interton Appraise v2.4", "appraise2.4.0.24.zip", "http://www.supportgn.com/files/interton/appraise2.4.0.24.zip"),
    ("Interton Appraise v1.5", "appraise1.50.8.3.zip", "http://www.supportgn.com/files/interton/appraise1.50.8.3.zip"),
    ("Interton CompuFit v4.4", "compufit4.4.zip", "http://www.supportgn.com/files/interton/compufit4.4.zip"),
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
        validVersion = input("\nPlease enter " + Fore.GREEN + "manual Fitting version" + Style.RESET_ALL + ": ")
        if (not len(validVersion.split('.')) == 4 or not validVersion.replace('.', '').isdecimal()):
            print("\nThe version you have selected is " + Fore.RED + "invalid" + Style.RESET_ALL + ".\nPlease try again. (" + Fore.YELLOW + "hint" + Style.RESET_ALL + ": it should be in a similar format to " + Fore.GREEN + "a.b.c.d" + Style.RESET_ALL + " where " + Fore.GREEN + "a" + Style.RESET_ALL + ", " + Fore.GREEN + "b" + Style.RESET_ALL + ", " + Fore.GREEN + "c" + Style.RESET_ALL + ", and " + Fore.GREEN + "d" + Style.RESET_ALL + " are integers)")
            validVersion = ""
        elif (input("\nYou have selected version (" + Fore.YELLOW + "Interton Fitting v" + validVersion + Style.RESET_ALL + ") are you sure you want to download it? [" + Style.DIM + "(" + Style.BRIGHT + Fore.GREEN + "Y" + Style.RESET_ALL + Style.DIM + ")" + Style.RESET_ALL + "/n] ") == "n"):
            validVersion = ""
    validVersions[targetVersion] = ('Interton Fitting v' + validVersion, 'Manually specified version', 'https://supportgn.gnonlineservices.com/downloads/interton/fitting_' + validVersion + '_releaseversion.zip')

print("\n\n")

# Create download folder
outputDir += validVersions[targetVersion][0] + "/"

if(libhearingdownloader.verboseDebug):
    print("V:" + str(targetVersion))
    print("T:" + validVersions[targetVersion][0])

# Download the file
libhearingdownloader.downloadFile(validVersions[targetVersion][2], outputDir + validVersions[targetVersion][2].split("/")[-1], "Downloading " + validVersions[targetVersion][0])

print("\n\nDownload Complete!")
