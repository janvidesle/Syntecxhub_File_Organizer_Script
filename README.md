# Syntecxhub_File_Organizer_Script
Auto-File-Organizer A lightweight, robust Python automation tool that keeps your folders tidy by automatically sorting files into categorized subfolders based on their extensions. Perfect for cleaning up "cluttered" Downloads or Desktop folders.
Features
Smart Categorization: Groups files into Images, Documents, Audio, Video, Archives, and Scripts.

Collision Prevention: Automatically renames files if a duplicate name exists in the destination folder (e.g., report.pdf becomes report_1.pdf).

Dry-Run Mode: Test the organization logic without moving a single file.

Activity Logging: Maintains a file_organizer.log to track every move made by the script.

Extensible: Easily add new file extensions or categories in the configuration dictionary.

🚀 Getting Started
1. Installation
No external libraries are required! This script uses Python's built-in os, shutil, and logging modules.

Bash
git clone https://github.com/YOUR_USERNAME/Auto-File-Organizer.git
cd Auto-File-Organizer
2. Configuration
Open organize.py and set the TARGET variable to the folder you want to clean:

Python
TARGET = "C:/Users/YourName/Downloads"  # Windows
# or
TARGET = "/Users/YourName/Downloads"    # macOS/Linux
3. Usage
Run the script manually:

Bash
python organize.py
🛠️ Automation (Scheduling)
To keep your folders clean 24/7, you can schedule this script to run automatically:

Windows (Task Scheduler)
Open Task Scheduler > Create Basic Task.

Set a trigger (e.g., Daily at 6:00 PM).

Action: Start a Program.

Program/script: python.exe

Add arguments: C:\path\to\your\organize.py

macOS/Linux (Cron)
Open terminal and type crontab -e.

Add the following line to run daily at midnight: 0 0 * * * /usr/bin/python3 /path/to/organize.py

🛡️ Safety
This script includes a Dry-Run mode. To see what would happen without moving files, set:

Python
organize_folder(TARGET, dry_run=True)
