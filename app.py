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

test = check_if_file()

print(test)
