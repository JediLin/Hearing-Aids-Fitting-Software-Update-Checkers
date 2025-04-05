#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import html
import requests
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader
import xml.etree.ElementTree as xml

just_fix_windows_console()

print("\n\n")
print("==================================================")
print("=     " + Style.BRIGHT + Fore.RED + "Bernafon" + Style.RESET_ALL + " OasisNXT Custom Update Checker    =")
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
    "OasisNXT is a trademark of Bernafon",
    "Bernafon is a trademark of Oticon A/S",
    "Demant is a trademark of Demant A/S",
    "Oticon is a subsidiary of Demant A/S",
    "Oticon is a trademark of Oticon A/S",
    "OasisNXT is created by Bernafon",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by",
    "Oticon or Demant A/S",
    "Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software.",
    "The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

print ("\n\nDownloading version index...")
headers = {
    "Host": "updater.bernafon.com",
    "Content-Type": "application/soap+xml; charset=utf-8"
}

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        # checker variables, may effect the latest version available from API
        # Download version data, pretending installed Oasis2 v20.22.95.0 with BernafonUpdater v27.3.26.0
        # This is required to get update for newer (2024+) versions.
        # Software names set by b:Name
        # Version numbers set by b:Major . b:Minor . b:Build . b:Revision
        # b:OEM set to some string other than Bernafon to get Custom version
        # 0153	Delight
        # 0156	ProAkustik
        # 0653	Lisound
        # 0664	Specsavers
        # 0714	Meditrend
        # 0800	GPL
        # 0805	Maico
        # 0854	Audilab
        # 0965	RITM
        # 1069	Hoerex
        # 2501	Sonic
        osVer = "Microsoft Windows NT 10.0.22621.0"
        targetMarket = "Default"
        baseOEM = "0153"
        baseVerMajor = "20"
        baseVerMinor = "22"
        baseVerBuild = "95"
        baseVerRev = "0"
        updrVerMajor = "27"
        updrVerMinor = "3"
        updrVerBuild = "26"
        updrVerRev = "0"
        rawXmlData = requests.post("https://updater.bernafon.com/UpdateWebService.svc", headers=headers, data='<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateWebService/CheckForUpdate</a:Action><a:MessageID>urn:uuid:00000000-0000-0000-0000-000000000000</a:MessageID><a:ReplyTo><a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address></a:ReplyTo><a:To s:mustUnderstand="1">https://updater.bernafon.com/UpdateWebService.svc</a:To></s:Header><s:Body><CheckForUpdate xmlns="http://tempuri.org/"><request xmlns:b="http://schemas.datacontract.org/2004/07/Wdh.Genesis.SoftwareUpdater.Common" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"><b:ClientId>00000000-0000-0000-0000-000000000000</b:ClientId><b:Languages xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/><b:Locale>' + targetMarket + '</b:Locale><b:Manufacturer>Bernafon</b:Manufacturer><b:OEM>' + baseOEM + '</b:OEM><b:OS>' + osVer + '</b:OS><b:RequestVersion>1</b:RequestVersion><b:Software><b:InstalledSoftware><b:Build>' + updrVerBuild + '</b:Build><b:Major>' + updrVerMajor + '</b:Major><b:Minor>' + updrVerMinor + '</b:Minor><b:Name>BernafonUpdater</b:Name><b:Revision>' + updrVerRev + '</b:Revision></b:InstalledSoftware><b:InstalledSoftware><b:Build>' + baseVerBuild + '</b:Build><b:Major>' + baseVerMajor + '</b:Major><b:Minor>' + baseVerMinor + '</b:Minor><b:Name>Oasis2</b:Name><b:Revision>' + baseVerRev + '</b:Revision></b:InstalledSoftware></b:Software></request></CheckForUpdate></s:Body></s:Envelope>')
        data = xml.fromstring(html.unescape(rawXmlData.text))
        break
    except:
        pass

    updaterRetries -= 1
if (updaterRetries == 0):
    print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": Update server could not be reached")
    exit(1)
    
