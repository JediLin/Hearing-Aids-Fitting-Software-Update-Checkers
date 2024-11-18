import os
import requests
import libhearingdownloader

updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        checkerRelease = requests.get("https://api.github.com/repos/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/releases/latest")
        if not (checkerRelease.json()['tag_name'] == libhearingdownloader.downloaderVersion):
            print("\n\n\nNEW VERSION AVAILABLE!!\n\nThe latest version of this script is " + checkerRelease.json()['tag_name'] + " (you are using "+ libhearingdownloader.downloaderVersion + ").\nPlease use 1) Self Update Checker option to download it.")
        break
    except:
        pass

    updaterRetries -= 1


downloaders = [
    ("EXIT", "", "exit.py"),
    ("Self (THIS script) Update Checker", "", "GitHub Checker.py"),
    ("Phonak Target Update Checker", "", "Phonak Target Checker.py"),
    ("Unitron TrueFit Update Checker", "", "Unitron TrueFit Checker.py"),
    ("Hansaton scout Update Checker", "", "HANSATON scout Checker.py"),
    ("Oticon Genie 2 v2024+ Update Checker", "", "Oticon Genie 2 2024 Checker.py"),
    ("Bernafon OasisNXT v2024+ Update Checker", "", "Bernafon OasisNXT 2024 Checker.py"),
    ("Sonic ExpressFit v2024+ Update Checker", "", "Sonici ExpressFit 2024 Checker.py"),
    ("Philips HearSuite v2024+ Update Checker", "", "Philips HearSuite 2024 Checker.py"),
    ("GN ReSound Update Checker", "", "GN ReSound Checker.py"),
    ("GN Beltone Update Checker", "", "GN Beltone Checker.py"),
    ("GN Interton Update Checker", "", "GN Interton Checker.py"),
    ("Signia Connexx Update Checker", "", "Signia Connexx Checker.py"),
    ("Rexton Connexx Update Checker", "", "Rexton Connexx Checker.py"),
    ("Audio Service Connexx Update Checker", "", "Audio Service Connexx Checker.py"),
    ("A&M Connexx Update Checker", "", "AM Connexx Checker.py"),
    ("Widex Compass GPS Update Checker", "", "Widex Compass GPS Checker.py"),
    ("Starkey Pro Fit Update Checker", "", "Starkey Pro Fit Checker.py"),
    ("Starkey Inspire OS Update Checker", "", "Starkey Inspire Checker.py"),
    ("...Extra and Legacy Softwares Update Checker", "", "Extra Menu.py"),
]

disclaimer = [
    "DISCLAIMER",
    "",
    "I (Bluebotlabz), do not take any responsability for what you do using this software",
    "All rights and credit go to their rightful owners. No copyright infringement intended.",
    "Bluebotlabz and this downloader are not affiliated with or endorsed by any of the companies mentioned in this repository",
    "Depending on how this software is used, it may violate the EULA and/or Terms and Conditions of the downloaded software",
    "This is an UNOFFICIAL downloader and use of the software downloaded using it may be limited"
]
libhearingdownloader.printDisclaimer(disclaimer)

print("\n")
print("==================================================")
print("= Hearing Aids Fitting Software Update Checkers  =")
print("==================================== " + libhearingdownloader.downloaderVersion + " =")
if (os.name != "nt"):
    print("NOTE: You are running this on a Unix (Or *NIX) Operating System, downloaded software is only available for Windows, but can still be downloaded via a Unix (Or *NIX) OS")
print("")

selectedDownloader = libhearingdownloader.selectFromList(downloaders, "checker", numberSeperator=')', confirmationCheck=False)

os.system('python ./"' + downloaders[selectedDownloader][2] + '"')
