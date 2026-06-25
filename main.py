"""First Python Automation: File Organizer.

This script organizes files in a folder by moving them into category folders.

Usage:
    python main.py /path/to/folder

Example:
    python main.py ~/Downloads
"""

from pathlib import Path
import argparse
import shutil

FILE_CATEGORIES = {
    "images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "documents": {".pdf", ".doc", ".docx", ".txt", ".md"},
    "spreadsheets": {".csv", ".xls", ".xlsx"},
    "archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "code": {".py", ".js", ".html", ".css", ".json"},
}


def get_category(file_path: Path) -> str:
    """Return a category name based on the file extension."""
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "other"


def organize_folder(folder_path: Path, dry_run: bool = False) -> int:
    """Organize files in a folder and return the number of files processed."""
    if not folder_path.exists():
        raise FileNotFoundError(f"Folder does not exist: {folder_path}")

    if not folder_path.is_dir():
        raise NotADirectoryError(f"Path is not a folder: {folder_path}")

    processed_files = 0

    for item in folder_path.iterdir():
        if item.is_dir():
            continue

        category = get_category(item)
        target_folder = folder_path / category
        target_path = target_folder / item.name

        if target_path.exists():
            print(f"Skipped duplicate: {item.name}")
            continue

        if dry_run:
            print(f"Would move {item.name} -> {category}/")
        else:
            target_folder.mkdir(exist_ok=True)
            shutil.move(str(item), str(target_path))
            print(f"Moved {item.name} -> {category}/")

        processed_files += 1

    return processed_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Organize files in a folder by file type."
    )
    parser.add_argument("folder", help="Folder to organize")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    folder_path = Path(args.folder).expanduser().resolve()

    try:
        processed_files = organize_folder(folder_path, dry_run=args.dry_run)
    except (FileNotFoundError, NotADirectoryError) as error:
        print(f"Error: {error}")
        return

    action = "Previewed" if args.dry_run else "Moved"
    print(f"{action} {processed_files} file(s).")


if __name__ == "__main__":
    main()
