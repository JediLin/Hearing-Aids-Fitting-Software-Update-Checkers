#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import requests
import re
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingchecker
import rot_codec

just_fix_windows_console()

print("\n\n")
ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
titleText = Style.BRIGHT + Fore.CYAN + "Sonic" + Style.RESET_ALL + " EXPRESSfit Pro Update Checker"
titleWidth = libhearingchecker.checkerTitleWidth
titleLenth = len(ansi_escape.sub('', titleText))
if (titleLenth > (titleWidth - 4)):
    titleWidth = round(titleLenth/2)*2+4

print("="*titleWidth)
print("=" + " "*(round((titleWidth-2-titleLenth)/2)-(round((titleWidth-2-titleLenth)/2)*2)+(titleWidth-2-titleLenth)) + titleText + " "*round((titleWidth-2-titleLenth)/2) + "=")
print("="*(titleWidth-3-len(libhearingchecker.checkerVersion)) + " " + Fore.GREEN + libhearingchecker.checkerVersion + Style.RESET_ALL + " =")

turboFile = Path("turbo.txt")
if not turboFile.is_file():
    libhearingchecker.printWarranty()

disclaimer = [
    "DISCLAIMER",
    "",
    "The contributors of the Hearing Aids Fitting Software Update Checkers (\"The Checker\")",
    "do not take any responsability for what you do with The Checker.",
    "",
    "Sonic Innovations is a trademark of Sonic Innovations, Inc.",
    "EXPRESSfit is a trademark of Sonic Innovations, Inc.",
    "Demant is a trademark of Demant A/S",
    "Sonic Inovations, Inc. is a subsidiary of Demant A/S",
    "Sonic EXPRESSfit is created by Sonic Innovations, Inc",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by",
    "Sonic Inovations, Inc. or Demant A/S",
    "Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software.",
    "The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingchecker.printDisclaimer(disclaimer)

filesToDownload = [
    "setup.exe",
    "Data2/Base.msi",
    "Data2/Cust_Sonic.msi",
    "Data2/FirmwareUpdates.msi",
    "Data2/Media.msi",
    "Data2/SonicUpdater.msi",
    "Tools/ExpressLinkDriver_x64.msi",
    "Tools/ExpressLinkDriver_x86.msi",
    "Tools/VC140_Runtime/vc_redist.x86.exe",
]

downloadURI = rot_codec.rot47_decode("9EEADi^^:?DE2==45?]D@?:4:]4@>^ac]a^ab]ac]`c]_^tIAC6DDu:E^$@?:4^eh234d3a^")

# Define list of valid versions and their download links (direct from CDN) (predefined to online and offline of latest version)
serverResponse = requests.get(downloadURI + filesToDownload[0])
if (serverResponse.status_code == 200):
    validVersions = [
        ("EXPRESSfit Pro 2024.2", "The latest SONIC EXPRESSFIT Installer (OFFLINE)"),
        ("EXPRESSfit Pro 2024.2", "The latest SONIC EXPRESSFIT Installer (ONLINE)"),
    ]
else:
    print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": Update server could not be reached")
    exit(1)

print("\n\nThe latest available version is " + Fore.GREEN + "EXPRESSfit Pro 2024.2" + Style.RESET_ALL + "\n\n")

# Select outputDir and targetVersion
outputDir = libhearingchecker.selectOutputFolder()
targetVersion = libhearingchecker.selectFromList(validVersions)
print("\n\n")

if (targetVersion == 0):
    outputDir += libhearingchecker.normalizePath("EXPRESSfit Pro 2024.2" + "/")
    # Download and save the files
    print("Downloading " + str(len(filesToDownload)) + " files\n")
    fileIndex = 1
    for fileToDownload in filesToDownload:
        libhearingchecker.downloadFile(downloadURI + fileToDownload, outputDir + fileToDownload, "Downloading " + fileToDownload.split("/")[-1] + " (" + str(fileIndex) + "/" + str(len(filesToDownload)) + ")")
        fileIndex += 1
elif (targetVersion == 1):
    outputDir += libhearingchecker.normalizePath("EXPRESSfit Pro 2024.2" + "/")
    # Download and save the files
    fileIndex = 1
    fileToDownload = "setup.exe"
    libhearingchecker.downloadFile(downloadURI + fileToDownload, outputDir + fileToDownload, "Downloading " + fileToDownload.split("/")[-1])

print("\n\nDownload Complete!")