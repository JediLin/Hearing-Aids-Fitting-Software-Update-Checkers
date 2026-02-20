#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import configparser
import os
import requests
import lxml.html
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlparse
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader
import rot_codec

just_fix_windows_console()

print("\n\n")
print("==================================================")
print("=       " + Style.BRIGHT + Fore.BLUE + "Starkey" + Style.RESET_ALL + " PatientBase Update Checker       =")
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

# Read configuration file for toggles with default True
config = configparser.ConfigParser()
config.read('config.ini')
certVerify = config.getboolean('Starkey', 'PatientBaseVerify', fallback='True')

# Get PatientBase update from the webpage
pbURI = rot_codec.rot47_decode("9EEADi^^A2E:6?E32D6]DE2C<6J962C:?8E649?@=@8:6D]4@>")
fallbackDownload = rot_codec.rot47_decode("9EEADi^^D@7EH2C65@H?=@25]DE2C<6J]4@>^!2E:6?Eq2D6^!2E:6?Eq2D6 $6EFA ag]`]`__`e]_]6I6")
try:
    if (certVerify == False):
        print("\n\n" + Fore.RED + "WARNING" + Style.RESET_ALL + ": Ignorning certification security verification for \n" + Fore.GREEN + pbURI + Style.RESET_ALL)
        print("\nYou shouldn't trust anything you get from this request.\nProceed with " + Fore.RED + "YOUR OWN RISK!!!" + Style.RESET_ALL)
        print("\nTo turn on the security verification, please \nedit " + Fore.GREEN + "config.ini" + Style.RESET_ALL + " file with any plain-text editor, \nsetting " + Fore.BLUE + "PatientBaseVerify" + Style.RESET_ALL + " to " + Fore.GREEN + "True" + Style.RESET_ALL + " in the " + Fore.BLUE + "[Starkey]" + Style.RESET_ALL + " section.")
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        test = requests.get(pbURI, verify=False)
        dom = lxml.html.fromstring(test.content)
    else:
        test = requests.get(pbURI)
        dom = lxml.html.fromstring(test.content)
    hrefs = [x for x in dom.xpath('//a/@href') if '//' in x and 'exe' in x]
    filename0 = os.path.basename(urlparse(hrefs[0]).path).replace('%20', ' ')
    link0 = hrefs[0].replace('%20', ' ')
except:
    if (certVerify == True):
        print("\n\nSomething goes wrong.")
        print("\nIt is possible that the server certification is expired \nso that the security verification is failed.")
        print("\nNote: If you want to turn off the security verification, \nplease edit " + Fore.GREEN + "config.ini" + Style.RESET_ALL + " file with any plain-text editor, \nsetting " + Fore.BLUE + "PatientBaseVerify" + Style.RESET_ALL + " to " + Fore.GREEN + "False" + Style.RESET_ALL + " in the " + Fore.BLUE + "[Starkey]" + Style.RESET_ALL + " section.")
    filename0 = "NOT FOUND"
    link0 = fallbackDownload

# Define list of valid versions and their download links (direct from CDN)
# sadly az493319.vo.msecnd.net is no longer available...
validVersions = [
    ("Current Version", "--"),
    ("PatientBase v" + filename0.replace('PatientBase Setup ', '').replace('.exe', ''), filename0, link0),
    (" ", "--"),
    ("Archived Version", "--"),
    ("PatientBase v28.0.10003.0", "for Pro Fit 1.0+ and Inspire 2023.1+", fallbackDownload),
#     ("PatientBase 26.0.10014.0", "for Inspire 2022.1 - 2023.0", rot_codec.rot47_decode("9EEADi^^2Kchbb`h]G@]>D64?5]?6E^:?DE2==^!2E:6?Eq2D6 $6EFA ae]_]`__`c]_]6I6")),
#     ("PatientBase 24.0.10102.0", "for Inspire 2021.0 - 2022.0", rot_codec.rot47_decode("9EEADi^^2Kchbb`h]G@]>D64?5]?6E^:?DE2==^!2E:6?Eq2D6 $6EFA ac]_]`_`_a]_]6I6")),
#     ("PatientBase 15.0.386.0", "for Inspire 2016 - 2020", rot_codec.rot47_decode("9EEADi^^2Kchbb`h]G@]>D64?5]?6E^:?DE2==^!2E:6?Eq2D6 $6EFA `d]_]bge]_]6I6")),
]
print("\n\nThe latest available version is " + Fore.GREEN + "v" + filename0.replace('PatientBase Setup ', '').replace('.exe', '') + Style.RESET_ALL + "\n\n")

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
