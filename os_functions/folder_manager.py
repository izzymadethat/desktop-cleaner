"""This function will create folders if they are not created"""

import os
import datetime

def create_folder(path, folders, date):
    """Create all folders and\or add a date folder."""

    for folder in folders:
        new_directory = os.path.join(path, folder, date)
        
        if not os.path.exists(new_directory):
            os.makedirs(new_directory, exist_ok=True)
