import os
import requests
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader

just_fix_windows_console()

downloaders = [
    (Style.DIM + "...Back to Main Menu" + Style.RESET_ALL, "", "Checker Menu.py"),
    (Style.BRIGHT + Fore.CYAN + "Sonova" + Style.RESET_ALL + ": Phonak Target MEDIA" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Phonak Target Media Checker.py"),
    (Fore.CYAN + "Sonova" + Style.RESET_ALL + ": Phonak Target SOUNDS" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Phonak Target Sounds Checker.py"),
    (Style.BRIGHT + Fore.BLUE + "Demant" + Style.RESET_ALL + ": Oticon Genie 2 (Legacy)" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Oticon Genie 2 Checker.py"),
    (Fore.BLUE + "Demant" + Style.RESET_ALL + ": Oticon Genie (Legacy)" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Oticon Genie Checker.py"),
    (Style.BRIGHT + Fore.BLUE + "Demant" + Style.RESET_ALL + ": Bernafon OasisNXT (Legacy)" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Bernafon OasisNXT Checker.py"),
    (Fore.BLUE + "Demant" + Style.RESET_ALL + ": Sonic ExpressFit (Legacy)" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Sonici ExpressFit Checker.py"),
    (Style.BRIGHT + Fore.BLUE + "Demant" + Style.RESET_ALL + ": Philips HearSuite (Legacy)" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Philips HearSuite Checker.py"),
]

print("\n")
print("===============================================")
print("=  " + Fore.YELLOW + "Extra and Legacy Software Update Checkers" + Style.RESET_ALL + "  =")
print("================================= " + Fore.GREEN + libhearingdownloader.downloaderVersion + Style.RESET_ALL + " =")
if (os.name != "nt"):
    print("NOTE: You are running The Checker on an Unix (*NIX) or mac Operating System. Hearing aids software requires Windows OS to run, but can still be checked on Unix (*NIX) or mac OS")
print("")

selectedDownloader = libhearingdownloader.selectFromList(downloaders, "checker", numberSeperator=')', confirmationCheck=False)

os.system('python ./"' + downloaders[selectedDownloader][2] + '"')
