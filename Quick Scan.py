import configparser
import re
import datetime
import tzlocal
import html
import json
import requests
import rot_codec
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
from iso3166 import countries
import libhearingdownloader
import xml.etree.ElementTree as xml

just_fix_windows_console()

# Read configuration file for toggles with default True
config = configparser.ConfigParser()
config.read('config.ini')
scanPhonak = config.getboolean('Phonak', 'QuickScan', fallback='True')
scanUnitron = config.getboolean('Unitron', 'QuickScan', fallback='True')
scanHansaton = config.getboolean('Hansaton', 'QuickScan', fallback='True')
scanOticon = config.getboolean('Oticon', 'QuickScan', fallback='True')
scanBernafon = config.getboolean('Bernafon', 'QuickScan', fallback='True')
scanSonic = config.getboolean('Sonic', 'QuickScan', fallback='True')
scanPhilips = config.getboolean('Philips', 'QuickScan', fallback='True')
scanReSound = config.getboolean('ReSound', 'QuickScan', fallback='True')
scanBeltone = config.getboolean('Beltone', 'QuickScan', fallback='True')
scanInterton = config.getboolean('Interton', 'QuickScan', fallback='True')
scanSignia = config.getboolean('Signia', 'QuickScan', fallback='True')
scanRexton = config.getboolean('Rexton', 'QuickScan', fallback='True')
scanAudioService = config.getboolean('AudioService', 'QuickScan', fallback='True')
scanAM = config.getboolean('AM', 'QuickScan', fallback='True')
scanWidex = config.getboolean('Widex', 'QuickScan', fallback='True')
scanStarkey = config.getboolean('Starkey', 'QuickScan', fallback='True')
scanSkipAll = False
if not (scanPhonak or scanUnitron or scanHansaton or scanOticon or scanBernafon or scanSonic or scanPhilips or scanReSound or scanBeltone or scanInterton or scanSignia or scanRexton or scanAudioService or scanAM or scanWidex or scanStarkey):
    scanSkipAll = True

print("\n\n")
print("==================================================")
print("=  " + Style.BRIGHT + Fore.YELLOW + "Hearing Aids Fitting Software Update Checkers" + Style.RESET_ALL + " =")
print("=                   " + Style.BRIGHT + Fore.RED + "Q" + Fore.YELLOW + "U" + Fore.CYAN + "I" + Fore.GREEN + "C" + Fore.BLUE + "K" + Style.RESET_ALL + " Scan                   =")
print("="*(47-len(libhearingdownloader.downloaderVersion)) + " " + Fore.GREEN + libhearingdownloader.downloaderVersion + Style.RESET_ALL + " =")

turboFile = Path("turbo.txt")
if not turboFile.is_file():
    libhearingdownloader.printWaranty()

disclaimer = [
    "DISCLAIMER",
    "",
    "The contributors of the Hearing Aids Fitting Software Update Checkers (\"The Checker\") do not take any responsability",
    "for what you do with The Checker. All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "The contributors of The Checker, and The Checker itself are not affiliated with or endorsed by any of the companies",
    "mentioned in The Checker. Depending on how The Checker is used, it may violate the EULA and/or Terms and Conditions",
    "of the associated software. The Checker is an UNOFFICIAL project and the use of associated software may be limited."
]

# Display disclaimer
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)
    exit(1)

# Sonova: Phonak, Unitron, Hansaton
def phonakTargetChecker(market):
    targetMarket = market
    baseVer = config.get('Phonak', 'Version', fallback='6.0.1.695')
    xmlns = "{http://cocoon.phonak.com}"
    updaterRetries = libhearingdownloader.updaterRetries
    while updaterRetries > 0:
        try:
            xmlData = requests.get("https://p-svc1.phonakpro.com/1/ObjectLocationService.svc/FittingApplicationInstaller/index?appName=Phonak%20Target&appVer=" + baseVer + "&dist=Phonak&country=" + targetMarket + "&subKeys=").text
            data = xml.fromstring(xmlData)
            break
        except:
            pass

        updaterRetries -= 1
    if (updaterRetries == 0):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    elif (xmlData == '<ArrayOfContentIndex xmlns="http://cocoon.phonak.com" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"/>'):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    else:
        latestVersion = data[0].find(xmlns + "UpdateVersion").find(xmlns + "Version").text
        print(Fore.GREEN + "v" + latestVersion + Style.RESET_ALL + " (" + targetMarket + ")", end="")

def unitronTrueFitChecker(market):
    targetMarket = market
    baseVer = config.get('Unitron', 'Version', fallback='5.1.0.25391')
    xmlns = "{http://cocoon.phonak.com}"
    updaterRetries = libhearingdownloader.updaterRetries
    while updaterRetries > 0:
        try:
            xmlData = requests.get("https://svc.myunitron.com/1/ObjectLocationService.svc/FittingApplicationInstaller/index?appName=Unitron%20TrueFit&appVer=" + baseVer + "&dist=Unitron&country=" + targetMarket + "&subKeys=").text
            data = xml.fromstring(xmlData)
            break
        except:
            pass

        updaterRetries -= 1
    if (updaterRetries == 0):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    elif (xmlData == '<ArrayOfContentIndex xmlns="http://cocoon.phonak.com" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"/>'):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    else:
        latestVersion = data[0].find(xmlns + "UpdateVersion").find(xmlns + "Version").text
        print(Fore.GREEN + "v" + latestVersion + Style.RESET_ALL + " (" + targetMarket + ")", end="")

def hansatonScoutChecker(market):
    targetMarket = market
    baseVer = config.get('Hansaton', 'Version', fallback='5.1.0.26954')
    xmlns = "{http://cocoon.phonak.com}"
    updaterRetries = libhearingdownloader.updaterRetries
    while updaterRetries > 0:
        try:
            xmlData = requests.get("https://svc.myunitron.com/1/ObjectLocationService.svc/FittingApplicationInstaller/index?appName=HANSATON%20scout&appVer=" + baseVer + "&dist=Balance&country=" + targetMarket + "&subKeys=").text
            data = xml.fromstring(xmlData)
            break
        except:
            pass

        updaterRetries -= 1
    if (updaterRetries == 0):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    elif (xmlData == '<ArrayOfContentIndex xmlns="http://cocoon.phonak.com" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"/>'):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    else:
        latestVersion = data[0].find(xmlns + "UpdateVersion").find(xmlns + "Version").text
        print(Fore.GREEN + "v" + latestVersion + Style.RESET_ALL + " (" + targetMarket + ")", end="")

