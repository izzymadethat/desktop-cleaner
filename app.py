""" Clean The Desktop And Organize Files."""
import sys
# sys.path.append("C:\Users\Isaiah Vickers\Documents\Github\desktop-cleaner")
import os
import datetime

# My imports
from modules.user_info import *
from modules.file_handle import File
from modules.log_entry import *
from modules.folder_manager import create_document_directory


def DesktopCleaner():
    document_folder = create_document_directory()
    directory = get_desktop_name()

    go_to_desktop(directory)

    app = File()

    folders = [
        'Document Files',
        'Media Files',
        'Audio Files',
        'Zip Files',
        'Setup Files',
        'Files To Be Reviewed'
    ]

    app.check_if_files(directory)
    app.move(directory, folders)

    # Create log with file data
    file_list = app.files
    file_count = app.count(file_list)
    app.get_extensions()
    file_extensions = app.extensions

    log_folder = create_log_folder(document_folder, app.get_current_day())

    os.chdir(log_folder)

    create_log(file_count, file_extensions, file_list)

if __name__ == '__main__':
    DesktopCleaner()
