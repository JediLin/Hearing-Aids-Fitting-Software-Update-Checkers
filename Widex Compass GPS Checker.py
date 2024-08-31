#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import os
import shutil
import zipfile
import requests
import libhearingdownloader
import xml.etree.ElementTree as xml


print("==================================================")
print("=        Widex Compass GPS Update Checker         =")
print("="*(47-len(libhearingdownloader.downloaderVersion)) + " " + libhearingdownloader.downloaderVersion + " =")

libhearingdownloader.printWaranty()
disclaimer = [
    "DISCLAIMER",
    "",
    "I (Bluebotlabz), do not take any responsability for what you do using this software",
    "Widex is a trademark of Widex A/S",
    "Widex A/S is a subsidiaries of WS Audiology A/S",
    "WS Audiology A/S is a trademark of Widex A/S",
    "Widex Compass GPS is created by Widex A/S",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "Bluebotlabz and this downloader are not affiliated with or endorsed by WS Audiology A/S or Widex A/S",
    "Depending on how this software is used, it may violate the EULA and/or Terms and Conditions of the downloaded software",
    "This is an UNOFFICIAL downloader and use of the software downloaded using it may be limited"
]

# Display disclaimer
libhearingdownloader.printDisclaimer(disclaimer)


# Special headers for the siavantos updater API
headers = {
    "SOAPAction": "http://tempuri.org/IUpdateService/CheckForUpdates",
    "Host": "widexautomaticupdate.cloudapp.net",
    "Content-Type": "text/xml; charset=utf-8"
}

updateData = '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body><CheckForUpdates xmlns="http://tempuri.org/"><statusDescriptor xmlns:a="http://schemas.datacontract.org/2004/07/Widex.AutomaticUpdate.UpdateService" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"><a:ClientId>00000000-0000-0000-0000-000000000000</a:ClientId><a:DistributorCode>70039</a:DistributorCode><a:ProductStatusDescriptors><a:ProductStatusDescriptor><a:PackageStatusDescriptors><a:PackageStatusDescriptor><a:PackageName>Code</a:PackageName><a:PackageVersion xmlns:b="http://schemas.datacontract.org/2004/07/System"><b:_Build>3079</b:_Build><b:_Major>4</b:_Major><b:_Minor>3</b:_Minor><b:_Revision>0</b:_Revision></a:PackageVersion></a:PackageStatusDescriptor><a:PackageStatusDescriptor><a:PackageName>en-GB</a:PackageName><a:PackageVersion xmlns:b="http://schemas.datacontract.org/2004/07/System"><b:_Build>3079</b:_Build><b:_Major>4</b:_Major><b:_Minor>3</b:_Minor><b:_Revision>0</b:_Revision></a:PackageVersion></a:PackageStatusDescriptor><a:PackageStatusDescriptor><a:PackageName>Compass</a:PackageName><a:PackageVersion xmlns:b="http://schemas.datacontract.org/2004/07/System"><b:_Build>3079</b:_Build><b:_Major>4</b:_Major><b:_Minor>3</b:_Minor><b:_Revision>0</b:_Revision></a:PackageVersion></a:PackageStatusDescriptor></a:PackageStatusDescriptors><a:ProductIdentifier>CompassGPS</a:ProductIdentifier><a:ProductName>COMPASS GPS</a:ProductName><a:ProductVersion xmlns:b="http://schemas.datacontract.org/2004/07/System"><b:_Build>3079</b:_Build><b:_Major>4</b:_Major><b:_Minor>3</b:_Minor><b:_Revision>0</b:_Revision></a:ProductVersion></a:ProductStatusDescriptor></a:ProductStatusDescriptors></statusDescriptor></CheckForUpdates></s:Body></s:Envelope>'