# Demant: Oticon, Bernafon, Sonic, Philips
def oticonGenie2Checker(market):
    targetMarket = market
    headers = {
        "Content-Type": "application/soap+xml; charset=utf-8"
    }

    updaterRetries = libhearingdownloader.updaterRetries
    while updaterRetries > 0:
        try:
            osVer = config.get('Oticon', 'OS', fallback='Microsoft Windows NT 10.0.22621.0')
            baseVer = config.get('Oticon', 'Version', fallback='20.22.95.0').split('.')
            updrVer = config.get('Oticon', 'Updater', fallback='27.2.19.0').split('.')
            baseVerMajor = baseVer[0]
            baseVerMinor = baseVer[1]
            baseVerBuild = baseVer[2]
            baseVerRev = baseVer[3]
            updrVerMajor = updrVer[0]
            updrVerMinor = updrVer[1]
            updrVerBuild = updrVer[2]
            updrVerRev = updrVer[3]
            rawXmlData = requests.post("https://updater.oticon.com/UpdateWebService.svc", headers=headers, data='<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateWebService/CheckForUpdate</a:Action><a:MessageID>urn:uuid:00000000-0000-0000-0000-000000000000</a:MessageID><a:ReplyTo><a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address></a:ReplyTo><a:To s:mustUnderstand="1">https://updater.oticon.com/UpdateWebService.svc</a:To></s:Header><s:Body><CheckForUpdate xmlns="http://tempuri.org/"><request xmlns:b="http://schemas.datacontract.org/2004/07/Wdh.Genesis.SoftwareUpdater.Common" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"><b:ClientId>00000000-0000-0000-0000-000000000000</b:ClientId><b:Languages xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/><b:Locale>' + targetMarket + '</b:Locale><b:Manufacturer>Oticon</b:Manufacturer><b:OEM>Oticon</b:OEM><b:OS>' + osVer + '</b:OS><b:RequestVersion>1</b:RequestVersion><b:Software><b:InstalledSoftware><b:Build>' + baseVerBuild + '</b:Build><b:Major>' + baseVerMajor + '</b:Major><b:Minor>' + baseVerMinor + '</b:Minor><b:Name>Genie2</b:Name><b:Revision>' + baseVerRev + '</b:Revision></b:InstalledSoftware><b:InstalledSoftware><b:Build>' + updrVerBuild + '</b:Build><b:Major>' + updrVerMajor + '</b:Major><b:Minor>' + updrVerMinor + '</b:Minor><b:Name>OticonUpdater</b:Name><b:Revision>' + updrVerRev + '</b:Revision></b:InstalledSoftware></b:Software></request></CheckForUpdate></s:Body></s:Envelope>')
            data = xml.fromstring(html.unescape(rawXmlData.text))
            break
        except:
            pass

        updaterRetries -= 1
    if (updaterRetries == 0):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    elif (rawXmlData.text == '<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateWebService/CheckForUpdateResponse</a:Action><a:RelatesTo>urn:uuid:00000000-0000-0000-0000-000000000000</a:RelatesTo></s:Header><s:Body><CheckForUpdateResponse xmlns="http://tempuri.org/"><CheckForUpdateResult/></CheckForUpdateResponse></s:Body></s:Envelope>'):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    else:
        packageXMLNS = '{http://www.wdh.com/xml/2012/06/25/updatemanifest.xsd}'
        updateVer = data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdateResponse").find('{http://tempuri.org/}' + "CheckForUpdateResult").find(packageXMLNS + "UpdateManifest").find(packageXMLNS + "Messages").find(packageXMLNS + "Message").text
        print(Fore.GREEN + "v" + re.sub(r"Genie 2 . ", "", updateVer) + Style.RESET_ALL + " (" + targetMarket + ")", end="")

def bernafonOasisNXTChecker(market):
    targetMarket = market
    headers = {
        "Host": "updater.bernafon.com",
        "Content-Type": "application/soap+xml; charset=utf-8"
    }

    updaterRetries = libhearingdownloader.updaterRetries
    while updaterRetries > 0:
        try:
            osVer = config.get('Bernafon', 'OS', fallback='Microsoft Windows NT 10.0.22621.0')
            baseVer = config.get('Bernafon', 'Version', fallback='20.22.95.0').split('.')
            updrVer = config.get('Bernafon', 'Updater', fallback='27.3.26.0').split('.')
            baseVerMajor = baseVer[0]
            baseVerMinor = baseVer[1]
            baseVerBuild = baseVer[2]
            baseVerRev = baseVer[3]
            updrVerMajor = updrVer[0]
            updrVerMinor = updrVer[1]
            updrVerBuild = updrVer[2]
            updrVerRev = updrVer[3]
            rawXmlData = requests.post("https://updater.bernafon.com/UpdateWebService.svc", headers=headers, data='<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateWebService/CheckForUpdate</a:Action><a:MessageID>urn:uuid:00000000-0000-0000-0000-000000000000</a:MessageID><a:ReplyTo><a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address></a:ReplyTo><a:To s:mustUnderstand="1">https://updater.bernafon.com/UpdateWebService.svc</a:To></s:Header><s:Body><CheckForUpdate xmlns="http://tempuri.org/"><request xmlns:b="http://schemas.datacontract.org/2004/07/Wdh.Genesis.SoftwareUpdater.Common" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"><b:ClientId>00000000-0000-0000-0000-000000000000</b:ClientId><b:Languages xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/><b:Locale>' + targetMarket + '</b:Locale><b:Manufacturer>Bernafon</b:Manufacturer><b:OEM>Bernafon</b:OEM><b:OS>' + osVer + '</b:OS><b:RequestVersion>1</b:RequestVersion><b:Software><b:InstalledSoftware><b:Build>' + updrVerBuild + '</b:Build><b:Major>' + updrVerMajor + '</b:Major><b:Minor>' + updrVerMinor + '</b:Minor><b:Name>BernafonUpdater</b:Name><b:Revision>' + updrVerRev + '</b:Revision></b:InstalledSoftware><b:InstalledSoftware><b:Build>' + baseVerBuild + '</b:Build><b:Major>' + baseVerMajor + '</b:Major><b:Minor>' + baseVerMinor + '</b:Minor><b:Name>Oasis2</b:Name><b:Revision>' + baseVerRev + '</b:Revision></b:InstalledSoftware></b:Software></request></CheckForUpdate></s:Body></s:Envelope>')
            data = xml.fromstring(html.unescape(rawXmlData.text))
            break
        except:
            pass

        updaterRetries -= 1
    if (updaterRetries == 0):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    elif (rawXmlData.text == '<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateWebService/CheckForUpdateResponse</a:Action><a:RelatesTo>urn:uuid:00000000-0000-0000-0000-000000000000</a:RelatesTo></s:Header><s:Body><CheckForUpdateResponse xmlns="http://tempuri.org/"><CheckForUpdateResult/></CheckForUpdateResponse></s:Body></s:Envelope>'):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    else:
        packageXMLNS = '{http://www.wdh.com/xml/2012/06/25/updatemanifest.xsd}'
        updateVer = data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdateResponse").find('{http://tempuri.org/}' + "CheckForUpdateResult").find(packageXMLNS + "UpdateManifest").find(packageXMLNS + "Messages").find(packageXMLNS + "Message").text
        print(Fore.GREEN + "v" + re.sub(r"OasisNXT ", "", updateVer) + Style.RESET_ALL + " (" + targetMarket + ")", end="")

