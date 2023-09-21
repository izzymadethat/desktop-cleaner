""" Clean The Desktop And Organize Files."""
import os
import datetime

# My imports
from modules.file_check import check_if_file
from modules.file_extension import get_file_extension
from modules.file_handle import count_files_organized, show_files_organized
from modules.log_entry import create_log

from os_functions.folder_manager import create_folders
from os_functions.move_files import *

# Today's Date
today = datetime.datetime.now()
current_day = today.strftime("%m_%d")

files = check_if_file()
extensions = get_file_extension(files)

files_organized = count_files_organized(files)
files_moved = show_files_organized(files)

print(files_moved, files_organized, files)

create_log(files_organized, files_moved, files)


# Create Folders
folder_path = "C:/Users/Isaiah Vickers/Desktop"
folders = [
    'Documents',
    'Media Files',
    'Audio Files',
    'Zip Files',
    'Setup Files',
    'Files To Be Reviewed'
]

create_folders(folder_path, folders)
move_all_files(folder_path, current_day)
