import os
import requests
import libhearingdownloader

selfUpdateOption = "Self Update Checker"
updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        checkerRelease = requests.get("https://api.github.com/repos/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/releases/latest")
        if not (checkerRelease.json()['tag_name'] == libhearingdownloader.downloaderVersion):
            selfUpdateOption += "  >> " + checkerRelease.json()['tag_name'] + " AVAILABLE <<"
            print("\n\n\nNEW VERSION AVAILABLE!!\n\nThe latest version of The Checker is " + checkerRelease.json()['tag_name'] + " (you are using "+ libhearingdownloader.downloaderVersion + ").\nPlease use 1) Self Update Checker option to download it.")
        break
    except:
        pass

    updaterRetries -= 1


downloaders = [
    ("EXIT", "", "exit.py"),
    (selfUpdateOption + "\n    -------------------", "", "GitHub Checker.py"),
    ("Phonak Target Update Checker", "", "Phonak Target Checker.py"),
    ("Unitron TrueFit Update Checker", "", "Unitron TrueFit Checker.py"),
    ("Hansaton scout Update Checker", "", "HANSATON scout Checker.py"),
    ("Oticon Genie 2 Update Checker", "", "Oticon Genie 2 2024 Checker.py"),
    ("Bernafon OasisNXT Update Checker", "", "Bernafon OasisNXT 2024 Checker.py"),
    ("Sonic ExpressFit Update Checker", "", "Sonici ExpressFit 2024 Checker.py"),
    ("Philips HearSuite Update Checker", "", "Philips HearSuite 2024 Checker.py"),
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
    ("...Extra & Legacy Software Update Checkers", "", "Extra Menu.py"),
]

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
libhearingdownloader.printDisclaimer(disclaimer)

print("\n")
print("==================================================")
print("= Hearing Aids Fitting Software Update Checkers  =")
print("==================================== " + libhearingdownloader.downloaderVersion + " =")
if (os.name != "nt"):
    print("NOTE: You are running The Checker on an Unix (*NIX) or mac Operating System. Hearing aids software requires Windows OS to run, but can still be checked on Unix (*NIX) or mac OS")
print("")

selectedDownloader = libhearingdownloader.selectFromList(downloaders, "checker", numberSeperator=')', confirmationCheck=False)

os.system('python ./"' + downloaders[selectedDownloader][2] + '"')
