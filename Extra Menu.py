import os
import requests
import libhearingdownloader


downloaders = [
    ("...Back to Main Menu", "", "Checker Menu.py"),
    ("Phonak Target MEDIA Update Checker", "", "Phonak Target Media Checker.py"),
    ("Phonak Target SOUNDS Update Checker", "", "Phonak Target Sounds Checker.py"),
    ("Oticon Genie 2 (Legacy) Update Checker", "", "Oticon Genie 2 Checker.py"),
    ("Oticon Genie (Legacy) Update Checker", "", "Oticon Genie Checker.py"),
    ("Bernafon OasisNXT (Legacy) Update Checker", "", "Bernafon OasisNXT Checker.py"),
    ("Sonic ExpressFit (Legacy) Update Checker", "", "Sonici ExpressFit Checker.py"),
    ("Philips HearSuite (Legacy) Update Checker", "", "Philips HearSuite Checker.py"),
]

print("\n")
print("===============================================")
print("= Extra and Legacy Softwares Update Checkers  =")
print("================================= " + libhearingdownloader.downloaderVersion + " =")
if (os.name != "nt"):
    print("NOTE: You are running this on a Unix (Or *NIX) Operating System, downloaded software is only available for Windows, but can still be downloaded via a Unix (Or *NIX) OS")
print("")

selectedDownloader = libhearingdownloader.selectFromList(downloaders, "checker", numberSeperator=')', confirmationCheck=False)

os.system('python ./"' + downloaders[selectedDownloader][2] + '"')
