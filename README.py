from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console(width=80)
help_file = open("CHANGES.md", "r+", encoding="utf-8")

#with console.pager(styles=1):
#  console.print(Panel(Markdown(help_file.read()), padding=2))
console.print(Panel(Markdown(help_file.read()), padding=2))
print("  Please scroll back manually to read the whole content.\n")
