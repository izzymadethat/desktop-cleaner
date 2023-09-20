import os

def check_if_file():
    """Check through the directory to make sure I am returning files."""
    directory = r'C:\\Users\\Isaiah Vickers\Desktop'
    files = []
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            files.append(file)
    return files

def get_file_extension(files_list):
    """Return a list of extensions for later use.
    This code splits each file found in check_if_file then add the ext
    to a list set so that I can make sure each file ext is stored properly."""

    extensions = set()
    for file in files_list:
        file_extension = os.path.splitext(file)[1]
        extensions.add(file_extension)
    return list(extensions)

test = check_if_file()
ext_test = get_file_extension(test)

print(ext_test)
