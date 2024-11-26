import time
import webbrowser
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style

just_fix_windows_console()

print("\nOpening " + Fore.CYAN + "https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/archive/refs/heads/main.zip" + Style.RESET_ALL + " ...")
time.sleep(2)
webbrowser.open("https://github.com/JediLin/Hearing-Aids-Fitting-Software-Update-Checkers/archive/refs/heads/main.zip")