def sonicExpressFitChecker(market):
    targetMarket = market
    headers = {
        "Content-Type": "application/soap+xml; charset=utf-8"
    }

    updaterRetries = libhearingdownloader.updaterRetries
    while updaterRetries > 0:
        try:
            osVer = config.get('Sonic', 'OS', fallback='Microsoft Windows NT 10.0.22621.0')
            baseVer = config.get('Sonic', 'Version', fallback='20.22.95.0').split('.')
            updrVer = config.get('Sonic', 'Updater', fallback='26.9.3.0').split('.')
            baseVerMajor = baseVer[0]
            baseVerMinor = baseVer[1]
            baseVerBuild = baseVer[2]
            baseVerRev = baseVer[3]
            updrVerMajor = updrVer[0]
            updrVerMinor = updrVer[1]
            updrVerBuild = updrVer[2]
            updrVerRev = updrVer[3]
            rawXmlData = requests.post("https://updater.sonicinnovations.com/UpdateWebService.svc", headers=headers, data='<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateWebService/CheckForUpdate</a:Action><a:MessageID>urn:uuid:00000000-0000-0000-0000-000000000000</a:MessageID><a:ReplyTo><a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address></a:ReplyTo><a:To s:mustUnderstand="1">https://updater.sonicinnovations.com/UpdateWebService.svc</a:To></s:Header><s:Body><CheckForUpdate xmlns="http://tempuri.org/"><request xmlns:b="http://schemas.datacontract.org/2004/07/Wdh.Genesis.SoftwareUpdater.Common" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"><b:ClientId>00000000-0000-0000-0000-000000000000</b:ClientId><b:Customer>Sonic</b:Customer><b:Languages xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/><b:Locale i:nil="true"/><b:Manufacturer>Sonic</b:Manufacturer><b:Market>' + targetMarket + '</b:Market><b:OEM i:nil="true"/><b:OS>' + osVer + '</b:OS><b:RequestVersion>2</b:RequestVersion><b:Software><b:InstalledSoftware><b:Build>' + baseVerBuild + '</b:Build><b:Major>' + baseVerMajor + '</b:Major><b:Minor>' + baseVerMinor + '</b:Minor><b:Name>ExpressFit2</b:Name><b:Revision>' + baseVerRev + '</b:Revision></b:InstalledSoftware><b:InstalledSoftware><b:Build>' + updrVerBuild + '</b:Build><b:Major>' + updrVerMajor + '</b:Major><b:Minor>' + updrVerMinor + '</b:Minor><b:Name>SonicUpdater</b:Name><b:Revision>' + updrVerRev + '</b:Revision></b:InstalledSoftware></b:Software></request></CheckForUpdate></s:Body></s:Envelope>')
            data = xml.fromstring(html.unescape(rawXmlData.text))
            break
        except:
            pass

        updaterRetries -= 1
    if (updaterRetries == 0):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    elif (rawXmlData.text == '<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateWebService/CheckForUpdateResponse</a:Action><a:RelatesTo>urn:uuid:00000000-0000-0000-0000-000000000000</a:RelatesTo></s:Header><s:Body><CheckForUpdateResponse xmlns="http://tempuri.org/"><CheckForUpdateResult/></CheckForUpdateResponse></s:Body></s:Envelope>'):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    else:
        packageXMLNS = '{http://www.wdh.com/xml/2012/06/25/updatemanifest.xsd}'
        updateVer = data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdateResponse").find('{http://tempuri.org/}' + "CheckForUpdateResult").find(packageXMLNS + "UpdateManifest").find(packageXMLNS + "Messages").find(packageXMLNS + "Message").text
        print(Fore.GREEN + "v" + re.sub(r"EXPRESSfit Pro ", "", updateVer) + Style.RESET_ALL + " (" + targetMarket + ")", end="")

def philipsHearSuiteChecker(market):
    targetMarket = market
    headers = {
        "Content-Type": "application/soap+xml; charset=utf-8"
    }

    updaterRetries = libhearingdownloader.updaterRetries
    while updaterRetries > 0:
        try:
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
            rawXmlData = requests.post("https://updater.sbohearing.com/UpdateWebService.svc", headers=headers, data='<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateWebService/CheckForUpdate</a:Action><a:MessageID>urn:uuid:00000000-0000-0000-0000-000000000000</a:MessageID><a:ReplyTo><a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address></a:ReplyTo><a:To s:mustUnderstand="1">https://updater.sbohearing.com/UpdateWebService.svc</a:To></s:Header><s:Body><CheckForUpdate xmlns="http://tempuri.org/"><request xmlns:b="http://schemas.datacontract.org/2004/07/Wdh.Genesis.SoftwareUpdater.Common" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"><b:ClientId>00000000-0000-0000-0000-000000000000</b:ClientId><b:Customer>Philips</b:Customer><b:Languages xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/><b:Locale i:nil="true"/><b:Manufacturer>Philips HearSuite</b:Manufacturer><b:Market>' + targetMarket + '</b:Market><b:OEM i:nil="true"/><b:OS>' + osVer + '</b:OS><b:RequestVersion>2</b:RequestVersion><b:Software><b:InstalledSoftware><b:Build>' + baseVerBuild + '</b:Build><b:Major>' + baseVerMajor + '</b:Major><b:Minor>' + baseVerMinor + '</b:Minor><b:Name>HearSuite2</b:Name><b:Revision>' + baseVerRev + '</b:Revision></b:InstalledSoftware><b:InstalledSoftware><b:Build>' + updrVerBuild + '</b:Build><b:Major>' + updrVerMajor + '</b:Major><b:Minor>' + updrVerMinor + '</b:Minor><b:Name>PhilipsHearSuiteUpdater</b:Name><b:Revision>' + updrVerRev + '</b:Revision></b:InstalledSoftware></b:Software></request></CheckForUpdate></s:Body></s:Envelope>')
            data = xml.fromstring(html.unescape(rawXmlData.text))
            break
        except:
            pass

        updaterRetries -= 1
    if (updaterRetries == 0):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    elif (rawXmlData.text == '<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateWebService/CheckForUpdateResponse</a:Action><a:RelatesTo>urn:uuid:00000000-0000-0000-0000-000000000000</a:RelatesTo></s:Header><s:Body><CheckForUpdateResponse xmlns="http://tempuri.org/"><CheckForUpdateResult/></CheckForUpdateResponse></s:Body></s:Envelope>'):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    else:
        packageXMLNS = '{http://www.wdh.com/xml/2012/06/25/updatemanifest.xsd}'
        updateVer = data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "CheckForUpdateResponse").find('{http://tempuri.org/}' + "CheckForUpdateResult").find(packageXMLNS + "UpdateManifest").find(packageXMLNS + "Messages").find(packageXMLNS + "Message").text
        print(Fore.GREEN + "v" + re.sub(r"Philips HearSuite ", "", updateVer) + Style.RESET_ALL + " (" + targetMarket + ")", end="")

