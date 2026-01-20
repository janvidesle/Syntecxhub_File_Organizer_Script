import os
import shutil
import logging
from datetime import datetime

# --- CONFIGURATION ---
# Map folder names to their associated extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh"],
}

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("file_organizer.log"), logging.StreamHandler()]
)

def handle_collision(dest_folder, file_name):
    """If file exists, appends a timestamp to avoid overwriting."""
    name, ext = os.path.splitext(file_name)
    counter = 1
    new_name = file_name
    
    while os.path.exists(os.path.join(dest_folder, new_name)):
        new_name = f"{name}_{counter}{ext}"
        counter += 1
    return new_name

def organize_folder(target_path, dry_run=False):
    if not os.path.isdir(target_path):
        logging.error(f"Invalid directory: {target_path}")
        return

    logging.info(f"{'[DRY RUN] ' if dry_run else ''}Starting organization in: {target_path}")

    for item in os.listdir(target_path):
        item_path = os.path.join(target_path, item)

        # Skip directories and the script/log themselves
        if os.path.isdir(item_path) or item == "organize.py" or item == "file_organizer.log":
            continue

        # Determine the file extension
        _, extension = os.path.splitext(item)
        extension = extension.lower()

        # Find the correct category
        dest_category = "Others"
        for category, extensions in FILE_CATEGORIES.items():
            if extension in extensions:
                dest_category = category
                break

        dest_folder_path = os.path.join(target_path, dest_category)

        # Move Logic
        if not dry_run:
            if not os.path.exists(dest_folder_path):
                os.makedirs(dest_folder_path)
            
            final_name = handle_collision(dest_folder_path, item)
            shutil.move(item_path, os.path.join(dest_folder_path, final_name))
            logging.info(f"MOVED: {item} -> {dest_category}/{final_name}")
        else:
            logging.info(f"WOULD MOVE: {item} -> {dest_category}")

if __name__ == "__main__":
    # Change this to the folder you want to clean
    TARGET = os.path.expanduser("~/Downloads") 
    
    # Set dry_run=True to test without moving anything
    organize_folder(TARGET, dry_run=False)