"""Check through the directory to make sure I am returning files."""
import os

def check_if_file():
    directory = r'C:\\Users\\Isaiah Vickers\Desktop'
    files = []
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            if not file_path.endswith('.lnk'):
                files.append(file)
    return files