# GN: ReSound, Beltone, Interton
def reSoundChecker():
    updaterRetries = libhearingdownloader.updaterRetries
    while updaterRetries > 0:
        try:
            rawXmlData = requests.get("http://www.supportgn.com/resound/subsites/releasessdb.xml")
            data = xml.fromstring(rawXmlData.text)
            break
        except:
            pass

        updaterRetries -= 1
    if (updaterRetries == 0):
        print(Fore.RED + "Error" + Style.RESET_ALL)
    else:
        availableFiles = {}
        currentCategory = "Other"
        for child in data:
            if (child[0].tag == "SEPARATOR"):
                currentCategory = child[0].text
            else:
                availableFiles[currentCategory] = availableFiles.get(currentCategory, [])
                availableFiles[currentCategory].append( (child.find("BUTTONTEXTDOWN").text, '', child.find("LINK").text) )
        print(Fore.GREEN + "v" + re.sub(r"ReSound Smart Fit ", "", list(availableFiles.keys())[0]) + Style.RESET_ALL)

def beltoneChecker():
    updaterRetries = libhearingdownloader.updaterRetries
    while updaterRetries > 0:
        try:
            rawXmlData = requests.get("http://www.supportgn.com/beltone/subsites/releasessdb.xml")
            data = xml.fromstring(rawXmlData.text)
            break
        except:
            pass

        updaterRetries -= 1
    if (updaterRetries == 0):
        print(Fore.RED + "Error" + Style.RESET_ALL)
    else:
        availableFiles = {}
        currentCategory = "Other"
        for child in data:
            if (child[0].tag == "SEPARATOR"):
                currentCategory = child[0].text
            else:
                availableFiles[currentCategory] = availableFiles.get(currentCategory, [])
                availableFiles[currentCategory].append( (child.find("BUTTONTEXTDOWN").text, '', child.find("LINK").text) )
        print(Fore.GREEN + "v" + re.sub(r"Beltone Solus Max ", "", list(availableFiles.keys())[0]) + Style.RESET_ALL)

def intertonChecker():
    updaterRetries = libhearingdownloader.updaterRetries
    while updaterRetries > 0:
        try:
            rawXmlData = requests.get("http://www.supportgn.com/interton/subsites/releasessdb.xml")
            data = xml.fromstring(rawXmlData.text)
            break
        except:
            pass

        updaterRetries -= 1
    if (updaterRetries == 0):
        print(Fore.RED + "Error" + Style.RESET_ALL)
    else:
        availableFiles = {}
        currentCategory = "Other"
        for child in data:
            if (child[0].tag == "SEPARATOR"):
                currentCategory = child[0].text
            else:
                availableFiles[currentCategory] = availableFiles.get(currentCategory, [])
                availableFiles[currentCategory].append( (child.find("BUTTONTEXTDOWN").text, '', child.find("LINK").text) )
        print(Fore.GREEN + "v" + re.sub(r"Interton Fitting ", "", list(availableFiles.keys())[0]) + Style.RESET_ALL)

# WSA: Signia, Rexton, Audio Service, A&M, Widex
def signiaConnexxChecker(market):
    targetMarket = market
    headers = {
        "Content-Type": "application/soap+xml; charset=utf-8",
        "Connection": "Keep-Alive"
    }

    updaterRetries = libhearingdownloader.updaterRetries
    while updaterRetries > 0:
        try:
            baseVer = config.get('Signia', 'Version', fallback='9.11.15.782')
            supVer = config.get('Signia', 'SupportTools', fallback='9.12.3.281')
            upmVer = config.get('Signia', 'UpdateManager', fallback='19.12.3.281')
            rawXmlData = requests.post("https://upman-client.cloudapi.sivantos.com/Service/UpdateManagerService.svc", headers=headers, data='<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateManagerService/GetPackages</a:Action><a:MessageID>urn:uuid:00000000-0000-0000-0000-000000000000</a:MessageID><a:ReplyTo><a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address></a:ReplyTo><a:To s:mustUnderstand="1">https://upman-client.cloudapi.sivantos.com/Service/UpdateManagerService.svc</a:To></s:Header><s:Body><GetPackages xmlns="http://tempuri.org/"><products xmlns:b="http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"><b:ProductInfo><b:CurrentVersion>' + upmVer + '</b:CurrentVersion><b:ProductName>Update Manager</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>' + supVer + '</b:CurrentVersion><b:ProductName>Programmer</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>' + baseVer + '</b:CurrentVersion><b:ProductName>SigniaConnexx</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>' + supVer + '</b:CurrentVersion><b:ProductName>Support Tools</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>4.8.0.0</b:CurrentVersion><b:ProductName>DotNetFramework</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>6.0.5.00</b:CurrentVersion><b:ProductName>DotNetCoreRuntime</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>10.0.22.0</b:CurrentVersion><b:ProductName>OperatingSystem</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>14.32.31.00</b:CurrentVersion><b:ProductName>VC2015Redistributable</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo></products></GetPackages></s:Body></s:Envelope>')
            data = xml.fromstring(rawXmlData.text)
            break
        except:
            pass

        updaterRetries -= 1
    if (updaterRetries == 0):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    elif (rawXmlData.text == '<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateManagerService/GetPackagesResponse</a:Action><a:RelatesTo>urn:uuid:00000000-0000-0000-0000-000000000000</a:RelatesTo></s:Header><s:Body><GetPackagesResponse xmlns="http://tempuri.org/"><GetPackagesResult xmlns:b="http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"/></GetPackagesResponse></s:Body></s:Envelope>'):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    else:
        packageXMLNS = '{http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS}'
        availableFiles = []
        appVer = data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "GetPackagesResponse").find('{http://tempuri.org/}' + "GetPackagesResult").find(packageXMLNS + "Package").find(packageXMLNS + "NewVersion").text
        for child in data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "GetPackagesResponse").find('{http://tempuri.org/}' + "GetPackagesResult").find(packageXMLNS + "Package").find(packageXMLNS + "PackageFiles"):
            availableFiles.append( (appVer, child.find(packageXMLNS + "FileName").text, child.find(packageXMLNS + "DownloadURL").text) )
        print(Fore.GREEN + "v" + availableFiles[0][0] + Style.RESET_ALL + " (" + targetMarket + ")", end="")

