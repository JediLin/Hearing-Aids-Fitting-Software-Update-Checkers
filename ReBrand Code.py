import rot_codec
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style

# Main switch: screen or file
mode = "screen"

just_fix_windows_console()
console = Console(width=100)

with open("ReBrand Unlock Code.enc", "r+", encoding="utf-8") as codeFile:
    content = codeFile.read()
    dec = rot_codec.rot47_decode(content)

if(mode == "screen"):
    console.print(Panel(Markdown(dec), padding=2))
    print("  Please scroll back manually to read the whole changelog.")
elif(mode == "file"):
    with open("ReBrand Unlock Code.md", "w", encoding="utf-8") as target:
        target.write(dec)
    print("\n\nDone! Please check " + Style.BRIGHT + Fore.GREEN + "ReBrand Unlock Code.md" + Style.RESET_ALL + " file.")
else:
    print("\n\nDon't know what to do.\nDo nothing.\n")

