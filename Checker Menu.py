import os
import requests
from pathlib import Path
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import libhearingdownloader

just_fix_windows_console()
selfUpdateOption = "Self Update Checker"
updaterRetries = libhearingdownloader.updaterRetries
while updaterRetries > 0:
    try:
        checkerRelease = requests.get("https://api.github.com/repos/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/releases/latest")
        if not (checkerRelease.json()['tag_name'] == libhearingdownloader.downloaderVersion):
            selfUpdateOption += Fore.CYAN + "  >> " + Style.BRIGHT + Fore.GREEN + checkerRelease.json()['tag_name'] + Style.NORMAL + " AVAILABLE " + Fore.CYAN + "<<" + Style.RESET_ALL
            print("\n\n\n" + Fore.YELLOW + "NEW VERSION AVAILABLE!!" + Style.RESET_ALL + "\n\nThe latest version of The Checker is " + Fore.GREEN + checkerRelease.json()['tag_name'] + Style.RESET_ALL + " (you are using "+ Fore.RED + libhearingdownloader.downloaderVersion + Style.RESET_ALL + ").\nPlease use" + Fore.YELLOW + Back.BLUE + Style.BRIGHT + " 1" + Fore.WHITE + Style.NORMAL + ") Self Update Checker " + Style.RESET_ALL + "option to download it.")
        break
    except:
        pass

    updaterRetries -= 1


downloaders = [
    ("EXIT", "", "exit.py"),
    (selfUpdateOption + "\n    " + Style.DIM + "----------------------------------------------" + Style.RESET_ALL, "", "GitHub Checker.py"),
    (Style.BRIGHT + Fore.CYAN + "Sonova" + Style.RESET_ALL + ": Phonak Target" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Phonak Target Checker.py"),
    (Fore.CYAN + "Sonova" + Style.RESET_ALL + ": Unitron TrueFit" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Unitron TrueFit Checker.py"),
    (Style.BRIGHT + Fore.CYAN + "Sonova" + Style.RESET_ALL + ": Hansaton scout" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "HANSATON scout Checker.py"),
    (Fore.BLUE + "Demant" + Style.RESET_ALL + ": Oticon Genie 2" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Oticon Genie 2 2024 Checker.py"),
    (Style.BRIGHT + Fore.BLUE + "Demant" + Style.RESET_ALL + ": Bernafon OasisNXT" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Bernafon OasisNXT 2024 Checker.py"),
    (Fore.BLUE + "Demant" + Style.RESET_ALL + ": Sonic ExpressFit" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Sonici ExpressFit 2024 Checker.py"),
    (Style.BRIGHT + Fore.BLUE + "Demant" + Style.RESET_ALL + ": Philips HearSuite" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Philips HearSuite 2024 Checker.py"),
    (Fore.MAGENTA + "GN" + Style.RESET_ALL + ": ReSound" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "GN ReSound Checker.py"),
    (Style.BRIGHT + Fore.MAGENTA + "GN" + Style.RESET_ALL + ": Beltone" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "GN Beltone Checker.py"),
    (Fore.MAGENTA + "GN" + Style.RESET_ALL + ": Interton" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "GN Interton Checker.py"),
    (Style.BRIGHT + Fore.RED + "WSA" + Style.RESET_ALL + ": Signia Connexx" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Signia Connexx Checker.py"),
    (Fore.RED + "WSA" + Style.RESET_ALL + ": Rexton Connexx" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Rexton Connexx Checker.py"),
    (Style.BRIGHT + Fore.RED + "WSA" + Style.RESET_ALL + ": Audio Service Connexx" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Audio Service Connexx Checker.py"),
    (Fore.RED + "WSA" + Style.RESET_ALL + ": A&M Connexx" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "AM Connexx Checker.py"),
    (Style.BRIGHT + Fore.RED + "WSA" + Style.RESET_ALL + ": Widex Compass GPS" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Widex Compass GPS Checker.py"),
    (Fore.YELLOW + "Starkey" + Style.RESET_ALL + ": Starkey Pro Fit" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Starkey Pro Fit Checker.py"),
    (Style.BRIGHT + Fore.YELLOW + "Starkey" + Style.RESET_ALL + ": Starkey Inspire OS" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Starkey Inspire Checker.py"),
    (Style.DIM + "...Extra & Legacy Software Update Checkers" + Style.RESET_ALL, "", "Extra Menu.py"),
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

turboFile = Path("turbo.txt")
if not turboFile.is_file():
    libhearingdownloader.printDisclaimer(disclaimer)

print("\n")
if turboFile.is_file():
    print("=" + Style.BRIGHT + Fore.BLACK + "// " + Fore.RED + "T" + Fore.YELLOW + "U" + Fore.CYAN + "R" + Fore.GREEN + "B" + Fore.BLUE + "O" + Fore.BLACK + " //" + Style.RESET_ALL + "======================================")
else:
    print("==================================================")
print("=  " + Fore.YELLOW + "Hearing Aids Fitting Software Update Checkers" + Style.RESET_ALL + " =")
print("==================================== " + Fore.GREEN + libhearingdownloader.downloaderVersion + Style.RESET_ALL + " =")
if (os.name != "nt"):
    print("NOTE: You are running The Checker on an Unix (*NIX) or mac Operating System. Hearing aids software requires Windows OS to run, but can still be checked on Unix (*NIX) or mac OS")
print("")

selectedDownloader = libhearingdownloader.selectFromList(downloaders, "checker", numberSeperator=')', confirmationCheck=False)

os.system('python ./"' + downloaders[selectedDownloader][2] + '"')