def rextonConnexxChecker(market):
    targetMarket = market
    headers = {
        "Content-Type": "application/soap+xml; charset=utf-8",
        "Connection": "Keep-Alive"
    }

    updaterRetries = libhearingdownloader.updaterRetries
    while updaterRetries > 0:
        try:
            baseVer = config.get('Rexton', 'Version', fallback='9.11.15.793')
            supVer = config.get('Rexton', 'SupportTools', fallback='9.12.3.281')
            upmVer = config.get('Rexton', 'UpdateManager', fallback='19.12.3.281')
            rawXmlData = requests.post("https://upman-client.cloudapi.sivantos.com/Service/UpdateManagerService.svc", headers=headers, data='<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateManagerService/GetPackages</a:Action><a:MessageID>urn:uuid:00000000-0000-0000-0000-000000000000</a:MessageID><a:ReplyTo><a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address></a:ReplyTo><a:To s:mustUnderstand="1">https://upman-client.cloudapi.sivantos.com/Service/UpdateManagerService.svc</a:To></s:Header><s:Body><GetPackages xmlns="http://tempuri.org/"><products xmlns:b="http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"><b:ProductInfo><b:CurrentVersion>' + upmVer + '</b:CurrentVersion><b:ProductName>Update Manager</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>' + supVer + '</b:CurrentVersion><b:ProductName>Programmer</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>' + baseVer + '</b:CurrentVersion><b:ProductName>RextonConnexx</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>' + supVer + '</b:CurrentVersion><b:ProductName>Support Tools</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>4.8.0.0</b:CurrentVersion><b:ProductName>DotNetFramework</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>6.0.5.00</b:CurrentVersion><b:ProductName>DotNetCoreRuntime</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>10.0.22.0</b:CurrentVersion><b:ProductName>OperatingSystem</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>14.32.31.00</b:CurrentVersion><b:ProductName>VC2015Redistributable</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo></products></GetPackages></s:Body></s:Envelope>')
            data = xml.fromstring(rawXmlData.text)
            break
        except:
            pass

        updaterRetries -= 1
    if (updaterRetries == 0):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    elif (rawXmlData.text == '<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateManagerService/GetPackagesResponse</a:Action><a:RelatesTo>urn:uuid:00000000-0000-0000-0000-000000000000</a:RelatesTo></s:Header><s:Body><GetPackagesResponse xmlns="http://tempuri.org/"><GetPackagesResult xmlns:b="http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"/></GetPackagesResponse></s:Body></s:Envelope>'):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    else:
        packageXMLNS = '{http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS}'
        availableFiles = []
        appVer = data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "GetPackagesResponse").find('{http://tempuri.org/}' + "GetPackagesResult").find(packageXMLNS + "Package").find(packageXMLNS + "NewVersion").text
        for child in data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "GetPackagesResponse").find('{http://tempuri.org/}' + "GetPackagesResult").find(packageXMLNS + "Package").find(packageXMLNS + "PackageFiles"):
            availableFiles.append( (appVer, child.find(packageXMLNS + "FileName").text, child.find(packageXMLNS + "DownloadURL").text) )
        print(Fore.GREEN + "v" + availableFiles[0][0] + Style.RESET_ALL + " (" + targetMarket + ")", end="")

def audioServiceConnexxChecker(market):
    targetMarket = market
    headers = {
        "Content-Type": "application/soap+xml; charset=utf-8",
        "Connection": "Keep-Alive"
    }

    updaterRetries = libhearingdownloader.updaterRetries
    while updaterRetries > 0:
        try:
            baseVer = config.get('AudioService', 'Version', fallback='9.12.0.1516')
            supVer = config.get('AudioService', 'SupportTools', fallback='9.12.3.281')
            upmVer = config.get('AudioService', 'UpdateManager', fallback='19.12.3.281')
            rawXmlData = requests.post("https://upman-client.cloudapi.sivantos.com/Service/UpdateManagerService.svc", headers=headers, data='<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateManagerService/GetPackages</a:Action><a:MessageID>urn:uuid:00000000-0000-0000-0000-000000000000</a:MessageID><a:ReplyTo><a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address></a:ReplyTo><a:To s:mustUnderstand="1">https://upman-client.cloudapi.sivantos.com/Service/UpdateManagerService.svc</a:To></s:Header><s:Body><GetPackages xmlns="http://tempuri.org/"><products xmlns:b="http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"><b:ProductInfo><b:CurrentVersion>' + upmVer + '</b:CurrentVersion><b:ProductName>Update Manager</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>' + supVer + '</b:CurrentVersion><b:ProductName>Programmer</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>' + baseVer + '</b:CurrentVersion><b:ProductName>AudioServiceConnexx</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>' + supVer + '</b:CurrentVersion><b:ProductName>Support Tools</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>4.8.0.0</b:CurrentVersion><b:ProductName>DotNetFramework</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>6.0.5.00</b:CurrentVersion><b:ProductName>DotNetCoreRuntime</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>10.0.22.0</b:CurrentVersion><b:ProductName>OperatingSystem</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>14.32.31.00</b:CurrentVersion><b:ProductName>VC2015Redistributable</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo></products></GetPackages></s:Body></s:Envelope>')
            data = xml.fromstring(rawXmlData.text)
            break
        except:
            pass

        updaterRetries -= 1
    if (updaterRetries == 0):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    elif (rawXmlData.text == '<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateManagerService/GetPackagesResponse</a:Action><a:RelatesTo>urn:uuid:00000000-0000-0000-0000-000000000000</a:RelatesTo></s:Header><s:Body><GetPackagesResponse xmlns="http://tempuri.org/"><GetPackagesResult xmlns:b="http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"/></GetPackagesResponse></s:Body></s:Envelope>'):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    else:
        packageXMLNS = '{http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS}'
        availableFiles = []
        appVer = data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "GetPackagesResponse").find('{http://tempuri.org/}' + "GetPackagesResult").find(packageXMLNS + "Package").find(packageXMLNS + "NewVersion").text
        for child in data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "GetPackagesResponse").find('{http://tempuri.org/}' + "GetPackagesResult").find(packageXMLNS + "Package").find(packageXMLNS + "PackageFiles"):
            availableFiles.append( (appVer, child.find(packageXMLNS + "FileName").text, child.find(packageXMLNS + "DownloadURL").text) )
        print(Fore.GREEN + "v" + availableFiles[0][0] + Style.RESET_ALL + " (" + targetMarket + ")", end="")

