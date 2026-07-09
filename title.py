from rich.console import Console
console = Console()

def title(word1, word2, color, color2):
    console.print(f"[{color}]-" * 148)
    console.print(f"[{color}]{word1} [{color2}]{word2}", justify="center")
    console.print(f"[{color2}]-" * 148)

def line(num):
    print('-' * num)


