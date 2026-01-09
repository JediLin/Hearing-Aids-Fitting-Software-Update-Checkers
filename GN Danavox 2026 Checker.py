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
import rot_codec

just_fix_windows_console()

print("\n\n")
print("==================================================")
print("=         " + Style.BRIGHT + Fore.CYAN + "Danavox" + Style.RESET_ALL + " Software Update Checker        =")
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
    "Danavox is a trademark of GN Hearing A/S and/or its affiliates (\"GN Group\")",
    "GN is a trademark of GN Store Nord A/S",
    "Danavox XE BeMore is a trademark of GN Group",
    "Danavox Danalogic is a trademark of GN Group",
    "GN Hearing A/S is a subsidiary of GN Store Nord A/S",
    "Danavox is a subsidiary of GN Hearing A/S",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by",
    "Danavox, GN Hearing A/S, GN Group or GN Store Nord A/S",
    "Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software.",
    "The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

# Get Danavox XE BeMore update from the webpage
dxebmURI = rot_codec.rot47_decode("9EEADi^^HHH]8?962C:?8]4@>^6?^AC@5F4ED^52?2G@I^") + "fitting-software-download"
try:
    test = requests.get(dxebmURI)
    dom = lxml.html.fromstring(test.content)
    hrefs = [x for x in dom.xpath('//a/@href') if '//' in x and 'zip' in x]
    link0 = hrefs[0].replace('%20', ' ')
    filename0 = os.path.basename(urlparse(link0).path)
    title0 = "Danavox XE BeMore v" + re.sub(r"_releaseversion\.zip", "", re.sub(r"xebemore_", "", filename0))
    link3 = link0.replace('bemore/xebemore', 'danalogic/danalogic')
    filename3 = filename0.replace('xebemore', 'danalogic')
    title3 = title0.replace('XE BeMore', 'Danalogic')
    try:
        link1 = hrefs[1].replace('%20', ' ')
        filename1 = os.path.basename(urlparse(link1).path)
        title1 = "Danavox XE BeMore v" + re.sub(r"_releaseversion\.zip", "", re.sub(r"xebemore_", "", filename1))
        link2 = link1.replace('bemore/xebemore', 'danalogic/danalogic')
        filename2 = filename1.replace('xebemore', 'danalogic')
        title2 = title1.replace('XE BeMore', 'Danalogic')
    except:
        link1 = ""
        filename1 = "--"
        title1 = "NOT FOUND"
        link2 = ""
        filename2 = "--"
        title2 = "NOT FOUND"
except:
    link0 = ""
    filename0 = "--"
    title0 = "NOT FOUND"
    link1 = ""
    filename1 = "--"
    title1 = "NOT FOUND"
    link2 = ""
    filename2 = "--"
    title2 = "NOT FOUND"
    link3 = ""
    filename3 = "--"
    title3 = "NOT FOUND"