def aMConnexxChecker(market):
    targetMarket = market
    headers = {
        "Content-Type": "application/soap+xml; charset=utf-8",
        "Connection": "Keep-Alive"
    }

    updaterRetries = libhearingdownloader.updaterRetries
    while updaterRetries > 0:
        try:
            baseVer = config.get('AM', 'Version', fallback='9.9.1.989')
            supVer = config.get('AM', 'SupportTools', fallback='9.12.3.281')
            upmVer = config.get('AM', 'UpdateManager', fallback='19.12.3.281')
            rawXmlData = requests.post("https://upman-client.cloudapi.sivantos.com/Service/UpdateManagerService.svc", headers=headers, data='<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateManagerService/GetPackages</a:Action><a:MessageID>urn:uuid:00000000-0000-0000-0000-000000000000</a:MessageID><a:ReplyTo><a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address></a:ReplyTo><a:To s:mustUnderstand="1">https://upman-client.cloudapi.sivantos.com/Service/UpdateManagerService.svc</a:To></s:Header><s:Body><GetPackages xmlns="http://tempuri.org/"><products xmlns:b="http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"><b:ProductInfo><b:CurrentVersion>' + supVer + '</b:CurrentVersion><b:ProductName>Programmer</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>' + upmVer + '</b:CurrentVersion><b:ProductName>Update Manager</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>' + supVer + '</b:CurrentVersion><b:ProductName>Support Tools</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>' + baseVer + '</b:CurrentVersion><b:ProductName>AMConnexx</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>4.8.0.0</b:CurrentVersion><b:ProductName>DotNetFramework</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion/><b:ProductName>DotNetCoreRuntime</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>10.0.22.0</b:CurrentVersion><b:ProductName>OperatingSystem</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo><b:ProductInfo><b:CurrentVersion>14.32.31.00</b:CurrentVersion><b:ProductName>VC2015Redistributable</b:ProductName><b:PublisherName>SAT</b:PublisherName><b:Countries xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><c:string>' + targetMarket + '</c:string></b:Countries><b:FieldTestCode/><b:CustomerID>00000000-0000-0000-0000-000000000000</b:CustomerID></b:ProductInfo></products></GetPackages></s:Body></s:Envelope>')
            data = xml.fromstring(rawXmlData.text)
            break
        except:
            pass

        updaterRetries -= 1
    if (updaterRetries == 0):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    elif (rawXmlData.text == '<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateManagerService/GetPackagesResponse</a:Action><a:RelatesTo>urn:uuid:00000000-0000-0000-0000-000000000000</a:RelatesTo></s:Header><s:Body><GetPackagesResponse xmlns="http://tempuri.org/"><GetPackagesResult xmlns:b="http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"/></GetPackagesResponse></s:Body></s:Envelope>'):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    else:
        packageXMLNS = '{http://schemas.datacontract.org/2004/07/SHS.SAT.UpdateManager.BackEnd.UWS}'
        availableFiles = []
        appVer = data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "GetPackagesResponse").find('{http://tempuri.org/}' + "GetPackagesResult").find(packageXMLNS + "Package").find(packageXMLNS + "NewVersion").text
        for child in data.find('{http://www.w3.org/2003/05/soap-envelope}' + "Body").find('{http://tempuri.org/}' + "GetPackagesResponse").find('{http://tempuri.org/}' + "GetPackagesResult").find(packageXMLNS + "Package").find(packageXMLNS + "PackageFiles"):
            availableFiles.append( (appVer, child.find(packageXMLNS + "FileName").text, child.find(packageXMLNS + "DownloadURL").text) )
        print(Fore.GREEN + "v" + availableFiles[0][0] + Style.RESET_ALL + " (" + targetMarket + ")", end="")

def widexCompassGPSChecker(market):
    targetMarket = market
    baseId = config.get('Widex', 'ID', fallback='CompassGPS')
    baseVer = config.get('Widex', 'Version', fallback='4.8.6193.0')
    apiKey = config.get('Widex', 'Key', fallback='24fbe5gacg`hcdf535dd34ed6_237347')
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
            postUrl = 'https://apimgmt.widex.com/fds/v1/api/Update?all=true&brevity=terse'
            rawPostData = '{"Id":"'+baseId+'","Version":"'+baseVer+'","Environment":[{"Name":"distributors","Value":"' + targetMarket + '"}]}'
            rawJsonData = requests.post(postUrl, headers=headers, data = rawPostData)
            data = json.loads(rawJsonData.text)
            break
        except:
            pass

        updaterRetries -= 1
    if (updaterRetries == 0):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    elif "statusCode" in data:
        print(data['message'] + " (" + targetMarket + ")", end="")
    elif "Packages" in data:
        if (data['Packages']==[]):
            print(Fore.GREEN + "v" + baseVer + Style.RESET_ALL + " (" + targetMarket + ")", end="")
        else:
            latestBaseVersion = data['Packages'][0]['Version']
            latestRevision = str(data['Packages'][0]['Revision'])
            print(Fore.GREEN + "v" + latestBaseVersion + " Rev." + latestRevision + Style.RESET_ALL + " (" + targetMarket + ")", end="")
    else:
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + targetMarket + ")", end="")

# Starkey
def getIP():
    ipEndpoint = 'https://ipinfo.io/json'
    ipResponse = requests.get(ipEndpoint, verify = True)
    if ipResponse.status_code != 200:
        exit()
    ipData = ipResponse.json()
    return ipData['ip']

