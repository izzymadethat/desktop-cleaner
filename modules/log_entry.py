"""
Handles code to write all information about the Desktop Clean to a txt file.

                The function takes 3 arguments:

~   The total file count ('file_handle.count_files_organized') as a string
~   The extension total number for each extension moved
        ('file_handle.show_files_organized') as a dictionary.
~   The exact files that were moved (file_check.check_file) as a list

"""

import os
import shutil
import datetime

from modules.folder_manager import *

def create_log(file_count, file_extensions, file_names):
    with open('log_file.txt', 'w', encoding='utf-8') as file:
        # Get current date
        today = get_log_date()

        # Write Headline
        file.write("\t\t=== Desktop Clean ===\n")
        file.write("\t\t\t Entry Log\n\n")

        # Write Cleanup information
        file.write(f"{file_count}\n\n")
        file.write("Count\t\t\tFile\n")
        for extension, count in file_extensions.items():
            file.write(f"{count} ........... \t{extension[1:]}\n")

        # Display file names
        file.write("\n\nFiles that were moved...\n")
        for name in file_names:
            file.write(f"{name}\n")

        # Disply Log Entry Data
        file.write("\n\n\t\t Log Details:\n")
        file.write(f"Log saved {today}")

def get_log_date():
    today = datetime.datetime.now()
    current_day = today.strftime('%m/%d/%Y %H:%M:%S')
    return current_day