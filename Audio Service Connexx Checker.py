#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
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
print("=      " + Style.BRIGHT + Fore.BLUE + "Audio Service" + Style.RESET_ALL + " Connexx Update Checker      =")
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
    "Audio Service is a trademark of SIVANTOS PTE. LTD.",
    "Siavantos is a trademark of SIVANTOS PTE. LTD.",
    "Audio Service and Siavantos are subsidiaries of WS Audiology A/S",
    "WS Audiology A/S is a trademark of Widex A/S",
    "Widex is a trademark of Widex A/S",
    "Audio Service Connexx is created by Audio Service",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by",
    "Signia GmbH, SIVANTOS PTE. LTD., WS Audiology A/S or Widex A/S",
    "Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions of the associated software.",
    "The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

# Read target market from GitHub or local configuration
fallbackMarket = "FR"
localMarketPath = Path("Audio Service.market")
onlineMarketPath = "https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/raw/refs/heads/main/Audio Service.market"
try:
    onlineMarketFile = requests.get(onlineMarketPath)
    onlineMarket = onlineMarketFile.text.split("\n", 1)[0]
    if (onlineMarket.isalpha()):
        defaultMarket = onlineMarket
    else:
        if localMarketPath.is_file():
            with localMarketPath.open("r") as localMarketFile:
                localMarket = localMarketFile.read().split("\n", 1)[0]
                if (localMarket.isalpha()):
                    defaultMarket = localMarket
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
            else:
                defaultMarket = fallbackMarket
    else:
        defaultMarket = fallbackMarket

# Target market input
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

print ("\n\nFetching version index...")
# Special headers for the siavantos updater API
headers = {
    "Content-Type": "application/soap+xml; charset=utf-8",
    "Connection": "Keep-Alive"
}

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        # checker variables, may effect the latest version available from API
        baseVer = "9.12.0.1516"
        supVer = "9.12.3.281"
        upmVer = "19.12.3.281"
        # Download update file list from updater API
        rawXmlData = requests.post("https://upman-client.cloudapi.sivantos.com/Service/UpdateManagerService.svc", headers=headers, data='<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateManagerService/GetPackages</a:Action><a:MessageID>urn:uuid:00000000-0000-0000-0000-000000000000</a:MessageID><a:ReplyTo><a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address></a:ReplyTo><a:To s:mustUnderstand="1">https://upman-client.cloudapi.sivantos.com/Service/UpdateManagerService.svc</a:To></s:Header><s:Body><GetPackages xmlns="http://tempuri.org/"><products xmlns:b="http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"><b:ProductInfo><b:CurrentVersion>' + upmVer + '</b:CurrentVersion><b:ProductName>Update Manager</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>' + supVer + '</b:CurrentVersion><b:ProductName>Programmer</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>' + baseVer + '</b:CurrentVersion><b:ProductName>AudioServiceConnexx</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>' + supVer + '</b:CurrentVersion><b:ProductName>Support Tools</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>4.8.0.0</b:CurrentVersion><b:ProductName>DotNetFramework</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>6.0.5.00</b:CurrentVersion><b:ProductName>DotNetCoreRuntime</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>10.0.22.0</b:CurrentVersion><b:ProductName>OperatingSystem</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>14.32.31.00</b:CurrentVersion><b:ProductName>VC2015Redistributable</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo></products></GetPackages></s:Body></s:Envelope>')
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

if (rawXmlData.text == '<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateManagerService/GetPackagesResponse</a:Action><a:RelatesTo>urn:uuid:00000000-0000-0000-0000-000000000000</a:RelatesTo></s:Header><s:Body><GetPackagesResponse xmlns="http://tempuri.org/"><GetPackagesResult xmlns:b="http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"/></GetPackagesResponse></s:Body></s:Envelope>'):
    print("\n" + Fore.RED + "Error" + Style.RESET_ALL + ": The latest available Audio Service Connexx version for " + Fore.GREEN + targetMarket + Style.RESET_ALL + " market is not found!\n\n")
    exit(1)

# Define XMLNS (the main one)
packageXMLNS = '{http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS}'
availableFiles = [] # List of available files

appVer = data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "GetPackagesResponse").find('{http://tempuri.org/}' + "GetPackagesResult").find(packageXMLNS + "Package").find(packageXMLNS + "NewVersion").text

for child in data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "GetPackagesResponse").find('{http://tempuri.org/}' + "GetPackagesResult").find(packageXMLNS + "Package").find(packageXMLNS + "PackageFiles"):
    availableFiles.append( (appVer, child.find(packageXMLNS + "FileName").text, child.find(packageXMLNS + "DownloadURL").text) )

if (libhearingdownloader.verboseDebug):
    print(availableFiles)

print("\n\nThe latest available Audio Service Connexx version for " + Fore.GREEN + targetMarket + Style.RESET_ALL + " market is " + Fore.GREEN + "v" + availableFiles[0][0] + Style.RESET_ALL + "\n\n")

# Select outputDir and targetFile
outputDir = libhearingdownloader.selectOutputFolder()
targetFile = availableFiles[libhearingdownloader.selectFromList(availableFiles)]

# Create download folder
downloadVer = 'Audio Service Connexx ' + targetFile[0]
outputDir += '.'.join(downloadVer.split('.')) + "/"
print("\n\n")

# Download file
libhearingdownloader.downloadFile(targetFile[2], outputDir + targetFile[1], "Downloading " + targetFile[1])

print("\n\nDownload Complete!")