import libhearingdownloader
import os


downloaders = [
    ("EXIT", "", "exit.py"),
    ("Phonak Target Update Checker", "", "Phonak Target Checker.py"),
    ("Phonak Target Media Update Checker", "", "Phonak Target Media Checker.py"),
    ("Phonak Target Sounds Update Checker", "", "Phonak Target Sounds Checker.py"),
    ("Unitron TrueFit Update Checker", "", "Unitron TrueFit Checker.py"),
    ("Hansaton scout Update Checker", "", "HANSATON scout Checker.py"),
    ("Oticon Genie 2 v2024+ Update Checker", "", "Oticon Genie 2 2024 Checker.py"),
#    ("Oticon Genie 2 Update Checker", "", "Oticon Genie 2 Checker.py"),
#    ("Oticon Genie Update Checker", "", "Oticon Genie Checker.py"),
    ("Bernafon OasisNXT v2024+ Update Checker", "", "Bernafon OasisNXT 2024 Checker.py"),
#    ("Bernafon OasisNXT Update Checker", "", "Bernafon OasisNXT Checker.py"),
    ("Sonic ExpressFit v2024+ Update Checker", "", "Sonici ExpressFit 2024 Checker.py"),
#    ("Sonic ExpressFit Update Checker", "", "Sonici ExpressFit Checker.py"),
    ("Philips HearSuite v2024+ Update Checker", "", "Philips HearSuite 2024 Checker.py"),
#    ("Philips HearSuite Update Checker", "", "Philips HearSuite Checker.py"),
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

print("==================================================")
print("= Hearing Aids Fitting Software Update Checkers  =")
print("==================================== " + libhearingdownloader.downloaderVersion + " =")
if (os.name != "nt"):
    print("NOTE: You are running this on a Unix (Or *NIX) Operating System, downloaded software is only available for Windows, but can still be downloaded via a Unix (Or *NIX) OS")
print("")

selectedDownloader = libhearingdownloader.selectFromList(downloaders, "checker", numberSeperator=')', confirmationCheck=False)

os.system('python ./"' + downloaders[selectedDownloader][2] + '"')
