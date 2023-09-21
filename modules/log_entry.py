"""
Handles code to write all information about the Desktop Clean to a txt file.

                The function takes 3 arguments:

~   The total file count ('file_handle.count_files_organized') as a string
~   The extension total number for each extension moved
        ('file_handle.show_files_organized') as a dictionary.
~   The exact files that were moved (file_check.check_file) as a list

"""

import os
import datetime

def create_log(file_count, file_extensions, file_names):
    with open('log_file.txt', 'w', encoding='utf-8') as file:
        # Write Headline
        file.write("\t\t=== Desktop Clean ===\n")
        file.write("\t\t\t Entry Log\n\n")
        today = datetime.datetime.now()

        # Write Cleanup information
        file.write(f"{file_count}\n\n")
        file.write("Count\t\t\tFile\n")
        for extension, count in file_extensions.items():
            file.write(f"{count} ........... \t{extension[1:]}\n")

        # Display file names just in case.
        file.write("\n\nFiles that were moved...\n")
        for name in file_names:
            file.write(f"{name}\n")

        file.write("\n\n\t\t Log Details:\n")
        file.write(f"Log saved {today}")