availableLanguages = [
    ("Chinese-CN", "zh-CN"),
    ("Chinese-TW", "zh-TW"),
    ("Czech-CZ", "cs-CZ"),
    ("Danish-DK", "da-DK"),
#    ("English-GB", "en-GB"), (already downloaded without this list)
    ("English-US", "en-US"),
    ("Finnish-FI", "fi-FI"),
    ("French-FR", "fr-FR"),
    ("German-DE", "de-DE"),
    ("Hungarian-HU", "hu-HU"),
    ("Italian-IT", "it-IT"),
    ("Japanese-JP", "ja-JP"),
    ("Korean-KR", "ko-KR"),
    ("Norwegian-NO", "nn-NO"),
    ("Polish-PL", "pl-PL"),
    ("Portuguese-PT", "pt-PT"),
    ("Russian-RU", "ru-RU"),
    ("Spanish-ES", "es-ES"),
    ("Swedish-SE", "sv-SE"),
    ("Turkish-TR", "tr-TR")
]

## targetLanguage = libhearingdownloader.selectFromList(availableLanguages, 'language', seperator='\t\t')
## updateData = updateData.replace('en-GB', availableLanguages[targetLanguage][1])

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        # Download update file list from updater API
        rawXmlData = requests.post("http://widexautomaticupdate.cloudapp.net/UpdateService.svc", headers=headers, data=updateData)
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
packageXMLNS = '{http://schemas.datacontract.org/2004/07/Widex.AutomaticUpdate.UpdateService}'
filesToDownload = [] # List of available files

for child in data.find('{http://schemas.xmlsoap.org/soap/envelope/}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdatesResponse").find('{http://tempuri.org/}' + "CheckForUpdatesResult").find(packageXMLNS + "ProductTargetDescriptors").find(packageXMLNS + "ProductTargetDescriptor").find(packageXMLNS + "PackageTargetDescriptors"):
    filesToDownload.append( (child.find(packageXMLNS + "Filename").text, child.find(packageXMLNS + "DownloadUrl").text) )

    if (child.find(packageXMLNS + "Filename").text == 'en-GB.msi'):
        for availableLanguage in availableLanguages:
            filesToDownload.append( (child.find(packageXMLNS + "Filename").text.replace('en-GB', availableLanguage[1]), child.find(packageXMLNS + "DownloadUrl").text.replace('en-GB', availableLanguage[1])) )

setupFileURL = data.find('{http://schemas.xmlsoap.org/soap/envelope/}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdatesResponse").find('{http://tempuri.org/}' + "CheckForUpdatesResult").find(packageXMLNS + "ProductTargetDescriptors").find(packageXMLNS + "ProductTargetDescriptor").find(packageXMLNS + "SetupFileDownloadUrl").text

filesToDownload.append( (setupFileURL.split("/")[-1], setupFileURL) )

if (libhearingdownloader.verboseDebug):
    print(filesToDownload)

# Select outputDir and targetFile
outputDir = libhearingdownloader.selectOutputFolder()

# Create download folder
outputDir += "Widex Compass GPS/"
print("\n\n")


# Download and save the files
print("Downloading " + str(len(filesToDownload)) + " files\n")
currentFile = 1
for fileToDownload in filesToDownload:
    if (libhearingdownloader.verboseDebug):
        print(fileToDownload)

    # Download file
    libhearingdownloader.downloadFile(fileToDownload[1], outputDir + fileToDownload[0], "Downloading " + fileToDownload[1].split("/")[-1] + " (" + str(currentFile) + "/" + str(len(filesToDownload)) + ")")

    currentFile += 1

print("\n\n")
print("Creating installer from zip")
with zipfile.ZipFile(outputDir + "Setup.exe.zip", 'r') as zipFile:
    zipFile.extractall(outputDir)

os.makedirs(outputDir + "installations/")

for file in filesToDownload[:-1]:
    shutil.move(outputDir + file[0], outputDir + "installations/" + file[0])

os.remove(outputDir + filesToDownload[-1][0])

print("\n\nDownload Complete!")