# Define list of valid versions and their download links
validVersions = [
    ("Current XE BeMore Versions", "--"),
    (title1, filename1, link1),
    (title0, filename0, link0),
    ("XE BeMore/manual", "Manually specify a version of Danavox XE BeMore (" + Fore.RED + "WARNING" + Style.RESET_ALL + ": ADVANCED USERS ONLY)", ""),
    (" ", "--"),
    ("Current Danalogic Versions", "--"),
    (title2, filename2, link2),
    (title3, filename3, link3),
    ("Danalogic/manual", "Manually specify a version of Danavox Danalogic (" + Fore.RED + "WARNING" + Style.RESET_ALL + ": ADVANCED USERS ONLY)", ""),
    (" ", "--"),
    ("Archived XE BeMore Versions", "--"),
    ("Danavox XE BeMore v2.3", "xebemore_2.3.334.0_releaseversion.zip", rot_codec.rot47_decode("9EEADi^^DFAA@CE8?]8?@?=:?6D6CG:46D]4@>^5@H?=@25D^<2^36>@C6^I636>@C60a]b]bbc]_0C6=62D6G6CD:@?]K:A")),
    ("Danavox XE BeMore v2.2", "xebemore_2.2.209.13_releaseversion.zip", rot_codec.rot47_decode("9EEADi^^DFAA@CE8?]8?@?=:?6D6CG:46D]4@>^5@H?=@25D^<2^36>@C6^I636>@C60a]a]a_h]`b0C6=62D6G6CD:@?]K:A")),
    ("Danavox XE BeMore v2.1 Update 2", "xebemore_2.1.305.17_releaseversion.zip", rot_codec.rot47_decode("9EEADi^^DFAA@CE8?]8?@?=:?6D6CG:46D]4@>^5@H?=@25D^<2^36>@C6^I636>@C60a]`]b_d]`f0C6=62D6G6CD:@?]K:A")),
    ("Danavox XE BeMore v2.0 Update 3", "xebemore_2.0.132.26_releaseversion.zip", rot_codec.rot47_decode("9EEADi^^DFAA@CE8?]8?@?=:?6D6CG:46D]4@>^5@H?=@25D^<2^36>@C6^I636>@C60a]_]`ba]ae0C6=62D6G6CD:@?]K:A")),
    ("Danavox XE BeMore v1.18", "XE_BeMore_1.18.324.0-ReleaseVersion.zip", rot_codec.rot47_decode("9EEADi^^DFAA@CE8?]8?@?=:?6D6CG:46D]4@>^5@H?=@25D^<2^36>@C6^)t0q6|@C60`]`g]bac]_") + "-ReleaseVersion.zip"),
    (" ", "--"),
    ("Archived Danalogic Versions", "--"),
    ("Danavox Danalogic v2.3", "danalogic_2.3.334.0_releaseversion.zip", rot_codec.rot47_decode("9EEADi^^DFAA@CE8?]8?@?=:?6D6CG:46D]4@>^5@H?=@25D^<2^52?2=@8:4^52?2=@8:40a]b]bbc]_0C6=62D6G6CD:@?]K:A")),
    ("Danavox Danalogic v2.2", "danalogic_2.2.209.13_releaseversion.zip", rot_codec.rot47_decode("9EEADi^^DFAA@CE8?]8?@?=:?6D6CG:46D]4@>^5@H?=@25D^<2^52?2=@8:4^52?2=@8:40a]a]a_h]`b0C6=62D6G6CD:@?]K:A")),
    ("Danavox Danalogic v2.1 Update 2", "danalogic_2.1.305.17_releaseversion.zip", rot_codec.rot47_decode("9EEADi^^DFAA@CE8?]8?@?=:?6D6CG:46D]4@>^5@H?=@25D^<2^52?2=@8:4^52?2=@8:40a]`]b_d]`f0C6=62D6G6CD:@?]K:A")),
    ("Danavox Danalogic v2.0 Update 3", "danalogic_2.0.132.26_releaseversion.zip", rot_codec.rot47_decode("9EEADi^^DFAA@CE8?]8?@?=:?6D6CG:46D]4@>^5@H?=@25D^<2^52?2=@8:4^52?2=@8:40a]_]`ba]ae0C6=62D6G6CD:@?]K:A")),
]
if(link1 == ""):
    if(link0 == ""):
        print("\n\nThe latest available versions are:\n- " + Fore.GREEN + validVersions[11][0] + Style.RESET_ALL + "\n- " + Fore.GREEN + validVersions[12][0] + Style.RESET_ALL + "\n\n")
    else:
        print("\n\nThe latest available versions are:\n- " + Fore.GREEN + title0 + Style.RESET_ALL + "\n- " + Fore.GREEN + title3 + Style.RESET_ALL + "\n\n")
else:
    print("\n\nThe latest available versions are:\n- " + Fore.GREEN + title1 + Style.RESET_ALL + "\n- " + Fore.GREEN + title2 + Style.RESET_ALL + "\n\n")