def getCN(ip):
    cnEndpoint = f'https://ipinfo.io/{ip}/json'
    cnResponse = requests.get(cnEndpoint, verify = True)
    if cnResponse.status_code != 200:
        exit()
    cnData = cnResponse.json()
    return cnData['country']

def starkeyProFitChecker():
    currentIP = ""
    currentCountry = ""
    currentIP = getIP()
    if(currentIP == ""):
        currentCountry = config.get('Starkey', 'Market', fallback='US')
    else:
        currentCountry = getCN(currentIP)

    if(currentCountry == ""):
        currentCountry = config.get('Starkey', 'Market', fallback='US')
    else:
        pass

    currentCountry_name = countries.get(currentCountry)
    defaultGeoIP = currentCountry_name.apolitical_name
    geoIP = defaultGeoIP

    currentTime = datetime.datetime.now(tz=tzlocal.get_localzone()).strftime('%m/%d/%Y %H:%M:%S')
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    updaterRetries = libhearingdownloader.updaterRetries
    while updaterRetries > 0:
        try:
            postUrl = 'https://inspireupdater.com/api/Update'
            baseVer = config.get('Starkey', 'ProFit', fallback='2.0.10074.0')
            rawPostData = '{"ClientID":"00000000-0000-0000-0000-000000000000","ClientID2":"00000000-0000-0000-0000-000000000000+0000000000000000000","Application":"ProFit","ApplicationProperties":[{"Name":"Version","TypeName":"System.String","Value":"' + baseVer + '"},{"Name":"manufacturer","TypeName":"System.String","Value":"Starkey"},{"Name":"targetAudience","TypeName":"System.String","Value":"Starkey International English"},{"Name":"locale","TypeName":"System.String","Value":"en"},{"Name":"Country","TypeName":"System.String","Value":"' + geoIP + '"},{"Name":"MachineName","TypeName":"System.String","Value":"0000"},{"Name":"Time","TypeName":"System.DateTime","Value":"' + currentTime + '"}],"TestMode":false}'
            rawJsonData = requests.post(postUrl, headers=headers, data = rawPostData, verify='inspireupdater-com-chain.pem')
            data = json.loads(rawJsonData.text)
            break
        except:
            pass

        updaterRetries -= 1
    if (updaterRetries == 0):
        print(Fore.RED + "Error" + Style.RESET_ALL + " (" + geoIP + ")", end="")
    else:
        if (data['Update'] is None):
            print(Fore.GREEN + "v" + baseVer + Style.RESET_ALL + " (" + geoIP + ")", end="")

        updateVer = data['Update']['Title'] + ' (' + data['Update']['Version'] + ')'
        print(Fore.GREEN + "v" + re.sub(r"\)", "", re.sub(r".+\(", "", updateVer)) + Style.RESET_ALL + " (" + geoIP + ")", end="")

# Give instruction and skip the rest script if all skipped
if scanSkipAll:
    print("\n" + Fore.YELLOW + "Notice" + Style.RESET_ALL + ": All scans are " + Fore.RED + "skipped" + Style.RESET_ALL + ".\n")
    print("Please edit " + Fore.GREEN + "config.ini" + Style.RESET_ALL + " file with any plain-text editor")
    print("to enable Quick Scan by setting " + Fore.BLUE + "QuickScan" + Style.RESET_ALL + " to " + Fore.GREEN + "True" + Style.RESET_ALL + " for")
    print("each hearing aid brand as you like.")
    exit(1)

