import os
import requests
import json
import libhearingdownloader

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        rawJsonData = requests.get("https://api.github.com/repos/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/releases/latest")
        data = json.loads(rawJsonData.text)
        break
    except:
        pass

    updaterRetries -= 1
if (updaterRetries == 0):
    print("Error: Update server could not be reached")
    exit(1)

if (libhearingdownloader.verboseDebug):
    print(rawJsonData.text)

print("\n\nThe latest available version is " + data['tag_name'])
print("\nYou are using " + libhearingdownloader.downloaderVersion + "\n")

if (data['tag_name'] == libhearingdownloader.downloaderVersion):
    print("No update available.")
    exit(1)

availableFiles = [] # List of available files
availableFiles.append( (os.path.basename(data['assets'][0]['browser_download_url']), data['assets'][0]['browser_download_url']) )

if (libhearingdownloader.verboseDebug):
    print(availableFiles)

# Select outputDir and targetFile
outputDir = libhearingdownloader.selectOutputFolder()
targetFile = availableFiles[libhearingdownloader.selectFromList(availableFiles)]

# Create download folder
downloadVer = 'Update Checker ' + data['tag_name']
outputDir += '.'.join(downloadVer.split('.')) + "/"
print("\n\n")

# Download file
libhearingdownloader.downloadFile(targetFile[1], outputDir + targetFile[0], "Downloading " + targetFile[0])

print("\n\nDownload Complete!")

