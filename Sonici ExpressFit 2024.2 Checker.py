#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import configparser
import html
import requests
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader
import rot_codec

just_fix_windows_console()

print("\n\n")
print("==================================================")
print("=       " + Style.BRIGHT + Fore.CYAN + "Sonic" + Style.RESET_ALL + " EXPRESSfit Pro Update Checker      =")
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
    libhearingdownloader.printDisclaimer(disclaimer)

filesToDownload = []

# Get list of files
filesToDownload.append("setup.exe")
filesToDownload.append("Tools/ExpressLinkDriver_x86.msi")
filesToDownload.append("Tools/ExpressLinkDriver_x64.msi")
filesToDownload.append("Tools/VC140_Runtime/vc_redist.x86.exe")
filesToDownload.append("Data2/SonicUpdater.msi")
filesToDownload.append("Data2/Media.msi")
filesToDownload.append("Data2/FirmwareUpdates.msi")
filesToDownload.append("Data2/Cust_Sonic.msi")
filesToDownload.append("Data2/Base.msi")

# Get download server uri
downloadURI = rot_codec.rot47_decode("9EEADi^^:?DE2==45?]D@?:4:]4@>^ac]a^ab]ac]`c]_^tIAC6DDu:E^$@?:4^eh234d3a^")

# Define list of valid versions and their download links (direct from CDN) (predefined to online and offline of latest version)
validVersions = [
    ("EXPRESSfit Pro 2024.2", "The latest SONIC EXPRESSFIT Installer (OFFLINE)"),
    ("EXPRESSfit Pro 2024.2", "The latest SONIC EXPRESSFIT Installer (ONLINE)"),
]
print("\n\nThe latest available version is " + Fore.GREEN + "EXPRESSfit Pro 2024.2" + Style.RESET_ALL + "\n\n")

if (libhearingdownloader.verboseDebug):
    print(filesToDownload)

# Select outputDir and targetVersion
outputDir = libhearingdownloader.selectOutputFolder()
targetVersion = libhearingdownloader.selectFromList(validVersions)
print("\n\n")


if (targetVersion == 0):
    outputDir += libhearingdownloader.normalizePath("EXPRESSfit Pro 2024.2" + "/")
    # Download and save the files
    print("Downloading " + str(len(filesToDownload)) + " files\n")
    fileIndex = 1
    for fileToDownload in filesToDownload:
        libhearingdownloader.downloadFile(downloadURI + fileToDownload, outputDir + fileToDownload, "Downloading " + fileToDownload.split("/")[-1] + " (" + str(fileIndex) + "/" + str(len(filesToDownload)) + ")")
        fileIndex += 1
elif (targetVersion == 1):
    outputDir += libhearingdownloader.normalizePath("EXPRESSfit Pro 2024.2" + "/")
    # Download and save the files
    fileIndex = 1
    fileToDownload = "setup.exe"
    libhearingdownloader.downloadFile(downloadURI + fileToDownload, outputDir + fileToDownload, "Downloading " + fileToDownload.split("/")[-1])

print("\n\nDownload Complete!")