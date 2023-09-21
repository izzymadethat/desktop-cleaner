""" Clean The Desktop And Organize Files."""
import os
import datetime

# My imports
from modules.file_check import check_if_file
from modules.file_extension import get_file_extension
from modules.file_handle import count_files_organized, show_files_organized
from modules.log_entry import create_log

test = check_if_file()
ext_test = get_file_extension(test)

files_organized = count_files_organized(test)
files_moved = show_files_organized(test)

print(files_moved, files_organized, test)

create_log(files_organized, files_moved, test)
