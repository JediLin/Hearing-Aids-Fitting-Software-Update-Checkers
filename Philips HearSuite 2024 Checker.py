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
from iso3166 import countries
import libhearingdownloader
import xml.etree.ElementTree as xml

just_fix_windows_console()

print("\n\n")
print("==================================================")
print("=        " + Style.BRIGHT + Fore.BLUE + "Philips" + Style.RESET_ALL + " HearSuite Update Checker        =")
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
    "Philips is a trademark of Koninklijke Philips N.V.",
    "Philips HearSuite is created by Philips",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by",
    "Philips",
    "Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software.",
    "The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

# Read configuration file for toggles with default True
config = configparser.ConfigParser()
config.read('config.ini')
fallbackMarket = config.get('Philips', 'Market', fallback='Default')

# Read target market from GitHub or local configuration
localMarketPath = Path("Philips.market")
onlineMarketPath = "https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/raw/refs/heads/main/Philips.market"
defaultMarketSrc = ""
try:
    onlineMarketFile = requests.get(onlineMarketPath)
    onlineMarket = onlineMarketFile.text.split("\n", 1)[0]
    if (onlineMarket.isalpha()):
        defaultMarket = onlineMarket
        defaultMarketSrc = "online-"
    else:
        if localMarketPath.is_file():
            with localMarketPath.open("r") as localMarketFile:
                localMarket = localMarketFile.read().split("\n", 1)[0]
                if (localMarket.isalpha()):
                    defaultMarket = localMarket
                    defaultMarketSrc = "local-"
                else:
                    defaultMarket = fallbackMarket
        else:
            defaultMarket = fallbackMarket
except:
    if localMarketPath.is_file():
        with localMarketPath.open("r") as localMarketFile:
            localMarket = localMarketFile.read().split("\n", 1)[0]
            if (localMarket.isalpha()):
                defaultMarket = localMarket
                defaultMarketSrc = "local-"
            else:
                defaultMarket = fallbackMarket
    else:
        defaultMarket = fallbackMarket

# Target market input
inputMarket = input("\nPlease enter " + Fore.GREEN + "target market country code" + Style.RESET_ALL + " [" + defaultMarketSrc + "default: " + Fore.YELLOW + defaultMarket + Style.RESET_ALL + "]: ")
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

print ("\n\nFetching version index...")
headers = {
    "Host": "updater.sbohearing.com",
    "Content-Type": "application/soap+xml; charset=utf-8"
}

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        # checker variables, may effect the latest version available from API
        # Download version data, pretending installed HearSuite2 v20.22.95.0 with PhilipsHearSuiteUpdater v26.9.3.0
        # This is required to get update for newer (2024.2+) versions.
        # Software names set by b:Name
        # Version numbers set by b:Major . b:Minor . b:Build . b:Revision
        osVer = config.get('Philips', 'OS', fallback='Microsoft Windows NT 10.0.22621.0')
        baseVer = config.get('Philips', 'Version', fallback='20.22.95.0').split('.')
        updrVer = config.get('Philips', 'Updater', fallback='26.9.3.0').split('.')
        baseVerMajor = baseVer[0]
        baseVerMinor = baseVer[1]
        baseVerBuild = baseVer[2]
        baseVerRev = baseVer[3]
        updrVerMajor = updrVer[0]
        updrVerMinor = updrVer[1]
        updrVerBuild = updrVer[2]
        updrVerRev = updrVer[3]
        osVer = "Microsoft Windows NT 10.0.22621.0"
        rawXmlData = requests.post("https://updater.sbohearing.com/UpdateWebService.svc", headers=headers, data='<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateWebService/CheckForUpdate</a:Action><a:MessageID>urn:uuid:00000000-0000-0000-0000-000000000000</a:MessageID><a:ReplyTo><a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address></a:ReplyTo><a:To s:mustUnderstand="1">https://updater.sbohearing.com/UpdateWebService.svc</a:To></s:Header><s:Body><CheckForUpdate xmlns="http://tempuri.org/"><request xmlns:b="http://schemas.datacontract.org/2004/07/Wdh.Genesis.SoftwareUpdater.Common" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"><b:ClientId>00000000-0000-0000-0000-000000000000</b:ClientId><b:Customer>Philips</b:Customer><b:Languages xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/><b:Locale i:nil="true"/><b:Manufacturer>Philips HearSuite</b:Manufacturer><b:Market>' + targetMarket + '</b:Market><b:OEM i:nil="true"/><b:OS>' + osVer + '</b:OS><b:RequestVersion>2</b:RequestVersion><b:Software><b:InstalledSoftware><b:Build>' + baseVerBuild + '</b:Build><b:Major>' + baseVerMajor + '</b:Major><b:Minor>' + baseVerMinor + '</b:Minor><b:Name>HearSuite2</b:Name><b:Revision>' + baseVerRev + '</b:Revision></b:InstalledSoftware><b:InstalledSoftware><b:Build>' + updrVerBuild + '</b:Build><b:Major>' + updrVerMajor + '</b:Major><b:Minor>' + updrVerMinor + '</b:Minor><b:Name>PhilipsHearSuiteUpdater</b:Name><b:Revision>' + updrVerRev + '</b:Revision></b:InstalledSoftware></b:Software></request></CheckForUpdate></s:Body></s:Envelope>')
        data = xml.fromstring(html.unescape(rawXmlData.text))
        break
    except Exception as e:
        print(e)
        pass

    updaterRetries -= 1
if (updaterRetries == 0):
    print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": Update server could not be reached")
    exit(1)

if (rawXmlData.text == '<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateWebService/CheckForUpdateResponse</a:Action><a:RelatesTo>urn:uuid:00000000-0000-0000-0000-000000000000</a:RelatesTo></s:Header><s:Body><CheckForUpdateResponse xmlns="http://tempuri.org/"><CheckForUpdateResult/></CheckForUpdateResponse></s:Body></s:Envelope>'):
    print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": The latest available version for " + Fore.GREEN + targetMarket + Style.RESET_ALL + " market is not found!\n\n")
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
    (data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdateResponse").find('{http://tempuri.org/}' + "CheckForUpdateResult").find(packageXMLNS + "UpdateManifest").find(packageXMLNS + "Messages").find(packageXMLNS + "Message").text, "The latest Philips HearSuite Installer (OFFLINE) (from the updater)"),
    (data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdateResponse").find('{http://tempuri.org/}' + "CheckForUpdateResult").find(packageXMLNS + "UpdateManifest").find(packageXMLNS + "Messages").find(packageXMLNS + "Message").text, "The latest Philips HearSuite Installer (ONLINE) (from the updater)"),
]
print("\n\nThe latest available version for " + Fore.GREEN + targetMarket + Style.RESET_ALL + " market is " + Fore.GREEN + data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdateResponse").find('{http://tempuri.org/}' + "CheckForUpdateResult").find(packageXMLNS + "UpdateManifest").find(packageXMLNS + "Messages").find(packageXMLNS + "Message").text + Style.RESET_ALL + "\n\n")

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