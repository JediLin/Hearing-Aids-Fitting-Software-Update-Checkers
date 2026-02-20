#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import configparser
import os
import requests
import lxml.html
import re
from urllib.parse import urlparse
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
try:
    noBrotli = ""
    import brotli
except:
    noBrotli = True
import libhearingdownloader
import rot_codec

just_fix_windows_console()

print("\n\n")
print("==================================================")
print("=     " + Style.BRIGHT + Fore.CYAN + "HIMSA" + Style.RESET_ALL + " Noahlink Wireless Update Checker     =")
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
    "HIMSA is a trademark of Hearing Instrument Manufacturers' Software Association.",
    "Noahlink Wireless is a trademark of Hearing Instrument Manufacturers' Software Association.",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by",
    "HIMSA II K/S",
    "Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software.",
    "The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

# Read configuration file
config = configparser.ConfigParser()
config.read('config.ini')
uaString = config.get('General', 'UA', fallback='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.3')

# Get HIMSA Noahlink Wireless update from the webpage
nwURI = rot_codec.rot47_decode("9EEADi^^HHH]9:>D2]4@>^9:>D205@H?=@25^") + "noahlink-wireless-downloads/"
try:
    test = requests.get(nwURI, headers={"Host": "www.himsa.com", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive", "Upgrade-Insecure-Requests": "1", "Referer": nwURI, "User-Agent": uaString})
    if (libhearingdownloader.verboseDebug):
        print(test.status_code)
        print(test.headers)
        print(test.content)
    # just import brotli makes requests can handle br encoding(?) ,no further decompression needed...let's keep code here just in case:
    #
    #if (test.headers.get("Content-Encoding") == "br"):
    #    data = brotli.decompress(test.content).decode("utf-8")
    #    print(data)
    #    dom = lxml.html.fromstring(data)
    #else:
    #
    dom = lxml.html.fromstring(test.content)
    hrefs = [x for x in dom.xpath('//a/@href') if '//' in x and 'exe' in x]
    if (libhearingdownloader.verboseDebug):
        print(hrefs)
    link0 = hrefs[0].replace('%20', ' ')
    filename0 = os.path.basename(urlparse(link0).path)
    title0 = "Noahlink Wireless Firmware Upgrader v" + re.sub(r"\.exe", "", re.sub(r"NLWUpgrade(r)*.", "", filename0))
    link1 = hrefs[1].replace('%20', ' ')
    filename1 = os.path.basename(urlparse(link1).path)
    title1 = "Noahlink Wireless Driver v" + re.sub(r"\.exe", "", re.sub(r"Driver_NLW_V.", "", filename1))
except:
    link0 = ""
    filename0 = "--"
    title0 = "NOT FOUND"
    link1 = ""
    filename1 = "--"
    title1 = "NOT FOUND"

if (noBrotli):
    print("\n" + Fore.RED + "WARNING" + Style.RESET_ALL + ": This checker is not supported in this version of Python.")
    print("You can try to use different version of Python to solve this issue.")

# Define list of valid versions and their download links
validVersions = [
    ("Current Versions", "--"),
    (title0, filename0, link0),
    (title1, filename1, link1),
    (" ", "--"),
    ("Archived Versions", "--"),
    ("Noahlink Wireless Firmware v3.6.0.0", "v2.25 (NW1) / v3.27 (NW2) (February 2026)", rot_codec.rot47_decode("9EEADi^^HHH]9:>D2]4@>^HA") + "-" + rot_codec.rot47_decode("4@?E6?E^FA=@25D^a_ae^_a^}{(&A8C2560b]e]_]_]6I6")),
    ("Noahlink Wireless Firmware v3.5.0.0", "v2.25 (NW1) / v3.25 (NW2) (July 2025)", rot_codec.rot47_decode("9EEADi^^HHH]9:>D2]4@>^HA") + "-" + rot_codec.rot47_decode("4@?E6?E^FA=@25D^a_ad^_f^}{(&A8C256C0b]d]_]_]6I6")),
    ("Noahlink Wireless Firmware v3.3.0.0", "v2.25 (NW1) / v3.23 (NW2) (April 2025)", rot_codec.rot47_decode("9EEADi^^9:>D27:=6D]4@>^}@29=:?<(:C6=6DD^}{(&A8C256C0b]b]_]_]6I6")),
    ("Noahlink Wireless Firmware v3.1.0.92", "v2.25 (NW1) / v3.17 (NW2) (May 2024)", rot_codec.rot47_decode("9EEADi^^9:>D27:=6D]4@>^}@29=:?<(:C6=6DD^}{(&A8C256C0b]`]_]ha]6I6")),
    ("Noahlink Wireless Firmware v2.24", "v2.24 (NW1 only)", rot_codec.rot47_decode("9EEADi^^9:>D27:=6D]4@>^}@29=:?<(:C6=6DD^}{(&A8C256Ca]ac]6I6")),
    ("Noahlink Wireless Driver v1.1.0.0", "for Windows 10 and 11 (March 2017)", rot_codec.rot47_decode("9EEADi^^9:>D27:=6D]4@>^}@29=:?<(:C6=6DD^sC:G6C0}{(0']`]`]_]_]6I6")),
]
if(link0 == ""):
    print("\n\nThe latest available versions are:\n- " + Fore.GREEN + validVersions[5][0] + Style.RESET_ALL + "\n- " + Fore.GREEN + validVersions[-1][0] + Style.RESET_ALL + "\n\n")
else:
    print("\n\nThe latest available versions are:\n- " + Fore.GREEN + title0 + Style.RESET_ALL + "\n- " + Fore.GREEN + title1 + Style.RESET_ALL + "\n\n")

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
