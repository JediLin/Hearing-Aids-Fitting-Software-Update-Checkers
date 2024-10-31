#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import html
import requests
import libhearingdownloader
import xml.etree.ElementTree as xml


print("==================================================")
print("=   Philips HearSuite (v2024+) Update Checker    =")
print("="*(47-len(libhearingdownloader.downloaderVersion)) + " " + libhearingdownloader.downloaderVersion + " =")

libhearingdownloader.printWaranty()
disclaimer = [
    "DISCLAIMER",
    "",
    "I (Bluebotlabz), do not take any responsability for what you do using this software",
    "Philips is a trademark of Koninklijke Philips N.V.",
    "Philips HearSuite is created by Philips",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "Bluebotlabz and this downloader are not affiliated with or endorsed by Philips",
    "Depending on how this software is used, it may violate the EULA and/or Terms and Conditions of the downloaded software",
    "This is an UNOFFICIAL downloader and use of the software downloaded using it may be limited"
]

# Display disclaimer
libhearingdownloader.printDisclaimer(disclaimer)

print ("Downloading version index")
headers = {
#    "Host": "updater.bernafon.com",
    "Content-Type": "application/soap+xml; charset=utf-8"
}

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        # Download version data
        rawXmlData = requests.post("https://updater.sbohearing.com/UpdateWebService.svc", headers=headers, data='<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/IUpdateWebService/CheckForUpdate</a:Action><a:MessageID>urn:uuid:00000000-0000-0000-0000-000000000000</a:MessageID><a:ReplyTo><a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address></a:ReplyTo><a:To s:mustUnderstand="1">https://updater.sbohearing.com/UpdateWebService.svc</a:To></s:Header><s:Body><CheckForUpdate xmlns="http://tempuri.org/"><request xmlns:b="http://schemas.datacontract.org/2004/07/Wdh.Genesis.SoftwareUpdater.Common" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"><b:ClientId>00000000-0000-0000-0000-000000000000</b:ClientId><b:Customer>Philips</b:Customer><b:Languages xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/><b:Locale i:nil="true"/><b:Manufacturer>Philips HearSuite</b:Manufacturer><b:Market>Default</b:Market><b:OEM i:nil="true"/><b:OS>Microsoft Windows NT 10.0.22621.0</b:OS><b:RequestVersion>2</b:RequestVersion><b:Software><b:InstalledSoftware><b:Build>95</b:Build><b:Major>20</b:Major><b:Minor>22</b:Minor><b:Name>HearSuite2</b:Name><b:Revision>0</b:Revision></b:InstalledSoftware><b:InstalledSoftware><b:Build>3</b:Build><b:Major>26</b:Major><b:Minor>9</b:Minor><b:Name>PhilipsHearSuiteUpdater</b:Name><b:Revision>0</b:Revision></b:InstalledSoftware></b:Software></request></CheckForUpdate></s:Body></s:Envelope>')
        data = xml.fromstring(html.unescape(rawXmlData.text))
        break
    except Exception as e:
        print(e)
        pass

    updaterRetries -= 1
if (updaterRetries == 0):
    print("Error: Update server could not be reached")
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