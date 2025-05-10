from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console(width=80)
with open("CHANGES.md", "r", encoding="utf-8") as changeFile:
    changeLog = changeFile.read()
    console.print(Panel(Markdown(changeLog), padding=2))
    print("  Please scroll back manually to read the whole changelog.")
