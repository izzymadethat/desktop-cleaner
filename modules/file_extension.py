"""Return a list of extensions for later use.
    This code splits each file found in check_if_file then add the ext
    to a list set so that I can make sure each file ext is stored properly."""

import os

def get_file_extension(files_list):
    extensions = set()
    for file in files_list:
        file_extension = os.path.splitext(file)[1]
        extensions.add(file_extension)
    return list(extensions) # returns one of each ext in list (Ex.".mp3")
