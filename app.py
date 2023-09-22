""" Clean The Desktop And Organize Files."""
import os
import datetime

# My imports
from modules.file_handle import File
from modules.log_entry import create_log


def DesktopCleaner():
    app = File()

    directory = r"C:\Users\Isaiah Vickers\Desktop"
    folders = [
        'Document Files',
        'Media Files',
        'Audio Files',
        'Zip Files',
        'Setup Files',
        'Files To Be Reviewed'
    ]

    app.check_if_files(directory)
    # app.move(directory, folders)
    # app.get_extensions()
    # print(app.extensions)
    

if __name__ == '__main__':
    DesktopCleaner()