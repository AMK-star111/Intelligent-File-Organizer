from pathlib import Path
from rich import print
from rules import FILE_RULES

# Locate Downloads folder
downloads_path = Path.home() / "Downloads"

print(f"[bold cyan]Scanning:[/bold cyan] {downloads_path}\n")

# Loop through files
for file in downloads_path.iterdir():

    # Ignore folders
    if file.is_file():

        extension = file.suffix.lower()

        category = FILE_RULES.get(extension, "Others")

        print(
            f"[green]{file.name}[/green] "
            f"→ [yellow]{category}[/yellow]"
        )

    