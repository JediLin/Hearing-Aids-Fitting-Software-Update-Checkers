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
print("=  Extra and Legacy Software Update Checkers  =")
print("================================= " + libhearingdownloader.downloaderVersion + " =")
if (os.name != "nt"):
    print("NOTE: You are running The Checker on an Unix (*NIX) or mac Operating System. Hearing aids software requires Windows OS to run, but can still be checked on Unix (*NIX) or mac OS")
print("")

selectedDownloader = libhearingdownloader.selectFromList(downloaders, "checker", numberSeperator=')', confirmationCheck=False)

os.system('python ./"' + downloaders[selectedDownloader][2] + '"')