# Select outputDir and targetVersion
outputDir = libhearingdownloader.selectOutputFolder()
targetVersion = libhearingdownloader.selectFromList(validVersions)
if (validVersions[targetVersion][0] == "XE BeMore/manual"):
    validVersion = ""
    while not validVersion:
        validVersion = input("\nPlease enter " + Fore.GREEN + "manual XE BeMore version" + Style.RESET_ALL + ": ")
        if (not len(validVersion.split('.')) == 4 or not validVersion.replace('.', '').isdecimal()):
            print("\nThe version you have selected is " + Fore.RED + "invalid" + Style.RESET_ALL + ".\nPlease try again. (" + Fore.YELLOW + "hint" + Style.RESET_ALL + ": it should be in a similar format to " + Fore.GREEN + "a.b.c.d" + Style.RESET_ALL + " where " + Fore.GREEN + "a" + Style.RESET_ALL + ", " + Fore.GREEN + "b" + Style.RESET_ALL + ", " + Fore.GREEN + "c" + Style.RESET_ALL + ", and " + Fore.GREEN + "d" + Style.RESET_ALL + " are integers)")
            validVersion = ""
        elif (input("\nYou have selected version (" + Fore.YELLOW + "Danavox XE BeMore v" + validVersion + Style.RESET_ALL + ") are you sure you want to download it? [" + Style.DIM + "(" + Style.BRIGHT + Fore.GREEN + "Y" + Style.RESET_ALL + Style.DIM + ")" + Style.RESET_ALL + "/n] ") == "n"):
            validVersion = ""
    validVersions[targetVersion] = ('Danavox XE BeMore v' + validVersion, 'Manually specified version', rot_codec.rot47_decode("9EEADi^^DFAA@CE8?]8?@?=:?6D6CG:46D]4@>^5@H?=@25D^<2^36>@C6^I636>@C60") + validVersion + '_releaseversion.zip')

if (validVersions[targetVersion][0] == "Danalogic/manual"):
    validVersion = ""
    while not validVersion:
        validVersion = input("\nPlease enter " + Fore.GREEN + "manual Danalogic version" + Style.RESET_ALL + ": ")
        if (not len(validVersion.split('.')) == 4 or not validVersion.replace('.', '').isdecimal()):
            print("\nThe version you have selected is " + Fore.RED + "invalid" + Style.RESET_ALL + ".\nPlease try again. (" + Fore.YELLOW + "hint" + Style.RESET_ALL + ": it should be in a similar format to " + Fore.GREEN + "a.b.c.d" + Style.RESET_ALL + " where " + Fore.GREEN + "a" + Style.RESET_ALL + ", " + Fore.GREEN + "b" + Style.RESET_ALL + ", " + Fore.GREEN + "c" + Style.RESET_ALL + ", and " + Fore.GREEN + "d" + Style.RESET_ALL + " are integers)")
            validVersion = ""
        elif (input("\nYou have selected version (" + Fore.YELLOW + "Danavox Danalogic v" + validVersion + Style.RESET_ALL + ") are you sure you want to download it? [" + Style.DIM + "(" + Style.BRIGHT + Fore.GREEN + "Y" + Style.RESET_ALL + Style.DIM + ")" + Style.RESET_ALL + "/n] ") == "n"):
            validVersion = ""
    validVersions[targetVersion] = ('Danavox Danalogic v' + validVersion, 'Manually specified version', rot_codec.rot47_decode("9EEADi^^DFAA@CE8?]8?@?=:?6D6CG:46D]4@>^5@H?=@25D^<2^52?2=@8:4^52?2=@8:40") + validVersion + '_releaseversion.zip')

print("\n\n")

# Create download folder
outputDir += validVersions[targetVersion][0] + "/"

if(libhearingdownloader.verboseDebug):
    print("V:" + str(targetVersion))
    print("T:" + validVersions[targetVersion][0])

# Download the file
libhearingdownloader.downloadFile(validVersions[targetVersion][2], outputDir + validVersions[targetVersion][2].split("/")[-1], "Downloading " + validVersions[targetVersion][0])

print("\n\nDownload Complete!")
