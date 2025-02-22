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
            selfUpdateOption = Back.BLUE + " Self Update Checker " + Style.RESET_ALL + Fore.CYAN + " >> " + Style.BRIGHT + Fore.GREEN + checkerRelease.json()['tag_name'] + Style.NORMAL + " AVAILABLE " + Fore.CYAN + "<<" + Style.RESET_ALL
            print("\n\n\n" + Fore.YELLOW + "NEW VERSION AVAILABLE!!" + Style.RESET_ALL + "\n\nThe latest version of The Checker is " + Fore.GREEN + checkerRelease.json()['tag_name'] + Style.RESET_ALL + " (you are using " + Fore.RED + libhearingdownloader.downloaderVersion + Style.RESET_ALL + ").\nPlease use " + Style.BRIGHT + Fore.GREEN + "1" + Style.NORMAL + Fore.WHITE + ") " + Style.RESET_ALL + Back.BLUE + " Self Update Checker " + Style.RESET_ALL + " option to download it.")
        break
    except:
        pass

    updaterRetries -= 1


downloaders = [
    (Style.RESET_ALL + Style.DIM + "EXIT" + Style.RESET_ALL, "", "exit.py"),
    (Style.RESET_ALL + selfUpdateOption + "\n    " + Style.DIM + "----------------------------------------------" + Style.RESET_ALL, "", "GitHub Checker.py"),
    (Style.RESET_ALL + "Sonova " + Style.BRIGHT + Fore.GREEN + "Phonak" + Style.RESET_ALL + " Target" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Phonak Target Checker.py"),
    (Style.RESET_ALL + "Sonova " + Style.BRIGHT + Fore.CYAN + "Unitron" + Style.RESET_ALL + " TrueFit" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Unitron TrueFit Checker.py"),
    (Style.RESET_ALL + "Sonova " + Style.BRIGHT + Fore.BLACK + "Hansaton" + Style.RESET_ALL + " scout" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "HANSATON scout Checker.py"),
    (Style.RESET_ALL + "Demant " + Style.BRIGHT + Fore.MAGENTA + "Oticon" + Style.RESET_ALL + " Genie 2" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Oticon Genie 2 2024 Checker.py"),
    (Style.RESET_ALL + "Demant " + Style.BRIGHT + Fore.RED + "Bernafon" + Style.RESET_ALL + " OasisNXT" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Bernafon OasisNXT 2024 Checker.py"),
    (Style.RESET_ALL + "Demant " + Style.BRIGHT + Fore.CYAN + "Sonic" + Style.RESET_ALL + " ExpressFit" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Sonici ExpressFit 2024 Checker.py"),
    (Style.RESET_ALL + "Demant " + Style.BRIGHT + Fore.BLUE + "Philips" + Style.RESET_ALL + " HearSuite" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Philips HearSuite 2024 Checker.py"),
    (Style.RESET_ALL + "GN " + Style.BRIGHT + Fore.RED + "ReSound" + Style.RESET_ALL + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "GN ReSound Checker.py"),
    (Style.RESET_ALL + "GN " + Style.BRIGHT + Fore.BLUE + "Beltone" + Style.RESET_ALL + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "GN Beltone Checker.py"),
    (Style.RESET_ALL + "GN " + Style.BRIGHT + Fore.YELLOW + "Interton" + Style.RESET_ALL + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "GN Interton Checker.py"),
    (Style.RESET_ALL + "WSA " + Style.BRIGHT + Fore.RED + "Signia" + Style.RESET_ALL + " Connexx" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Signia Connexx Checker.py"),
    (Style.RESET_ALL + "WSA " + Style.BRIGHT + Fore.YELLOW + "Rexton" + Style.RESET_ALL + " Connexx" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Rexton Connexx Checker.py"),
    (Style.RESET_ALL + "WSA " + Style.BRIGHT + Fore.BLUE + "Audio Service" + Style.RESET_ALL + " Connexx" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Audio Service Connexx Checker.py"),
    (Style.RESET_ALL + "WSA " + Fore.YELLOW + "A&M" + Style.RESET_ALL + " Connexx" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "AM Connexx Checker.py"),
    (Style.RESET_ALL + "WSA " + Style.BRIGHT + Fore.WHITE + "Widex" + Style.RESET_ALL + " Compass GPS" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Widex Compass GPS Checker.py"),
    (Style.RESET_ALL + Style.BRIGHT + Fore.BLUE + "Starkey" + Style.RESET_ALL + " Pro Fit" + Style.DIM + " Update Checker" + Style.RESET_ALL, "", "Starkey Pro Fit Checker.py"),
    (Style.RESET_ALL + Style.DIM + "...Extra & Legacy Software Update Checkers" + Style.RESET_ALL, "", "Extra Menu.py"),
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
    print("\n\n\n")
    if not (checkerRelease.json()['tag_name'] == libhearingdownloader.downloaderVersion):
        selfUpdateOption = Back.BLUE + " Self Update Checker " + Style.RESET_ALL + Fore.CYAN + " >> " + Style.BRIGHT + Fore.GREEN + checkerRelease.json()['tag_name'] + Style.NORMAL + " AVAILABLE " + Fore.CYAN + "<<" + Style.RESET_ALL
        print("\n\n\n" + Fore.YELLOW + "NEW VERSION AVAILABLE!!" + Style.RESET_ALL + "\n\nThe latest version of The Checker is " + Fore.GREEN + checkerRelease.json()['tag_name'] + Style.RESET_ALL + " (you are using "+ Fore.RED + libhearingdownloader.downloaderVersion + Style.RESET_ALL + ").\nPlease use " + Style.BRIGHT + Fore.GREEN + "1" + Style.NORMAL + Fore.WHITE + ") " + Style.RESET_ALL + Back.BLUE + " Self Update Checker " + Style.RESET_ALL + " option to download it.")

print("")
if turboFile.is_file():
    print("=" + Style.BRIGHT + Fore.BLACK + "// " + Fore.RED + "T" + Fore.YELLOW + "U" + Fore.CYAN + "R" + Fore.GREEN + "B" + Fore.BLUE + "O" + Fore.BLACK + " //" + Style.RESET_ALL + "======================================")
else:
    print("==================================================")
print("=  " + Style.BRIGHT + Fore.YELLOW + "Hearing Aids Fitting Software Update Checkers" + Style.RESET_ALL + " =")
print("==================================== " + Fore.GREEN + libhearingdownloader.downloaderVersion + Style.RESET_ALL + " =")
if (os.name != "nt"):
    print("NOTE: You are running The Checker on an Unix (*NIX) or mac Operating System. Hearing aids software requires Windows OS to run, but can still be checked on Unix (*NIX) or mac OS")

selectedDownloader = libhearingdownloader.selectFromList(downloaders, "checker", numberSeperator=')', confirmationCheck=False)

os.system('python ./"' + downloaders[selectedDownloader][2] + '"')
