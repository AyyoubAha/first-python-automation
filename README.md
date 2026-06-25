# First Python Automation

My first practical Python automation project.

This repository is designed as a small but real portfolio project: a beginner-friendly command-line tool that organizes files inside a folder by file type.

## Problem

Folders like Downloads, Desktop, or project folders often become messy. Files with different formats end up in the same place and become hard to find.

## Solution

This script scans a folder and moves files into category folders such as:

- images
- documents
- spreadsheets
- archives
- code
- other

## Why This Project Matters

This is a simple project, but it teaches important foundations for later AI and automation work:

- working with files and folders
- using Python's standard library
- handling command-line input
- writing readable code
- documenting projects clearly
- thinking in workflows

## How To Run

Clone the repository:

```bash
git clone https://github.com/AyyoubAha/first-python-automation.git
cd first-python-automation
```

Run the script:

```bash
python main.py /path/to/folder
```

Example:

```bash
python main.py ~/Downloads
```

## Safety Notes

This first version moves files. Test it on a copy of a folder first.

Planned improvement: add a `--dry-run` mode before moving files.

## Project Roadmap

- [x] Create starter repository
- [x] Add file organizer script
- [ ] Add dry-run mode
- [ ] Add undo log
- [ ] Add tests
- [ ] Add demo GIF or screenshot
- [ ] Write a short case study

## Tech Stack

- Python 3
- pathlib
- shutil
- argparse

## Author

Ayyoub Aharchi  
Learning in public from zero to AI Builder.
