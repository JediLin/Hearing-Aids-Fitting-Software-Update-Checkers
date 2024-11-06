#############################################################
#                                                           #
#                   Copyright Bluebotlabz                   #
#                                                           #
#############################################################
import os
import datetime
import html
import ast
import json
import requests
import libhearingdownloader


print("==================================================")
print("=       Starkey Inspire OS Update Checker        =")
print("="*(47-len(libhearingdownloader.downloaderVersion)) + " " + libhearingdownloader.downloaderVersion + " =")

libhearingdownloader.printWaranty()
disclaimer = [
    "DISCLAIMER",
    "",
    "I (Bluebotlabz), do not take any responsability for what you do using this software",
    "Starkey is a trademark of Starkey Laboratories, Inc.",
    "Inspire OS is created by Starkey Laboratories, Inc.",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "",
    "Bluebotlabz and this downloader are not affiliated with or endorsed by Starkey Laboratories, Inc.",
    "Depending on how this software is used, it may violate the EULA and/or Terms and Conditions of the downloaded software",
    "This is an UNOFFICIAL downloader and use of the software downloaded using it may be limited"
]

# Display disclaimer
libhearingdownloader.printDisclaimer(disclaimer)

# Starkey updater API will check system time...
currentTime = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%m/%d/%Y %H:%M:%S')
headers = {
    "Content-Type": "application/json; charset=utf-8"
}

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        # Please change geoIP country/region to match your IP address. The update server may check it.
        geoIP = 'Taiwan'
        # Download version data, pretending installed Inspire OS v27.0.10074.0
        postUrl = 'https://inspireupdater.com/api/Update'
        rawPostData = '{"ClientID":"00000000-0000-0000-0000-000000000000","ClientID2":"00000000-0000-0000-0000-000000000000+0000000000000000000","Application":"Inspire OS","ApplicationProperties":[{"Name":"Version","TypeName":"System.Version","Value":"27.0.10074.0"},{"Name":"manufacturer","TypeName":"System.String","Value":"Starkey"},{"Name":"targetAudience","TypeName":"System.String","Value":"Starkey International English"},{"Name":"locale","TypeName":"System.String","Value":"en"},{"Name":"BillToAccountNumber","TypeName":"System.String","Value":"unknown"},{"Name":"ShipToAccountNumber","TypeName":"System.String","Value":"unknown"},{"Name":"Country","TypeName":"System.String","Value":"' + geoIP + '"},{"Name":"Country","TypeName":"System.String","Value":"' + geoIP + '"},{"Name":"MachineName","TypeName":"System.String","Value":"0000"},{"Name":"OSVersion","TypeName":"System.String","Value":"Microsoft Windows NT 6.1.7601 Service Pack 1"},{"Name":"OSBitWidth","TypeName":"System.Byte","Value":"64"},{"Name":"Time","TypeName":"System.DateTime","Value":"' + currentTime + '"}],"TestMode":false}'
        rawJsonData = requests.post(postUrl, headers=headers, data = rawPostData, verify='inspireupdater-com-chain.pem')
        data = json.loads(rawJsonData.text)
        break
    except:
        pass

    updaterRetries -= 1
if (updaterRetries == 0):
    print("Error: Update server could not be reached")
    exit(1)

if (libhearingdownloader.verboseDebug):
    print(rawPostData)
    print(rawJsonData.text)

appVer = data['Update']['Title'] + ' (' + data['Update']['Version'] + ')'
print ("Version info:")
print(appVer)
print(data['Update']['Description'])
filesList = json.dumps(ast.literal_eval(str(data['Update']['Files'][0])))
fileData = json.loads(filesList)

availableFiles = [] # List of available files
availableFiles.append( (os.path.basename(fileData['Url']), fileData['Url']) )

if (libhearingdownloader.verboseDebug):
    print(availableFiles)

# Select outputDir and targetFile
outputDir = libhearingdownloader.selectOutputFolder()
targetFile = availableFiles[libhearingdownloader.selectFromList(availableFiles)]

# Create download folder
downloadVer = 'Starkey InspireOS ' + data['Update']['Version']
outputDir += '.'.join(downloadVer.split('.')) + "/"
print("\n\n")

# Download file
libhearingdownloader.downloadFile(targetFile[1], outputDir + targetFile[0], "Downloading " + targetFile[0])

print("\n\nDownload Complete!")