# check last time performing Quick Scan
timestampPath = Path("Quick Scan.timestamp")
if timestampPath.is_file():
    with timestampPath.open("r+") as timestampFile:
        timestampLast = datetime.datetime.strptime(timestampFile.read(), "%Y-%m-%d %H:%M:%S")
        timestampCurrent = datetime.datetime.strptime(datetime.datetime.now(tz=tzlocal.get_localzone()).strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        timestampDiff = timestampCurrent - timestampLast
        if (timestampDiff < datetime.timedelta(hours=1)):
            print("\n" + Fore.RED + "WARNING" + Style.RESET_ALL + ": You have done Quick Scan within an hour (" + Fore.YELLOW + str(timestampDiff) + Style.RESET_ALL + " to be precise).")
            print("You should cool down a while to prevent being blocked from API servers.\n")
            inputCont = ""
            inputCont = input("Do you want to perform Quick Scan anyway? [" + Style.BRIGHT + Fore.BLACK + "(" + Style.RESET_ALL + Fore.GREEN + "No" + Style.BRIGHT + Fore.BLACK + ")" + Style.RESET_ALL + "/yes]: ")
            if (inputCont.lower() == "yes" or inputCont.lower() == "y"):
                timestampFile.seek(0)
                timestampFile.write(datetime.datetime.now(tz=tzlocal.get_localzone()).strftime('%Y-%m-%d %H:%M:%S'))
                timestampFile.truncate()
            else:
                exit(1)
        else:
            timestampFile.seek(0)
            timestampFile.write(datetime.datetime.now(tz=tzlocal.get_localzone()).strftime('%Y-%m-%d %H:%M:%S'))
            timestampFile.truncate()
else:
    with timestampPath.open("w") as timestampFile:
        timestampFile.write(datetime.datetime.now(tz=tzlocal.get_localzone()).strftime('%Y-%m-%d %H:%M:%S'))

print("")

print("Phonak Target: ", end="")
if (scanPhonak):
    marketList = config.get('Phonak', 'MarketScan', fallback='GB,US,CA,ES,FR,TW').split(',')
    marketListCount = len(marketList)
    marketListItem = 0
    while marketListItem < marketListCount:
        try:
            phonakTargetChecker(marketList[marketListItem])
            if (marketListItem + 1 == marketListCount):
                print(".")
            else:
                print(", ", end="")
        except:
            pass

        marketListItem += 1
else:
    print(Style.DIM + "skipped." + Style.RESET_ALL)

print("Unitron TrueFit: ", end="")
if (scanUnitron):
    marketList = config.get('Unitron', 'MarketScan', fallback='GB,US,CA,ES,FR,TW').split(',')
    marketListCount = len(marketList)
    marketListItem = 0
    while marketListItem < marketListCount:
        try:
            unitronTrueFitChecker(marketList[marketListItem])
            if (marketListItem + 1 == marketListCount):
                print(".")
            else:
                print(", ", end="")
        except:
            pass

        marketListItem += 1
else:
    print(Style.DIM + "skipped." + Style.RESET_ALL)

print("Hansaton scout: ", end="")
if (scanHansaton):
    marketList = config.get('Hansaton', 'MarketScan', fallback='GB,US,CA,ES,FR,DE,TW').split(',')
    marketListCount = len(marketList)
    marketListItem = 0
    while marketListItem < marketListCount:
        try:
            hansatonScoutChecker(marketList[marketListItem])
            if (marketListItem + 1 == marketListCount):
                print(".")
            else:
                print(", ", end="")
        except:
            pass

        marketListItem += 1
else:
    print(Style.DIM + "skipped." + Style.RESET_ALL)

print("Oticon Genie 2: ", end="")
if (scanOticon):
    marketList = config.get('Oticon', 'MarketScan', fallback='GB,US,CA,ES,FR,TW').split(',')
    marketListCount = len(marketList)
    marketListItem = 0
    while marketListItem < marketListCount:
        try:
            oticonGenie2Checker(marketList[marketListItem])
            if (marketListItem + 1 == marketListCount):
                print(".")
            else:
                print(", ", end="")
        except:
            pass

        marketListItem += 1
else:
    print(Style.DIM + "skipped." + Style.RESET_ALL)

print("Bernafon OasisNXT: ", end="")
if (scanBernafon):
    marketList = config.get('Bernafon', 'MarketScan', fallback='Default,GB,US,CA,ES,FR,TW').split(',')
    marketListCount = len(marketList)
    marketListItem = 0
    while marketListItem < marketListCount:
        try:
            bernafonOasisNXTChecker(marketList[marketListItem])
            if (marketListItem + 1 == marketListCount):
                print(".")
            else:
                print(", ", end="")
        except:
            pass

        marketListItem += 1
else:
    print(Style.DIM + "skipped." + Style.RESET_ALL)

print("Sonic EXPRESSfit Pro: ", end="")
if (scanSonic):
    marketList = config.get('Sonic', 'MarketScan', fallback='Default,GB,US,CA,ES,FR,TW').split(',')
    marketListCount = len(marketList)
    marketListItem = 0
    while marketListItem < marketListCount:
        try:
            sonicExpressFitChecker(marketList[marketListItem])
            if (marketListItem + 1 == marketListCount):
                print(".")
            else:
                print(", ", end="")
        except:
            pass

        marketListItem += 1
else:
    print(Style.DIM + "skipped." + Style.RESET_ALL)

print("Philips HearSuite: ", end="")
if (scanPhilips):
    marketList = config.get('Philips', 'MarketScan', fallback='Default,GB,US,CA,ES,FR,TW').split(',')
    marketListCount = len(marketList)
    marketListItem = 0
    while marketListItem < marketListCount:
        try:
            philipsHearSuiteChecker(marketList[marketListItem])
            if (marketListItem + 1 == marketListCount):
                print(".")
            else:
                print(", ", end="")
        except:
            pass

        marketListItem += 1
else:
    print(Style.DIM + "skipped." + Style.RESET_ALL)

print("ReSound Smart Fit: ", end="")
if (scanReSound):
    reSoundChecker()
else:
    print(Style.DIM + "skipped." + Style.RESET_ALL)

print("Beltone Solus Max: ", end="")
if (scanBeltone):
    beltoneChecker()
else:
    print(Style.DIM + "skipped." + Style.RESET_ALL)

print("Interton Fitting: ", end="")
if (scanInterton):
    intertonChecker()
else:
    print(Style.DIM + "skipped." + Style.RESET_ALL)

print("Signia Connexx: ", end="")
if (scanSignia):
    marketList = config.get('Signia', 'MarketScan', fallback='GB,US,CA,ES,FR,TW').split(',')
    marketListCount = len(marketList)
    marketListItem = 0
    while marketListItem < marketListCount:
        try:
            signiaConnexxChecker(marketList[marketListItem])
            if (marketListItem + 1 == marketListCount):
                print(".")
            else:
                print(", ", end="")
        except:
            pass

        marketListItem += 1
else:
    print(Style.DIM + "skipped." + Style.RESET_ALL)

print("Rexton Connexx: ", end="")
if (scanRexton):
    marketList = config.get('Rexton', 'MarketScan', fallback='GB,US,ES,FR,TW').split(',')
    marketListCount = len(marketList)
    marketListItem = 0
    while marketListItem < marketListCount:
        try:
            rextonConnexxChecker(marketList[marketListItem])
            if (marketListItem + 1 == marketListCount):
                print(".")
            else:
                print(", ", end="")
        except:
            pass

        marketListItem += 1
else:
    print(Style.DIM + "skipped." + Style.RESET_ALL)

print("Audio Service Connexx: ", end="")
if (scanAudioService):
    marketList = config.get('AudioService', 'MarketScan', fallback='GB,ES,FR,TW').split(',')
    marketListCount = len(marketList)
    marketListItem = 0
    while marketListItem < marketListCount:
        try:
            audioServiceConnexxChecker(marketList[marketListItem])
            if (marketListItem + 1 == marketListCount):
                print(".")
            else:
                print(", ", end="")
        except:
            pass

        marketListItem += 1
else:
    print(Style.DIM + "skipped." + Style.RESET_ALL)

print("A&M Connexx: ", end="")
if (scanAM):
    marketList = config.get('AM', 'MarketScan', fallback='TW').split(',')
    marketListCount = len(marketList)
    marketListItem = 0
    while marketListItem < marketListCount:
        try:
            aMConnexxChecker(marketList[marketListItem])
            if (marketListItem + 1 == marketListCount):
                print(".")
            else:
                print(", ", end="")
        except:
            pass

        marketListItem += 1
else:
    print(Style.DIM + "skipped." + Style.RESET_ALL)

print("Widex Compass GPS: ", end="")
if (scanWidex):
    marketList = config.get('Widex', 'MarketScan', fallback='Main_Test_Distributor,Alternate_Test_Distributor,USA,United Kingdom').split(',')
    marketListCount = len(marketList)
    marketListItem = 0
    while marketListItem < marketListCount:
        try:
            widexCompassGPSChecker(marketList[marketListItem])
            if (marketListItem + 1 == marketListCount):
                print(".")
            else:
                print(", ", end="")
        except:
            pass

        marketListItem += 1
else:
    print(Style.DIM + "skipped." + Style.RESET_ALL)

print("Starkey Pro Fit: ", end="")
if (scanStarkey):
    starkeyProFitChecker()
    print(".")
else:
    print(Style.DIM + "skipped." + Style.RESET_ALL)
