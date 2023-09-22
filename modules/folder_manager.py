"""This function will create folders if they are not created"""

import os
from pathlib import Path
import datetime

def create_folder(path, folders, date):
    """Create all folders and/or add a date folder."""

    for folder in folders:
        new_directory = os.path.join(path, folder, date)
        
        if not os.path.exists(new_directory):
            os.makedirs(new_directory, exist_ok=True)


def create_document_directory():
    document_folder = str(Path.home() / 'Documents')
    new_destination = os.path.join(document_folder, 'Desktop Cleaner')
    os.makedirs(new_destination, exist_ok=True)
    return new_destination

def create_log_folder(destination, date):
    path = os.path.join(destination, date)
    os.makedirs(path, exist_ok=True)
    return path

def create_folder_date():
    now = datetime.datetime.now()
    current_date =now.strftime("%m_%d")
    return current_date

    