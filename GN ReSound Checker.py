#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import requests
import libhearingdownloader
import xml.etree.ElementTree as xml


print("==================================================")
print("=        ReSound Software Update Checker         =")
print("="*(47-len(libhearingdownloader.downloaderVersion)) + " " + libhearingdownloader.downloaderVersion + " =")

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

# Define variables
rootDownloadURL = "http://www.supportgn.com/files/"

# Display disclaimer
libhearingdownloader.printDisclaimer(disclaimer)

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        # Download update file list from updater API
        rawXmlData = requests.get("http://www.supportgn.com/resound/subsites/releasessdb.xml")
        data = xml.fromstring(rawXmlData.text)
        break
    except:
        pass

    updaterRetries -= 1
if (updaterRetries == 0):
    print("Error: Update server could not be reached")
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

print("\n\nThe latest available version is " + list(availableFiles.keys())[0] + "\n\n")

categories = []
for category in availableFiles.keys():
    categories.append( (category, "") )

# Select outputDir and targetFile
outputDir = libhearingdownloader.selectOutputFolder()

simpleSelection = libhearingdownloader.selectFromList(categories, prompt="category to download from", headerSeperator='\n')
targetCategory = categories[simpleSelection][0]
if (libhearingdownloader.verboseDebug):
    print(targetCategory)

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