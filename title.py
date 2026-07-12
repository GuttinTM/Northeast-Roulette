from rich.console import Console
console = Console(width=100)

def title(word1, color, word2="", color2=""):
    console.print(f"[{color}]-" * 100)
    console.print(f"[{color}]{word1} [{color2}]{word2}", justify='center')
    console.print(f"[{color2}]-" * 100)

def line(num):
    print('-' * num)


