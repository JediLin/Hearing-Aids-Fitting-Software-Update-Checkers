#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import requests
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader
import xml.etree.ElementTree as xml

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

# Define variables
rootDownloadURL = "http://www.supportgn.com/files/"

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        # Download update file list from updater API
        rawXmlData = requests.get("http://www.supportgn.com/beltone/subsites/releasessdb.xml")
        data = xml.fromstring(rawXmlData.text)
        break
    except:
        pass

    updaterRetries -= 1
if (updaterRetries == 0):
    print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": Update server could not be reached")
    exit(1)

if (libhearingdownloader.verboseDebug):
    print(rawXmlData.text)

# Define XMLNS (the main one)
availableFiles = {} # List of available files

currentCategory = "Other"
for child in data:
    if (child[0].tag == "SEPARATOR"):
        #availableFiles.append( ("== " + child[0].text + " ==", '--') )
        currentCategory = child[0].text
    else:
        #availableFiles.append( (child.find("BUTTONTEXTDOWN").text, '', child.find("LINK").text) )
        availableFiles[currentCategory] = availableFiles.get(currentCategory, [])
        availableFiles[currentCategory].append( (child.find("BUTTONTEXTDOWN").text, '', child.find("LINK").text) )

if (libhearingdownloader.verboseDebug):
    print(availableFiles)

print("\n\nThe latest available version is " + Fore.GREEN + list(availableFiles.keys())[0] + Style.RESET_ALL + "\n\n")

categories = []
for category in availableFiles.keys():
    categories.append( (category, "") )

categories.append( ('manual', 'Manually specify a version of Beltone Solus Max (' + Fore.RED + 'WARNING' + Style.RESET_ALL + ': ADVANCED USERS ONLY)') )

# Select outputDir and targetFile
outputDir = libhearingdownloader.selectOutputFolder()

simpleSelection = libhearingdownloader.selectFromList(categories, prompt="category to download from", headerSeperator='\n')
targetCategory = categories[simpleSelection][0]
if (libhearingdownloader.verboseDebug):
    print(targetCategory)

if (targetCategory == 'manual'):
    targetVersion = ''
    while not targetVersion:
        targetVersion = input("\nPlease enter " + Fore.GREEN + "manual Solus Max version" + Style.RESET_ALL + ": ")
        if (not len(targetVersion.split('.')) == 4 or not targetVersion.replace('.', '').isdecimal()):
            print("\nThe version you have selected is " + Fore.RED + "invalid" + Style.RESET_ALL + ".\nPlease try again. (" + Fore.YELLOW + "hint" + Style.RESET_ALL + ": it should be in a similar format to " + Fore.GREEN + "a.b.c.d" + Style.RESET_ALL + " where " + Fore.GREEN + "a" + Style.RESET_ALL + ", " + Fore.GREEN + "b" + Style.RESET_ALL + ", " + Fore.GREEN + "c" + Style.RESET_ALL + ", and " + Fore.GREEN + "d" + Style.RESET_ALL + " are integers)")
            targetVersion = ''
        elif (input("\nYou have selected version (" + Fore.YELLOW + targetVersion + Style.RESET_ALL + ") are you sure you want to download it? [" + Style.DIM + "(" + Style.BRIGHT + Fore.GREEN + "Y" + Style.RESET_ALL + Style.DIM + ")" + Style.RESET_ALL + "/n] ") == "n"):
            targetVersion = ''
    availableFiles = [('Beltone Solus Max v' + targetVersion, 'Manually specified version', 'https://supportgn.gnonlineservices.com/downloads/beltone/solusmax_' + targetVersion + '_releaseversion.zip')]
else:
    availableFiles = availableFiles[targetCategory]

selectedFile = libhearingdownloader.selectFromList(availableFiles, prompt="software to download", headerSeperator='\n')

targetURL = availableFiles[selectedFile][2]
targetFile = availableFiles[selectedFile]

if (not ("http://" in targetURL or "https://" in targetURL)):
    targetURL = rootDownloadURL + targetURL

# Create download folder
#outputDir += '.'.join(targetFile[0].split('.')[:-1]) + "/"
outputLocation = outputDir + '.'.join(targetFile[2].split("/")[-1].split(".")[:-1]) + "/" + targetFile[2].split("/")[-1]
print("\n\n")

# Download file
libhearingdownloader.downloadFile(targetURL, outputLocation, "Downloading " + targetFile[0])

print("\n\nDownload Complete!")