#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import os
import html
import ast
import json
import requests
import rot_codec
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
from iso3166 import countries
import libhearingdownloader

just_fix_windows_console()

print("\n\n")
print("==================================================")
print("=        " + Style.BRIGHT + Fore.WHITE + "Widex" + Style.RESET_ALL + " Compass GPS Update Checker        =")
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
    "Widex is a trademark of Widex A/S",
    "Widex A/S is a subsidiaries of WS Audiology A/S",
    "WS Audiology A/S is a trademark of Widex A/S",
    "Widex Compass GPS is created by Widex A/S",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by",
    "WS Audiology A/S or Widex A/S",
    "Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software.",
    "The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

# Target market input
defaultMarket = "US"
inputMarket = input("\nPlease enter " + Fore.GREEN + "target market country code" + Style.RESET_ALL + " [default: " + Fore.YELLOW + defaultMarket + Style.RESET_ALL + "]: ")
if (inputMarket == "" or inputMarket.lower() == defaultMarket.lower()):
    targetMarket = defaultMarket
    print("\nChecking for " + Fore.GREEN + targetMarket + Style.RESET_ALL + " market...")
else:
    try:
        targetMarket = countries.get(inputMarket).alpha2
        print("\nChecking for " + Fore.GREEN + targetMarket + Style.RESET_ALL + " market...")
    except:
        targetMarket = defaultMarket
        print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": Market code is invalid. Using " + Fore.GREEN + defaultMarket + Style.RESET_ALL + " instead...")

# Base information
baseId = "CompassGPS"
baseVer = "4.8.6193.0"

# API key
apiKey = "24fbe5gacg`hcdf535dd34ed6_237347"

# Special headers for the Widex updater API
headers = {
    "Ocp-Apim-Subscription-Key": rot_codec.rot47_decode(apiKey),
    "x-ApiEnvironment": "prod",
    "x-ClientProgram": baseId+"/"+baseVer,
    "Content-Type": "application/json; charset=utf-8",
    "Host": "apimgmt.widex.com"
}

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        # Download update file list from updater API
        postUrl = 'https://apimgmt.widex.com/fds/v1/api/Update?all=true&brevity=terse'
        rawPostData = '{"Id":"'+baseId+'","Version":"'+baseVer+'","Environment":[{"Name":"distributors","Value":"' + targetMarket + '"}]}'
        rawJsonData = requests.post(postUrl, headers=headers, data = rawPostData)
        # Expect something like {"Packages": [],"CustomProperties": {}}
        data = json.loads(rawJsonData.text)
        break
    except:
        pass

    updaterRetries -= 1
if (updaterRetries == 0):
    print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": Update server could not be reached")
    exit(1)
    
if (libhearingdownloader.verboseDebug):
    print(rawPostData)
    print(rawJsonData.text)

if "statusCode" in data:
    print("\n\n" + data['message'])

if "Packages" in data:
    if (data['Packages']==[]):
        print("\n\nThe latest available " + baseId + " version is " + Fore.GREEN + "v" + baseVer + Style.RESET_ALL + "\n\n")
        print("No further update available.")
    else:
        # For now, show what we got...
        print("\n\nUpdate server responded:\n")
        print(rawJsonData.text)
        print("\n\n")

# UNFINISHED!!!!
# (These are copied from Starkey. Further modification required.)
#
# appVer = data['Update']['Title'] + ' (' + data['Update']['Version'] + ')'
# print ("Version info:")
# print(appVer)
# print(data['Update']['Description'])
# filesList = json.dumps(ast.literal_eval(str(data['Update']['Files'][0])))
# fileData = json.loads(filesList)
#
# availableFiles = [] # List of available files
# availableFiles.append( (os.path.basename(fileData['Url']), fileData['Url']) )




# Nothing to download YET!
# filesToDownload.append( (setupFileURL.split("/")[-1], setupFileURL) )
# 
# if (libhearingdownloader.verboseDebug):
#     print(filesToDownload)
# 
# # Select outputDir and targetFile
# outputDir = libhearingdownloader.selectOutputFolder()
# 
# # Create download folder
# outputDir += "Widex Compass GPS/"
# print("\n\n")
# 
# 
# # Download and save the files
# print("Downloading " + str(len(filesToDownload)) + " files\n")
# currentFile = 1
# for fileToDownload in filesToDownload:
#     if (libhearingdownloader.verboseDebug):
#         print(fileToDownload)
# 
#     # Download file
#     libhearingdownloader.downloadFile(fileToDownload[1], outputDir + fileToDownload[0], "Downloading " + fileToDownload[1].split("/")[-1] + " (" + str(currentFile) + "/" + str(len(filesToDownload)) + ")")
# 
#     currentFile += 1
# 
# print("\n\n")
# print("Creating installer from zip")
# with zipfile.ZipFile(outputDir + "Setup.exe.zip", 'r') as zipFile:
#     zipFile.extractall(outputDir)
# 
# os.makedirs(outputDir + "installations/")
# 
# for file in filesToDownload[:-1]:
#     shutil.move(outputDir + file[0], outputDir + "installations/" + file[0])
# 
# os.remove(outputDir + filesToDownload[-1][0])
# 
# print("\n\nDownload Complete!")
