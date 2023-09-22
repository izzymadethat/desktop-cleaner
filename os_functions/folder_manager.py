"""This function will create folders if they are not created"""

import os
import datetime

def create_folders(folder_path, folders):
    """Create all folders and\or add a date folder."""
    today = datetime.datetime.now()
    current_day = today.strftime("%m_%d")

    for folder in folders:
        new_directory = os.path.join(folder_path, folder)

        if os.path.exists(new_directory):
            continue
        else:
            os.mkdir(new_directory)

        date_folder = os.path.join(new_directory, current_day)

        if not os.path.exists(date_folder):
            os.mkdir(date_folder)