packageXMLNS = '{http://www.wdh.com/xml/2012/06/25/updatemanifest.xsd}'
filesToDownload = []

if (libhearingdownloader.verboseDebug):
    print(html.unescape(rawXmlData.text))

# Get list of files
for fileData in data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdateResponse").find('{http://tempuri.org/}' + "CheckForUpdateResult").find(packageXMLNS + "UpdateManifest").find(packageXMLNS + "DownloadJob").find(packageXMLNS + "Files"):
    filesToDownload.append(fileData.find(packageXMLNS + "FileName").text)

# Get download server uri
downloadURI = data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdateResponse").find('{http://tempuri.org/}' + "CheckForUpdateResult").find(packageXMLNS + "UpdateManifest").find(packageXMLNS + "DownloadJob").find(packageXMLNS + "ServerUri").text

# Get latest version
if (libhearingdownloader.verboseDebug):
    print(data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdateResponse").find('{http://tempuri.org/}' + "CheckForUpdateResult").find(packageXMLNS + "UpdateManifest").find(packageXMLNS + "Messages").find(packageXMLNS + "Message").text   + "--" +   data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdateResponse").find('{http://tempuri.org/}' + "CheckForUpdateResult").find(packageXMLNS + "UpdateManifest").find(packageXMLNS + "Version").text)

# Define list of valid versions and their download links (direct from CDN) (predefined to online and offline of latest version)
validVersions = [
    (data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdateResponse").find('{http://tempuri.org/}' + "CheckForUpdateResult").find(packageXMLNS + "UpdateManifest").find(packageXMLNS + "Messages").find(packageXMLNS + "Message").text, "The latest OasisNXT Custom Installer (OFFLINE) (from the updater)"),
    (data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdateResponse").find('{http://tempuri.org/}' + "CheckForUpdateResult").find(packageXMLNS + "UpdateManifest").find(packageXMLNS + "Messages").find(packageXMLNS + "Message").text, "The latest OasisNXT Custom Installer (ONLINE) (from the updater)"),
]
print("\n\nThe latest available version is " + Fore.GREEN + data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdateResponse").find('{http://tempuri.org/}' + "CheckForUpdateResult").find(packageXMLNS + "UpdateManifest").find(packageXMLNS + "Messages").find(packageXMLNS + "Message").text + Style.RESET_ALL + "\n\n")

if (libhearingdownloader.verboseDebug):
    print(filesToDownload)

# Select outputDir and targetVersion
outputDir = libhearingdownloader.selectOutputFolder()
targetVersion = libhearingdownloader.selectFromList(validVersions)
print("\n\n")


if (targetVersion == 0):
    outputDir += libhearingdownloader.normalizePath( data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdateResponse").find('{http://tempuri.org/}' + "CheckForUpdateResult").find(packageXMLNS + "UpdateManifest").find(packageXMLNS + "Messages").find(packageXMLNS + "Message").text + "/")

    # Download and save the files
    print("Downloading " + str(len(filesToDownload)) + " files\n")
    fileIndex = 1
    for fileToDownload in filesToDownload:
        libhearingdownloader.downloadFile(downloadURI + fileToDownload, outputDir + fileToDownload, "Downloading " + fileToDownload.split("/")[-1] + " (" + str(fileIndex) + "/" + str(len(filesToDownload)) + ")")
        fileIndex += 1
elif (targetVersion == 1):
    outputDir += libhearingdownloader.normalizePath( data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdateResponse").find('{http://tempuri.org/}' + "CheckForUpdateResult").find(packageXMLNS + "UpdateManifest").find(packageXMLNS + "Messages").find(packageXMLNS + "Message").text + "/")

    # Download and save the files
    fileIndex = 1
    fileToDownload = "setup.exe"
    libhearingdownloader.downloadFile(downloadURI + fileToDownload, outputDir + fileToDownload, "Downloading " + fileToDownload.split("/")[-1])

print("\n\nDownload Complete!")